# Page has a link to google drive which has logos and a few customer phone recordings

## Report Details
- **Report ID**: 864712
- **URL**: https://hackerone.com/reports/864712
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-02T11:26:53.842Z
- **Disclosed**: 2022-02-21T08:15:22.671Z

## Reporter
- **Username**: codersanjay
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Description:** 

* Go to ███████

Refer to the screenshot below

██████

As you can see in the above image, there is is link to access zomato logos.This redirected me to a google drive page which not only had logos but also customer care recordings where sensitive information like **Customer mobile numbers,customer names,what food they ordered,order id's** were disclosed.

Refer to the screenshot below.

███

Now go to **recordings** folder.

██████

As you can see in the above image,there are about 35 recordings wherein sensitive information is being disclosed.I guess everything is uploaded yesterday (May 1st).

I suspect there would be more of a recordings added to this folder as I see a folder named **Till Date Recordings** which is empty as of now.

## Steps To Reproduce:

1. Go to Go to █████
2.Click on the google drive link for logos
3.Go to recordings folder
4.Find all customercare recordings

## Supporting Material/References:

 The following is one of the audio recording found wherein customer number,name is disclosed.

  * ██████████

## Impact

Sensitive PII disclosure.

## Attachments
No attachments
