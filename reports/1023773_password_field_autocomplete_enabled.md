# password field autocomplete enabled

## Report Details
- **Report ID**: 1023773
- **URL**: https://hackerone.com/reports/1023773
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-01T08:47:23.917Z
- **Disclosed**: 2022-09-27T23:26:28.449Z

## Reporter
- **Username**: er_salil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:
[Most browsers have a facility to remember user credentials that are entered into HTML forms. This function can be configured by the user and also by applications that employ user credentials. If the function is enabled, then credentials entered by the user are stored on their local computer and retrieved by the browser on future visits to the same application.
The stored credentials can be captured by an attacker who gains control over the user's computer. Further, an attacker who finds a separate application vulnerability such as cross-site scripting may be able to exploit this to retrieve a user's browser-stored credentials.]

## Platform(s) Affected:
[both]

## Steps To Reproduce:
[follow the steps]

  1. [signup with the new details]
  1. [go to login page]
  1. [there we will see password details are automatically filled]

## Supporting Material/References:
[none]

## Impact

This autocomplete password can be sniffed without user permission

## Attachments
No attachments
