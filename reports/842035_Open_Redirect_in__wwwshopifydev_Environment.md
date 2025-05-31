# Open Redirect in  www.shopify.dev Environment 

## Report Details
- **Report ID**: 842035
- **URL**: https://hackerone.com/reports/842035
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-06T23:24:23.133Z
- **Disclosed**: 2021-11-18T19:12:15.693Z

## Reporter
- **Username**: beerboy_ankit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary
Reported vulnerability allows attacker for open/unknown redirect for victim user 

## Steps to reproduce

1) Go to https://shopify.dev/concepts/shopify-introduction
2) Click on search
3) Type ``` POC ``` in search box and hit enter 
4) Right click on first result displayed as ```POS``` and click on copy  link address which will look like below.
```
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=%2Ftools%2Fapp-bridge%2Factions%2Fpos&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false
```
5) Modify ```result_url``` parameter in link shown above to ```result_url=@www.facebook.com```

6) Final link will look like this
```
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false

```
7) alternatively You can also directly  access below link for your convenience
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false


Culprit for redirect is ``` @ ``` character which will bypass the logic implemented to redirect user to access resource on www.shopify.dev itself and follow url after ``` @ ``` 


Note: I am submitting this report as this bypass technique can be use to any other domain on Shopify if same logic is implemented and could leads attacker for wider attack scope.


Thanks you!

## Impact

Invalidated Redirect

## Attachments
No attachments
