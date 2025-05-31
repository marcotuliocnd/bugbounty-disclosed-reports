# xss filter bypass [polldaddy]

## Report Details
- **Report ID**: 264832
- **URL**: https://hackerone.com/reports/264832
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-30T20:06:15.434Z
- **Disclosed**: 2017-10-01T15:56:17.013Z

## Reporter
- **Username**: paresh_parmar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi,

previously reported xss https://hackerone.com/reports/107405 which is fixed, but i am able to bypass that fix. 

Payload for bypass : `<a href="javascript&colon;alert&lpar;document&period;domain&rpar;">Click Here</a>` 

# Steps:
-  Login into Polldaddy account polldaddy.com
- go to ___POLLS___  and create new poll
- in answers. enter xss payload `<a href="javascript&colon;alert&lpar;document&period;domain&rpar;">Click Here</a>` 

{F217173}

- Save it 
-  go here :where you can edit style  https://polldaddy.com/polls/XXXXX/style-edit/  
{F217170}

scroll down and click on it , xss will trigger.
{F217172}

Ref: https://hackerone.com/reports/107405

Thanks



## Attachments
- Screenshot_(3301).png
- Screenshot_(3302).png
- Screenshot_(3303).png
