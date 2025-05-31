# SQL injection in partner id field on https://www.teavana.com (Sign-up form)

## Report Details
- **Report ID**: 269279
- **URL**: https://hackerone.com/reports/269279
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-18T17:25:04.779Z
- **Disclosed**: 2018-01-23T01:06:00.770Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
While signing up for "teavana" shopping account on it came to notice that the partner id validation fails and exists SQL injection.

So this is what I did:

1) Visit https://www.teavana.com/us/en/account
2) Click on signin > create shopping account
3) In the partnerno, gave an input of "1234" (1.PNG)
     Result :No issue as expected . Signup fails
     message: "We are unable to verify starbucks partner id" (2 .PNG)
4) Changed input to "1234' OR 1=1" (without double qoutes) (3.PNG)
    Result: This time signup succeeds!!! (4.PNG) 



## Attachments
No attachments
