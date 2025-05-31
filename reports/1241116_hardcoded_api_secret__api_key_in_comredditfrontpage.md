# hardcoded api secret & api key in com.reddit.frontpage

## Report Details
- **Report ID**: 1241116
- **URL**: https://hackerone.com/reports/1241116
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-06-22T12:54:48.583Z
- **Disclosed**: 2021-10-21T19:47:40.687Z

## Reporter
- **Username**: 0xcharan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
hi security team,
in file Resources/Resources.arsc/res/values/strings.xml
i have found
<string name="twitter_consumer_key">███</string>
<string name="twitter_consumer_secret">███</string>

It shouldn't be disclosed to third parties it meant for deveoplers as per https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens

poc:-
curl --user "██████:███"  --data 'grant_type=client_credentials' 'https://api.twitter.
com/oauth2/token'

response:-
{"token_type":"bearer","access_token":"████"}

it meant to request successful as official docs say https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens

## Impact

leakage of twitter_consumer_key and twitter_consumer_secret to public it meant for deveoplers only

## Attachments
- Capture.PNG
- Capture_1.PNG
