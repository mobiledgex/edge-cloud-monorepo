## [2022-03-06] - Mar 06, 2022
[Details](../../commit/2022-03-06)

### edge-cloud:
- [EDGECLOUD-6237](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6237): MC api /orgcloudletinfo/show reveals cluster and vm app info for other organizations ([#1670](https://github.com/mobiledgex/edge-cloud/pull/1670)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-6237](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6237): MC api /orgcloudletinfo/show reveals cluster and vm app info for other organizations ([#1995](https://github.com/mobiledgex/edge-cloud-infra/pull/1995)) (Ashish Jain)

## [2022-03-05] - Mar 05, 2022
[Details](../../commit/2022-03-05)

### edge-cloud:
- [EDGECLOUD-6226](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6226) fix runcommand exploit allowing access to parent VM ([#1669](https://github.com/mobiledgex/edge-cloud/pull/1669)) (Jon)
- Vcd oauth switchover ([#1661](https://github.com/mobiledgex/edge-cloud/pull/1661)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-6226](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6226) fix runcommand exploit ([#1996](https://github.com/mobiledgex/edge-cloud-infra/pull/1996)) (Jon)
- [EDGECLOUD-6236](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6236) Users can delete AlertReceviers from other orgs ([#1997](https://github.com/mobiledgex/edge-cloud-infra/pull/1997)) (Lev Shvarts)
- Vcd oauth switchover ([#1980](https://github.com/mobiledgex/edge-cloud-infra/pull/1980)) (Jim)
- [EDGECLOUD-6232](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6232): Account creation and password reset request emails vulnerable to phishing ([#1993](https://github.com/mobiledgex/edge-cloud-infra/pull/1993)) (Ashish Jain)
- [EDGECLOUD-6234](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6234): MC /artifactory/summary leaks user and org information ([#1994](https://github.com/mobiledgex/edge-cloud-infra/pull/1994)) (Ashish Jain)

## [2022-03-04] - Mar 04, 2022
[Details](../../commit/2022-03-04)

### edge-cloud-infra:
- In dev mode, pick CRM from mobiledgex-dev registry ([#1990](https://github.com/mobiledgex/edge-cloud-infra/pull/1990)) (Venky)
- [EDGECLOUD-6221](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6221) disallow user from changing org billing parent ([#1989](https://github.com/mobiledgex/edge-cloud-infra/pull/1989)) (Jon)
- [EDGECLOUD-6223](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6223) disallow user with no orgs from seeing events ([#1988](https://github.com/mobiledgex/edge-cloud-infra/pull/1988)) (Jon)

## [2022-03-03] - Mar 03, 2022
[Details](../../commit/2022-03-03)

### edge-cloud:
- Update open source software handling to include software mirroring ([#1666](https://github.com/mobiledgex/edge-cloud/pull/1666)) (Jon)
- [EDGECLOUD-6165](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6165) Adjust AppInst key defaults for single k8s cloudlet ([#1667](https://github.com/mobiledgex/edge-cloud/pull/1667)) (Jon)

### edge-cloud-infra:
- Update third-party-notices to reference mirrored source code ([#1986](https://github.com/mobiledgex/edge-cloud-infra/pull/1986)) (Jon)
- Missed upgrading chef recipe version ([#1987](https://github.com/mobiledgex/edge-cloud-infra/pull/1987)) (Venky)

## [2022-03-02] - Mar 02, 2022
[Details](../../commit/2022-03-02)

### edge-cloud:
- Fix redis memory leak ([#1664](https://github.com/mobiledgex/edge-cloud/pull/1664)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-6179](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6179)  mc crashes while fetching cloudletpool/cluster usage ([#1977](https://github.com/mobiledgex/edge-cloud-infra/pull/1977)) (Lev Shvarts)
- Upgrade Artifactory to 7.19.12 ([#1985](https://github.com/mobiledgex/edge-cloud-infra/pull/1985)) (Venky)

## [2022-03-01] - Mar 01, 2022
[Details](../../commit/2022-03-01)

### edge-cloud-infra:
- do chef init after platform init ([#1984](https://github.com/mobiledgex/edge-cloud-infra/pull/1984)) (Jim)
- [EDGECLOUD-6202](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6202) Base image update to include updated chef client ([#1982](https://github.com/mobiledgex/edge-cloud-infra/pull/1982)) (Venky)

## [2022-02-28] - Feb 28, 2022
[Details](../../commit/2022-02-28)

### edge-cloud-infra:
- crmserver restaring on VCD when create cloudlet has a trust policy ([#1983](https://github.com/mobiledgex/edge-cloud-infra/pull/1983)) (Devdatta)

## [2022-02-27] - Feb 27, 2022
[Details](../../commit/2022-02-27)

### edge-cloud:
- Fix cloudlet cleanup issues ([#1663](https://github.com/mobiledgex/edge-cloud/pull/1663)) (Ashish Jain)
- Fix rootLB TLS certs refresh thread as it can end up using expired certs ([#1662](https://github.com/mobiledgex/edge-cloud/pull/1662)) (Ashish Jain)
   - [EDGECLOUD-6198](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6198): RootLB TLS certs refresh thread can end up using expired certs

### edge-cloud-infra:
- Fix cloudlet cleanup issues ([#1981](https://github.com/mobiledgex/edge-cloud-infra/pull/1981)) (Ashish Jain)

## [2022-02-25] - Feb 25, 2022
[Details](../../commit/2022-02-25)

### edge-cloud:
- Fix LB portmap lookup for a namespace ([#1660](https://github.com/mobiledgex/edge-cloud/pull/1660)) (Devdatta)
- [EDGECLOUD-6161](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6161) disallow VM/docker apps on single kubernetes cluster platform ([#1659](https://github.com/mobiledgex/edge-cloud/pull/1659)) (Jon)
- [EDGECLOUD-6151](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6151) More logs for error cases ([#1658](https://github.com/mobiledgex/edge-cloud/pull/1658)) (Bruce Armstrong)

### edge-cloud-infra:
- [EDGECLOUD-6160](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6160) disallow operator org for singlekubernetesclusterowner org ([#1979](https://github.com/mobiledgex/edge-cloud-infra/pull/1979)) (Jon)
- [EDGECLOUD-6151](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6151) Add error checking for IP address parameters ([#1960](https://github.com/mobiledgex/edge-cloud-infra/pull/1960)) (Bruce Armstrong)
   - * [EDGECLOUD-6151](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6151) Add error checking for IP address parameters
- Match externally exposed federation port with container port ([#1978](https://github.com/mobiledgex/edge-cloud-infra/pull/1978)) (Venky)

## [2022-02-24] - Feb 24, 2022
[Details](../../commit/2022-02-24)

### edge-cloud:
- Fix cloudlet undo on create failures ([#1654](https://github.com/mobiledgex/edge-cloud/pull/1654)) (Ashish Jain)
- fix RunCommand exec and add check to ensure ready to update init version ([#1657](https://github.com/mobiledgex/edge-cloud/pull/1657)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-5979](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5979): Able to create a federatorzone with invalid country code ([#1976](https://github.com/mobiledgex/edge-cloud-infra/pull/1976)) (Ashish Jain)
- [EDGECLOUD-5325](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5325) Set up teleport using chef ([#1970](https://github.com/mobiledgex/edge-cloud-infra/pull/1970)) (Venky)
- Flag to pick builds from dev registry for deployment ([#1975](https://github.com/mobiledgex/edge-cloud-infra/pull/1975)) (Venky)

## [2022-02-23] - Feb 23, 2022
[Details](../../commit/2022-02-23)

### edge-cloud:
- [EDGECLOUD-5679](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5679): Fix issue to get correct dockerapp container IDs ([#1653](https://github.com/mobiledgex/edge-cloud/pull/1653)) (Ashish Jain)
- enhance debug command for HA, also fix trailing slash for mc show node ([#1656](https://github.com/mobiledgex/edge-cloud/pull/1656)) (Jim)
- subsequent switchover after redis failure does not work properly ([#1652](https://github.com/mobiledgex/edge-cloud/pull/1652)) (Jim)

### edge-cloud-infra:
- Cleanup rootLB DNS entry on cloudlet deletion ([#1972](https://github.com/mobiledgex/edge-cloud-infra/pull/1972)) (Ashish Jain)
- User API key bug fixes ([#1971](https://github.com/mobiledgex/edge-cloud-infra/pull/1971)) (Ashish Jain)
- Federation bug fixes ([#1969](https://github.com/mobiledgex/edge-cloud-infra/pull/1969)) (Ashish Jain)
- fix access cloudlet for k8s deploy ([#1974](https://github.com/mobiledgex/edge-cloud-infra/pull/1974)) (Jim)
- Enable pod autoscaling on DME ([#1973](https://github.com/mobiledgex/edge-cloud-infra/pull/1973)) (Venky)
- CRM H/A chef changes for master node down ([#1968](https://github.com/mobiledgex/edge-cloud-infra/pull/1968)) (Jim)

## [2022-02-22] - Feb 22, 2022
[Details](../../commit/2022-02-22)

### edge-cloud:
- Security Rules : allow uppercase for Protocol ([#1651](https://github.com/mobiledgex/edge-cloud/pull/1651)) (Devdatta)

### edge-cloud-infra:
- Have ansible deployments optionally bypass teleport ([#1967](https://github.com/mobiledgex/edge-cloud-infra/pull/1967)) (Venky)

## [2022-02-21] - Feb 21, 2022
[Details](../../commit/2022-02-21)

### edge-cloud:
- H/A fixes ([#1639](https://github.com/mobiledgex/edge-cloud/pull/1639)) (Jim)

### edge-cloud-infra:
- H/A fixes ([#1938](https://github.com/mobiledgex/edge-cloud-infra/pull/1938)) (Jim)
- Customise Jenkins builds for staging setup ([#1966](https://github.com/mobiledgex/edge-cloud-infra/pull/1966)) (Venky)

## [2022-02-19] - Feb 19, 2022
[Details](../../commit/2022-02-19)

### edge-cloud-infra:
- Add the APAC region to the staging setup ([#1965](https://github.com/mobiledgex/edge-cloud-infra/pull/1965)) (Venky)
- [EDGECLOUD-6144](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6144): Show other details as part of federator create output ([#1964](https://github.com/mobiledgex/edge-cloud-infra/pull/1964)) (Ashish Jain)
- [EDGECLOUD-6144](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6144): Enable federation endpoint on staging setup ([#1963](https://github.com/mobiledgex/edge-cloud-infra/pull/1963)) (Ashish Jain)

## [2022-02-18] - Feb 18, 2022
[Details](../../commit/2022-02-18)

### edge-cloud:
- [EDGECLOUD-6155](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6155): Unable to add federation cloudlets to cloudlet pool ([#1650](https://github.com/mobiledgex/edge-cloud/pull/1650)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-6155](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6155): Unable to add federation cloudlets to cloudlet pool ([#1962](https://github.com/mobiledgex/edge-cloud-infra/pull/1962)) (Ashish Jain)

## [2022-02-17] - Feb 17, 2022
[Details](../../commit/2022-02-17)

### edge-cloud:
- Anthos: ConfigYaml file cleanup with DeleteAppInst ([#1649](https://github.com/mobiledgex/edge-cloud/pull/1649)) (Devdatta)

### edge-cloud-infra:
- Support for deploying custom builds from `mobiledgex-dev` project in harbor ([#1959](https://github.com/mobiledgex/edge-cloud-infra/pull/1959)) (Venky)

## [2022-02-16] - Feb 16, 2022
[Details](../../commit/2022-02-16)

### edge-cloud-infra:
- H/A healthcheck fix ([#1961](https://github.com/mobiledgex/edge-cloud-infra/pull/1961)) (Jim)
- [EDGECLOUD-6104](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6104)  MC crash with missing "thanos_metrics" in Postgres ([#1951](https://github.com/mobiledgex/edge-cloud-infra/pull/1951)) (Lev Shvarts)
- [EDGECLOUD-6144](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6144): Fix FRM vault policy to read mexenv.json for updating DNS entry ([#1958](https://github.com/mobiledgex/edge-cloud-infra/pull/1958)) (Ashish Jain)
- Support all Telefonica orgs in teleport ([#1956](https://github.com/mobiledgex/edge-cloud-infra/pull/1956)) (Venky)
- [EDGECLOUD-6146](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6146) Gitlab upgrade to 14.5.4 ([#1952](https://github.com/mobiledgex/edge-cloud-infra/pull/1952)) (Venky)

## [2022-02-15] - Feb 15, 2022
[Details](../../commit/2022-02-15)

### edge-cloud:
- [EDGECLOUD-6150](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6150) fail CreateCloudlet if SingleKubernetesClusterOwner set on non-single cluster cloudlet ([#1648](https://github.com/mobiledgex/edge-cloud/pull/1648)) (Jon)
- [EDGECLOUD-6145](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6145): Fix small comment issue ([#1647](https://github.com/mobiledgex/edge-cloud/pull/1647)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-6133](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6133) check specific SingleKubernetesClusterOwner org exists ([#1957](https://github.com/mobiledgex/edge-cloud-infra/pull/1957)) (Jon)
- [EDGECLOUD-5917](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5917) add custom descriptions for swagger fix; fix login args ([#1950](https://github.com/mobiledgex/edge-cloud-infra/pull/1950)) (Jon)
- Consolidate hardcoded changes & fix app related onboarding issues ([#1955](https://github.com/mobiledgex/edge-cloud-infra/pull/1955)) (Ashish Jain)
- [EDGECLOUD-6144](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6144): Add federation APIKey read policy for FRM service ([#1954](https://github.com/mobiledgex/edge-cloud-infra/pull/1954)) (Ashish Jain)
- Manage teleport bypass whitelist using terraform ([#1953](https://github.com/mobiledgex/edge-cloud-infra/pull/1953)) (Venky)

## [2022-02-14] - Feb 14, 2022
[Details](../../commit/2022-02-14)

### edge-cloud:
- [EDGECLOUD-5838](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5838): App deployment support for federation ([#1646](https://github.com/mobiledgex/edge-cloud/pull/1646)) (Ashish Jain)

### edge-cloud-infra:
- new chef policy for k8s platform workers ([#1949](https://github.com/mobiledgex/edge-cloud-infra/pull/1949)) (Jim)
- [EDGECLOUD-5838](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5838): App deployment support for federation ([#1948](https://github.com/mobiledgex/edge-cloud-infra/pull/1948)) (Ashish Jain)

## [2022-02-12] - Feb 12, 2022
[Details](../../commit/2022-02-12)

### edge-cloud:
- [EDGECLOUD-5918](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5918) make upgrade functions thread safe ([#1644](https://github.com/mobiledgex/edge-cloud/pull/1644)) (Jon)
- [EDGECLOUD-5318](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5318) add tty and stdin options to mcctl exec commands ([#1645](https://github.com/mobiledgex/edge-cloud/pull/1645)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5318](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5318) add tty and stdin options to mcctl exec commands ([#1946](https://github.com/mobiledgex/edge-cloud-infra/pull/1946)) (Jon)
- Added cloudletpool tag validation and fixed cloudletorg tag ([#1947](https://github.com/mobiledgex/edge-cloud-infra/pull/1947)) (Lev Shvarts)
   - * [EDGECLOUD-6120](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6120) "usage cloudletpool" should sanitize the cloudletpool and cloudletpoolorg args
   - * [EDGECLOUD-6061](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6061) clientappusage metrics not returning metrics when using cloudlet/cloudlet-org only

## [2022-02-11] - Feb 11, 2022
[Details](../../commit/2022-02-11)

### edge-cloud:
- trustpolicyexception not creating rules for autocluster ([#1642](https://github.com/mobiledgex/edge-cloud/pull/1642)) (Devdatta)

### edge-cloud-infra:
- Add Tom to the vault access lists in main and QA ([#1945](https://github.com/mobiledgex/edge-cloud-infra/pull/1945)) (Venky)
- [EDGECLOUD-5325](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5325) TEF wants their ops team to be able to access VMs running in their infra ([#1944](https://github.com/mobiledgex/edge-cloud-infra/pull/1944)) (Venky)
- fix remove ip error ([#1943](https://github.com/mobiledgex/edge-cloud-infra/pull/1943)) (Jim)
- Turn on ntpd or timesyncd on all VMs ([#1942](https://github.com/mobiledgex/edge-cloud-infra/pull/1942)) (Venky)

## [2022-02-10] - Feb 10, 2022
[Details](../../commit/2022-02-10)

### edge-cloud:
- [EDGECLOUD-5613](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5613): Resource Management for AWS-EKS based Cloudlets ([#1638](https://github.com/mobiledgex/edge-cloud/pull/1638)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5611](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5611) Automatic scanning of developer VM images ([#1941](https://github.com/mobiledgex/edge-cloud-infra/pull/1941)) (Venky)
- [EDGECLOUD-6107](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6107) cloudletusage metrics should check cloudlet exists for flavorusage ([#1940](https://github.com/mobiledgex/edge-cloud-infra/pull/1940)) (Lev Shvarts)
- [EDGECLOUD-5613](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5613): Resource Management for AWS-EKS based Cloudlets ([#1937](https://github.com/mobiledgex/edge-cloud-infra/pull/1937)) (Ashish Jain)

## [2022-02-09] - Feb 09, 2022
[Details](../../commit/2022-02-09)

### edge-cloud:
- [EDGECLOUD-5918](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5918) ensure idempotent upgrade functions ([#1643](https://github.com/mobiledgex/edge-cloud/pull/1643)) (Jon)
- fix nil error check ([#1641](https://github.com/mobiledgex/edge-cloud/pull/1641)) (Devdatta)

### edge-cloud-infra:
- Fix help string for locationTile and add input validation for usage apis ([#1939](https://github.com/mobiledgex/edge-cloud-infra/pull/1939)) (Lev Shvarts)
   - [EDGECLOUD-6103](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6103) "usage app" and "metrics app" give inconsistent error for sql injection attempt
   - [EDGECLOUD-5921](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5921) mcctl usage for metrics clientappusage locationtile needs update for support of deviceinfo

## [2022-02-08] - Feb 08, 2022
[Details](../../commit/2022-02-08)

### edge-cloud:
- [EDGECLOUD-5995](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5995) Remove dash from mcctl args ([#1637](https://github.com/mobiledgex/edge-cloud/pull/1637)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5995](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5995) Remove dash from mcctl args ([#1935](https://github.com/mobiledgex/edge-cloud-infra/pull/1935)) (Jon)
- add internal ip to hosts to ensure weave initializes properly ([#1928](https://github.com/mobiledgex/edge-cloud-infra/pull/1928)) (Jim)
- Implement minimum version checks for teleport ([#1936](https://github.com/mobiledgex/edge-cloud-infra/pull/1936)) (Venky)

### edge-proto:
- [EDGECLOUD-5995](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5995) Remove dash from mcctl args ([#55](https://github.com/mobiledgex/edge-proto/pull/55)) (Jon)

## [2022-02-05] - Feb 05, 2022
[Details](../../commit/2022-02-05)

### edge-cloud:
- Change alert names, fix time format error ([#1636](https://github.com/mobiledgex/edge-cloud/pull/1636)) (Lev Shvarts)
   - * [EDGECLOUD-5895](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5895) AppInst Health Check fail values should be renamed
   -    - Autogen files and other fixes for the new names(see main PR in edge-proto: [EDGECLOUD-5895](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5895) AppInst Health 
   - * [EDGECLOUD-5880](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5880) mcctl usage command time format example doesnt work
- swagger documentation fixes ([#1635](https://github.com/mobiledgex/edge-cloud/pull/1635)) (Jon)

### edge-cloud-infra:
- Metrics object validation, alert names renaming and time error change ([#1934](https://github.com/mobiledgex/edge-cloud-infra/pull/1934)) (Lev Shvarts)
   - * [EDGECLOUD-6032](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6032) cloudletusage metrics should require cloudlets:x.cloudlet-org with cloudlets:x.cloudlet
   - * [EDGECLOUD-5895](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5895) AppInst Health Check fail values should be renamed
   -    - Autogen files and modifications to cloudlet prom rules for the new names(see main PR in edge-proto: [EDGECLOUD-5895](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5895) AppInst Health Check fail values should be renamed edge-proto#54)
   - * [EDGECLOUD-5880](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5880) mcctl usage command time format example doesnt work
- swagger documentations fixes ([#1933](https://github.com/mobiledgex/edge-cloud-infra/pull/1933)) (Jon)

### edge-proto:
- [EDGECLOUD-5895](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5895) AppInst Health Check fail values should be renamed([#54](https://github.com/mobiledgex/edge-proto/pull/54)) (Lev Shvarts)
- HealthCheck name changes (Lev Shvarts)

## [2022-02-04] - Feb 04, 2022
[Details](../../commit/2022-02-04)

### edge-cloud:
- [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) New e2e-tests for QOS Sessions ([#1632](https://github.com/mobiledgex/edge-cloud/pull/1632)) (Bruce Armstrong)
   - * [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) New e2e-tests for QOS Sessions
- Revert "[EDGECLOUD-6074](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6074): Update dependencies for MacOS Monterey build (#1623)" (Venky Tumkur)
- Revert "Go 1.17.6 docker build changes (#1633)" (Venky Tumkur)
- fix e2e ([#1634](https://github.com/mobiledgex/edge-cloud/pull/1634)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) New e2e-tests for QOS Sessions ([#1927](https://github.com/mobiledgex/edge-cloud-infra/pull/1927)) (Bruce Armstrong)
   - * [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) New e2e-tests for QOS Sessions
- Revert "[EDGECLOUD-6074](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6074): Infra go.mod updates for Monterey compilation. Remove bad test file. (#1921)" (Venky Tumkur)
- Flag to skip vault setup during dev deployments ([#1932](https://github.com/mobiledgex/edge-cloud-infra/pull/1932)) (Venky)
- [EDGECLOUD-6102](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6102): VMPool k8s cluster creation fails as install-k8s scripts args have changed ([#1931](https://github.com/mobiledgex/edge-cloud-infra/pull/1931)) (Ashish Jain)
- infra portion of e2e fix for HA ([#1930](https://github.com/mobiledgex/edge-cloud-infra/pull/1930)) (Jim)
- look for node in lowercase ([#1929](https://github.com/mobiledgex/edge-cloud-infra/pull/1929)) (Jim)

## [2022-02-03-1] - Feb 03, 2022
[Details](../../commit/2022-02-03-1)

### edge-cloud:
- Go 1.17.6 docker build changes ([#1633](https://github.com/mobiledgex/edge-cloud/pull/1633)) (Venky)

## [2022-02-03] - Feb 03, 2022
[Details](../../commit/2022-02-03)

### edge-cloud:
- [EDGECLOUD-6074](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6074): Update dependencies for MacOS Monterey build ([#1623](https://github.com/mobiledgex/edge-cloud/pull/1623)) (lgarner)
   - * [EDGECLOUD-6074](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6074): Update dependencies for MacOS Monterey build
- UpdateCloudlet() trustpolicy update time out error message fix  ([#1631](https://github.com/mobiledgex/edge-cloud/pull/1631)) (Devdatta)
- add cloudlet alias for network ([#1630](https://github.com/mobiledgex/edge-cloud/pull/1630)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-6074](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6074): Infra go.mod updates for Monterey compilation. Remove bad test file. ([#1921](https://github.com/mobiledgex/edge-cloud-infra/pull/1921)) (lgarner)
   - * [EDGECLOUD-6074](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6074): Infra go.mod updates for Monterey compilation. Remove invalid broken test case for golang 1.17.
- network alias ([#1926](https://github.com/mobiledgex/edge-cloud-infra/pull/1926)) (Jim)
- [EDGECLOUD-6020](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6020) Encrypt etcd backups ([#1924](https://github.com/mobiledgex/edge-cloud-infra/pull/1924)) (Venky)

## [2022-02-02] - Feb 02, 2022
[Details](../../commit/2022-02-02)

### edge-cloud:
- Trustpolicyexception ([#1629](https://github.com/mobiledgex/edge-cloud/pull/1629)) (Devdatta)

### edge-cloud-infra:
- Fix set_services cookbook version in k8s_crm policy ([#1925](https://github.com/mobiledgex/edge-cloud-infra/pull/1925)) (Venky)

## [2022-02-01] - Feb 01, 2022
[Details](../../commit/2022-02-01)

### edge-cloud:
- CRM H/A part 3 ([#1626](https://github.com/mobiledgex/edge-cloud/pull/1626)) (Jim)
- Removing inadvertently added dump.rdb file (brucearmstrong)
- [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) QosPrioritySessionCreate and QosPrioritySessionDelete ([#1624](https://github.com/mobiledgex/edge-cloud/pull/1624)) (Bruce Armstrong)
   - * [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) QosPrioritySessionCreate and QosPrioritySessionDelete
- Switch edge-cloud builds to the forked go-swagger ([#1628](https://github.com/mobiledgex/edge-cloud/pull/1628)) (Venky)

### edge-cloud-infra:
- CRM H/A part 3 ([#1923](https://github.com/mobiledgex/edge-cloud-infra/pull/1923)) (Jim)
- [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) QosPrioritySessionCreate and QosPrioritySessionDelete ([#1922](https://github.com/mobiledgex/edge-cloud-infra/pull/1922)) (Bruce Armstrong)
   - * [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) QosPrioritySessionCreate and QosPrioritySessionDelete
- Swaggerfix ([#1919](https://github.com/mobiledgex/edge-cloud-infra/pull/1919)) (Jon)

### edge-proto:
- Merge pull request #53 from mobiledgex/qos-sessions-create-delete (Bruce Armstrong)
   - [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) QosPrioritySessionCreate and QosPrioritySessionDelete
- New FindCloudlet QOS result fields (brucearmstrong)
- [EDGECLOUD-5982](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5982) QosPrioritySessionCreate and QosPrioritySessionDelete (brucearmstrong)

## [2022-01-30] - Jan 30, 2022
[Details](../../commit/2022-01-30)

### edge-cloud:
- Tpe fixes/edgecloud 6022 ([#1627](https://github.com/mobiledgex/edge-cloud/pull/1627)) (Devdatta)
   - * [EDGECLOUD-6022](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6022), [EDGECLOUD-6025](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6025), [EDGECLOUD-6041](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6041) : various trustPolicyException fixes

## [2022-01-28] - Jan 28, 2022
[Details](../../commit/2022-01-28)

### edge-cloud:
- [EDGECLOUD-6067](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6067): vmpool update gets stuck and eventually times out ([#1620](https://github.com/mobiledgex/edge-cloud/pull/1620)) (Ashish Jain)
   - * [EDGECLOUD-6067](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6067): vmpool update gets stuck and eventually times out
- Fix unit-tests ([#1621](https://github.com/mobiledgex/edge-cloud/pull/1621)) (Ashish Jain)
- [EDGECLOUD-6068](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6068): Retry auto deletion of appinst if an action is in progress ([#1622](https://github.com/mobiledgex/edge-cloud/pull/1622)) (Ashish Jain)

### edge-cloud-infra:
- Remove cluster option from fake_envoy_exporter ([#1920](https://github.com/mobiledgex/edge-cloud-infra/pull/1920)) (Lev Shvarts)
- [EDGECLOUD-6062](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6062) Upgrade base image to address CVE-2021-4034 ([#1918](https://github.com/mobiledgex/edge-cloud-infra/pull/1918)) (Venky)

## [2022-01-27] - Jan 27, 2022
[Details](../../commit/2022-01-27)

### edge-cloud:
- [EDGECLOUD-6036](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6036) check for and add missing mcctl help comments ([#1618](https://github.com/mobiledgex/edge-cloud/pull/1618)) (Jon)
- [EDGECLOUD-6063](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6063) Thanos metrics pipeline for cloudlet prometheus data ([#1596](https://github.com/mobiledgex/edge-cloud/pull/1596)) (Lev Shvarts)
- TrustPolicyException fixes ([#1619](https://github.com/mobiledgex/edge-cloud/pull/1619)) (Devdatta)
   - * [EDGECLOUD-6022](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6022), [EDGECLOUD-6025](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6025), [EDGECLOUD-6041](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6041) : various trustPolicyException fixes

### edge-cloud-infra:
- [EDGECLOUD-6036](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6036) check for and add missing mcctl help comments ([#1913](https://github.com/mobiledgex/edge-cloud-infra/pull/1913)) (Jon)
- [EDGECLOUD-6063](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6063) Thanos metrics pipeline for cloudlet prometheus data ([#1884](https://github.com/mobiledgex/edge-cloud-infra/pull/1884)) (Lev Shvarts)

### edge-proto:
- [EDGECLOUD-6036](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6036) check for and add missing mcctl help comments ([#52](https://github.com/mobiledgex/edge-proto/pull/52)) (Jon)

## [2022-01-26] - Jan 26, 2022
[Details](../../commit/2022-01-26)

### edge-cloud:
- API docs updates ([#1613](https://github.com/mobiledgex/edge-cloud/pull/1613)) (Venky)

### edge-cloud-infra:
- Reduce number of shards used by Jaeger indexes ([#1916](https://github.com/mobiledgex/edge-cloud-infra/pull/1916)) (Venky)
- API docs updates ([#1903](https://github.com/mobiledgex/edge-cloud-infra/pull/1903)) (Venky)

## [2022-01-25] - Jan 25, 2022
[Details](../../commit/2022-01-25)

### edge-cloud:
- Remove dead files that are no longer needed/relevant ([#1617](https://github.com/mobiledgex/edge-cloud/pull/1617)) (Jon)

### edge-cloud-infra:
- add standalone redis for e2e ([#1917](https://github.com/mobiledgex/edge-cloud-infra/pull/1917)) (Jim)
- Switch controller to redis HA ([#1915](https://github.com/mobiledgex/edge-cloud-infra/pull/1915)) (Venky)

## [2022-01-23] - Jan 23, 2022
[Details](../../commit/2022-01-23)

### edge-cloud-infra:
- Fix redis deployment in Ansible ([#1914](https://github.com/mobiledgex/edge-cloud-infra/pull/1914)) (Venky)

## [2022-01-22] - Jan 22, 2022
[Details](../../commit/2022-01-22)

### edge-cloud:
- [EDGECLOUD-4697](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4697): Use redis for StreamObjs ([#1579](https://github.com/mobiledgex/edge-cloud/pull/1579)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-4697](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4697): Use redis for StreamObjs ([#1892](https://github.com/mobiledgex/edge-cloud-infra/pull/1892)) (Ashish Jain)
- Set up redis in each region ([#1912](https://github.com/mobiledgex/edge-cloud-infra/pull/1912)) (Venky)

## [2022-01-21] - Jan 21, 2022
[Details](../../commit/2022-01-21)

### edge-cloud:
- Adding e2e-tests for QOS Priority Sessions ([#1614](https://github.com/mobiledgex/edge-cloud/pull/1614)) (Bruce Armstrong)

### edge-cloud-infra:
- Adding e2e-tests for QOS Priority Sessions ([#1904](https://github.com/mobiledgex/edge-cloud-infra/pull/1904)) (Bruce Armstrong)
- [EDGECLOUD-6007](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6007) failed login attempt delay time should show whole seconds ([#1910](https://github.com/mobiledgex/edge-cloud-infra/pull/1910)) (Jon)
- [EDGECLOUD-6026](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6026) user update for email that already exists needs better error message ([#1909](https://github.com/mobiledgex/edge-cloud-infra/pull/1909)) (Jon)
- Teleport version bump ([#1911](https://github.com/mobiledgex/edge-cloud-infra/pull/1911)) (Venky)
- Gitlab security upgrade to 14.5.3 ([#1907](https://github.com/mobiledgex/edge-cloud-infra/pull/1907)) (Venky)

## [2022-01-20] - Jan 20, 2022
[Details](../../commit/2022-01-20)

### edge-cloud:
- [EDGECLOUD-6015](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6015) capitalize mcctl arg help comments ([#1616](https://github.com/mobiledgex/edge-cloud/pull/1616)) (Jon)
- CRM H/A part 2 ([#1607](https://github.com/mobiledgex/edge-cloud/pull/1607)) (Jim)
- Update readme to include description and useful info ([#1615](https://github.com/mobiledgex/edge-cloud/pull/1615)) (Jon)
- [EDGECLOUD-6023](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6023) trustpolicyexception should only be allowed on a trusted app ([#1612](https://github.com/mobiledgex/edge-cloud/pull/1612)) (Devdatta)
   - * [EDGECLOUD-6023](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6023) trustpolicyexception should only be allowed on a trusted app and [EDGECLOUD-6024](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6024) trustpolicyexception should have outboundsecurityrules as mandatory
   - * [EDGECLOUD-6023](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6023) trustpolicyexception API tests, setting trusted in test_data.go as a part of PR comments

### edge-cloud-infra:
- tweak k8s install scripts to use only master ip and not derive the ip from network info ([#1905](https://github.com/mobiledgex/edge-cloud-infra/pull/1905)) (Jim)
- go.mod changes from edge-cloud change ([#1908](https://github.com/mobiledgex/edge-cloud-infra/pull/1908)) (Jon)
- CRM H/A part 2 ([#1897](https://github.com/mobiledgex/edge-cloud-infra/pull/1897)) (Jim)
- Update readme to include description and useful info ([#1906](https://github.com/mobiledgex/edge-cloud-infra/pull/1906)) (Jon)

### edge-proto:
- Add README.md ([#51](https://github.com/mobiledgex/edge-proto/pull/51)) (Jon)

## [2022-01-19] - Jan 19, 2022
[Details](../../commit/2022-01-19)

### edge-cloud:
- Add parsedeps program to print out open-source dependencies ([#1611](https://github.com/mobiledgex/edge-cloud/pull/1611)) (Jon)

## [2022-01-18] - Jan 18, 2022
[Details](../../commit/2022-01-18)

### edge-cloud-infra:
- [EDGECLOUD-5326](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5326) Automatic scanning of developer docker ([#1902](https://github.com/mobiledgex/edge-cloud-infra/pull/1902)) (Venky)

## [2022-01-15] - Jan 15, 2022
[Details](../../commit/2022-01-15)

### edge-cloud-infra:
- Workflow to upload THIRD-PARTY-NOTICES file to Artifactory ([#1901](https://github.com/mobiledgex/edge-cloud-infra/pull/1901)) (Venky)
- Install third party notice file on platform VMs ([#1899](https://github.com/mobiledgex/edge-cloud-infra/pull/1899)) (Venky)
- third party notices for shipped software ([#1900](https://github.com/mobiledgex/edge-cloud-infra/pull/1900)) (Jon)

## [2022-01-13] - Jan 13, 2022
[Details](../../commit/2022-01-13)

### edge-cloud:
- [EDGECLOUD-6011](https://mobiledgex.atlassian.net/browse/EDGECLOUD-6011) trustpolicyexception not creating rules in openstack ([#1610](https://github.com/mobiledgex/edge-cloud/pull/1610)) (Devdatta)

## [2022-01-12] - Jan 12, 2022
[Details](../../commit/2022-01-12)

### edge-cloud:
- add to keyworker ([#1609](https://github.com/mobiledgex/edge-cloud/pull/1609)) (Jim)
- [EDGECLOUD-5957](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5957) [EDGECLOUD-5958](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5958) update vcpus copyinfields fixes ([#1608](https://github.com/mobiledgex/edge-cloud/pull/1608)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5957](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5957) [EDGECLOUD-5958](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5958) update vcpus copyinfields fixes ([#1898](https://github.com/mobiledgex/edge-cloud-infra/pull/1898)) (Jon)

## [2022-01-11] - Jan 11, 2022
[Details](../../commit/2022-01-11)

### edge-cloud:
- [EDGECLOUD-5956](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5956) allow update App to AllowServerless=false ([#1605](https://github.com/mobiledgex/edge-cloud/pull/1605)) (Jon)

### edge-cloud-infra:
- tpe update (by admin) with rules and nonexisting org, should give correct error of key not found ([#1895](https://github.com/mobiledgex/edge-cloud-infra/pull/1895)) (Devdatta)
- [EDGECLOUD-5819](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5819) Gitlab missing content-security-policy header ([#1896](https://github.com/mobiledgex/edge-cloud-infra/pull/1896)) (Venky)

## [2022-01-08] - Jan 08, 2022
[Details](../../commit/2022-01-08)

### edge-cloud:
- [EDGECLOUD-5984](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5984): IgnoreCRM override should ignore DeletePrepare flag if set during object deletion ([#1604](https://github.com/mobiledgex/edge-cloud/pull/1604)) (Ashish Jain)
- [EDGECLOUD-5674](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5674) mcctl cloudlet showflavorsfor should have cloudlet and cloudlet-org as optional ([#1603](https://github.com/mobiledgex/edge-cloud/pull/1603)) (Jon)

### edge-cloud-infra:
- Adding DT QOS Priority Session server simulator. ([#1894](https://github.com/mobiledgex/edge-cloud-infra/pull/1894)) (Bruce Armstrong)
- [EDGECLOUD-5674](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5674) mcctl cloudlet showflavorsfor should have cloudlet and cloudlet-org as optional ([#1893](https://github.com/mobiledgex/edge-cloud-infra/pull/1893)) (Jon)

## [2022-01-07] - Jan 07, 2022
[Details](../../commit/2022-01-07)

### edge-cloud:
- [EDGECLOUD-5711](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5711) [EDGECLOUD-5766](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5766) more consistent parse error messages ([#1598](https://github.com/mobiledgex/edge-cloud/pull/1598)) (Jon)
- Add log sync list data error ([#1602](https://github.com/mobiledgex/edge-cloud/pull/1602)) (Ashish Jain)
- tpe cli, changed app-ver to appvers and app-name to appname to be consistent with other cli.s ([#1599](https://github.com/mobiledgex/edge-cloud/pull/1599)) (Devdatta)

### edge-cloud-infra:
- [EDGECLOUD-5711](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5711) [EDGECLOUD-5766](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5766) more consistent parse error messages ([#1886](https://github.com/mobiledgex/edge-cloud-infra/pull/1886)) (Jon)
- [EDGECLOUD-5906](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5906) Gitlab security upgrade to version 14.x ([#1891](https://github.com/mobiledgex/edge-cloud-infra/pull/1891)) (Venky)
- Open up teleport port on QA kafka node ([#1890](https://github.com/mobiledgex/edge-cloud-infra/pull/1890)) (Venky)
- tpe cli, changed app-ver to appvers and app-name to appname to be consistent with other cli.s ([#1887](https://github.com/mobiledgex/edge-cloud-infra/pull/1887)) (Devdatta)

## [2022-01-06] - Jan 06, 2022
[Details](../../commit/2022-01-06)

### edge-cloud:
- fix port range for network policy ([#1600](https://github.com/mobiledgex/edge-cloud/pull/1600)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-5976](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5976): Unable to delete a federator ([#1889](https://github.com/mobiledgex/edge-cloud-infra/pull/1889)) (Ashish Jain)
- Fix teleport auth service cert to have right domain ([#1888](https://github.com/mobiledgex/edge-cloud-infra/pull/1888)) (Venky)
- [EDGECLOUD-5811](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5811) Restrict SSH access to trusted IPs ([#1882](https://github.com/mobiledgex/edge-cloud-infra/pull/1882)) (Venky)

## [2022-01-05] - Jan 05, 2022
[Details](../../commit/2022-01-05)

### edge-cloud:
- fix error message for docker clusters on k8s baremetal ([#1597](https://github.com/mobiledgex/edge-cloud/pull/1597)) (Jim)
- [EDGECLOUD-5947](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5947) AutoScale Scale down not working ([#1595](https://github.com/mobiledgex/edge-cloud/pull/1595)) (Jon)

### edge-cloud-infra:
- tweaks for additional networks on shared lb ([#1885](https://github.com/mobiledgex/edge-cloud-infra/pull/1885)) (Jim)
- Fix Ansible requirements ([#1883](https://github.com/mobiledgex/edge-cloud-infra/pull/1883)) (Venky)
- [EDGECLOUD-5947](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5947) AutoScale Scale down not working ([#1881](https://github.com/mobiledgex/edge-cloud-infra/pull/1881)) (Jon)

## [2021-12-31] - Dec 31, 2021
[Details](../../commit/2021-12-31)

### edge-cloud-infra:
- [EDGECLOUD-5816](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5816) Console uses weak ciphers ([#1879](https://github.com/mobiledgex/edge-cloud-infra/pull/1879)) (Venky)
- access cloudlet support ([#1880](https://github.com/mobiledgex/edge-cloud-infra/pull/1880)) (Jim)
- [EDGECLOUD-5952](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5952): Fix show filtering for Federation APIs ([#1876](https://github.com/mobiledgex/edge-cloud-infra/pull/1876)) (Ashish Jain)

## [2021-12-30] - Dec 30, 2021
[Details](../../commit/2021-12-30)

### edge-cloud:
- [EDGECLOUD-5853](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5853) Unique URIs and DNS labels ([#1588](https://github.com/mobiledgex/edge-cloud/pull/1588)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5853](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5853) Unique URIs and DNS labels ([#1860](https://github.com/mobiledgex/edge-cloud-infra/pull/1860)) (Jon)
- Update vault TLS ciphers list ([#1877](https://github.com/mobiledgex/edge-cloud-infra/pull/1877)) (Venky)

## [2021-12-29] - Dec 29, 2021
[Details](../../commit/2021-12-29)

### edge-cloud:
- change order of validation checks ([#1593](https://github.com/mobiledgex/edge-cloud/pull/1593)) (Jim)

### edge-cloud-infra:
- Federation bug fixes ([#1871](https://github.com/mobiledgex/edge-cloud-infra/pull/1871)) (Ashish Jain)
   - * [EDGECLOUD-5938](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5938): Bad error message while creating federatorzone with invalid geolocation
   - * [EDGECLOUD-5946](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5946): FederatorZone register does not fail when zone list is empty
- [EDGECLOUD-5812](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5812) Restrict InfluxDB access to trusted IPs ([#1873](https://github.com/mobiledgex/edge-cloud-infra/pull/1873)) (Venky)

## [2021-12-28] - Dec 28, 2021
[Details](../../commit/2021-12-28)

### edge-cloud:
- UpdateTrustPolicyException with unknown cloudlet org, gives wrong error ([#1592](https://github.com/mobiledgex/edge-cloud/pull/1592)) (Devdatta)
   - * Fixed [EDGECLOUD-5965](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5965) UpdateTrustPolicyException with unknown cloudlet org, gives wrong error
   - * Fixed [EDGECLOUD-5965](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5965) UpdateTrustPolicyException with unknown cloudlet org, gives wrong error: PR comments

### edge-cloud-infra:
- UpdateTrustPolicyException with unknown cloudlet org, gives wrong error ([#1875](https://github.com/mobiledgex/edge-cloud-infra/pull/1875)) (Devdatta)
   - * Fixed [EDGECLOUD-5965](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5965) UpdateTrustPolicyException with unknown cloudlet org, gives wrong error

## [2021-12-24] - Dec 24, 2021
[Details](../../commit/2021-12-24)

### edge-cloud-infra:
- [EDGECLOUD-5813](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5813) InfluxDB uses weak ciphers ([#1874](https://github.com/mobiledgex/edge-cloud-infra/pull/1874)) (Venky)

## [2021-12-23] - Dec 23, 2021
[Details](../../commit/2021-12-23)

### edge-cloud-infra:
- Intercluster iptables ([#1872](https://github.com/mobiledgex/edge-cloud-infra/pull/1872)) (Jim)
- [EDGECLOUD-5910](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5910) Open up CORS settings on API server ([#1857](https://github.com/mobiledgex/edge-cloud-infra/pull/1857)) (Venky)
- [EDGECLOUD-5826](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5826) Disable vault LDAP logins ([#1869](https://github.com/mobiledgex/edge-cloud-infra/pull/1869)) (Venky)
- [EDGECLOUD-5823](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5823) Edgeturn ingress reveals nginx version ([#1870](https://github.com/mobiledgex/edge-cloud-infra/pull/1870)) (Venky)

## [2021-12-22] - Dec 22, 2021
[Details](../../commit/2021-12-22)

### edge-cloud-infra:
- include metallb containers in baseimage ([#1868](https://github.com/mobiledgex/edge-cloud-infra/pull/1868)) (Jim)

## [2021-12-21] - Dec 21, 2021
[Details](../../commit/2021-12-21)

### edge-cloud:
- Fix test-mex.go, fix one e2e-test and fix in UpdateTrustPolicyException ([#1589](https://github.com/mobiledgex/edge-cloud/pull/1589)) (Devdatta)
- Fixing URL for session DELETE ([#1591](https://github.com/mobiledgex/edge-cloud/pull/1591)) (Bruce Armstrong)

### edge-cloud-infra:
- Fix test-mex-infa ([#1861](https://github.com/mobiledgex/edge-cloud-infra/pull/1861)) (Devdatta)
- fix crash due to wrong slice being used ([#1867](https://github.com/mobiledgex/edge-cloud-infra/pull/1867)) (Jim)
- fix floating ip count ([#1866](https://github.com/mobiledgex/edge-cloud-infra/pull/1866)) (Jim)
- Fixing URL for session DELETE ([#1865](https://github.com/mobiledgex/edge-cloud-infra/pull/1865)) (Bruce Armstrong)

## [2021-12-19] - Dec 19, 2021
[Details](../../commit/2021-12-19)

### edge-cloud-infra:
- Sharedlb commonnet ([#1864](https://github.com/mobiledgex/edge-cloud-infra/pull/1864)) (Jim)

## [2021-12-18] - Dec 18, 2021
[Details](../../commit/2021-12-18)

### edge-cloud:
- fix fake platform update clusterinst resources ([#1590](https://github.com/mobiledgex/edge-cloud/pull/1590)) (Jon)

### edge-cloud-infra:
- fix fake platform update clusterinst resources ([#1862](https://github.com/mobiledgex/edge-cloud-infra/pull/1862)) (Jon)
- [EDGECLOUD-5934](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5934) mcctl is missing the not match fields for events find/show/terms ([#1863](https://github.com/mobiledgex/edge-cloud-infra/pull/1863)) (Jon)

## [2021-12-16] - Dec 16, 2021
[Details](../../commit/2021-12-16)

### edge-cloud:
- e2e-test file comparison by diffs ([#1586](https://github.com/mobiledgex/edge-cloud/pull/1586)) (Jon)

### edge-cloud-infra:
- e2e-test file comparison by diffs ([#1859](https://github.com/mobiledgex/edge-cloud-infra/pull/1859)) (Jon)

## [2021-12-15] - Dec 15, 2021
[Details](../../commit/2021-12-15)

### edge-cloud:
- tpeErrorMessage/[EDGECLOUD-5925](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5925) ([#1587](https://github.com/mobiledgex/edge-cloud/pull/1587)) (Devdatta)
   - * error message inconsistencies [EDGECLOUD-5925](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5925)
- Per DT, removing DEFAULT profile names. Fixing LOW_LATENCY ([#1585](https://github.com/mobiledgex/edge-cloud/pull/1585)) (Bruce Armstrong)

### edge-cloud-infra:
- Per DT, removing DEFAULT profile names. Fixing LOW_LATENCY ([#1858](https://github.com/mobiledgex/edge-cloud-infra/pull/1858)) (Bruce Armstrong)

## [2021-12-14] - Dec 14, 2021
[Details](../../commit/2021-12-14)

### edge-cloud:
- TrustPolicyException Cli : various bugfixes ([#1582](https://github.com/mobiledgex/edge-cloud/pull/1582)) (Devdatta)

### edge-cloud-infra:
- TrustPolicyException Cli : various bugfixes ([#1854](https://github.com/mobiledgex/edge-cloud-infra/pull/1854)) (Devdatta)

## [2021-12-10-1] - Dec 10, 2021
[Details](../../commit/2021-12-10-1)

### edge-cloud:
- Fixing default session duration time and adding logs ([#1584](https://github.com/mobiledgex/edge-cloud/pull/1584)) (Bruce Armstrong)

### edge-cloud-infra:
- DME access to sessions API keys ([#1856](https://github.com/mobiledgex/edge-cloud-infra/pull/1856)) (Venky)

## [2021-12-09] - Dec 09, 2021
[Details](../../commit/2021-12-09)

### edge-cloud:
- Include session ID and QOS profile in Tags of FindCloudletReply ([#1583](https://github.com/mobiledgex/edge-cloud/pull/1583)) (Bruce Armstrong)
- TDG QOS priority session creation ([#1577](https://github.com/mobiledgex/edge-cloud/pull/1577)) (Bruce Armstrong)
- [EDGECLOUD-5907](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5907) Upgrade edge-cloud-base-image to fix CVE 2021-43527 ([#1581](https://github.com/mobiledgex/edge-cloud/pull/1581)) (Venky)

### edge-cloud-infra:
- Fixing a mis-named profile ([#1855](https://github.com/mobiledgex/edge-cloud-infra/pull/1855)) (Bruce Armstrong)
- TDG QOS priority session creation ([#1851](https://github.com/mobiledgex/edge-cloud-infra/pull/1851)) (Bruce Armstrong)
- Support for short-lived kubeconfigs for CI/CD ([#1840](https://github.com/mobiledgex/edge-cloud-infra/pull/1840)) (Venky)

## [2021-12-08] - Dec 08, 2021
[Details](../../commit/2021-12-08)

### edge-cloud:
- Fix controller lease expire issue if alerts sync takes lot of time ([#1580](https://github.com/mobiledgex/edge-cloud/pull/1580)) (Ashish Jain)
   - [EDGECLOUD-5903](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5903): Controller etcd lease might expire if there are lots of alerts

### edge-cloud-infra:
- Teleport ops access ([#1848](https://github.com/mobiledgex/edge-cloud-infra/pull/1848)) (Venky)

## [2021-12-07] - Dec 07, 2021
[Details](../../commit/2021-12-07)

### edge-cloud:
- e2e-test unmarshal strict, sorted ([#1576](https://github.com/mobiledgex/edge-cloud/pull/1576)) (Jon)
- [EDGECLOUD-5746](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5746) remove cellID from DME metrics ([#1565](https://github.com/mobiledgex/edge-cloud/pull/1565)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5759](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5759)  Cloudlet usage API cloudlets array filter not working ([#1853](https://github.com/mobiledgex/edge-cloud-infra/pull/1853)) (Lev Shvarts)
- e2e-test unmarshal strict, sorted ([#1850](https://github.com/mobiledgex/edge-cloud-infra/pull/1850)) (Jon)
- [EDGECLOUD-5746](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5746) remove cellID from DME metrics ([#1836](https://github.com/mobiledgex/edge-cloud-infra/pull/1836)) (Lev Shvarts)

### edge-proto:
- [EDGECLOUD-5746](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5746) remove cellID from DME metrics (Lev Shvarts)
- remove empty spaces (Lev Shvarts)
- Remove cell_id from protobuf (Lev Shvarts)

## [2021-12-06] - Dec 06, 2021
[Details](../../commit/2021-12-06)

### edge-cloud:
- add metrics ip label ([#1575](https://github.com/mobiledgex/edge-cloud/pull/1575)) (Jim)
- add sudo option for DeleteFile ([#1578](https://github.com/mobiledgex/edge-cloud/pull/1578)) (Jim)

### edge-cloud-infra:
- metrics ip label ([#1849](https://github.com/mobiledgex/edge-cloud-infra/pull/1849)) (Jim)
- persist ips via netplan. Remove lbinfo ([#1852](https://github.com/mobiledgex/edge-cloud-infra/pull/1852)) (Jim)

## [2021-12-02] - Dec 02, 2021
[Details](../../commit/2021-12-02)

### edge-cloud:
- [EDGECLOUD-5667](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5667) Output JSON enum values as strings ([#1573](https://github.com/mobiledgex/edge-cloud/pull/1573)) (Jon)
- namespaces are limited to 63 chars and cannot end in dash ([#1574](https://github.com/mobiledgex/edge-cloud/pull/1574)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-5667](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5667) Output JSON enum values as strings ([#1846](https://github.com/mobiledgex/edge-cloud-infra/pull/1846)) (Jon)
- Federation bug fixes ([#1847](https://github.com/mobiledgex/edge-cloud-infra/pull/1847)) (Ashish Jain)

## [2021-11-30] - Nov 30, 2021
[Details](../../commit/2021-11-30)

### edge-cloud:
- Pull in the latest edge-cloud base image with the VCD CLI ([#1572](https://github.com/mobiledgex/edge-cloud/pull/1572)) (Venky)

### edge-cloud-infra:
- Federation bug fixes ([#1844](https://github.com/mobiledgex/edge-cloud-infra/pull/1844)) (Ashish Jain)
- [EDGECLOUD-5707](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5707) timed lockouts for failed login attempts ([#1835](https://github.com/mobiledgex/edge-cloud-infra/pull/1835)) (Jon)
- Enable federation on the dev setup ([#1845](https://github.com/mobiledgex/edge-cloud-infra/pull/1845)) (Venky)

## [2021-11-27-1] - Nov 29, 2021
[Details](../../commit/2021-11-27-1)

### edge-cloud:
- Fix e2e-tests ([#1570](https://github.com/mobiledgex/edge-cloud/pull/1570)) (Ashish Jain)

## [2021-11-27] - Nov 27, 2021
[Details](../../commit/2021-11-27)

### edge-cloud:
- frm service build ([#1571](https://github.com/mobiledgex/edge-cloud/pull/1571)) (Venky)

### edge-cloud-infra:
- Frm deployment ([#1843](https://github.com/mobiledgex/edge-cloud-infra/pull/1843)) (Venky)

## [2021-11-25] - Nov 25, 2021
[Details](../../commit/2021-11-25)

### edge-cloud-infra:
- [EDGECLOUD-5846](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5846) Shepherd keeps restarting after upgrade to HF4 ([#1839](https://github.com/mobiledgex/edge-cloud-infra/pull/1839)) (Ashish Jain)

## [2021-11-24] - Nov 24, 2021
[Details](../../commit/2021-11-24)

### edge-cloud-infra:
- fix dns ([#1838](https://github.com/mobiledgex/edge-cloud-infra/pull/1838)) (Jim)

## [2021-11-23] - Nov 23, 2021
[Details](../../commit/2021-11-23)

### edge-cloud:
- TrustPolicyException PR comments addressed ([#1555](https://github.com/mobiledgex/edge-cloud/pull/1555)) (Devdatta)
- [EDGECLOUD-5840](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5840): Controller allows setting deprecated values to appinst autoclusteripaccess field ([#1563](https://github.com/mobiledgex/edge-cloud/pull/1563)) (Ashish Jain)

### edge-cloud-infra:
- TrustPolicyException PR comments addressed ([#1822](https://github.com/mobiledgex/edge-cloud-infra/pull/1822)) (Devdatta)
- Fix intermittent e2e tests failures for client app/cloudlet metrics ([#1825](https://github.com/mobiledgex/edge-cloud-infra/pull/1825)) (Lev Shvarts)
- Adding Tom to the upg setup access list ([#1834](https://github.com/mobiledgex/edge-cloud-infra/pull/1834)) (Venky)

## [2021-11-21] - Nov 21, 2021
[Details](../../commit/2021-11-21)

### edge-cloud:
- [EDGECLOUD-5802](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5802) VM App Deployment aliasing fix: AppInstId ([#1562](https://github.com/mobiledgex/edge-cloud/pull/1562)) (Jon)
- k8s baremetal MT fix ([#1561](https://github.com/mobiledgex/edge-cloud/pull/1561)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-5802](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5802) VM App Deployment aliasing fix: AppInstId ([#1833](https://github.com/mobiledgex/edge-cloud-infra/pull/1833)) (Jon)
- renaming CreateDeveloperDefinedNamespaces ([#1832](https://github.com/mobiledgex/edge-cloud-infra/pull/1832)) (Jim)
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Federation enhancements ([#1821](https://github.com/mobiledgex/edge-cloud-infra/pull/1821)) (Ashish Jain)

## [2021-11-20] - Nov 20, 2021
[Details](../../commit/2021-11-20)

### edge-cloud:
- [EDGECLOUD-5829](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5829): CRM without restagtable doesn't receive updates to GPU driver cache ([#1558](https://github.com/mobiledgex/edge-cloud/pull/1558)) (Ashish Jain)
- Fix uncaught unit-test failure ([#1559](https://github.com/mobiledgex/edge-cloud/pull/1559)) (Ashish Jain)
- default the HA role ([#1560](https://github.com/mobiledgex/edge-cloud/pull/1560)) (Jim)
- [EDGECLOUD-5828](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5828): Support for cloudlet specific GPU driver license config ([#1556](https://github.com/mobiledgex/edge-cloud/pull/1556)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5218](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5218): add vcd-cli to rundebug and docker base image ([#1829](https://github.com/mobiledgex/edge-cloud-infra/pull/1829)) (mwilliams-mex)
   - * [EDGECLOUD-5218](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5218): add vcd-cli to rundebug and docker base image
   - * [EDGECLOUD-5218](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5218): bump qemu utils to .38
   - * [EDGECLOUD-5218](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5218): add example usage, remove dead code
- Support for teleport access to Telefonica VMs ([#1828](https://github.com/mobiledgex/edge-cloud-infra/pull/1828)) (Venky)
- [EDGECLOUD-5828](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5828): Support of cloudlet specific GPU driver license config ([#1827](https://github.com/mobiledgex/edge-cloud-infra/pull/1827)) (Ashish Jain)
- Fix build ([#1831](https://github.com/mobiledgex/edge-cloud-infra/pull/1831)) (Lev Shvarts)
- [EDGECLOUD-5775](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5775)  shepherd not starting on anthos ([#1830](https://github.com/mobiledgex/edge-cloud-infra/pull/1830)) (Lev Shvarts)

## [2021-11-19] - Nov 19, 2021
[Details](../../commit/2021-11-19)

### edge-cloud:
- CRM high availability part 1 ([#1546](https://github.com/mobiledgex/edge-cloud/pull/1546)) (Jim)

### edge-cloud-infra:
- CRM high availability part 1 ([#1805](https://github.com/mobiledgex/edge-cloud-infra/pull/1805)) (Jim)
- Vcd api reduce ([#1824](https://github.com/mobiledgex/edge-cloud-infra/pull/1824)) (Jim)
- Vault role for federation access ([#1826](https://github.com/mobiledgex/edge-cloud-infra/pull/1826)) (Venky)

## [2021-11-18] - Nov 18, 2021
[Details](../../commit/2021-11-18)

### edge-cloud:
- [EDGECLOUD-5751](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5751) add refs auto-gen tests ([#1554](https://github.com/mobiledgex/edge-cloud/pull/1554)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5751](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5751) add refs auto-gen tests ([#1820](https://github.com/mobiledgex/edge-cloud-infra/pull/1820)) (Jon)

## [2021-11-17] - Nov 17, 2021
[Details](../../commit/2021-11-17)

### edge-cloud-infra:
- Add missing files ([#1819](https://github.com/mobiledgex/edge-cloud-infra/pull/1819)) (Lev Shvarts)

## [2021-11-16] - Nov 16, 2021
[Details](../../commit/2021-11-16)

### edge-cloud:
- SendAllEnd fix for CRM startup ([#1553](https://github.com/mobiledgex/edge-cloud/pull/1553)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5710](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5710) usage with unknown app/cloudlet returns columns only ([#1817](https://github.com/mobiledgex/edge-cloud-infra/pull/1817)) (Lev Shvarts)
- Disable password expiry in platform VMs too ([#1818](https://github.com/mobiledgex/edge-cloud-infra/pull/1818)) (Venky)

## [2021-11-13] - Nov 13, 2021
[Details](../../commit/2021-11-13)

### edge-cloud:
- [EDGECLOUD-5772](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5772) Adding an alertpolicy to an app does not require creating a new revision of the app([#1552](https://github.com/mobiledgex/edge-cloud/pull/1552)) (Lev Shvarts)
- [EDGECLOUD-5790](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5790) App instance health status wrongly shows “Cloudletoffline” status for an online & operational cloudlet  ([#1551](https://github.com/mobiledgex/edge-cloud/pull/1551)) (Lev Shvarts)
- [EDGECLOUD-5751](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5751) delete_prepare and auto tests ([#1548](https://github.com/mobiledgex/edge-cloud/pull/1548)) (Jon)
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Add registered partner zones as cloudlets ([#1547](https://github.com/mobiledgex/edge-cloud/pull/1547)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5790](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5790)  App instance health status wrongly shows “Cloudletoffline” status for an online & operational cloudlet ([#1815](https://github.com/mobiledgex/edge-cloud-infra/pull/1815)) (Lev Shvarts)
- [EDGECLOUD-5751](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5751) delete_prepare and auto tests ([#1811](https://github.com/mobiledgex/edge-cloud-infra/pull/1811)) (Jon)
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): API Key based authentication for federation API endpoint ([#1809](https://github.com/mobiledgex/edge-cloud-infra/pull/1809)) (Ashish Jain)
- [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):update fed plat GetConsoleUrl signature ([#1816](https://github.com/mobiledgex/edge-cloud-infra/pull/1816)) (mwilliams-mex)
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Add registered partner zones as cloudlets ([#1807](https://github.com/mobiledgex/edge-cloud-infra/pull/1807)) (Ashish Jain)
- [EDGECLOUD-5651](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5651) Disable ubuntu account password expiry in all chef-managed VMs ([#1814](https://github.com/mobiledgex/edge-cloud-infra/pull/1814)) (Venky)

## [2021-11-11] - Nov 11, 2021
[Details](../../commit/2021-11-11)

### edge-cloud:
- Ec 5765 ([#1550](https://github.com/mobiledgex/edge-cloud/pull/1550)) (mwilliams-mex)
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):review comments
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):e2e test
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):review comment for e2e yml file
- [EDGECLOUD-5798](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5798): Fix controller crash ([#1549](https://github.com/mobiledgex/edge-cloud/pull/1549)) (Ashish Jain)

### edge-cloud-infra:
- Add aliases to billingevents and clean up common args ([#1813](https://github.com/mobiledgex/edge-cloud-infra/pull/1813)) (Lev Shvarts)
- [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):add cloudlet name suffix to vmApps ([#1804](https://github.com/mobiledgex/edge-cloud-infra/pull/1804)) (mwilliams-mex)
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):add cloudlet name suffix to vmApps
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):review comments
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):review comments
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):Review comments
   - * [EDGECLOUD-5765](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5765):Review comments
- Harbot cert renewal fix ([#1812](https://github.com/mobiledgex/edge-cloud-infra/pull/1812)) (Venky)

## [2021-11-10] - Nov 10, 2021
[Details](../../commit/2021-11-10)

### edge-cloud:
- [EDGECLOUD-5751](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5751) controller race conditions tests ([#1545](https://github.com/mobiledgex/edge-cloud/pull/1545)) (Jon)

### edge-cloud-infra:
- fix e2e test ([#1810](https://github.com/mobiledgex/edge-cloud-infra/pull/1810)) (Jon)
- Infra changes for federated MC ([#1808](https://github.com/mobiledgex/edge-cloud-infra/pull/1808)) (Venky)

## [2021-11-09] - Nov 09, 2021
[Details](../../commit/2021-11-09)

### edge-cloud-infra:
- Upgrade setup ansible and terraform manifests ([#1806](https://github.com/mobiledgex/edge-cloud-infra/pull/1806)) (Venky)

## [2021-11-06] - Nov 06, 2021
[Details](../../commit/2021-11-06)

### edge-cloud-infra:
- Pod autoscaling for controller and DME ([#1796](https://github.com/mobiledgex/edge-cloud-infra/pull/1796)) (Venky)

## [2021-11-04] - Nov 04, 2021
[Details](../../commit/2021-11-04)

### edge-cloud:
- [EDGECLOUD-5546](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5546) Handle non-fatal errors in cluster-svc prometheus deployments ([#1541](https://github.com/mobiledgex/edge-cloud/pull/1541)) (Devdatta)
   - * [EDGECLOUD-5546](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5546): addressing review comments from Jon
   - * [EDGECLOUD-5546](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5546): added cloudletDeletedCb for cleanup, changed array to a map for retryMapValue

### edge-cloud-infra:
- Bump up teleport proxy to version 7.3.3 ([#1803](https://github.com/mobiledgex/edge-cloud-infra/pull/1803)) (Venky)

## [2021-11-03] - Nov 03, 2021
[Details](../../commit/2021-11-03)

### edge-cloud:
- [EDGECLOUD-5774](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5774): K8s svc manifest empty protocol should default to TCP ([#1543](https://github.com/mobiledgex/edge-cloud/pull/1543)) (Ashish Jain)

### edge-cloud-infra:
- Harden VMs by turning off global cron and at access ([#1802](https://github.com/mobiledgex/edge-cloud-infra/pull/1802)) (Venky)
- [EDGECLOUD-5767](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5767):  vSphere CRM fails to initialized and panics trying to add IptablesRules ([#1801](https://github.com/mobiledgex/edge-cloud-infra/pull/1801)) (Devdatta)
   - * [EDGECLOUD-5767](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5767): nil pointer checks before deereferencing OutboundSecurityRules
   - * [EDGECLOUD-5767](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5767): Even if no TP, it should still call SetupIptablesRulesForRootLB for the ssh
   - * [EDGECLOUD-5767](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5767): PR comments : removed setting unnecessary explicit nil

## [2021-11-02] - Nov 02, 2021
[Details](../../commit/2021-11-02)

### edge-cloud:
- [EDGECLOUD-5520](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5520) mt/st single cluster platform ([#1542](https://github.com/mobiledgex/edge-cloud/pull/1542)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5520](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5520) mt/st single cluster platform ([#1799](https://github.com/mobiledgex/edge-cloud-infra/pull/1799)) (Jon)
- Upgrade Gitlab to version 13.12.12 ([#1800](https://github.com/mobiledgex/edge-cloud-infra/pull/1800)) (Venky)

## [2021-10-30] - Oct 30, 2021
[Details](../../commit/2021-10-30)

### edge-cloud:
- [EDGECLOUD-5337](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5337) Configurable rate limiting for dme persistent connections ([#1540](https://github.com/mobiledgex/edge-cloud/pull/1540)) (Bruce Armstrong)
   - * [EDGECLOUD-5337](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5337) Configurable rate limiting for dme persistent connections
- Fix upgrade unit-test ([#1539](https://github.com/mobiledgex/edge-cloud/pull/1539)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Federation changes ([#1798](https://github.com/mobiledgex/edge-cloud-infra/pull/1798)) (Ashish Jain)

## [2021-10-28] - Oct 28, 2021
[Details](../../commit/2021-10-28)

### edge-cloud:
- Add auto-gen'd files ([#1538](https://github.com/mobiledgex/edge-cloud/pull/1538)) (Ashish Jain)

### edge-cloud-infra:
- Add auto-gen'd files ([#1797](https://github.com/mobiledgex/edge-cloud-infra/pull/1797)) (Ashish Jain)

## [2021-10-26] - Oct 26, 2021
[Details](../../commit/2021-10-26)

### edge-cloud:
- [EDGECLOUD-5561](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5561) appinstlatency request failing with deadline exceeded ([#1537](https://github.com/mobiledgex/edge-cloud/pull/1537)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5561](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5561) appinstlatency request failing with deadline exceeded ([#1795](https://github.com/mobiledgex/edge-cloud-infra/pull/1795)) (Jon)
- [EDGECLOUD-5742](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5742)  clientapiusage with numsamples give wrong number of reqs ([#1791](https://github.com/mobiledgex/edge-cloud-infra/pull/1791)) (Lev Shvarts)
- VCD UpdateClusterInst fixes ([#1794](https://github.com/mobiledgex/edge-cloud-infra/pull/1794)) (Jim)

## [2021-10-24] - Oct 24, 2021
[Details](../../commit/2021-10-24)

### edge-cloud:
- edge-cloud Trustpolicyexception Openstack and VCD  ([#1491](https://github.com/mobiledgex/edge-cloud/pull/1491)) (Devdatta)

### edge-cloud-infra:
- edge-cloud-infra Trustpolicyexception Openstack and VCD  ([#1749](https://github.com/mobiledgex/edge-cloud-infra/pull/1749)) (Devdatta)

## [2021-10-23] - Oct 23, 2021
[Details](../../commit/2021-10-23)

### edge-cloud:
- k8s cluster-inst node resource info ([#1535](https://github.com/mobiledgex/edge-cloud/pull/1535)) (Jon)

### edge-cloud-infra:
- k8s cluster-inst node resource info ([#1792](https://github.com/mobiledgex/edge-cloud-infra/pull/1792)) (Jon)
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Federation fixes + TLS support ([#1793](https://github.com/mobiledgex/edge-cloud-infra/pull/1793)) (Ashish Jain)

## [2021-10-22] - Oct 22, 2021
[Details](../../commit/2021-10-22)

### edge-cloud:
- [EDGECLOUD-5687](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5687) Fix capitalization of error message ([#1534](https://github.com/mobiledgex/edge-cloud/pull/1534)) (Bruce Armstrong)
   - * [EDGECLOUD-5687](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5687) Fix capitalization of error message
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Add revision/requestID to each federation object ([#1536](https://github.com/mobiledgex/edge-cloud/pull/1536)) (Ashish Jain)
   - * [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Add revision/requestID to each federation object

### edge-cloud-infra:
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Add revision/requestID to each federation object ([#1790](https://github.com/mobiledgex/edge-cloud-infra/pull/1790)) (Ashish Jain)
   - * [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Add revision/requestID to each federation object

## [2021-10-21] - Oct 21, 2021
[Details](../../commit/2021-10-21)

### edge-cloud:
- [EDGECLOUD-5749](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5749) controller crash related to crmserver ([#1533](https://github.com/mobiledgex/edge-cloud/pull/1533)) (Jon)
- new unsigned decimal proto type for milli vcpus ([#1532](https://github.com/mobiledgex/edge-cloud/pull/1532)) (Jon)

### edge-cloud-infra:
- Teleport for audited access to region kubernetes clusters ([#1789](https://github.com/mobiledgex/edge-cloud-infra/pull/1789)) (Venky)
- new unsigned decimal proto type for milli vcpus ([#1787](https://github.com/mobiledgex/edge-cloud-infra/pull/1787)) (Jon)
- On AddAppInst use client's carrier for search ([#1788](https://github.com/mobiledgex/edge-cloud-infra/pull/1788)) (Bruce Armstrong)
- [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Use federation ID as an identifier and not as an authentication key ([#1785](https://github.com/mobiledgex/edge-cloud-infra/pull/1785)) (Ashish Jain)

## [2021-10-19-1] - Oct 19, 2021
[Details](../../commit/2021-10-19-1)

### edge-cloud-infra:
- [EDGECLOUD-5736](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5736): Fix MC crash ([#1786](https://github.com/mobiledgex/edge-cloud-infra/pull/1786)) (Ashish Jain)
- Monitor Jaeger metrics ([#1783](https://github.com/mobiledgex/edge-cloud-infra/pull/1783)) (Venky)

## [2021-10-19] - Oct 19, 2021
[Details](../../commit/2021-10-19)

### edge-cloud:
- Support for Federation Interconnect with other Operator Platforms ([#1494](https://github.com/mobiledgex/edge-cloud/pull/1494)) (Ashish Jain)
   - [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Support for Federation Interconnect with other operator platforms 

### edge-cloud-infra:
- fix port detach ([#1784](https://github.com/mobiledgex/edge-cloud-infra/pull/1784)) (Jim)
- Support for Federation Interconnect with other Operator Platforms (OPs) ([#1740](https://github.com/mobiledgex/edge-cloud-infra/pull/1740)) (Ashish Jain)
   - [EDGECLOUD-5704](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5704): Support for Federation Interconnect with other operator platforms 

## [2021-10-18] - Oct 18, 2021
[Details](../../commit/2021-10-18)

### edge-cloud-infra:
- Sync up current state of infra with terraform ([#1781](https://github.com/mobiledgex/edge-cloud-infra/pull/1781)) (Venky)

## [2021-10-16] - Oct 16, 2021
[Details](../../commit/2021-10-16)

### edge-cloud:
- Fix for minor bug that probably doesn't cause harm ([#1531](https://github.com/mobiledgex/edge-cloud/pull/1531)) (Bruce Armstrong)
- DME REST API noTLS fix ([#1529](https://github.com/mobiledgex/edge-cloud/pull/1529)) (Jon)
- [EDGECLOUD-5726](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5726): DME crash in dme-common.RemoveApp ([#1530](https://github.com/mobiledgex/edge-cloud/pull/1530)) (Ashish Jain)

### edge-cloud-infra:
- Fix e2e test failure ([#1782](https://github.com/mobiledgex/edge-cloud-infra/pull/1782)) (Lev Shvarts)

## [2021-10-15] - Oct 15, 2021
[Details](../../commit/2021-10-15)

### edge-cloud:
- fix yaml ([#1528](https://github.com/mobiledgex/edge-cloud/pull/1528)) (Jim)
- [EDGECLOUD-5712](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5712) appinst alerts are not triggering for cpu mem and disk ([#1527](https://github.com/mobiledgex/edge-cloud/pull/1527)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5712](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5712) appinst alerts are not triggering for cpu mem and disk ([#1780](https://github.com/mobiledgex/edge-cloud-infra/pull/1780)) (Lev Shvarts)

## [2021-10-14] - Oct 14, 2021
[Details](../../commit/2021-10-14)

### edge-cloud:
- [EDGECLOUD-5675](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5675) edge-cloud build fails in proto generated files ([#1517](https://github.com/mobiledgex/edge-cloud/pull/1517)) (Jon)
- e2e-test use docker network instead of link ([#1526](https://github.com/mobiledgex/edge-cloud/pull/1526)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5675](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5675) edge-cloud build fails in proto generated files ([#1769](https://github.com/mobiledgex/edge-cloud-infra/pull/1769)) (Jon)
- e2e-test use docker network instead of link ([#1779](https://github.com/mobiledgex/edge-cloud-infra/pull/1779)) (Jon)

### edge-proto:
- [EDGECLOUD-5675](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5675) edge-cloud build fails in proto generated files ([#47](https://github.com/mobiledgex/edge-proto/pull/47)) (Jon)

## [2021-10-13] - Oct 13, 2021
[Details](../../commit/2021-10-13)

### edge-cloud:
- validate additional cluster networks ([#1525](https://github.com/mobiledgex/edge-cloud/pull/1525)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-5247](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5247)  clientapiusage does not report the cellID/foundCloudlet/foundOperator value ([#1778](https://github.com/mobiledgex/edge-cloud-infra/pull/1778)) (Lev Shvarts)

## [2021-10-12] - Oct 12, 2021
[Details](../../commit/2021-10-12)

### edge-cloud:
- [EDGECLOUD-5502](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5502) Reverting float format change ([#1524](https://github.com/mobiledgex/edge-cloud/pull/1524)) (Bruce Armstrong)
- [EDGECLOUD-5673](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5673) shepherd got Prometheus LB IP not found after upgrade from HF3 to R3.1 ([#1523](https://github.com/mobiledgex/edge-cloud/pull/1523)) (Lev Shvarts)

## [2021-10-10] - Oct 10, 2021
[Details](../../commit/2021-10-10)

### edge-cloud-infra:
- fix intel issues ([#1777](https://github.com/mobiledgex/edge-cloud-infra/pull/1777)) (Jim)

## [2021-10-09] - Oct 09, 2021
[Details](../../commit/2021-10-09)

### edge-cloud-infra:
- Base image 4.7.0 ([#1774](https://github.com/mobiledgex/edge-cloud-infra/pull/1774)) (Venky)
   - - [EDGECLOUD-5651](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5651) Set the ubuntu user password to not expire in base images

## [2021-10-08] - Oct 08, 2021
[Details](../../commit/2021-10-08)

### edge-cloud:
- [EDGECLOUD-5502](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5502) Removing extra period ([#1522](https://github.com/mobiledgex/edge-cloud/pull/1522)) (Bruce Armstrong)
   - * [EDGECLOUD-5502](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5502) Removing extra period

### edge-cloud-infra:
- [EDGECLOUD-5502](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5502) Removing extra period ([#1776](https://github.com/mobiledgex/edge-cloud-infra/pull/1776)) (Bruce Armstrong)
- multi cluster networks part 2 ([#1773](https://github.com/mobiledgex/edge-cloud-infra/pull/1773)) (Jim)
- Rename 'Fake' to 'Simulated' as part of PDF report & fix sort order of cloudlets ([#1775](https://github.com/mobiledgex/edge-cloud-infra/pull/1775)) (Ashish Jain)
- [EDGECLOUD-5682](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5682) [EDGECLOUD-5681](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5681) [EDGECLOUD-5679](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5679) Cloudlet usage validation and clientapiusage fix ([#1772](https://github.com/mobiledgex/edge-cloud-infra/pull/1772)) (Lev Shvarts)

## [2021-10-07] - Oct 07, 2021
[Details](../../commit/2021-10-07)

### edge-cloud:
- [EDGECLOUD-5475](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5475) [EDGECLOUD-5465](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5465) rate limit api minor fixes ([#1521](https://github.com/mobiledgex/edge-cloud/pull/1521)) (Jon)
- [EDGECLOUD-5477](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5477) Flavor should be mandatory argument when creating an App ([#1520](https://github.com/mobiledgex/edge-cloud/pull/1520)) (Jon)
- [EDGECLOUD-4609](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4609)  CloudletDown alert not clearing when running 2 controllers in replica ([#1519](https://github.com/mobiledgex/edge-cloud/pull/1519)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5475](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5475) [EDGECLOUD-5465](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5465) rate limit api minor fixes ([#1771](https://github.com/mobiledgex/edge-cloud-infra/pull/1771)) (Jon)
- [EDGECLOUD-4609](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4609)  CloudletDown alert not clearing when running 2 controllers in replica ([#1770](https://github.com/mobiledgex/edge-cloud-infra/pull/1770)) (Lev Shvarts)

## [2021-10-06] - Oct 06, 2021
[Details](../../commit/2021-10-06)

### edge-cloud:
- [EDGECLOUD-5487](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5487) [EDGECLOUD-5481](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5481) [EDGECLOUD-5480](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5480) ratelimit err msg fixes ([#1518](https://github.com/mobiledgex/edge-cloud/pull/1518)) (Jon)

## [2021-10-05] - Oct 05, 2021
[Details](../../commit/2021-10-05)

### edge-cloud-infra:
- Fix entrypoint in debug docker baseimages ([#1768](https://github.com/mobiledgex/edge-cloud-infra/pull/1768)) (Venky)

## [2021-10-03] - Oct 03, 2021
[Details](../../commit/2021-10-03)

### edge-cloud:
- Docker base image bump ([#1515](https://github.com/mobiledgex/edge-cloud/pull/1515)) (Venky)

## [2021-10-02] - Oct 02, 2021
[Details](../../commit/2021-10-02)

### edge-cloud:
- Cloudlet cleanup onerr ([#1516](https://github.com/mobiledgex/edge-cloud/pull/1516)) (Jim)
- [EDGECLOUD-5494](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5494) able to add more rate limit flows than maxnumperipratelimiters ([#1514](https://github.com/mobiledgex/edge-cloud/pull/1514)) (Jon)
- [EDGECLOUD-5658](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5658) able to add the same alliance org twice to the same cloudlet ([#1513](https://github.com/mobiledgex/edge-cloud/pull/1513)) (Jon)

### edge-cloud-infra:
- Cloudlet cleanup onerr ([#1767](https://github.com/mobiledgex/edge-cloud-infra/pull/1767)) (Jim)
- [EDGECLOUD-5494](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5494) able to add more rate limit flows than maxnumperipratelimiters ([#1765](https://github.com/mobiledgex/edge-cloud-infra/pull/1765)) (Jon)
- Docker base image build workflow ([#1766](https://github.com/mobiledgex/edge-cloud-infra/pull/1766)) (Venky)

## [2021-10-01] - Oct 01, 2021
[Details](../../commit/2021-10-01)

### edge-cloud:
- Switch to debug images for component docker images ([#1512](https://github.com/mobiledgex/edge-cloud/pull/1512)) (Venky)
- [EDGECLOUD-5623](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5623) DME rate limiting not working with Global apiname ([#1506](https://github.com/mobiledgex/edge-cloud/pull/1506)) (Jon)

## [2021-09-30] - Sep 30, 2021
[Details](../../commit/2021-09-30)

### edge-cloud:
- [EDGECLOUD-5609](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5609) ShowFlavorsFor API Optional Arg to Filter By Operator ([#1509](https://github.com/mobiledgex/edge-cloud/pull/1509)) (Jon)
- [EDGECLOUD-5561](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5561) debug: appinstlatency request failing with deadline exceeded ([#1511](https://github.com/mobiledgex/edge-cloud/pull/1511)) (Jon)
- [EDGECLOUD-5502](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5502) Correcting capitalization ([#1510](https://github.com/mobiledgex/edge-cloud/pull/1510)) (Bruce Armstrong)
   - * [EDGECLOUD-5502](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5502) Correcting capitalization
- [EDGECLOUD-5626](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5626) Alert for RootLB down has "instance" in the labels ([#1508](https://github.com/mobiledgex/edge-cloud/pull/1508)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5614](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5614) [EDGECLOUD-5626](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5626) Metrics bugs ([#1764](https://github.com/mobiledgex/edge-cloud-infra/pull/1764)) (Lev Shvarts)
- [EDGECLOUD-5618](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5618) AddCloudletPoolMember without region gives wrong error message ([#1763](https://github.com/mobiledgex/edge-cloud-infra/pull/1763)) (Jon)

## [2021-09-29-1] - Sep 29, 2021
[Details](../../commit/2021-09-29-1)

### edge-cloud:
- [EDGECLOUD-5656](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5656) Report generation fails with error "Missing logo" ([#1507](https://github.com/mobiledgex/edge-cloud/pull/1507)) (Venky)

## [2021-09-29] - Sep 29, 2021
[Details](../../commit/2021-09-29)

### edge-cloud:
- [EDGECLOUD-5648](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5648) [EDGECLOUD-5647](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5647) fix various help comments ([#1505](https://github.com/mobiledgex/edge-cloud/pull/1505)) (Jon)
- [EDGECLOUD-5653](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5653): US Controller keeps crashing during regression run ([#1504](https://github.com/mobiledgex/edge-cloud/pull/1504)) (Ashish Jain)
- [EDGECLOUD-5604](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5604)  active connections graph data appears to go backward when two apps share the same internal port ([#1503](https://github.com/mobiledgex/edge-cloud/pull/1503)) (Lev Shvarts)
- [EDGECLOUD-5642](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5642) bad allianceorg gives for forbidden ([#1502](https://github.com/mobiledgex/edge-cloud/pull/1502)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5254](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5254) Validate limit or numsamples is a positive value ([#1762](https://github.com/mobiledgex/edge-cloud-infra/pull/1762)) (Bruce Armstrong)
   - * [EDGECLOUD-5254](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5254) Validate limit is a positive value
- [EDGECLOUD-5648](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5648) [EDGECLOUD-5647](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5647) fix various help comments ([#1761](https://github.com/mobiledgex/edge-cloud-infra/pull/1761)) (Jon)
- [EDGECLOUD-5642](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5642) bad allianceorg gives for forbidden ([#1759](https://github.com/mobiledgex/edge-cloud-infra/pull/1759)) (Jon)
- Switch back to the full edge-cloud image for the controller ([#1760](https://github.com/mobiledgex/edge-cloud-infra/pull/1760)) (Venky)

### edge-proto:
- [EDGECLOUD-5648](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5648) fix help comments capitalization ([#46](https://github.com/mobiledgex/edge-proto/pull/46)) (Jon)

## [2021-09-28] - Sep 28, 2021
[Details](../../commit/2021-09-28)

### edge-cloud:
- Switch to component-specific docker images ([#1499](https://github.com/mobiledgex/edge-cloud/pull/1499)) (Venky)

### edge-cloud-infra:
- Switch to component-specific docker images ([#1757](https://github.com/mobiledgex/edge-cloud-infra/pull/1757)) (Venky)

## [2021-09-25] - Sep 25, 2021
[Details](../../commit/2021-09-25)

### edge-cloud:
- Cluster networks ([#1492](https://github.com/mobiledgex/edge-cloud/pull/1492)) (Jim)
- [EDGECLOUD-5623](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5623) spew-rate-limit-mgr ([#1500](https://github.com/mobiledgex/edge-cloud/pull/1500)) (Jon)

### edge-cloud-infra:
- fix GetAppInstRuntime in public cloudlet CRM ([#1753](https://github.com/mobiledgex/edge-cloud-infra/pull/1753)) (Jim)
- initial changes ([#1754](https://github.com/mobiledgex/edge-cloud-infra/pull/1754)) (Jim)

## [2021-09-23] - Sep 23, 2021
[Details](../../commit/2021-09-23)

### edge-cloud:
- [EDGECLOUD-5549](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5549) Cloudlet alliance orgs ([#1495](https://github.com/mobiledgex/edge-cloud/pull/1495)) (Jon)
- [EDGECLOUD-5630](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5630): After updating a k8s appinst the runcommand tries to fetch the old pod name ([#1498](https://github.com/mobiledgex/edge-cloud/pull/1498)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5549](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5549) Cloudlet alliance orgs ([#1755](https://github.com/mobiledgex/edge-cloud-infra/pull/1755)) (Jon)
- Rename ctrlapi package to ctrlclient ([#1756](https://github.com/mobiledgex/edge-cloud-infra/pull/1756)) (Ashish Jain)

## [2021-09-22] - Sep 22, 2021
[Details](../../commit/2021-09-22)

### edge-cloud:
- [EDGECLOUD-5624](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5624) controller crash on appinstrefs DeleteRequestedInsts ([#1497](https://github.com/mobiledgex/edge-cloud/pull/1497)) (Jon)
- [EDGECLOUD-5596](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5596) mcctl audit operation bad args causes mcctl crash ([#1496](https://github.com/mobiledgex/edge-cloud/pull/1496)) (Jon)

## [2021-09-21] - Sep 21, 2021
[Details](../../commit/2021-09-21)

### edge-cloud:
- unit test fixes ([#1493](https://github.com/mobiledgex/edge-cloud/pull/1493)) (Jon)

### edge-cloud-infra:
- unit test fixes ([#1751](https://github.com/mobiledgex/edge-cloud-infra/pull/1751)) (Jon)

## [2021-09-18] - Sep 18, 2021
[Details](../../commit/2021-09-18)

### edge-cloud-infra:
- [EDGECLOUD-5584](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5584) cloudletusage metrics gives db error when using unknown cloudlet org ([#1752](https://github.com/mobiledgex/edge-cloud-infra/pull/1752)) (Lev Shvarts)
- Move controller gRPC client calls from orm to ctrlapi package ([#1750](https://github.com/mobiledgex/edge-cloud-infra/pull/1750)) (Ashish Jain)

## [2021-09-16] - Sep 16, 2021
[Details](../../commit/2021-09-16)

### edge-cloud:
- Disable alert policy on MT clusters ([#1489](https://github.com/mobiledgex/edge-cloud/pull/1489)) (Lev Shvarts)
- fix e2e test ([#1490](https://github.com/mobiledgex/edge-cloud/pull/1490)) (Jim)
- [EDGECLOUD-5602](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5602) Edge-cloud docker baseimage update for security issues ([#1487](https://github.com/mobiledgex/edge-cloud/pull/1487)) (Venky)

### edge-cloud-infra:
- fix infra e2e test ([#1748](https://github.com/mobiledgex/edge-cloud-infra/pull/1748)) (Jim)
- KIND platform integration for shepherd ([#1746](https://github.com/mobiledgex/edge-cloud-infra/pull/1746)) (Lev Shvarts)
- [EDGECLOUD-5584](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5584)  cloudletusage metrics gives db error when using unknown cloudlet org ([#1743](https://github.com/mobiledgex/edge-cloud-infra/pull/1743)) (Lev Shvarts)
- [EDGECLOUD-5602](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5602) Edge-cloud docker baseimage update for security issues ([#1745](https://github.com/mobiledgex/edge-cloud-infra/pull/1745)) (Venky)
- Move common functions from orm package to ormutil package ([#1747](https://github.com/mobiledgex/edge-cloud-infra/pull/1747)) (Ashish Jain)

## [2021-09-15] - Sep 15, 2021
[Details](../../commit/2021-09-15)

### edge-cloud:
- fix race condition when doing multiple updates ([#1488](https://github.com/mobiledgex/edge-cloud/pull/1488)) (Jim)

## [2021-09-14] - Sep 14, 2021
[Details](../../commit/2021-09-14)

### edge-cloud-infra:
- [EDGECLOUD-5597](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5597): GPU cluster instance creation fails with ssh connection rejected issue on KDDI setup ([#1744](https://github.com/mobiledgex/edge-cloud-infra/pull/1744)) (Ashish Jain)

## [2021-09-11] - Sep 11, 2021
[Details](../../commit/2021-09-11)

### edge-cloud-infra:
- Wildcard selector(*) for group metrics ([#1735](https://github.com/mobiledgex/edge-cloud-infra/pull/1735)) (Lev Shvarts)

## [2021-09-09] - Sep 09, 2021
[Details](../../commit/2021-09-09)

### edge-cloud:
- Fix CRM server unit test ([#1483](https://github.com/mobiledgex/edge-cloud/pull/1483)) (Ashish Jain)

## [2021-09-08] - Sep 08, 2021
[Details](../../commit/2021-09-08)

### edge-cloud:
- add const for disk ([#1486](https://github.com/mobiledgex/edge-cloud/pull/1486)) (Jim)

### edge-cloud-infra:
- vcd disk usage ([#1742](https://github.com/mobiledgex/edge-cloud-infra/pull/1742)) (Jim)
- use common namespace code so metadata:name is applied ([#1738](https://github.com/mobiledgex/edge-cloud-infra/pull/1738)) (Jim)
- [EDGECLOUD-5578](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5578): Add ability in Chef to perform actions like stop, restart, delete on docker containers ([#1736](https://github.com/mobiledgex/edge-cloud-infra/pull/1736)) (Ashish Jain)
- Missed updating chef cookbooks/policy ([#1739](https://github.com/mobiledgex/edge-cloud-infra/pull/1739)) (Venky)
- Turn on commercial certs ([#1737](https://github.com/mobiledgex/edge-cloud-infra/pull/1737)) (Venky)

## [2021-09-07] - Sep 07, 2021
[Details](../../commit/2021-09-07)

### edge-cloud:
- use wildcard certs ([#1484](https://github.com/mobiledgex/edge-cloud/pull/1484)) (Jim)
- [EDGECLOUD-5499](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5499) kafka messages don't have a timestamp ([#1481](https://github.com/mobiledgex/edge-cloud/pull/1481)) (Jon)

## [2021-09-06] - Sep 06, 2021
[Details](../../commit/2021-09-06)

### edge-cloud:
- separate UpdateLoadBalancerPortMap into new function ([#1480](https://github.com/mobiledgex/edge-cloud/pull/1480)) (Jim)
   - [EDGECLOUD-5558](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5558) Shepherd cannot collect prometheus stats with MetalLB IP

### edge-cloud-infra:
- Fix Prometheus when using MetalLB ([#1729](https://github.com/mobiledgex/edge-cloud-infra/pull/1729)) (Jim)

## [2021-09-05] - Sep 05, 2021
[Details](../../commit/2021-09-05)

### edge-cloud:
- [EDGECLOUD-5565](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5565): R3.0 Orange_Spain MXFUN-EDC99 cloudlet upgrade failed ([#1482](https://github.com/mobiledgex/edge-cloud/pull/1482)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5565](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5565): R3.0 Orange_Spain MXFUN-EDC99 cloudlet upgrade failed ([#1733](https://github.com/mobiledgex/edge-cloud-infra/pull/1733)) (Ashish Jain)
- [EDGECLOUD-5564](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5564): R3.0 NTT VM Pool cloudlet upgrade failed ([#1732](https://github.com/mobiledgex/edge-cloud-infra/pull/1732)) (Ashish Jain)
- Compact and defrag etcd after backup ([#1734](https://github.com/mobiledgex/edge-cloud-infra/pull/1734)) (Venky)

## [2021-09-04] - Sep 04, 2021
[Details](../../commit/2021-09-04)

### edge-cloud-infra:
- [EDGECLOUD-5547](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5547)  docker app instance stats are showing >100% ([#1730](https://github.com/mobiledgex/edge-cloud-infra/pull/1730)) (Lev Shvarts)

## [2021-09-03] - Sep 03, 2021
[Details](../../commit/2021-09-03)

### edge-cloud:
- add apiname to createapiendpointlimiter ([#1479](https://github.com/mobiledgex/edge-cloud/pull/1479)) (franklin-huang-mobiledgex)

### edge-cloud-infra:
- [EDGECLOUD-5530](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5530) metrics maxmetricsdatapoints is not honored ([#1731](https://github.com/mobiledgex/edge-cloud-infra/pull/1731)) (Lev Shvarts)
- Region cluster upgrades in main ([#1728](https://github.com/mobiledgex/edge-cloud-infra/pull/1728)) (Venky)
- createuser api name var ([#1727](https://github.com/mobiledgex/edge-cloud-infra/pull/1727)) (franklin-huang-mobiledgex)

## [2021-09-02] - Sep 02, 2021
[Details](../../commit/2021-09-02)

### edge-cloud:
- [EDGECLOUD-5560](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5560) reservable clusterinsts deleted on controller restart ([#1478](https://github.com/mobiledgex/edge-cloud/pull/1478)) (Jon)
- [EDGECLOUD-5538](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5538) Need configurable cluster-svc app flavor ([#1474](https://github.com/mobiledgex/edge-cloud/pull/1474)) (Lev Shvarts)
- [EDGECLOUD-5512](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5512): Add debug command to trigger refresh of RootLB certs ([#1476](https://github.com/mobiledgex/edge-cloud/pull/1476)) (Ashish Jain)
- [EDGECLOUD-5556](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5556): Sidecar app creation fails when controller is on R3.0 and CRM is on R2.4.x ([#1477](https://github.com/mobiledgex/edge-cloud/pull/1477)) (Ashish Jain)
- [EDGECLOUD-5527](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5527) able to delete Cloudlet with associated AutoProvPolicy ([#1475](https://github.com/mobiledgex/edge-cloud/pull/1475)) (Jon)
- Continuous query and retention fixes ([#1472](https://github.com/mobiledgex/edge-cloud/pull/1472)) (franklin-huang-mobiledgex)

### edge-cloud-infra:
- [EDGECLOUD-5538](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5538) Need configurable cluster-svc app flavor ([#1723](https://github.com/mobiledgex/edge-cloud-infra/pull/1723)) (Lev Shvarts)
- [EDGECLOUD-5554](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5554): GPU driver state is not shown for Operator Manager ([#1725](https://github.com/mobiledgex/edge-cloud-infra/pull/1725)) (Ashish Jain)
- fix anthos sharedlb certs ([#1726](https://github.com/mobiledgex/edge-cloud-infra/pull/1726)) (Jim)

## [2021-09-01] - Sep 01, 2021
[Details](../../commit/2021-09-01)

### edge-cloud:
- [EDGECLOUD-5513](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5513) add cloudletpool member required args ([#1473](https://github.com/mobiledgex/edge-cloud/pull/1473)) (Jon)

### edge-cloud-infra:
- Cluster and cloudlet grouped metrics api ([#1716](https://github.com/mobiledgex/edge-cloud-infra/pull/1716)) (Lev Shvarts)
- [EDGECLOUD-5551](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5551) VCD cloudlet metrics don't get recorded ([#1724](https://github.com/mobiledgex/edge-cloud-infra/pull/1724)) (Lev Shvarts)
- [EDGECLOUD-5514](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5514) authz addcloudletpoolmember fix error messages ([#1721](https://github.com/mobiledgex/edge-cloud-infra/pull/1721)) (Jon)
- [EDGECLOUD-5548](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5548) CVE-2021-3711/12 - Base image needs openssl package update ([#1722](https://github.com/mobiledgex/edge-cloud-infra/pull/1722)) (Venky)
- Flag to control actual staging deployment ([#1720](https://github.com/mobiledgex/edge-cloud-infra/pull/1720)) (Venky)

## [2021-08-31] - Aug 31, 2021
[Details](../../commit/2021-08-31)

### edge-cloud:
- Influxq unittest fix ([#1471](https://github.com/mobiledgex/edge-cloud/pull/1471)) (franklin-huang-mobiledgex)

## [2021-08-30] - 2021-08-30
[Details](../../commit/2021-08-30)

### edge-cloud-infra:
- fix edgeevent unit test: remove appinsts to clear out maps ([#1718](https://github.com/mobiledgex/edge-cloud-infra/pull/1718)) (franklin-huang-mobiledgex)
- [EDGECLOUD-5529](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5529) [EDGECLOUD-5534](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5534) Check for startage/endage. Change Port from value to a tag ([#1717](https://github.com/mobiledgex/edge-cloud-infra/pull/1717)) (Lev Shvarts)
   - [EDGECLOUD-5534](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5534)
   - [EDGECLOUD-5529](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5529)

## [2021-08-29] - 2021-08-29
[Details](../../commit/2021-08-29)

### edge-cloud:
- [EDGECLOUD-4438](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4438), [EDGECLOUD-5324](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5324) ([#1465](https://github.com/mobiledgex/edge-cloud/pull/1465)) (franklin-huang-mobiledgex)
- MetalLB and Anthos ([#1469](https://github.com/mobiledgex/edge-cloud/pull/1469)) (Jim)
- fix anthos autocluster ([#1470](https://github.com/mobiledgex/edge-cloud/pull/1470)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-4438](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4438), [EDGECLOUD-5324](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5324) ([#1709](https://github.com/mobiledgex/edge-cloud-infra/pull/1709)) (franklin-huang-mobiledgex)
- MetalLB and Anthos ([#1713](https://github.com/mobiledgex/edge-cloud-infra/pull/1713)) (Jim)

### edge-proto:
- [EDGECLOUD-4438](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4438), [EDGECLOUD-5324](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5324) ([#44](https://github.com/mobiledgex/edge-proto/pull/44)) (franklin-huang-mobiledgex)

## [2021-08-28] - 2021-08-28
[Details](../../commit/2021-08-28)

### edge-cloud-infra:
- make copies of props ([#1715](https://github.com/mobiledgex/edge-cloud-infra/pull/1715)) (Jim)

## [2021-08-27] - 2021-08-27
[Details](../../commit/2021-08-27)

### edge-cloud-infra:
- [EDGECLOUD-5496](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5496) [EDGECLOUD-5528](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5528)  App metrics response contains version value concatenated with app name for some app ([#1711](https://github.com/mobiledgex/edge-cloud-infra/pull/1711)) (Lev Shvarts)
   - [EDGECLOUD-5496](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5496)
   - [EDGECLOUD-5528](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5528)

## [2021-08-26-1] - 2021-08-26
[Details](../../commit/2021-08-26-1)

### edge-cloud:
- [EDGECLOUD-5512](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5512): Failed to refresh TLS certs as expired SSH certs are used ([#1468](https://github.com/mobiledgex/edge-cloud/pull/1468)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5512](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5512): Failed to refresh TLS certs as expired SSH certs are used ([#1712](https://github.com/mobiledgex/edge-cloud-infra/pull/1712)) (Ashish Jain)
- Enable Chargify in main and staging ([#1714](https://github.com/mobiledgex/edge-cloud-infra/pull/1714)) (Venky)

## [2021-08-25] - 2021-08-25
[Details](../../commit/2021-08-25)

### edge-cloud:
- Fix cleanup code ([#1466](https://github.com/mobiledgex/edge-cloud/pull/1466)) (Ashish Jain)

## [2021-08-24] - 2021-08-24
[Details](../../commit/2021-08-24)

### edge-cloud:
- [EDGECLOUD-4988](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4988) disallow cloudletpool add with existing developer objects ([#1463](https://github.com/mobiledgex/edge-cloud/pull/1463)) (Jon)
- renew the internal use mex certs ([#1464](https://github.com/mobiledgex/edge-cloud/pull/1464)) (Jim)

### edge-cloud-infra:
- [EDGECLOUD-4988](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4988) disallow cloudletpool add with existing developer objects ([#1708](https://github.com/mobiledgex/edge-cloud-infra/pull/1708)) (Jon)

## [2021-08-21] - 2021-08-21
[Details](../../commit/2021-08-21)

### edge-cloud:
- [EDGECLOUD-5142](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5142) Metrics - make use of MetricsCommon in App/Cluster/Cloudlet metrics([#1462](https://github.com/mobiledgex/edge-cloud/pull/1462)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5142](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5142)  Metrics - make use of MetricsCommon in App/Cluster/Cloudlet metrics ([#1707](https://github.com/mobiledgex/edge-cloud-infra/pull/1707)) (Lev Shvarts)

## [2021-08-20] - 2021-08-20
[Details](../../commit/2021-08-20)

### edge-cloud:
- Continuous query settings updates ([#1461](https://github.com/mobiledgex/edge-cloud/pull/1461)) (franklin-huang-mobiledgex)

### edge-cloud-infra:
- Continuous query settings updates ([#1705](https://github.com/mobiledgex/edge-cloud-infra/pull/1705)) (franklin-huang-mobiledgex)
- fix taint when master name is >63 char ([#1706](https://github.com/mobiledgex/edge-cloud-infra/pull/1706)) (Jim)

## [2021-08-17] - 2021-08-17
[Details](../../commit/2021-08-17)

### edge-cloud:
- [EDGECLOUD-5473](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5473) mcctl help text for alertpolicy need to capitalize sentences ([#1460](https://github.com/mobiledgex/edge-cloud/pull/1460)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-2352](https://mobiledgex.atlassian.net/browse/EDGECLOUD-2352) Clean up mexenv.json from local vault, comment changes ([#1703](https://github.com/mobiledgex/edge-cloud-infra/pull/1703)) (Lev Shvarts)

## [2021-08-15] - 2021-08-15
[Details](../../commit/2021-08-15)

### edge-cloud-infra:
- [EDGECLOUD-5469](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5469): mcctl "app create" needs updated arg description for accessports and skiphcports ([#1704](https://github.com/mobiledgex/edge-cloud-infra/pull/1704)) (Ashish Jain)

## [2021-08-14] - 2021-08-14 (R3.0 RC3)
[Details](../../commit/2021-08-14)

### edge-cloud:
- Fix maxpktsize config for k8s apps + fix comments ([#1459](https://github.com/mobiledgex/edge-cloud/pull/1459)) (Ashish Jain)
- Small followup for PR 1456 ([#1458](https://github.com/mobiledgex/edge-cloud/pull/1458)) (Lev Shvarts)

### edge-cloud-infra:
- Autogen file ([#1701](https://github.com/mobiledgex/edge-cloud-infra/pull/1701)) (Lev Shvarts)
- [EDGECLOUD-4894](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4894) Alerts: Request to include timestamp ([#1700](https://github.com/mobiledgex/edge-cloud-infra/pull/1700)) (Lev Shvarts)
- Bump up controller/DME replica count for QA ([#1702](https://github.com/mobiledgex/edge-cloud-infra/pull/1702)) (Venky)

## [2021-08-13] - 2021-08-13
[Details](../../commit/2021-08-13)

### edge-cloud:
- [EDGECLOUD-5448](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5448) alertpolicy tirigger-time needs to limit value of input([#1456](https://github.com/mobiledgex/edge-cloud/pull/1456)) (Lev Shvarts)
- [EDGECLOUD-5459](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5459): mcctl "ratelimitsettings showmaxreqs" does not work with filtering ([#1455](https://github.com/mobiledgex/edge-cloud/pull/1455)) (franklin-huang-mobiledgex)
- Fix docker exec command ([#1457](https://github.com/mobiledgex/edge-cloud/pull/1457)) (Ashish Jain)
   - [EDGECLOUD-5463](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5463): Envoy restarts on rootlb with TLS setting on access ports

### edge-cloud-infra:
- Disable VCD template import property ([#1699](https://github.com/mobiledgex/edge-cloud-infra/pull/1699)) (Jim)
- [EDGECLOUD-5448](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5448)  alertpolicy tirigger-time needs to limit value of input ([#1698](https://github.com/mobiledgex/edge-cloud-infra/pull/1698)) (Lev Shvarts)

## [2021-08-12] - 2021-08-12
[Details](../../commit/2021-08-12)

### edge-cloud:
- add UpdateClientCarrier to EdgeEventsHandler interface ([#1453](https://github.com/mobiledgex/edge-cloud/pull/1453)) (franklin-huang-mobiledgex)
- [EDGECLOUD-5463](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5463): Envoy restarts on rootlb with TLS setting on access ports ([#1454](https://github.com/mobiledgex/edge-cloud/pull/1454)) (Ashish Jain)

### edge-cloud-infra:
- optimize taint add/remove timing ([#1697](https://github.com/mobiledgex/edge-cloud-infra/pull/1697)) (Jim)
- add UpdateClientCarrier function to edgeeventshandler ([#1695](https://github.com/mobiledgex/edge-cloud-infra/pull/1695)) (franklin-huang-mobiledgex)
- [EDGECLOUD-5273](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5273) [EDGECLOUD-5248](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5248) [EDGECLOUD-5435](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5435) Metrics api fixes ([#1696](https://github.com/mobiledgex/edge-cloud-infra/pull/1696)) (Lev Shvarts)
   - * [EDGECLOUD-5273](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5273) unable to query dme metrics query with real cloudlet/cloudletorg
   - * [EDGECLOUD-5248](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5248) VM app instance disk stats are not reported correctly for OpenStack
   - * [EDGECLOUD-5435](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5435) metrics filtered by cluster-org doesn't work
- fix svc patching with namespace ([#1694](https://github.com/mobiledgex/edge-cloud-infra/pull/1694)) (Jim)

## [2021-08-11] - 2021-08-11
[Details](../../commit/2021-08-11)

### edge-cloud:
- Show ratelimit api fixes ([#1450](https://github.com/mobiledgex/edge-cloud/pull/1450)) (franklin-huang-mobiledgex)
   - * show flow/maxreqs filter by more than just key, remove extra args from showratelimitsettings ([EDGECLOUD-5315](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5315): unable to do "ratelimitsettingsmc show" by flowsettings or maxreqssettings)
- namespace service fix ([#1452](https://github.com/mobiledgex/edge-cloud/pull/1452)) (Jim)

### edge-cloud-infra:
- Show ratelimit mc api fixes ([#1692](https://github.com/mobiledgex/edge-cloud-infra/pull/1692)) (franklin-huang-mobiledgex)
   - * allow filter show flow/maxreqs mcratelimitsettings by more than just key, get rid of extra args for ShowRateLimitMcSettings ([EDGECLOUD-5315](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5315): unable to do "ratelimitsettingsmc show" by flowsettings or maxreqssettings, [EDGECLOUD-5310](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5310): ratelimitsettingsmc createflow of duplicate flow should give better error message)

## [2021-08-10] - 2021-08-10
[Details](../../commit/2021-08-10)

### edge-cloud:
- master taint fix ([#1451](https://github.com/mobiledgex/edge-cloud/pull/1451)) (Jim)
- [EDGECLOUD-5230](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5230): Envoy crashing for UDP packet size larger than 1500 ([#1443](https://github.com/mobiledgex/edge-cloud/pull/1443)) (Ashish Jain)

### edge-cloud-infra:
- master taint on update ([#1693](https://github.com/mobiledgex/edge-cloud-infra/pull/1693)) (Jim)
- [EDGECLOUD-5230](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5230): Envoy crashing for UDP packet size large than 1500 ([#1691](https://github.com/mobiledgex/edge-cloud-infra/pull/1691)) (Ashish Jain)

### edge-proto:
- [EDGECLOUD-5230](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5230): Envoy crashing for UDP packet size large than 1500 (Ashish Jain)
- change pktsize -> maxpktsize (Ashish Jain)
- Merge branch 'master' of github.com:mobiledgex/edge-proto into fixenvoyvers (Ashish Jain)
- [EDGECLOUD-5230](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5230): Envoy crashing for UDP packet size large than 1500 (Ashish Jain)

## [2021-08-08] - 2021-08-08
[Details](../../commit/2021-08-08)

### edge-cloud:
- [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):set cd.settings to defaults ([#1449](https://github.com/mobiledgex/edge-cloud/pull/1449)) (mwilliams-mex)
- developer namespaces ([#1448](https://github.com/mobiledgex/edge-cloud/pull/1448)) (Jim)
- [EDGECLOUD-5358](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5358): Add unit-tests for Operator's access to billing events ([#1438](https://github.com/mobiledgex/edge-cloud/pull/1438)) (Ashish Jain)

### edge-cloud-infra:
- developer namespaces ([#1690](https://github.com/mobiledgex/edge-cloud-infra/pull/1690)) (Jim)
- [EDGECLOUD-5358](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5358): Add unit-tests for Operator's access to billing events ([#1672](https://github.com/mobiledgex/edge-cloud-infra/pull/1672)) (Ashish Jain)

## [2021-08-07] - 2021-08-07
[Details](../../commit/2021-08-07)

### edge-cloud:
- Ratelimit settings api fixes ([#1446](https://github.com/mobiledgex/edge-cloud/pull/1446)) (franklin-huang-mobiledgex)
   - * [EDGECLOUD-5436](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5436): mcctl ratelimitsettings should make FlowAlgorithm required
   - * [EDGECLOUD-5438](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5438): ratelimitsettings reqsPerSecond/burstSize should be underscore format
   - * [EDGECLOUD-5432](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5432): ratelimitsettings for LeakyBucketAlgorithm should not require burstsize arg
- [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):Address potential race on thread startup with settings value ([#1447](https://github.com/mobiledgex/edge-cloud/pull/1447)) (mwilliams-mex)
- [EDGECLOUD-2583](https://mobiledgex.atlassian.net/browse/EDGECLOUD-2583): PlatformFindCloudlet with bad client_token returns wrong status code ([#1445](https://github.com/mobiledgex/edge-cloud/pull/1445)) (franklin-huang-mobiledgex)

### edge-cloud-infra:
- MC Ratelimit settings api fixes ([#1689](https://github.com/mobiledgex/edge-cloud-infra/pull/1689)) (franklin-huang-mobiledgex)
   - * [EDGECLOUD-5437](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5437): mcctl ratelimitsettingsmc createflow should make flow settings required
   - * [EDGECLOUD-5310](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5310): ratelimitsettingsmc createflow of duplicate flow should give better error message
- [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):fix units add misisng  m for settings e2e tests ([#1688](https://github.com/mobiledgex/edge-cloud-infra/pull/1688)) (mwilliams-mex)

## [2021-08-06] - 2021-08-06 (R3.0 RC2)
[Details](../../commit/2021-08-06)

### edge-cloud:
- Mark appinsts down when cloudlet down ([#1444](https://github.com/mobiledgex/edge-cloud/pull/1444)) (Jim)
- Resthrd ([#1441](https://github.com/mobiledgex/edge-cloud/pull/1441)) (mwilliams-mex)
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):InfraResourceUpdateThread initial
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):add update lastCloudletResRefreshTime
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):Review comments + e2e tests
- [EDGECLOUD-5427](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5427) allow operator to see apps for cloudlet pools ([#1442](https://github.com/mobiledgex/edge-cloud/pull/1442)) (Jon)

### edge-cloud-infra:
- fix e2e test affected by edge-cloud change ([#1686](https://github.com/mobiledgex/edge-cloud-infra/pull/1686)) (Jim)
- Resthrd ([#1687](https://github.com/mobiledgex/edge-cloud-infra/pull/1687)) (mwilliams-mex)
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):InfraResourceUpdateThread initial
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191): add new setting for e2e tests
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191): e2e data .yml files missing newlines at end of file
   - * [EDGECLOUD-5191](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5191):Add missing newlines at the end of the files
- [EDGECLOUD-5427](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5427) allow operator to see apps for cloudlet pools ([#1684](https://github.com/mobiledgex/edge-cloud-infra/pull/1684)) (Jon)

### edge-proto:
- Merge pull request #42 from mobiledgex/cloudlet-down (Jim)
- add HEALTH_CHECK_CLOUDLET_OFFLINE (Jim)

## [2021-08-05] - 2021-08-05
[Details](../../commit/2021-08-05)

### edge-cloud:
- [EDGECLOUD-5399](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5399)  Add information to help txt for alertpolicy annotations for description and title ([#1440](https://github.com/mobiledgex/edge-cloud/pull/1440)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5426](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5426): Fix issues with Operator's access to appinst/clusterinst billingevents ([#1685](https://github.com/mobiledgex/edge-cloud-infra/pull/1685)) (Ashish Jain)
- [EDGECLOUD-5399](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5399)  Add information to help txt for alertpolicy annotations for description and title ([#1683](https://github.com/mobiledgex/edge-cloud-infra/pull/1683)) (Lev Shvarts)

## [2021-08-04] - 2021-08-04
[Details](../../commit/2021-08-04)

### edge-cloud:
- Speed up docker builds using buildx ([#1439](https://github.com/mobiledgex/edge-cloud/pull/1439)) (Venky)
- [EDGECLOUD-5246](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5246) Trust Policy timeout error message fixed ([#1437](https://github.com/mobiledgex/edge-cloud/pull/1437)) (Devdatta)
   - * [EDGECLOUD-5246](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5246) Trust Policy timeout error message fixed
   - * [EDGECLOUD-5246](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5246) review comments addressed
   - * [EDGECLOUD-5246](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5246) Jon's review comments addressed
   - * [EDGECLOUD-5246](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5246) Jon's review comments2

### edge-cloud-infra:
- Vcd networks enhance ([#1676](https://github.com/mobiledgex/edge-cloud-infra/pull/1676)) (Jim)

## [2021-08-03] - 2021-08-03
[Details](../../commit/2021-08-03)

### edge-cloud:
- [EDGECLOUD-5268](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5268)  need to sanitize the metrics args before building and sending influxdb query ([#1436](https://github.com/mobiledgex/edge-cloud/pull/1436)) (Lev Shvarts)

### edge-cloud-infra:
- [EDGECLOUD-5268](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5268) need to sanitize the metrics args before building and sending influxdb query ([#1682](https://github.com/mobiledgex/edge-cloud-infra/pull/1682)) (Lev Shvarts)
- [EDGECLOUD-5268](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5268) need to sanitize the metrics args before building and sending influxdb query([#1674](https://github.com/mobiledgex/edge-cloud-infra/pull/1674)) (Lev Shvarts)
- [EDGECLOUD-5421](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5421): Remove latency stats from ClientApiUsage ([#1681](https://github.com/mobiledgex/edge-cloud-infra/pull/1681)) (franklin-huang-mobiledgex)
- [EDGECLOUD-5245](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5245) [EDGECLOUD-5127](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5127) Removed cluster and cluster-org from clientapi metrics. Added a null check ([#1679](https://github.com/mobiledgex/edge-cloud-infra/pull/1679)) (Lev Shvarts)
- [EDGECLOUD-5066](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5066) show filter by empty value failed because value null ([#1680](https://github.com/mobiledgex/edge-cloud-infra/pull/1680)) (Jon)
- [EDGECLOUD-5265](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5265) mc context deadline exceeded errors - conn cache ([#1678](https://github.com/mobiledgex/edge-cloud-infra/pull/1678)) (Jon)

## [2021-07-31] - 2021-07-31 (R3.0 RC1)
[Details](../../commit/2021-07-31)

### edge-cloud-infra:
- [EDGECLOUD-5405](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5405)  clientappusage metrics not giving the correct interval as developer ([#1677](https://github.com/mobiledgex/edge-cloud-infra/pull/1677)) (Lev Shvarts)
- Fix MC crash as ratelimitmgr is not initialised ([#1675](https://github.com/mobiledgex/edge-cloud-infra/pull/1675)) (Ashish Jain)

## [2021-07-30] - 2021-07-30
[Details](../../commit/2021-07-30)

### edge-cloud-infra:
- [EDGECLOUD-5389](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5389) Add case for an operator that is also a developer ([#1671](https://github.com/mobiledgex/edge-cloud-infra/pull/1671)) (Lev Shvarts)
- [EDGECLOUD-5389](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5389): Remove hardcoded controller notify port in MC ([#1673](https://github.com/mobiledgex/edge-cloud-infra/pull/1673)) (Ashish Jain)

## [2021-07-29] - 2021-07-29
[Details](../../commit/2021-07-29)

### edge-cloud-infra:
- [EDGECLOUD-5367](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5367): ShowFlavorsFor should be supported for developers ([#1669](https://github.com/mobiledgex/edge-cloud-infra/pull/1669)) (Ashish Jain)
- [EDGECLOUD-5241](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5241)  better error when using unsupported selectors ([#1667](https://github.com/mobiledgex/edge-cloud-infra/pull/1667)) (Lev Shvarts)
- [EDGECLOUD-5358](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5358): Operator Should be able to view Developer's Audit, Event and Usage if they are part of Cloudlet Pool ([#1670](https://github.com/mobiledgex/edge-cloud-infra/pull/1670)) (Ashish Jain)
- E2e clustersvc fix ([#1668](https://github.com/mobiledgex/edge-cloud-infra/pull/1668)) (Devdatta)

## [2021-07-28] - 2021-07-28
[Details](../../commit/2021-07-28)

### edge-cloud:
- Check trigger time correctly ([#1435](https://github.com/mobiledgex/edge-cloud/pull/1435)) (Lev Shvarts)

### edge-cloud-infra:
- e2e clusterSvc alert fixes ([#1666](https://github.com/mobiledgex/edge-cloud-infra/pull/1666)) (Devdatta)
- Change pod cpu promql query ([#1665](https://github.com/mobiledgex/edge-cloud-infra/pull/1665)) (Lev Shvarts)

## [2021-07-27] - 2021-07-27
[Details](../../commit/2021-07-27)

### edge-cloud:
- [EDGECLOUD-5343](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5343) rate limit mc e2e-test ShowApp2 failed ([#1434](https://github.com/mobiledgex/edge-cloud/pull/1434)) (Jon)
- [EDGECLOUD-5269](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5269) metrics request with startage lower than endage gives incorrect error ([#1432](https://github.com/mobiledgex/edge-cloud/pull/1432)) (Jon)
- Fix e2e-tests ([#1433](https://github.com/mobiledgex/edge-cloud/pull/1433)) (Ashish Jain)

### edge-cloud-infra:
- [EDGECLOUD-5343](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5343) rate limit mc e2e-test ShowApp2 failed ([#1664](https://github.com/mobiledgex/edge-cloud-infra/pull/1664)) (Jon)
- prometheus e2e-test fixes missing files ([#1663](https://github.com/mobiledgex/edge-cloud-infra/pull/1663)) (Jon)
- [EDGECLOUD-5328](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5328): GPUdriver gets pre-installed on k8s worker node in WWT setup ([#1661](https://github.com/mobiledgex/edge-cloud-infra/pull/1661)) (Ashish Jain)

## [2021-07-25] - 2021-07-25
[Details](../../commit/2021-07-25)

### edge-cloud:
- [EDGECLOUD-4292](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4292) e2e tests code for Cluster svc alerts ([#1428](https://github.com/mobiledgex/edge-cloud/pull/1428)) (Devdatta)
   - * [EDGECLOUD-4292](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4292) Alert needs to be raised by cluster-svc when prometheus deployment fails
   - * [EDGECLOUD-4292](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4292) Alert needs to be raised by cluster-svc when prometheus deployment fails - review comments
   - * [EDGECLOUD-4292](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4292) Alert needs to be raised by cluster-svc when prometheus deployment fails - review comments2
- [EDGECLOUD-5303](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5303) [EDGECLOUD-5304](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5304) error message mentions edgeproto ([#1430](https://github.com/mobiledgex/edge-cloud/pull/1430)) (Jon)
- prometheus e2e-test fixes ([#1429](https://github.com/mobiledgex/edge-cloud/pull/1429)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-4292](https://mobiledgex.atlassian.net/browse/EDGECLOUD-4292) e2e tests code for Cluster svc alerts ([#1657](https://github.com/mobiledgex/edge-cloud-infra/pull/1657)) (Devdatta)
   - * [EDGECLOUD-2044](https://mobiledgex.atlassian.net/browse/EDGECLOUD-2044): Suppressing show o/p for dynamic AppInst
- [EDGECLOUD-5303](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5303) [EDGECLOUD-5304](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5304) error message mentions edgeproto ([#1660](https://github.com/mobiledgex/edge-cloud-infra/pull/1660)) (Jon)
   - * [EDGECLOUD-5303](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5303) [EDGECLOUD-5304](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5304) error message mentions edgeproto
- prometheus e2e-test fixes ([#1658](https://github.com/mobiledgex/edge-cloud-infra/pull/1658)) (Jon)

## [2021-07-24] - 2021-07-24
[Details](../../commit/2021-07-24)

### edge-cloud:
- [EDGECLOUD-5335](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5335) Add a lockprotecting cpuprofile file ([#1431](https://github.com/mobiledgex/edge-cloud/pull/1431)) (Lev Shvarts)
- [EDGECLOUD-5327](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5327) mc crashes while performing operation with map based input ([#1427](https://github.com/mobiledgex/edge-cloud/pull/1427)) (Jon)

### edge-cloud-infra:
- [EDGECLOUD-5314](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5314) fix help ([#1659](https://github.com/mobiledgex/edge-cloud-infra/pull/1659)) (Jim)
- [EDGECLOUD-5328](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5328): GPUdriver gets pre-installed on k8s worker node in WWT setup ([#1656](https://github.com/mobiledgex/edge-cloud-infra/pull/1656)) (Ashish Jain)
   - * [EDGECLOUD-5328](https://mobiledgex.atlassian.net/browse/EDGECLOUD-5328): GPUdriver gets pre-installed on k8s worker node in WWT setup

