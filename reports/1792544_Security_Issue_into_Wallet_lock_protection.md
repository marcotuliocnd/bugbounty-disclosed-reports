# Security Issue into Wallet lock protection 

## Report Details
- **Report ID**: 1792544
- **URL**: https://hackerone.com/reports/1792544
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-12-04T17:20:39.808Z
- **Disclosed**: 2023-01-11T13:17:23.226Z

## Reporter
- **Username**: bug_vs_me
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hiro

## Vulnerability Information
# Description

While testing wallet extension i generally try to test multiple endpoints, so 2 tabs were open of wallet on chrome-extension://ldinpeekobnhjjdofggfgjlcehhmanlj/popup.html


So i tried to lock Wallet extension buti found that i can still use browser in 2nd tab, why i had already locked wallet,


So there is a security issue where wallet is not properly encrypted after user press lock

Wallet should close all open tabs of wallets and encrypt data for all tabs, It's very insecure way of password protection or lock protection


# Steps To reproduce

To understand clearly i had created a POC video 
{F2061644}

1. Open two tabs of chrome-extension://ldinpeekobnhjjdofggfgjlcehhmanlj/popup.html
2. lock wallet in any of 1 tab and you can see you can access wallet on other tab and still able to do transaction as shown in POC{F2061648}


# HOW to fix?

Edit code and make sure when user click on lock wallet wallet should encrypt data in all tabs or close rest of the tabs to protect user and make lock protection work more securely

Thank you

## Impact

This is totally fail of lock protection AND attacker can use this vulnerability to craft custom attacks

## Attachments
- hiro-wallet.mkv
- image.png
