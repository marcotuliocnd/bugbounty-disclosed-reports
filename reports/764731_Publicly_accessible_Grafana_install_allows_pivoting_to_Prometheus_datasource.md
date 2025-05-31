# Publicly accessible Grafana install allows pivoting to Prometheus datasource

## Report Details
- **Report ID**: 764731
- **URL**: https://hackerone.com/reports/764731
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-26T12:27:07.725Z
- **Disclosed**: 2020-05-14T17:11:26.153Z

## Reporter
- **Username**: gnarlygoat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A publicly accessible Grafana install exposes semi sensitive Dashboards. This also exposes the Prometheus proxied datasources which allow direct queries to a Prometheus instance which reveals sensitive data an opens the instance up to potential DoS via crafted requests.

**Description:**

## Impact
Medium-Low

## Step-by-step Reproduction Instructions

1. Grafana instance - https://████████/stats/
2. Example semi sensitive dashboard: https://████████/stats/d/███/
3. This dashboard reveals an unrestricted Prometheus proxy API at https://███/stats/api/datasources/proxy/1/api/v1/
4. This API can be queried in many ways to include resource intensive queries which could result in a DoS. An example of exposed datasets:
https://██████/stats/api/datasources/proxy/1/api/v1/label/__name__/values. A query crafted to require high resource usage would result in a denial of service.
5. This can reveal much more sensitive data as well such as internal ip addresess assigned to interfaces https://████/stats/api/datasources/proxy/1/api/v1/query?query=node_network_address_assign_type

 or

`curl -s 'https://██████/stats/api/datasources/proxy/1/api/v1/query?query=node_network_address_assign_type' |     python2 -c "import sys, json; print json.load(sys.stdin)['data']['result'][0]"`
 (Ip addresses are in decimal)

## Product, Version, and Configuration (If applicable)
 Grafana v6.4.4 
## Suggested Mitigation/Remediation Actions
Implement controls to disallow public access

## Impact

Denial of Service
Utilize exposed network and device data for network reconnaissance

## Attachments
No attachments
