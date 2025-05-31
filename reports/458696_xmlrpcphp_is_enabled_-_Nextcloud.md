# xmlrpc.php is enabled - Nextcloud

## Report Details
- **Report ID**: 458696
- **URL**: https://hackerone.com/reports/458696
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-07T17:23:40.923Z
- **Disclosed**: 2020-03-01T13:20:04.659Z

## Reporter
- **Username**: shiv_shakti
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Nextcloud Team,

Summary: An attacker can devise a XML request to list all the methods that are enabled on the server. Replace Get with POST request and add method call in the request.

To reproduce the vulnerability you need to use Firefox browser and Burpsuite

    Open: https://nextcloud.com/xmlrpc.php.

This URL is publicly accessible, thus confirming the presence of the vulnerability. Proceed further in order to get request/response for above vulnerability.

    Capture the Get method in burpsuite tool

    Send the Get method in repeater tab.

    As "XML-RPC server accepts POST requests only" write POST instead of GET in Request window.

    Write the method list command below for Post request in Request window like:

<?xml version="1.0" encoding="utf-8"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

    We will get all the available methods for https://nextcloud.com/xmlrpc.php

Regards
jaimaakali

## Impact

Unauthorized Access

## Attachments
- Screenshot_from_2018-12-07_14-54-23.png
- Screenshot_from_2018-12-07_14-54-39.png
