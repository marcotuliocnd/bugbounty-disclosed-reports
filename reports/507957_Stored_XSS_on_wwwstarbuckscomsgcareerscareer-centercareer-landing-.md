# Stored XSS on www.starbucks.com.sg/careers/career-center/career-landing-*

## Report Details
- **Report ID**: 507957
- **URL**: https://hackerone.com/reports/507957
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-11T15:02:21.231Z
- **Disclosed**: 2019-04-10T21:20:41.032Z

## Reporter
- **Username**: 13ern
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** 
While enumeration of the webpage for Starbucks I observed the following pages.

https://www.starbucks.com.sg/careers/career-center/career-landing-5?

The webpage have been highly spam by automated scanners or malicious attack.
By clicking on any of the pages it would redirect the user to a wordpress website

```
<a href="https://obatkebaskesemutan.wordpress.com/" rel="dofollow noopener" style="z-index:9999999999999999;oncontextmenu:return false;onkeydown:return false;onmousedown:return false;position:fixed;top:0px !important;left:0px;width:100%;height:100%;color:transparent !important;display:block;text-align:center;font-size:0px;background-color:transparent;background-position:center;background-repeat:no-repeat;background-size:cover;" target="_blank" title="Obat Herbal">Obat Kebas</a>

```
The owner of the following wordpress pages could manipulate user into redirecting to a Starbucks page for a job offer and an user by clicking on the webpage would redirect to a website of its choosing.

{F439338}
{F439340}

* List any recommendations for bug fix
Remove the pages from Starbucks webpage.

## Impact

The owner of the following wordpress pages could manipulate user into redirecting to a Starbucks page for a job offer and an user by clicking on the webpage would redirect to a website of its choosing.

## Attachments
- Capture.PNG
- Capture2.PNG
