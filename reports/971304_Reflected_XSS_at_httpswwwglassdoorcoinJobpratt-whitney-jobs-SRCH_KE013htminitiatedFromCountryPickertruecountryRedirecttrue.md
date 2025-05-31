# Reflected XSS at https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

## Report Details
- **Report ID**: 971304
- **URL**: https://hackerone.com/reports/971304
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-31T14:47:57.703Z
- **Disclosed**: 2021-04-16T02:52:31.497Z

## Reporter
- **Username**: n1xk_10
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
Summary:  There is a reflected XSS vulnerability in   https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

Vulnerability Type: Reflected XSS
Browsers tested: Chrome, Firefox
Payload: %22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3e

Steps To Reproduce:
1. Navigate to  https://www.glassdoor.co.in/Job/pratt-whitney-jobs-SRCH_KE0,13.htm?initiatedFromCountryPicker=true&countryRedirect=true

2.   /Job/[INPUT]pratt-whitney-jobs-SRCH_KE0,13.htm?
     if we input any value in the path then it is reflected on the page.
     Enter this payload here: %22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3e

3. But there is a character length limitation to the input.

4.   /Job/pratt-whitney-jobs-SRCH_KE0,[This value].htm? 
     We can bypass the character limitation by changing this value

5. Now change this value from 13 to 50

6.   Now open this url: https://www.glassdoor.co.in/Job/%22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3epratt-whitney-jobs-SRCH_KE0,50.htm?initiatedFromCountryPicker=true&countryRedirect=true
     See the response in browser, an alert will pop up

## Impact

Using XSS an attacker can steals the victim cookie and can also redirect him to a malicious site controlled by the attacker.

## Attachments
- Screenshot_at_2020-08-31_20-13-09.png
