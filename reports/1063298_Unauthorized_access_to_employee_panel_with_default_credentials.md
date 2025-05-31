# Unauthorized access to employee panel with default credentials.

## Report Details
- **Report ID**: 1063298
- **URL**: https://hackerone.com/reports/1063298
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-21T09:30:04.359Z
- **Disclosed**: 2021-11-13T20:46:19.578Z

## Reporter
- **Username**: 7azimo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## Summary:
Hello, 
When hunting for your web application.

I have managed to go https://cars.fas.gsa.gov/cars/cars and get displayed with a form.
I have already tried to login to Cars and without success.
However i've noticed the loginChk() function and change the value of the form hence bypassing it and logging in succesfuly.

## Steps To Reproduce:


  1. go to https://cars.fas.gsa.gov/cars/cars
  2. type loginChk()  function in console. 
  3. It would return false. 
  4. Now  type in console ( can be opened using F12). 
       document.forms[0].scSelCen.value = "admin"
  5. Now try to login by clicking on CARS button.

## Supporting Material/References:
Navigator used : google chrome.

If you need any additional information. feel free to ask me.

PS :  I think the website went for a maintenance right now.
Even though i didn't use anything of that panel.

## Impact

Any attacker would have the access to admin panel and do whatever he wants.
As i can see , it's a platform for reporting accidents.

## Attachments
No attachments
