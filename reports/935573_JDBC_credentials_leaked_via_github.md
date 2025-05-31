# JDBC credentials leaked via github

## Report Details
- **Report ID**: 935573
- **URL**: https://hackerone.com/reports/935573
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-07-22T23:21:52.278Z
- **Disclosed**: 2020-07-27T16:44:01.064Z

## Reporter
- **Username**: walidhossain010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:
jdbc credentials found on a public github repo.though the repo belongs to yelp or not there is a doubt.I have found many more sensitive data on that repo.so kindly check the repo all together.sensitive data found publicly.
## Platform(s) Affected:
website
## Steps To Reproduce:
1. visit the link 
```https://github.com/supernebula/yelp-j/blob/36de49095d7f3221e3a50adf9bd7ab26ef585f24/yelp/yelp-web-search/src/main/resources/application-dev.properties
```
 you will see leaked credentials.also visit other path to discover more sensitive info.

## Impact

private credentials disclosure.

## Attachments
- Screenshot_2020-07-23_at_5.17.27_AM.png
