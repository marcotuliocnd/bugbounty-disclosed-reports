# Bypass apiserver proxy filter

## Report Details
- **Report ID**: 859962
- **URL**: https://hackerone.com/reports/859962
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-27T00:04:50.125Z
- **Disclosed**: 2021-05-27T19:11:03.856Z

## Reporter
- **Username**: javierprovecho
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:

TL,DR: Time-of-check (apiserver proxy filter) Time-of-use (apiserver proxy request) Race Condition.

When the apiserver is proxying a request to a node though one of its addresses, it performs a filter validation. If the address type is a DNS record (Hostname, ExternalDNS, InternalDNS), the apiserver performs two DNS queries, one for filter validation, another for proxying the request. If the attacker sets the hostname to a custom DNS server, that is able return different values with zero TTL, it is possible to bypass that filter. 

## Kubernetes Version:
1.18.0

## Steps To Reproduce:

### Preparation

  1. Create a server with port UDP/53 (DNS) exposed.
  2. Delegate a subdomain (e.g. fake.example.com) to the IP address of the server as a NS record.
  3. Copy, build and run the custom DNS server (source code attached, use `go mod init` and `go mod tidy`).
  4. Test that it successfully resolves any subdomain of the delegated zone (e.g. toctou.fake.example.com).

### Execution

  1. Create a KIND cluster (manifest attached, defaults to v1.17).
  2. Create a Node (manifest attached, edit to change domain).
  3. Start `kubectl proxy`.
  4. Execute `curl localhost:8001/api/v1/nodes/toctou:80/proxy/`.

## Supporting Material/References:

  * `toctou-cluster.yml`, a KIND cluster manifest
  * `toctou-node.yml`, a Node with a custom address.
  * `toctou-dns-server.go`, a custom DNS server that returns different results to consecutive queries.

## Impact

https://github.com/kubernetes/kubernetes/pull/71980 was merged to mitigate dangerous proxying through the apiserver. An attacker with access to create nodes and send requests to them through apiserver proxy, could access cloud metadata endpoints or localhost services. This is specially important on as a service providers like https://github.com/oneinfra/oneinfra but could affect any vendor.

## Attachments
- toctou-dns-server.go
- toctou-node.yml
- toctou-cluster.yml
