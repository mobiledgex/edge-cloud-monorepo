#!/usr/bin/env python3

import argparse
from datetime import datetime
import logging
import os
import re
import requests
import subprocess

markup = (
    (re.compile(r'(EDGECLOUD-\d+)'), "[\\1](https://mobiledgex.atlassian.net/browse/\\1)".format),
    (re.compile(r'\(#(\d+)\)$'), "([#\\1](https://github.com/mobiledgex/{0}/pull/\\1))".format),
)

pr_re = {
    "issue": re.compile(r'\* ((EDGECLOUD-\d+).*)'),
    "end": re.compile(r'### Description'),
}

def update_submodules():
    logging.info("Updating submodules")
    subprocess.run(["git", "submodule", "update", "--remote"])

def markup_line(line, mod):
    jiras = set(markup[0][0].findall(line))
    pr = markup[1][0].search(line)
    for pat, repl in markup:
        line = re.sub(pat, repl(mod), line)
    return line, jiras

def get_pr_body(mod, pr):
    url = "{0}/repos/{1}/{2}/pulls/{3}".format(
                os.environ["GITHUB_API_URL"],
                os.path.dirname(os.environ["GITHUB_REPOSITORY"]),
                mod, pr)
    r = requests.get(url,
                     headers={"Authorization": "Token {0}".format(os.environ.get("GITHUB_TOKEN"))})
    if r.status_code == requests.codes.ok:
        return r.json()["body"]
    return ""

def get_changelog_for_commit(mod, commit):
    logging.info("Fetching changelog for commit " + commit)
    p = subprocess.run(["git", "-C", mod, "log", "-1", "--pretty=%an%n%s%n%b", commit],
                       capture_output=True, text=True)

    lines = p.stdout.splitlines()
    author = lines.pop(0)
    subject = lines.pop(0)
    m = markup[1][0].search(subject)
    pr = m[1] if m else None

    subject, jiras = markup_line(subject, mod)

    body = []
    for line in lines:
        # Check if line has a JIRA ticket ID
        m = re.search(markup[0][0], line)
        if m:
            l, lj = markup_line(line, mod)
            new_jiras = lj - jiras
            if new_jiras:
                body.append(l)
            jiras = jiras | new_jiras

    try:
        for line in get_pr_body(mod, pr).splitlines():
            if pr_re["end"].match(line):
                break
            m = pr_re["issue"].match(line)
            if m:
                if m[2] not in jiras:
                    l, _ = markup_line(m[1], mod)
                    body.append(l)
    except Exception as e:
        logging.exception("Failed to fetch PR body")

    cl = f"- {subject} ({author})"
    for line in body:
        cl += f"\n   - {line}"
    return cl

def get_changelog_for_module(mod, rev_range):
    logging.info("Fetching changelog for " + mod)
    p = subprocess.run(["git", "-C", mod, "log", "--pretty=%H", rev_range],
                       capture_output=True, text=True)

    commits = p.stdout.splitlines()
    cl = []
    for commit in commits:
        cl.append(get_changelog_for_commit(mod, commit))

    logging.debug(cl)
    return "\n".join(cl)

def get_changelog(tag):
    # Title
    datestamp = datetime.now().strftime("%b %d, %Y")
    title = f"## [{tag}] - {datestamp}\n[Details](../../commit/{tag})\n\n"

    # Submodule commits
    p = subprocess.run(["git", "submodule", "summary"],
                       capture_output=True, text=True)
    logging.debug("Summary: " + p.stdout)
    mod_re = re.compile(r'^\*\s([^\s]+)\s([^\s]+)')
    changed_mods = []
    for line in p.stdout.splitlines():
        m = mod_re.search(line)
        if m:
            mod = m[1]
            rev_range = m[2]
            cl = f"### {mod}:\n"
            cl += get_changelog_for_module(mod, rev_range)
            changed_mods.append(cl)

    if not changed_mods:
        # No changes in any of the submodules; skip changelog generation
        return ""

    return title + "\n\n".join(changed_mods)

def prepend_changelog(cl, tag):
    cl_file = "CHANGELOG.md"
    try:
        with open(cl_file) as f:
            old_cl = f.read()
    except FileNotFoundError:
        old_cl = ""

    with open(cl_file, "w") as f:
        f.write(cl + "\n\n" + old_cl)

def tag_and_push(tag):
    subprocess.run(["git", "config", "user.name", "MobiledgeX Ops"])
    subprocess.run(["git", "config", "user.email", "mobiledgex.ops@mobiledgex.com"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", tag])
    subprocess.run(["git", "tag", "-a", "-m", tag, tag])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "origin", tag])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tag", help="tag name")
    parser.add_argument("--no-update", action="store_true",
                        help="skip updating submodules", default=False)
    parser.add_argument("--no-push", action="store_true",
                        help="skip updating submodules", default=False)
    parser.add_argument("--debug", action="store_true",
                        help="enable debug logs")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    if not args.no_update:
        update_submodules()

    cl = get_changelog(args.tag)
    if cl:
        prepend_changelog(cl, args.tag)
    else:
        logging.info("No submodule changes; not updating changelog")

    if not args.no_push:
        tag_and_push(args.tag)

if __name__ == "__main__":
    main()
