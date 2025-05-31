# UI Redressing ( ClickJacking ) Issue on Information submit form 

## Report Details
- **Report ID**: 163753
- **URL**: https://hackerone.com/reports/163753
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-27T08:01:37.366Z
- **Disclosed**: 2016-08-29T16:03:25.112Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
I found that There is a Form for Submitting User Information for applying for Beta Program. 
But this has NO Protection against Clickjacking Issue & also this form needs the following inputs that can b somewhat useful for an attacker.

#Information Like: 
Name: 
Email: 
Company 

Following is HTML code i used to test it!

<html>
	<--Clickjacking Test by KHizer--> 
	<style>
		iframe { 
		width: 800px; 
		height: 500px; 
		position: absolute; 
		top: 0; left: 0; 
		filter: alpha(opacity=50); 
		opacity: 0.5; 
		}  
	</style>
	<iframe src="https://www.legalrobot.com/">
</html>

Screen shots attached :D

Thanks,
KHIZER JAVED

## Attachments
- Screenshot_from_2016-08-27_00-45-30.png
- Screenshot_from_2016-08-27_00-48-41.png
