# Tampering the mail id on chatbox

## Report Details
- **Report ID**: 260239
- **URL**: https://hackerone.com/reports/260239
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-15T07:34:36.590Z
- **Disclosed**: 2017-08-16T09:18:56.764Z

## Reporter
- **Username**: hulsker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
hi sir , i found a vulnerability i.e tampering the data .

steps to reproduce

1) login to https://app.legalrobot-uat.com
2) open https://app.legalrobot-uat.com/account
3) at right side bottom corner , there is a chat symbol.
4) just enter the message there , and capture the request  using burpsuite and send the request in to repeater tab , after that change the maild owner mail id to some other xxxx mail id and click on send 
5) at the response tab we will get the response 200 ok.

Thank you sir , hope you understand . here is the poc pics, 

## Attachments
- Screenshot_(582).png
- Screenshot_(581).png
