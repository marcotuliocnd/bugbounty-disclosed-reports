# Following links are vulnerable to clickjacking

## Report Details
- **Report ID**: 289246
- **URL**: https://hackerone.com/reports/289246
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-10T18:29:40.983Z
- **Disclosed**: 2018-01-11T09:47:45.261Z

## Reporter
- **Username**: karma1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** [The below listed links, dont have X-FRAME-OPTIONS set to DENY or SAMEORIGIN and they are vulnerable to clickjacking]

**Description:** [The following url can be easily vulnerable to clickjacking]

**Browsers Verified In:**
  * [Firefox V56]
  

**Steps To Reproduce:** [add details for how we can reproduce the issue]
  1. [Run below code from browser and you will see listed links are vulnerable to clickjacking attack]
  2. [<!DOCTYPE html>
<html>

<frameset cols="25%,*,25%">
  <frame src="https://www.semrush.com/?l=us">
  <frame src="https://www.semrush.com/academy/">
  <frame src="https://www.semrush.com/ranking-factors/">
</frameset>

</html>]

**Following links are vulnerable to clickjacking**

+ https://www.semrush.com/semrush-opensearch.xml
+ https://www.semrush.com/academy/
+ https://www.semrush.com/ranking-factors/
+ https://www.semrush.com/manifest.json
+ https://www.semrush.com/?l=us
+ https://www.semrush.com/blog/
+ https://www.semrush.com/ 
+ https://www.semrush.com/prices/
+ https://www.semrush.com/.
+ https://www.semrush.com/.?l=us
  

**Supporting Material/References:**
  * Screenshot is attached with ticket


## Attachments
- Tryit_Editor_v3.5_-_Google_Chrome.jpg
