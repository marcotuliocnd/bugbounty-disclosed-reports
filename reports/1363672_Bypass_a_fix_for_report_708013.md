# Bypass a fix for report #708013

## Report Details
- **Report ID**: 1363672
- **URL**: https://hackerone.com/reports/1363672
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-08T13:32:44.319Z
- **Disclosed**: 2021-12-07T13:14:41.104Z

## Reporter
- **Username**: scaramouche31
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
`customerAccessTokenCreate` mutation in the Storefront API does not correctly throttle login attempts. An issue in similar report https://hackerone.com/reports/708013 was already fixed, however, there is still a bypass.

## Steps To Reproduce:
1. Grab a Storefront  API Token (I got it from the Buy Button App)
2. Make a request to the Storefront GraphQL endpoint (you can use mine):
```
POST /api/2020-07/graphql HTTP/2
Host: scara31-store3.myshopify.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json
Accept-Language: *
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Sdk-Variant: javascript
X-Sdk-Version: 2.11.0
X-Shopify-Storefront-Access-Token: 2951b2eb0072b7751631108de6c46359
X-Sdk-Variant-Source: buy-button-js
Origin: null
Content-Length: 161
Te: trailers

{"query":"mutation { customerAccessTokenCreate(input: {email: \"███\", password: \"████████\" }) { customerAccessToken { accessToken } } }"}
```
The actual creds are ███████ - █████████
3. Send requests until you get `Login attempt limit exceeded`
4. Add a whitespace at the end of email.
5. Observe that you have bypassed the limit though the email is still valid (to prove it try `{email: \"█████ \", password: \"███\" }` and get the token)
Video PoC:
███████

##Possible remediation:
Consider whitespace as a character. I would also recommend to try some other stuff like empty character (https://emptycharacter.com/) and null byte in different forms.

## Supporting Material:
https://hackerone.com/reports/708013

I hope I don't need to write too much about the attack scenario, PoC script for bruteforce and Impact as the very same report was already accepted.

## Impact

If the brute force attack succeeds, the attacker will gain access to user's Shopify account, including contact information and order history.

## Attachments
No attachments
