# Information disclosure via enabled Django Debug Mode 

## Report Details
- **Report ID**: 2201370
- **URL**: https://hackerone.com/reports/2201370
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-11T12:54:23.270Z
- **Disclosed**: 2024-12-25T08:12:21.321Z

## Reporter
- **Username**: nhx1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

Vulnerable URL:  `██████████`

I observed that Django Debug Mode was enabled. It was leaking error messages and API endpoints so I decided to exploit it further to see what I could do. Here's a list of things I was able to do:

1. ** Register arbitrary user accounts **
2. ** Enumerate email addresses of registered user accounts **
3. **View all debug information such as API endpoints**
4. **Looks like it's also possible to fetch DNS records of registered domains from the endpoint `/api/domains/dns-records`, these records leak Origin IPs which might be highly confidential in nature** I haven't tested this from my end since I don't want to access any sensitive information. :) 


## API Information
{F2765264}

## Registering arbitrary user accounts
{F2765262}

## Email enumeration
{F2765267}



I stopped at this point so that you could review it from your end...

The email I used to registered was **██████**

## Steps To Reproduce:
[add details for how we can reproduce the issue]

### Request to register arbitrary user accounts and enumerate email addresses
```
POST /api/auth/register/ HTTP/1.1
Host: backend.webreg.mtn.zm
Cookie: ███████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html; q=1.0, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: ████████
X-Csrftoken: ██████████
X-Requested-With: XMLHttpRequest
Content-Length: 80
Origin: ██████████: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{
"email": "██████████",
"password": "password██████████"
}
```

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

An actor could get access to information he/she is not supposed to get.

## Attachments
- image.png
- image.png
- image.png
