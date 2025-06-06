# Specially constructed multi-part requests cause multi-second response times; vulnerable to DoS

## Report Details
- **Report ID**: 431561
- **URL**: https://hackerone.com/reports/431561
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-31T00:31:56.429Z
- **Disclosed**: 2018-12-05T21:46:17.275Z

## Reporter
- **Username**: bjeanes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
The multi-part body parsing in Rack and consequently Rails has a worse-than-linear performance relative to the number of parts in the request body.

In small scale (i.e. non-disruptive) tests on a variety of Rails applications on the internet, including my own, GitHub.com, Heroku API, Instacart, Shopify, Bugcrowd, and others, it was trivial to cause request servicing to take long enough to cause gateway timeouts. It would not be particularly difficult to generate enough of these requests to tie up the majority of web serving resources for a typical Rails application.

This vulnerability has also been separately disclosed to rack-core mailing list by me.

## Steps To Reproduce:

I've created a script that can be run here against any Rack-based application: https://gist.github.com/bjeanes/63580e27c197885d4b07160fae132108

By default it generates a request body with 10,000 parts which, in my testing, was enough to cause GitHub API to take between 15-25 seconds to service the request once the request transfer had completed.

## Addendum

Some benchmarking of Rack is included here, which was also sent to rack-core:

```
N = number of parts, 
boundary used is as generated by Chrome, but larger boundaries cause
higher impact

Rehearsal --------------------------------------------
N: 1       0.032670   0.006635   0.039305 (  0.044159)
N: 100     0.008245   0.001319   0.009564 (  0.009971)
N: 1000    0.149332   0.079087   0.228419 (  0.255769)
N: 2000    0.398711   0.276931   0.675642 (  0.691356)
N: 5000    2.254126   1.569181   3.823307 (  3.871649)
N: 10000   7.134949   4.350681  11.485630 ( 12.083888)
N: 20000  15.946187  10.491861  26.438048 ( 28.684177)
---------------------------------- total: 42.699915sec

               user     system      total        real
N: 1       0.000372   0.000003   0.000375 (  0.000371)
N: 100     0.004889   0.000021   0.004910 (  0.004977)
N: 1000    0.117571   0.015548   0.133119 (  0.192915)
N: 2000    0.468934   0.309703   0.778637 (  0.870675)
N: 5000    2.086055   1.482317   3.568372 (  3.830543)
N: 10000   7.110589   4.488229  11.598818 ( 12.110710)
N: 20000  14.559701   9.948678  24.508379 ( 25.537332)
```

This is not technically in the Rails codebase, but it is in a non-optional dependency of every Rails application. Furthermore, I did receive some feedback from core members that a Rack vulnerability is likely to be eligible for this bounty: https://twitter.com/_matthewd/status/1057266505056800768.

Discovered by Bo Jeanes (@bjeanes) and Jack Chen (@chendo) and vetted after the fact by Charlie Somerville (@charliesome).

## Impact

Resource starvation of web request servicing, by causing multiple long-running requests. Attack can be constructed with just a HTML web form, making it literally click-button easy. That it can be generated from a form also has potential implications when combined with XSS or some other mechanism where an attacker could cause arbitrary user agents en masse to send such requests.

## Attachments
No attachments
