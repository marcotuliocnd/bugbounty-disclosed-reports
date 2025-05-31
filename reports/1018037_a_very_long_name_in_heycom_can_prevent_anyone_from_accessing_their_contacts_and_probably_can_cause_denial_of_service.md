# a very long name in hey.com can prevent anyone from accessing their contacts and probably can cause denial of service

## Report Details
- **Report ID**: 1018037
- **URL**: https://hackerone.com/reports/1018037
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-24T22:32:42.256Z
- **Disclosed**: 2020-11-10T13:21:36.935Z

## Reporter
- **Username**: tw4v3sx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Summary :
=========
after trying to change my initial name to something long i found out that their are no limits to how long it can be , so i directly changed it to something very long {F1050497} which caused my account to really slow down when accessing it and in **the android app , it just keeps crashing** whenever i open it ( no way to access my account at all ) + if i make it longer i get a **500 Internal Server Error response** which highly suggests that this can cause a **server side denial of service .**

Description:
==========
due to not checking the length of the name one can change it to a very long one causing both a server side denial of service  and a client side one

server side : 
------------

one can send multiple requests to change the name of the account and each of them containing a very long name which will cause a 500 internal server error leading to an extensive Resource Consumption.

client side : 
-----------
- if one is able to change the name another account he will also have the ability to crash his android app therefore preventing him from accessing his account.
- if one with a long name sends a message to any email he will slowwwwww down everything where the message appears including folders (inbox , trash ..) and prevent him from accessing his contacts where the email's name also appears , because the app will hang on a loading screen for about 40min each time , and this can be more if for example he sends multiple messages or use multiple accounts ( each on with a long name ) to send a message to the victim mail.

Proof of Concept:
==============

1. open `https://app.hey.com/contacts/%user_id_number%/user/edit`and change the name to the one attached {F1050497} and submit.
1. now u can't open the android app and u can slow down anyone's account just by sending them a message (or multiple ones).

## Impact

- **Attacker can perform a DoS Attack against the server**
- **slow down anyone's account**
- **crash the android app**

## Attachments
- name.txt
