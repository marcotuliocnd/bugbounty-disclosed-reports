# No server side check on terms of service page which leads to bypass

## Report Details
- **Report ID**: 1338256
- **URL**: https://hackerone.com/reports/1338256
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-13T10:00:17.746Z
- **Disclosed**: 2021-10-05T09:19:47.972Z

## Reporter
- **Username**: hackipy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi team,
I have found that there is no server side check implemented on the "Acronis Terms of Service and Privacy Statement" Page that is shown after filling the registration form which results in bypassing it without even accepting it.

Steps To Reproduce:

  1. Register as a new user by filling out the form.
  2. After that a new page will open it will require the user to check the box otherwise the button will remain disabled.
  3. Right click on the button choose inspect element.
  4. Find the button tag and remove the attribute "disabled=disabled" and "is-disabled" from the class.
  5. Now press enter and close the inspect element.
  6. As you can see the button is now enabled you can click on it and it will take you to your account.

Recommendations:

 A server side check must be implemented here so that if an attacker or a scammer bypasses the client side validation using inspect element the server 
 will validate the action and give an error based upon it preventing the attacker from going to the next page.

POC video attached!

Thanks.

## Impact

This bug has a very straight forward impact. Lack of server side check here will lead the attacker bypass the page easily and register as a legitimate user. The server will have no clue if the person registering had accepted the terms of service and privacy statement or not.

## Attachments
- acronis_pp_bypass.mp4
