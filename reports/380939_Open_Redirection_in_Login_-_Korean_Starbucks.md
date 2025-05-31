# Open Redirection in Login - Korean Starbucks

## Report Details
- **Report ID**: 380939
- **URL**: https://hackerone.com/reports/380939
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-12T12:07:22.382Z
- **Disclosed**: 2019-03-20T16:49:58.028Z

## Reporter
- **Username**: jtjisgod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Summary:
Open Redirection is performed in Korean Starbucks login page.
An attacker can redirect victim to other site such as fishing.

Description:
When victim visit https://www.istarbucks.co.kr/login/login.do?redirect_url=//www.bughunting.net this site, and login, he/she is redirected to www.bughunting.net page.

PoC 
https://www.istarbucks.co.kr/login/login.do?redirect_url=//www.bughunting.net

Etc
I attached a PoC video.

## Impact

Fishing

## Attachments
- starbucks_korea_open_redirect-2018-07-12_21.03.07.mp4
