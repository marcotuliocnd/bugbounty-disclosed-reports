# Grafana Improper authorization 

## Report Details
- **Report ID**: 802011
- **URL**: https://hackerone.com/reports/802011
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-21T18:58:16.337Z
- **Disclosed**: 2020-10-31T03:14:15.243Z

## Reporter
- **Username**: lazydog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
new report from part2.
wrong configuration causes Grafana datasource to use root user(with influxdb admin priv).

## Component Version:
test-infra:master

## Steps To Reproduce:
in normally configuration read-only user used by grafana, but in my test i found datasource user wite admin perms.
refer: https://github.com/kubernetes/test-infra/blob/master/velodrome/grafana-stack/datasource.sh
so i think maybe other scripts make this problem.

open url http://velodrome.k8s.io/, find the follwing requests:

```
GET /api/datasources/proxy/4/query?db=metrics&q=SELECT%20%0A%20%201-(sum(%22consistent_builds%22)%2Fsum(%22builds%22))%0AFROM%0A%20%20%22flakes_daily%22%20%0AWHERE%20%0A%20%20time%20%3E%20now()%20-%2030d%0A%20%20AND%20%22job%22%20%3D~%20%2F%5E(pr%3Apull-kubernetes-kubemark-e2e-gce-big%7Cpr%3Apull-kubernetes-bazel-build%7Cpr%3Apull-kubernetes-bazel-test%7Cpr%3Apull-kubernetes-dependencies%7Cpr%3Apull-kubernetes-e2e-gce%7Cpr%3Apull-kubernetes-e2e-gce-100-performance%7Cpr%3Apull-kubernetes-e2e-kind%7Cpr%3Apull-kubernetes-integration%7Cpr%3Apull-kubernetes-node-e2e%7Cpr%3Apull-kubernetes-typecheck%7Cpr%3Apull-kubernetes-verify)%24%2F%0Agroup%20by%20job%2C%20time(20m)%20fill(none)&epoch=ms HTTP/1.1
Host: velodrome.k8s.io
Accept: application/json, text/plain, */*
X-Grafana-Org-Id: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36 Edg/80.0.361.54
Referer: http://velodrome.k8s.io/dashboard/db/job-health-merge-blocking?orgId=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: close
```
By trying I found that this datasource is incorrectly configured with a user.
we can use admin perms user throuth proxy access Influxdb.
so I use this vuln, created a admin user.
{F724548}

execute ```show databases,``` we found that we have admin permissions
{F724549}

## Impact

maybe denial of service this component ,because admin can drop all Influxdb database.

## Attachments
- createuser.jpg
- withadminperms.jpg
