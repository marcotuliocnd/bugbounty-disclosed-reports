# Non-revoked API Key Disclosure in a Disclosed API Key Disclosure Report on Stripo

## Report Details
- **Report ID**: 1047125
- **URL**: https://hackerone.com/reports/1047125
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-30T15:28:22.960Z
- **Disclosed**: 2020-12-04T14:14:43.670Z

## Reporter
- **Username**: whoisbinit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
Can you imagine discovering an API key disclosure vulnerability in a disclosed API key disclosure report? The same thing is what I came across while going through the disclosed reports at Stripo Inc. Plus, the disclosed API key isn't even revoked, and therefore I am still able to use the same API key to fetch response from the target.

I am talking about #983331 where a security researcher reported secret API key leakage vulnerability in a JavaScript file at Stripo. This report is disclosed on HackerOne, and the team at Stripo have forgotten to blur the API keys from the report before disclosing it to the public. The API keys from Aviary and YouTube are disclosed in that report, and I tried using these API keys, and found out that they can still be used to fetch response from YouTube's API using Stripo's disclosed API key. I didn't check on Aviary though since I found out that Aviary is already a defunct image editor.

## Steps To Reproduce:

### API Key Disclosure:
To reproduce the API Key Disclosure vulnerability, you can perform the following steps:
  1. Visit https://hackerone.com/stripo/hacktivity?filter=type%3Apublic&type=team
  2. You will see a disclosed report entitled "**Public and secret api key leaked in JavaScript source**". Visit this report: https://hackerone.com/reports/983331
  3. You will see the following two lines in the report:

```
aviaryApiKey: "███████",
youtubeApiKey: "██████████",
```

You can see the API keys from Aviary and YouTube are disclosed in this report.

### API Key Validation:
Just because an API key is disclosed in a disclosed report, it doesn't mean that the API key actually works. Therefore, I decided to check whether the YouTube API Key is still working or not. For this purpose, you can follow these steps:
  1. Visit https://developers.google.com/youtube/v3/docs,
  2. Start looking for different services on how you can use the disclosed API key against YouTube Data API! I decided to check this one: https://youtube.googleapis.com/youtube/v3/search?key=<Valid-API-Key-Here>
  3. Replace the value of the **`key`** parameter in the URL with the Stripo's disclosed API key; i.e. **`███████`**. Therefore, the URL will become: https://youtube.googleapis.com/youtube/v3/search?key=█████
  4. Now, visit the URL you crafted in Step 3, and you will see that the YouTube Data API responds back with the results it should show for this particular API endpoint.

## Supporting Material/References:

  * I have attached a screenshot of the API keys being disclosed in the disclosed report along with this report.
  * I have also attached a sample Proof-of-Concept response that YouTube Data API showed for one of the YouTube API requests made using the Stripo's YouTube API Key.

## Impact

By taking an advantage of this vulnerability, an attacker would be able to use Stripo's YouTube API Key for calling different API endpoints in services provided in the YouTube Data API.

## Attachments
No attachments
