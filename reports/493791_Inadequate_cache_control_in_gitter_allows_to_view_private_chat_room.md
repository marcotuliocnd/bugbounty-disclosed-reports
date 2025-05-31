# Inadequate cache control in gitter allows to view private chat room

## Report Details
- **Report ID**: 493791
- **URL**: https://hackerone.com/reports/493791
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-02-11T07:07:32.178Z
- **Disclosed**: 2019-03-08T18:41:50.920Z

## Reporter
- **Username**: dhakal_ananda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi Gitlab,

**Summary:**
I have found a inadequate cache control vulnerability in Gitter.

**Description:**
You can use the backspace button to get the full access to the account. There is no cache control and the browser saves sensitive information of a private chat room.
This report is influenced by the disclosed report #407763. The impact and attack scenario is also the same.

## Steps To Reproduce:

1. Sign in to Gitter
2. Go to a private room
3. Sign-out from the device
4. Click on backspace
5. Chat in the private room

You can access the private room without actually being logged in. You can also chat from the logged out account.

## Impact

Sensitive information can get disclosed through a single backspace.

## Attachments
No attachments
