# Brave payments remembers history even after clearing all browser data.

## Report Details
- **Report ID**: 203088
- **URL**: https://hackerone.com/reports/203088
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-03T04:43:24.333Z
- **Disclosed**: 2017-08-10T05:11:12.297Z

## Reporter
- **Username**: sumit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:

As a user you expect the browser to not persist data after clearing browser data. The Brave payments feature persists the websites details and usage.

## Products affected: 
Brave	                        0.13.1
rev	                                9dd06f9
Muon	                        2.0.18
libchromiumcontent	54.0.2840.100
V8	                                5.4.500.41
Node.js	                        7.0.0
Update Channel	        dev
os.platform	                darwin
os.release	                16.4.0
os.arch	                        x64

## Steps To Reproduce:

 * Open a porn site or any site and spend some time on it
 * Clear browsing data of the browser with all options enabled (screenshot attached)
 * It'll ask to restart the browser, do it (optional)
 * Now navigate to brave payments page
 * Voila! Your porn history is there

## Supporting Material/References:

  * Screenshot of the clear browsing data panel with all the settings enabled
  * Screenshot of the porn website listed on the brave payments page


## Attachments
- brave-payments.png
- clear-data.png
