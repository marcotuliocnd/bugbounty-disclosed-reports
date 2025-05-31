# Completed Compromise & Source Code Disclosure via Exposed Jenkins Dashboard at https://jenkins101.udemy.com

## Report Details
- **Report ID**: 182104
- **URL**: https://hackerone.com/reports/182104
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-14T15:58:13.907Z
- **Disclosed**: 2017-06-17T13:59:38.366Z

## Reporter
- **Username**: cha5m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
Howdy, @udemy!

Summary:
=======
I am writing to inform you of a critical information disclosure bug via an exposed Jenkins dashboard located at https://jenkins101.udemy.com. Upon navigating to this address, I was asked to authenticate with my Github account. After authenticating, I was surprised to find that I had complete access to the corresponding Jenkins Dashboard as seen in the screenshot below:

{F134658}

Impact:
=====
Contained within these files was the complete Udemy Django source code. This included complete database schemas and keys/ credentials for the following services:

* Crowdin
* Amazon Redshift
* Exchange
* Facebook
* Google
* Maxmind
* Sendgrid
* Sift
* Twilio
* Zencoder
* Level3
* Apple
* Salesforce
* Celery
* Paypal
* Stripe
* Freshdesk
* and more

To verify that these credentials were active, I attempted to login into Sendgrid. I was able to take over the Udemy Sendgrid account as seen in the screenshot below. I did not make any change/ access any information.

{F134656}

Mitigation
=====

Mitigation for this should be fairly straightforward, simply ensuring proper user authentication should prevent future unauthorized users from access the dashboard. I am not storing any of the informaiton that I came across, however, rekeying the compromised systems may not be a bad idea.

I hope this reports helps! Please let me know if you have any questions! 😁

Best,
@n0rb3r7

## Attachments
- Screenshot_2016-11-14_10.49.00.png
- Screenshot_2016-11-14_10.54.39.png
