# Stored XSS in the file search filter

## Report Details
- **Report ID**: 873584
- **URL**: https://hackerone.com/reports/873584
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-13T18:05:58.255Z
- **Disclosed**: 2020-07-03T19:51:36.848Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
1. Download Concrete5 8.5.2 and install it
2. Log into your Concrete5 instance as admin
3. Go to Dashboard >Files > Search
4. In the file search bar, click **Advanced**
5. In the window that appears, enter a phrase and click the save button, paste the following payload: `<img src=1 onerror=alert(1)>` and click the save button
6.  In the filter search bar, click **Edit** and wait for the malicious code to execute

## Impact

If a user has been added to the administrators group, then he can create a malicious filter and wait for someone else to change this filter

## Attachments
No attachments
