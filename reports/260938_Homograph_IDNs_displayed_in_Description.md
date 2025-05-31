# Homograph IDNs displayed in Description

## Report Details
- **Report ID**: 260938
- **URL**: https://hackerone.com/reports/260938
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-17T05:43:53.276Z
- **Disclosed**: 2017-09-16T23:12:32.548Z

## Reporter
- **Username**: d4rk_g1rl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
The IDN: http://ebаy.com/ is a homograph for the latin ebay.com. if you copy and paste a link, you might think that you are going to ebay.com. in fact, you are going to a homograph url http://xn--eby-7cd.com/

it would be safer to show the punycode version of the url so that it would be apparent that something weird is going on. that is, show http://eb@y.com/ instead of http://ebаy.com/

#STEPS TO REPRODUCE:

1. Login to your account https://app.legalrobot-uat.com
2. Navigate this URL:

      https://app.legalrobot-uat.com/roadmap

3. Click the "Add a new idea" button
4. Actually their is no problem on Name but in Description.
5. Put http://ebаy.com/ on Description
6. Click the "Add Idea" Button
7. Notice that it display http://ebаy.com/ See my attached photo {F213601}

Thanks,

## Attachments
- homo.png
