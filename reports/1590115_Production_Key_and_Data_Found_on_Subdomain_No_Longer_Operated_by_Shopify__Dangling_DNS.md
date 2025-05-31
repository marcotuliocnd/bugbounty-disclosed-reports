# Production Key and Data Found on Subdomain No Longer Operated by Shopify / Dangling DNS

## Report Details
- **Report ID**: 1590115
- **URL**: https://hackerone.com/reports/1590115
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-06-02T21:24:13.318Z
- **Disclosed**: 2024-05-01T18:17:15.231Z

## Reporter
- **Username**: ryanmoles6
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello, Shopify team.
I found the subdomain in
http://honeybee-honeybee-ingress-data-presto-us-central1-2.shopify-data-presto-global.shopifykloud.com/languages

I was allowed to view the source code of the app's configuration (I'm not really sure), he used base64 to encode the source file, I decrypted it through a third party and found a lot of source code, even including, some content that should not be on the internet, for this I recorded a demo video where I will show how I decrypted and retrieved sensitive information within the site

I didn't look at all the source code, I found one place where I could prove the harm



'''
SCAN

{"name":"main/settings.py

███


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '███'

'''

## Impact

Key compromise can cause takeover, or direct operation of the production environment

## Attachments
No attachments
