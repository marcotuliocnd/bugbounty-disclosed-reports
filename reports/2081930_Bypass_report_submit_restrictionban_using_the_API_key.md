# Bypass report submit restriction/ban using the API key

## Report Details
- **Report ID**: 2081930
- **URL**: https://hackerone.com/reports/2081930
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-24T13:12:32.619Z
- **Disclosed**: 2023-10-29T11:23:39.167Z

## Reporter
- **Username**: light3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
#Description:

* Banned researcher allows to submit reports through the API key, when user ban reports on his account he can't submit any reports to any programs until his ban time is gone, I was able to submit the report through the API key

##Steps to reproduce:

* I contacted the support then they banned my account to send reports as shown below:

{F2531260}

* Then after they banned my account I wasn't able to send any report also when I create directly from the request I receives 403 forbidden

* I go to create a sandbox program and API key:

{F2531264}

{F2531263}

* I navigate to the documentation:

https://api.hackerone.com/hacker-resources/#reports-create-report

* So after creating the API key using the below request/command I was able to submit the reports to any program without any restrictions on reports

```bash
curl "https://api.hackerone.com/v1/hackers/reports"   -X POST   -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU="   -H 'Content-Type: application/json'   -H 'Accept: application/json'   -d @- <<EOD
{
  "data": {
    "type": "report",
    "attributes": {
      "team_handle": "HackerOne-test_h1b",
      "title": "string",
      "vulnerability_information": "test tst tst",
      "impact": "tst tst",
      "severity_rating": "none",
      "weakness_id": 1
    }
  }
}
EOD
```

* And here the report has been sent:

{F2531274}

* Also here I reported a report to a real program I picked Sony for test report but I'm sorry for submitting test report to the program and to the team please accept my apologies

{F2531276}

* Also for more confirmation if you need me to send a report to HackerOne as more proof please request

Thanks, Have a great day,

light3r, mrmax4o4

## Impact

An banned reports researcher have the ability to send report after he banned from HackerOne that's allow him to bypass the reports restrictions, also he banned for his behavior so he may send a high volume of reports to a lot of teams without any restriction this after he bypass the first ban and reports submission restriction as shown above and submit the reports through the API instead of the GraphQL

## Attachments
- Screenshot_2023-07-24_at_3.59.32_PM.png
- Screenshot_2023-07-24_at_4.01.41_PM.png
- Screenshot_2023-07-24_at_4.01.17_PM.png
- Screenshot_2023-07-24_at_4.05.59_PM.png
- image.png
