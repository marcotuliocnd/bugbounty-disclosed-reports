# Sub Domain Takeover

## Report Details
- **Report ID**: 221133
- **URL**: https://hackerone.com/reports/221133
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-04-15T04:58:00.526Z
- **Disclosed**: 2017-10-24T16:13:22.787Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# One of Gratipay's sub domains points to Heroku with no app created.

## Description

Gratipay's sub domain http://www.gratipay.com.herokudns.com/ points to Heroku but is not in use. 

## Steps To Reproduce

###Details

 - Upon realization of vulnerability, installed and created a Heroku dependencies and application.

 - Added http://www.gratipay.com.herokudns.com/ to my list of domains through Heroku CLI. 

heroku domains:add www.gratipay.com.herokudns.com

After verifying my Heroku account this was easy to point the sub domain to my application. 

- Uploaded my application with text "B3nac sub domain takeover POC." and refreshed the domain to find it pointed to my application successfully.  
  
## Fix

If the domain is not in use, then it is recommended to point the dns entry away from the third party program.

## Supporting Material/References:

  * I've attached the uploaded takeover python application/website screenshot.

## Attachments
- POC.png
- HerokuCLI.png
