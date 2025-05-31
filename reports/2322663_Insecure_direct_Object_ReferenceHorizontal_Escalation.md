# Insecure direct Object Reference(Horizontal Escalation)

## Report Details
- **Report ID**: 2322663
- **URL**: https://hackerone.com/reports/2322663
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-01-16T20:17:41.840Z
- **Disclosed**: 2025-01-31T11:08:44.093Z

## Reporter
- **Username**: aliyueka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Goto https://mtn.ng/offers/ login with your credential, on the dashboard navigate mouse cursor to the button below click on any of the bar. Scroll down on the text, then right click and in the option click on "inspect" do a modification on card title and card body, close the inspect and click on "SMS offer" 

## Steps To Reproduce:
STEP 1:
Go to https://mtn.ng/offers/
{F2985276}
Enter your number and click on Submit Button
{F2985277}
Click on "OK"
{F2985279}



STEP 2:
Enter the OTP code sent to your number
{F2985280}
Click on "Validate"



STEP 3:
MTN offer dashboard will automatically display
{F2985284}
Scroll down and click on "Data4ME Bundles 4Me (2)"
{F2985292}



STEP 4:
On the data offer text right click and click on "inspect"
{F2985306}
Do some modification of your choice and close the window
{F2985309}



STEP 5:
Changes reflect to the page
{F2985311}
Click on "SMS Offer"



STEP 6:
SMS will be sent to the provided number with modified text
{F2985317}

## Impact

1. No MTN number is safe from this attack as the attacker(s) only need the victims number(Authentication is not require).

2. Attacker(s) has full control over the text field.

3.  Anonymity achieved as SMS received from "MYMTN"

4. May or May not compromise the admin panel depends on the attacker tools/Scanners that is being use to the malicious activities.

5. It can generate Message traffic if SMS bomber is used.

## Attachments
- STEP1.PNG
- STEP2.PNG
- STEP3.PNG
- STEP4.PNG
- STEP5.PNG
- MTN2STEP1.PNG
- MTN2STEP2.PNG
- MTN2STEP3.PNG
- MTN2STEP4.PNG
- MTN2.PNG
- MTN2.mp4
