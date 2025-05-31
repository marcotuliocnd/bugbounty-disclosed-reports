# paypal client_id And stripe api key indexed on web archive

## Report Details
- **Report ID**: 2380084
- **URL**: https://hackerone.com/reports/2380084
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-02-19T14:19:23.738Z
- **Disclosed**: 2024-10-18T09:09:06.558Z

## Reporter
- **Username**: ghaazy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
hello security team i have found paypal cleient_id And stripe api key  and sentry dsn are indexed in web archive 
## Steps To Reproduce:
go to  https://web.archive.org/cdx/search/cdx?url=subscriptions.firefox.com/*&collapse=urlkey&output=text&fl=original
search for cliebtId 
you will find this 
```
https://subscriptions.firefox.com/%7B%22env%22%3A%22production%22%2C%22googleAnalytics%22%3A%7B%22enabled%22%3Atrue%2C%22measurementId%22%3A%22G-9N75BKQ2SE%22%2C%22supportedProductIds%22%3A%22prod_MIex7Q079igFZJ%2Cprod_KGizMiBqUJdYoY%2Cprod_FvnsFHIfezy3ZI%2Cprod_LKvr8fYGbBxcaZ%2Cprod_OiV9RSaatywSRy%22%2C%22debugMode%22%3Afalse%7D%2C%22legalDocLinks%22%3A%7B%22privacyNotice%22%3A%22https%3A%2F%2Fwww.mozilla.org%2Fprivacy%2Ffirefox-private-network%22%2C%22termsOfService%22%3A%22https%3A%2F%2Fwww.mozilla.org%2Fabout%2Flegal%2Fterms%2Ffirefox-private-network%22%7D%2C%22productRedirectURLs%22%3A%7B%22prod_FvnsFHIfezy3ZI%22%3A%22https%3A%2F%2Fwww.mozilla.org%2Fproducts%2Fvpn%2Fdownload%2F%22%7D%2C%22sentry%22%3A%7B%22dsn%22%3A%22https%3A%2F%2Fbd67bbdfad9b46a7a2f0faf4aa02c122%40o1069899.ingest.sentry.io%2F6231072%22%2C%22env%22%3A%22prod%22%2C%22sampleRate%22%3A1%2C%22serverName%22%3A%22fxa-payments-broker%22%2C%22clientName%22%3A%22fxa-payments-client%22%7D%2C%22servers%22%3A%7B%22auth%22%3A%7B%22url%22%3A%22https%3A%2F%2Fapi.accounts.firefox.com%22%7D%2C%22content%22%3A%7B%22url%22%3A%22https%3A%2F%2Faccounts.firefox.com%22%7D%2C%22oauth%22%3A%7B%22url%22%3A%22https%3A%2F%2Foauth.accounts.firefox.com%22%2C%22clientId%22%3A%2259cceb6f8c32317c%22%7D%2C%22profile%22%3A%7B%22url%22%3A%22https%3A%2F%2Fprofile.accounts.firefox.com%22%7D%7D%2C%22paypal%22%3A%7B%22apiUrl%22%3A%22https%3A%2F%2Fwww.paypal.com%22%2C%22clientId%22%3A%22Adb5V3A0jC394H-2nZL9JRBzcre0bNjxm_tqzezZDTTSheL4ANKqvG79uyDw1lwtxuXbDPK7Kdp6pMbr%22%2C%22scriptUrl%22%3A%22https%3A%2F%2Fwww.paypal.com%22%7D%2C%22stripe%22%3A%7B%22apiKey%22%3A%22pk_live_HgtiWdwlc5Uq8ZRsPAXIAyRY00CA51o613%22%7D%2C%22version%22%3A%221.275.3%22%7D
```
i decoded it and then used https://beautifier.io/ to make it look better 
and i found this 
{F3060182}

you need to request from internet archive to exclude subscriptions.firefox.com
because as you an see here 
{F3060188}
these data is new and indexed in Jan 12, 2024

## Impact

## Summary:
exposure of sensitive data

## Attachments
- image.png
- image.png
