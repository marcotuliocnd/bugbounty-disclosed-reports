# Leaking Of Sensitive Information on Github

## Report Details
- **Report ID**: 837733
- **URL**: https://hackerone.com/reports/837733
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-03T05:02:44.576Z
- **Disclosed**: 2020-04-03T14:03:04.467Z

## Reporter
- **Username**: harris0ft
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
##Summary:
Sensitive Data were leaked in https://github.com/liberapay/liberapay.com

##Steps To Reproduce:

1. Install gitleaks from https://github.com/zricethezav/gitleaks

2. Run the following command in a Linux terminal


```
gitleaks -v --pretty -r=https://github.com/liberapay/liberapay.com
```


The following keys were leaked:

```
1. AWS ID: "AKIAJRT6BUQHIPYENYWQ"

2. 'twitch_secret' : "o090sc7828d7gljtrqc5n4vcpx3bfx"
 
3. 'facebook_app_secret' : "3bcb5dc6ce821e5202870c1e6ef5bbc4"
   'facebook_app_id' :  "1418954898427187"

4. 'twitter_id'  :  "h8bBZtoPNz63S5RkZdbo9R5zb"
   'twitter_consumer_key' : "h8bBZtoPNz63S5RkZdbo9R5zb"

5. 'github_client_secret'  :  "46f75669895e96029d57b64832d6f2c8e6291a0e"

6. 'bitbucket_secret' : "Y5G6A9BaWDxn2gLKZwwkrGtVE3Zjd7y7"

7. 'google_client_secret'  :  "7AkgPekyWr6stQWdM6y1TtV6"

8. 'openstreetmap_secret'  : "W08UgEhxQnh7nMzB7GfSFcqcwPnZMmKMNyxWdcw4"

9. 'GITHUB_CLIENT_SECRET'  :  "e69825fafa163a0b0b6d2424c107a49333d46985"

10. 'BALANCED_API_SECRET'] = '90bb3648ca0a11e1a977026ba7e239a9'"

11. FB.init( { apiKey: 'a279adbe87e2b3c505e777af99a5260d', xfbml: true } );",

12. "Google API key" :  "AIzaSyDFwxAtyIPi08FgI58rMsL5A9CqvL3kOaY"

```

## Impact

I didn't try anything with the keys, just thought it would be a good idea to share this finding with you in case it can be used in a way that I don't know. So its up to you to assess the risk.

Best Regards

## Attachments
No attachments
