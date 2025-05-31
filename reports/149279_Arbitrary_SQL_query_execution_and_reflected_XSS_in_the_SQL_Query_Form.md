# Arbitrary SQL query execution and reflected XSS in the "SQL Query Form"

## Report Details
- **Report ID**: 149279
- **URL**: https://hackerone.com/reports/149279
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-05T06:37:06.437Z
- **Disclosed**: 2016-08-18T02:22:07.937Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
Hello,

The mentioned module is vulnerable to SQL injection due to the fact that a query can be done in a GET request, with the query is Base64 encoded and supplied as the value of the parameter "thequery".

This allows an attacker to perform arbitrary SQL queries if they trick an authenticated admin to click a specially crafted link, which can have devastating outcomes, including the deletion/dropping of whole records/databases, the insertion of new data, etc, following is a PoC:

http://localhost/ee/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw==

With c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw== as the Base64 encoded form of `select * from exp_members`.
Also, the same GET parameter is vulnerable to reflected XSS, which originates from the fact that MySQL errors get thrown unencoded when a malformed SQL query is processed. This, in combination with the previously mentioned flaw, can make an attacker not only capable of executing arbitrary SQL queries, but also able to read whatever data is returned from a query, in addition to the normal attacks that can be done with an XSS, following is a PoC:

http://localhost/ee/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg==

Where c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg== is the Base64 encoded form of `select <svg onload=alert(1)>`.

Regards

## Attachments
No attachments
