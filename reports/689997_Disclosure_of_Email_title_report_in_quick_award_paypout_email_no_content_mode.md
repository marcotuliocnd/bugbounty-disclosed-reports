# Disclosure of Email title report in quick award paypout email (no content mode)

## Report Details
- **Report ID**: 689997
- **URL**: https://hackerone.com/reports/689997
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-07T04:06:06.929Z
- **Disclosed**: 2019-10-11T18:12:19.939Z

## Reporter
- **Username**: kunal94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello H1 Security Team

#Description
In report #645264 and #669776, email title disclosure has been fixed in no content settings.
However, there is one more area which needs to be fix - "Instant bounty Award Email".
In this email, even though email settings have been set as "No content", still it's displaying Report Title.


#Step to Reproduce
+ Go to Program Email settings `/program_name/email_settings` and set email Settings as "no content".
{F576922}

+ Now, Reward someone with quick Bounty Payout API.
```
curl "https://api.hackerone.com/v1/programs/42738/bounties" \
  -X POST \
  -u "dummy:xxxxxxxx" \
  -H "Content-Type: application/json" \
  -d @- <<EOD
    {
      "data": {
        "type": "bounty",
        "attributes": {
          "amount": 100,
          "reference": "aaaaa",
          "title": "SQL injection in example.com",
          "recipient": "example@example.com",
          "currency": "USD",
          "severity_rating": "high"
        }
      }
    }
EOD
```
+ In email, it's disclosing the Report Title even though Email settings has been set to "no content".
{F576923}

Thanks
Kunal

## Impact

+ Email report Title is been leaked in the settings as Email-notification: No content.

## Attachments
- poc.jpg
- poc1.jpg
