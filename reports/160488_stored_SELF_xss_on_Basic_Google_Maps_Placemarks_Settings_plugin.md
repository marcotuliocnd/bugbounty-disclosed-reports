# stored SELF xss on Basic Google Maps Placemarks Settings plugin

## Report Details
- **Report ID**: 160488
- **URL**: https://hackerone.com/reports/160488
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-18T18:03:14.022Z
- **Disclosed**: 2016-09-27T21:46:23.112Z

## Reporter
- **Username**: b6117130df17feef13481e3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi Ian,

I have to say, normally I don't report and vendors doesn't accept self xss vulnerabilities as valid, but I'm encouraged by #9375
So, I'm reporting this. 

Placemark title field is NOT sanitizing the user input properly. 
I've updated wordpress to latest, and checked your plugin's versiyon from SVN also, it is latest, too. You can confirm in the attached PoC Screenshots.
Thanks for giving opportunity to test your plugins! Keep up good work.

If you don't find this report useful for you, you can just close it as informative or whatever you like.

Regards

## Attachments
- im0.jpg
- im1.jpg
- notf.jpg
- prev.jpg
