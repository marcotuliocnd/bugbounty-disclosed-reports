# Sql Injection At █████████

## Report Details
- **Report ID**: 1723896
- **URL**: https://hackerone.com/reports/1723896
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-05T22:29:42.868Z
- **Disclosed**: 2023-01-06T19:02:47.214Z

## Reporter
- **Username**: w13d0m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hi Security Team I Hope You Are Doing Well 

Sql Injection is a common attack vector that uses malicious SQL code for backend database manipulation to access information that was not intended to be displayed.


1: Visit This Endpoint ``  https://█████/ `` As You Can See This Website Using Asp.net That's Mean To Os Equal Windows.
2: Visit This Endpoint `` https://█████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568 `` As You Experienced  Sometimes To Check The Parameters Put``  '  `` To Know Vulnerable Or Not , If You Put `` ' `` In This Request As `` https://████████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568' `` The Response Said Invalid Request Means To Maybe Vulnerable.
3: So I Decided To Sure That This Endpoint Vulnerable To Sql Injection  Or Not , I Using Sqlmap As You Can See In My PoC Video.

## References

███

## Impact

The impact SQL injection can have on a business is far-reaching. A successful attack may result in the unauthorized viewing of user lists, the deletion of entire tables and, in certain cases, the attacker gaining administrative rights to a database, all of which are highly detrimental to a business.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1: Visit This Endpoint ``  https://███████/ `` As You Can See This Website Using Asp.net That's Mean To Os Equal Windows.
2: Visit This Endpoint `` https://██████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568 `` As You Experienced  Sometimes To Check The Parameters Put``  '  `` To Know Vulnerable Or Not , If You Put `` ' `` In This Request As `` https://██████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568' `` The Response Said Invalid Request Means To Maybe Vulnerable.
3: So I Decided To Sure That This Endpoint Vulnerable To Sql Injection  Or Not , I Using Sqlmap As You Can See In My PoC Video.


Thanks And King Regards

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
