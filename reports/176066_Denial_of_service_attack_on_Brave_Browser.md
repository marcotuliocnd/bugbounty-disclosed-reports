# Denial of service attack on Brave Browser.

## Report Details
- **Report ID**: 176066
- **URL**: https://hackerone.com/reports/176066
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-16T00:14:22.107Z
- **Disclosed**: 2017-02-10T23:56:24.807Z

## Reporter
- **Username**: sahiltikoo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information


## Summary:
Hey there,

Basically,an HTML sent by an attacker to a victim can cause dos attack(whole system log's out) when that file is opened by the victim in his brave browser.This vulnerability is occurring because browser is not able to handle the input passed in alert() JavaScript function.This bug has been tested on latest brave browser in Linux platform.

## Products affected: 

Brave's Browser in Linux(Kali Linux)

## Steps To Reproduce:


1 create an html file like :-

Brave.html( it is attached as POC below) i couldn't write the content of file here because the value inside alert() parameter is too large to be displayed here.

2 Open the file in your Brave browser in Linux platform.

## Supporting Material/References:

I have attached an html file below just download it and open it up in brave browser on linux system and 

screen will show "OH! something went wrong and you will be logged out".


## Attachments
- Brave.html
