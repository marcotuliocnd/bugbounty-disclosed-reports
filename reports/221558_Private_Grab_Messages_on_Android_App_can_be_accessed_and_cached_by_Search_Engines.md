# Private Grab Messages on Android App can be accessed and cached by Search Engines

## Report Details
- **Report ID**: 221558
- **URL**: https://hackerone.com/reports/221558
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-17T12:51:11.969Z
- **Disclosed**: 2017-09-14T02:59:28.642Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
##Description
Hello. Today i discovered, that Search Engines can access the private users messages (OTP pins, Group invites information etc.)
It happens because the `https://grab-attention.grabtaxi.com` host allows search indexing, and can leak the auth_token to the Search Engines which also can lead to privilege escalation.
When vieving "Notifications" section on the app, i noticed the unsecure GET request to the `https://grab-attention.grabtaxi.com/passenger/passenger.html?auth_token=[my_token]&view=268435456`. I was surprised, when tried to repeat it in the browser - it gave me access to my messages.

##POC
{F176465}
{F176466}

## Steps To Reproduce:
1. Cheking the private messages of other user (me):
https://grab-attention.grabtaxi.com/passenger/passenger.html?auth_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJQQVNTRU5HRVIiLCJleHAiOjQ2NDUyMzk1NDUsImlhdCI6MTQ5MTYzOTU0NSwianRpIjoiZWI0YmFiMjUtYzA2Yi00MGIzLWJiZTctMzZkYzFmMWRkZTMyIiwibG1lIjoiU1lTVEVNIiwibmFtZSI6IiIsInN1YiI6IjM2NWE0NjY0LTY1MGEtNDBjZC05YWU2LTQ4YWQwN2Q2NGY2OSJ9.eTX2dWnooTxm50Dv1VYoIZanOqCe073_AmVk97VE4p7m4e26mcWtnZzQz5IR1EwuWbs52qJLzzAIZ5KcpWoKCvadu6zuRQzy2xRk8BcFDUXGl8w8doPJbuSIHMY0K-x8Q-█████████ZTdgxLI&view=268435456#/
2. Checking that search engines can crawl it:
Use this Google DORK (search text):
`passenger site:grab-attention.grabtaxi.com`
and press Search.
You will see this cached page with auth_token (actually it was cutted due to big query length) - but it is still a huge information disclosure.


## Suggested fix
1. Disable Search indexing on `https://grab-attention.grabtaxi.com`
2. For the better security you can change the request method to the `https://grab-attention.grabtaxi.com/passenger/passenger.html` endpoint from GET to POST (or encrypt it) due to that fact that auth_token are leaked in the query parameters.


## Attachments
- test.PNG
- test2.PNG
