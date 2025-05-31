# Stored XSS in Document Title

## Report Details
- **Report ID**: 1321407
- **URL**: https://hackerone.com/reports/1321407
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-27T14:00:58.415Z
- **Disclosed**: 2021-09-27T14:00:01.507Z

## Reporter
- **Username**: thd3rboy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: localizejs

## Vulnerability Information
Summary :

Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS.

Vulnerable URL : https://app.localizestaging.com/documents

Payload XSS : 
"><img src=x onerror=alert(document.domain)> 

Step to Reproduces :
1. Login to your account
2. Create Project
3. What are you translating? (select documents)
4. Upload Document
5. Input XSS payload in Document Title = "><img src=x onerror=alert(document.domain)> 
6. Save it
7. XSS triggered

## Impact

Can steal Cookie, Can run javascript code, and get information sensitive

## Attachments
- Screenshot_20210827_205146.jpg
