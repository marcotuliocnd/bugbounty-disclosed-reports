# Cache poisoning via X-Forwarded-Host in www.shopify.com/partners/blog

## Report Details
- **Report ID**: 977851
- **URL**: https://hackerone.com/reports/977851
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-09T20:28:19.711Z
- **Disclosed**: 2020-09-11T17:03:05.108Z

## Reporter
- **Username**: dakitu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello, run in loop requests with```  X-Forwarded-Host: your_hackerz_site.com ``` - after some time You will notice in response ``` your_hackerz_site.com ```

{F981839}

now remove ``` X-Forwarded-Host  ``` - there still be our url:

{F981841}

i've logged to my VPS to verify this bug and downloaded poisoned page (https://www.shopify.com/partners/blog/7-web-design-and-development-awards-you-should-enter) , it's contains links to collabolator:

{F981844}

{F981845}

Looks like there is no URL keys so i stopped testing cause i'm breaking site functionally, but it was be worth to check if we can poison  ```  X-Forwarded-Host : foobar.pl"><img src=x onerror=blah> ``` or try use other headers, if i get permission i can try other vectors on a older article to prevent distributing users.

## Impact

poisoning links, eg. FB share button:

``` https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fa4129912adehq5m14ryflu01ovx68j0ur0ho6.burpcollaborator.net%2Fpartners%2Fblog%2F7-web-design-and-development-awards-you-should-enter ```

## Attachments
- Screenshot_2020-09-09_22-19-31.png
- Screenshot_2020-09-09_22-19-31.png
- Screenshot_2020-09-09_22-22-31.png
- Screenshot_2020-09-09_22-22-44.png
