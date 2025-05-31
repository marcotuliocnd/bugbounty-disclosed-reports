# Stored XSS on express entries

## Report Details
- **Report ID**: 873474
- **URL**: https://hackerone.com/reports/873474
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-13T15:08:57.463Z
- **Disclosed**: 2020-07-03T19:51:03.890Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
1. Download Concrete5 8.5.2 and install it
2. Log into your Concrete5 instance as admin
3. Go to Dashboard > System settings > Express entities (/index.php/dashboard/system/express/entities) 
4. Сlick on the **Create** button
5. in the field **Name** paste the following text: `</h1><script>alert(1)</script><h1>`
6. Go to tab **View Objects**

## Impact

If the user was added to the group of administrators, then he can create an express object with a payload in the name and give a link to another administrator to view the created object.

## Attachments
No attachments
