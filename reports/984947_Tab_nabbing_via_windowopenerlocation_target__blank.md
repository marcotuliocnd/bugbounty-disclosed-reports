# Tab nabbing via window.opener.location (target "_blank")

## Report Details
- **Report ID**: 984947
- **URL**: https://hackerone.com/reports/984947
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-09-17T19:35:31.403Z
- **Disclosed**: 2020-12-26T16:42:32.124Z

## Reporter
- **Username**: subnetix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
When you open a link using target="_blank", the page that opens in a new tab get access to the initial tab and change its location using the window.opener.location function.
## Platform(s) Affected:
website

## Steps To Reproduce for the first target _blank:
  1. First target "_blank" 
  1. On https://www.tumblr.com/customize add the following script : 

```javascript
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
``` 

  1. Send to test account your link blog.
  1. On the test account open the link ; the initial page will be changed.
  1. Watch the POC video if you want more details.

## Steps To Reproduce for the second target _blank:
  1. Second target "_blank" 
  1. On https://www.tumblr.com/customize add the following script : 

```javascript
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
``` 

  1. Send to test account random message.
  1. On the test account click on the account name and the blog view page will be opened, next click on account blog link.
  1. Watch the POC video if you want more details. 

## Steps To Reproduce for the third target _blank:
  1. Third target "_blank" 
  1. On https://www.tumblr.com/customize add the following script : 

```javascript
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
``` 
  1. Send to test account your link blog.
  1. On the test account navigate somewhere, click on the name account of sender ; the initial page will be changed.
  1. Watch the POC video if you want more details.

## Supporting Material/References:

  * don't forget to close all tabs
  * POCs ! 
  * relative report that can maybe help you : https://hackerone.com/reports/179568

## Impact

It can allow an attacker to open a malicious site on the victim account.
Perform phishing attacks.

## Attachments
- report-1.mp4
- report-2.mp4
- report-3.mp4
