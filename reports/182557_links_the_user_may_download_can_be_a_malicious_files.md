# links the user may download can be a malicious files

## Report Details
- **Report ID**: 182557
- **URL**: https://hackerone.com/reports/182557
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-16T16:34:01.706Z
- **Disclosed**: 2017-08-10T05:10:18.208Z

## Reporter
- **Username**: seifelsallamy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hi,

## Summary:

This vulnerability is pretty simple and pretty dangerous at the same time 

Almost any link the user tries to download it's extension is set according to the file extension in the path 
if the path is `/` then it download's it according to the domain name  
Eg:
[1] http://example.com/example.php
if the user downloaded the link the file type would be `.php`
that's not very dangerous though 

[2] http://example.com/example.exe
if the user downloaded the link the file type would be `.exe`
Okey that's dangerous but it requires a lot of social engineering 
 
[3] http://example.com/
if the user downloaded the link the file type would be `.com`
this requires less social engineering and it's pretty dangerous 
why?
because `.com` files are executable files which may can do what `.exe` can do
here's links about `.com` files
https://en.wikipedia.org/wiki/COM_file
and the difference between `.exe` and `.com`
https://blogs.msdn.microsoft.com/oldnewthing/20080324-00/?p=23033

there's a new many domain names which may can create malicious extensions like `.com`
as example
`.com.py`
which can create a python file 

any website can make his favorable extension in the domain path and when the user downloads it it will be downloaded by the extension
as example http://example.com/example.exe

## Products affected: 

windows 10 x64 brave latest version 

## Steps To Reproduce:

there is 3 ways to reproduce 
[1]
execute this html 
`<a href="http://example.com" download>http://example.com</a>`
right click on the link > Save Link as... > Save
[2]
go to http://example.com
right click > Save Page as... > Save
[3]
execute this html and directly click the link it will download directly 
`<a href="http://example.com" download>http://example.com</a>`


####Note : 
The none exist pages can't be downloaded 

----------
Any link the users tries to download must be `.htm` or `.html`


## Supporting Material/References:
F135079

Thanks!

## Attachments
- RCE_At_Brave_Browser.jpg
