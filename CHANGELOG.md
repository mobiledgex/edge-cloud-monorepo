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

