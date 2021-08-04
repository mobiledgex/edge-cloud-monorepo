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

## [2021-07-31] - 2021-07-31
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

