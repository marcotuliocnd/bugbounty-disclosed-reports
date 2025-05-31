# Stored XSS in Acronis Cyber Protect Console

## Report Details
- **Report ID**: 1064095
- **URL**: https://hackerone.com/reports/1064095
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-22T04:06:46.641Z
- **Disclosed**: 2021-06-10T13:07:05.630Z

## Reporter
- **Username**: sbakhour
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Dear Acronis Security Team,

## Summary
There is a possibility of storing an XSS on the https://mc-beta-cloud.acronis.com/ui/ console.

## Steps To Reproduce
[add details for how we can reproduce the issue]

  1. Login to the console with the given account
  2. Go to "Protection" under "PLANS"
  3. Click on "Create Plan"
  4. Click on "Add devices" and select the device to add (in my case I selected my PC where the agent is installed)
  5. Name the new created protection plan with this payload  <video><source onerror="javascript:alert(document.domain)">
  6. Click on "Create" button and wait till the plan is created
  7. Once the plan is created go back to the "Protection" under "Plans" and select the created plan by selecting the checkbox
  8. On the "Actions" pane at the right side, click on the "Stop" button
  9. A confirmation box will appear to stop the plan
  10. Click on the red "Confirm" button and the XSS will fire up
  11. Reload the pages by re-visiting https://mc-beta-cloud.acronis.com/ui/
  12. Click again on "Protection" under "Plans"
  13. Select the plan created with this payload name <video><source onerror="javascript:alert(document.domain)">
  14. Repeat steps 8,9,10 and the XSS will fire up again confirming that it is a stored XSS.

## Recommendations
You can prevent XSS by escaping, validating inputs in fields and sanitizing. Plan names are not supposed to contain special characters or payloads.

##Supporting Material/References::
Please refer to the attached screenshot & video for reference.

##Browser Tested:
Mozilla Firefox 68.9.0esr (64-bit)

##Operating System Tested:
Windows 10 Professional 64-bit
Kali Linux 2020 32-bit

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

## Attachments
- Acronis_Cyber_Cloud_Stored_XSS_21-12-20.JPG
- Stored_XSS_Acronis_21-12-20.mp4
