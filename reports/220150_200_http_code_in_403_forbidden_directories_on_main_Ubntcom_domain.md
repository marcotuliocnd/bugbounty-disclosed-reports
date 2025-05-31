# 200 http code in 403 forbidden directories on main Ubnt.com domain

## Report Details
- **Report ID**: 220150
- **URL**: https://hackerone.com/reports/220150
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-11T08:00:19.664Z
- **Disclosed**: 2017-04-19T14:08:00.177Z

## Reporter
- **Username**: 4websecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Hello,

My investigations revealed that we have accesible directory in forbidden directory:

http://www.ubnt.com/static/ - forbidden
http://www.ubnt.com/static/cm/ - forbidden
Here we have http://www.ubnt.com/static/cm/mode/ accesible and then /xm/l and /django/ foders

POC:
http://www.ubnt.com/static/cm/mode/ - 200 http code (accesible)
http://www.ubnt.com/static/cm/mode/xml/ - 200 http code (accesible)
http://www.ubnt.com/static/cm/mode/django/ - 200 http code (accesible)

Now, i didn't looked up very close to this pages content, but for sure we are not supposed to acces them. Thank you.

Kind Regards.


## Attachments
No attachments
