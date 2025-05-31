# Several Subdomains Takeover

## Report Details
- **Report ID**: 1591085
- **URL**: https://hackerone.com/reports/1591085
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-06-04T12:14:40.430Z
- **Disclosed**: 2022-06-08T20:36:30.328Z

## Reporter
- **Username**: 3amii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
there are some subdomains in reddit.com those are vulnerable to takeover subdomain attack. I found these subdomains while I have been testing the subdomains of reddit.com.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. create a user account in reddit.com.
  2. there are some subdomain as sample: webcovid19.reddit.com (151.101.13.140) and click on this subdomain.
  3. you will see "Sorry, there aren’t any communities on Reddit with that name" message.
  4. now create an community with the same name "webcovid19".and you will not find any message as above.
  5. well done. now you have the subdomain for your community.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

1-for details, please find attached screenshots.
2-use this subdomain finder to find subdomains.
https://subdomainfinder.c99.nl/

## Impact

attacker can use available unclaimed subdomains for malicious intention

## Attachments
- reddit_list_-available-subdomain.PNG
- are-not-any-communities.PNG
- create-community-with-same-_domain.PNG
- created-community.PNG
