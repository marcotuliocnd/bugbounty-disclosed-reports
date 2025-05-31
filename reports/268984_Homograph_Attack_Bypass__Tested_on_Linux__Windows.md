# Homograph Attack Bypass [ Tested on Linux & Windows ]

## Report Details
- **Report ID**: 268984
- **URL**: https://hackerone.com/reports/268984
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-17T05:42:23.050Z
- **Disclosed**: 2017-09-21T03:25:02.684Z

## Reporter
- **Username**: apapedulimu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
##Summary:
at #175286 you has been patched, and i try it work, but i've another way to bypass it. when we add a site to our Homepage with `@`, it's not validate a url properly, make sure it's display the punycode.

##Products affected:

Brave	0.18.36 ( Linux & Windows )

##Steps To Reproduce:

1. In browser add homepage with IDN `@ebаy.com/`
1. now close and open browser again
1. you can see it's redirect to http://xn--eby-7cd.com/

{F221533}

##References:
https://hackerone.com/reports/175286

##Video 
https://youtu.be/aCDeZRdRCuk (unlisted)

## Attachments
- Screenshot_2017-09-17_12-22-55.png
