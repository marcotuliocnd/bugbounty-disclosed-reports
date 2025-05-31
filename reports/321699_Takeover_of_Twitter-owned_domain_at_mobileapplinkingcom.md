# Takeover of Twitter-owned domain at mobileapplinking.com

## Report Details
- **Report ID**: 321699
- **URL**: https://hackerone.com/reports/321699
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-03-04T00:44:29.806Z
- **Disclosed**: 2019-02-28T00:26:15.645Z

## Reporter
- **Username**: healdb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** Not sure there is much of a security impact to this, more of a best practice, but the domain mobileapplinking.com, which is registered to Twitter Inc. is vulnerable to takeover using github pages.

**Description:** The domain mobileapplinking.com is owned and registered by Twitter.com, as can be seen through the WHOIS data attached to this report. However, the DNS for the site links to a non-existent Github pages site. This left it open for takeover through Github Pages. The site is currently registered under my github pages account, as can be seen at mobileapplinking.com/takeover

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Register a new github pages site
  1. Create a CNAME file with the URL mobileapplinking.com
  1. Browse to mobileapplinking.com and observe the taken over site.

## Impact: If this site was defaced and used to transmit illegal or inflammatory things, and it was found that Twitter owned the domain, it could negatively effect the Twitter brand.

## Supporting Material/References:

  * whois_mobileapplinking.png - screenshot of WHOIS data showing twitter ownership.

## Impact

If this site was defaced and used to transmit illegal or inflammatory things, and it was found that Twitter owned the domain, it could negatively effect the Twitter brand.

## Attachments
- whois_mobileapplinking.png
