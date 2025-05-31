# Improper Access Control in Ali Express Importer

## Report Details
- **Report ID**: 1609955
- **URL**: https://hackerone.com/reports/1609955
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-23T02:07:14.060Z
- **Disclosed**: 2023-02-01T03:33:34.215Z

## Reporter
- **Username**: penguinshelp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
## Summary:
Good day team,

I found another improper access control flaw in Ali Express Review Importer that can be used to view all and any existing reviews in Judge.Me app. This is similar to my other reports  #1450807 and #1382652. Basically the same bug with #1450807 just on a different app and endpoint :)

## Steps To Reproduce:

1. Login as an admin to your test Shopify instance

2. Install the apps 'Judge.me Product Reviews' and 'Ali Express Review Importer' (both owned by Judge.me)

2. Add a new review to your Judge.Me app. 'Reviews' ->  'Write a Review'

2. Add/Edit a Shopify staff member and give access only to 'Ali Express Review Importer' app 

2. Login to the staff account with only 'Ali Express Review Importer'

2. Go to apps and open the 'Ali Express Review Importer' to establish/start Judge.me session

2. Visit this url to attempt to view reviews from Judge.Me App: `https://judge.me/index.json?shopdomain={yourshop}.myshopify.com&page=1&2. 
per_page=25&offset=0` . Capture the request for this using any proxy intercepting tool like Burp Suite 

2. Since you don't have a valid session for the Judge.Me app you will be prompted to login as a shop owner

2. Now in the 'Ali Express Review Importer app, click 'Reviews' -> and then click the refresh icon on the left side of the search bar. Capture the request for this one too since we'd need the cookie in the request.
{F1785201}

2. Replace the cookie in the request from step 7 to the recently acquired cookie in step 9

2. Send the edited request, the request from step 6 with the new cookie, and you should now be able to view any reviews including hidden/archived ones from Judge.Me App without having access to the Judge.Me app itself

Note: 
Steps 1-4 are done by Admin
Steps 5-11 are done by user with only Ali Express Importer access

## Supporting Material/References:
{F1785202}

If you have any questions on this or if there's anything I can help with please let me know.

Have a nice day!

-PenguinsHelp

## Impact

Staff with no access to 'Judge.me App' can view reviews which they supposedly doesn't have access to

## Attachments
- Capture.PNG
- Judge.Me_Improper_Access_Control_-_Ali_Express_Importer.mp4
