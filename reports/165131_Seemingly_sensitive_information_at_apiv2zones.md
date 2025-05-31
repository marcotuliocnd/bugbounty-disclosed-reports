# Seemingly sensitive information at /api/v2/zones

## Report Details
- **Report ID**: 165131
- **URL**: https://hackerone.com/reports/165131
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-01T22:16:06.226Z
- **Disclosed**: 2016-11-16T19:59:26.593Z

## Reporter
- **Username**: sameoldstory
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Overview
==
https://www.instacart.com/api/v2/zones is accessible by a regular Instacart user and seems to return sensitive information such as names, emails, phone numbers, money amounts and dates.

```
GET /api/v2/zones

{
  "meta": {
    "code": 200
  },
  "data": {
    "zones": [
      ...
      {
        "id": 73,
        "name": "████",
        "created_at": "2014-10-01T01:36:07.302Z",
        "updated_at": "2016-06-14T23:32:39.147Z",
        ...
        "active": true,
        "supervisor_phone": "███████",
        ...
        "hourly_guarantee_amount_cents": █████████,
        "hourly_guarantee_amount_currency": "USD",
        "guarantee_ends_at": "2015-12-31T00:00:00.000Z",
        ...
        "applicant_supervisor_name": "█████",
        "applicant_supervisor_phone": "████",
        ...
        "applicant_supervisor_email": "██████",
        "use_phone_screening": false,
        ...
        "strict_shopper_probation": true,
        "picking_only_hourly_guarantee_amount_cents": █████████,
        ...
```

Security Implications
==

It's hard for me to evaluate how sensitive the information is, but it definitely doesn't look like something you would put up on the website for everyone to see. I guess a competitor company could make good use of it. Also an attacker could use the information to plan social engineering attacks.


## Attachments
No attachments
