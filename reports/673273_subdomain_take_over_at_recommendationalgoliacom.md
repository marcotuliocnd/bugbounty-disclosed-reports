# subdomain take over at recommendation.algolia.com

## Report Details
- **Report ID**: 673273
- **URL**: https://hackerone.com/reports/673273
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-14T09:14:02.191Z
- **Disclosed**: 2019-08-14T13:53:03.340Z

## Reporter
- **Username**: badcracker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
##Description
hello sir,
your subdomain recommendation.algolia.com cname is recommendation.us and recommendation.us is for sell which can lead to subdomain take over
##steps to reproduce
1. check the cname of recommendation.algolia.com
2. see that the cname "recommendation.us" is for sell using lookup tool

##poc:
{F555251}

## Impact

Attackers are able to purchase recommendation.us then they will be able to takeover recommendation.algolia.com and post porn pictures or phishing forums

## Attachments
- Screenshot-2019-8-14_Recommendation_us_WHOIS__DNS__Domain_Info_-_DomainTools.png
