# After changing the storefront password, the preview link is still valid

## Report Details
- **Report ID**: 1370749
- **URL**: https://hackerone.com/reports/1370749
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-15T06:20:01.831Z
- **Disclosed**: 2022-04-21T22:38:45.570Z

## Reporter
- **Username**: tomorrow_future
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
##Description:

1. The user needs to know the storefront password to generate the preview link.
2. After the administrator changes the storefront password, users can still access the storefront through the preview link. 

3.reason:
（1）User can generate preview link.
（2）Simply changing the password will not invalidate the preview link. Only after closing and restarting the storefront password, the previous preview link will become invalid.

##Step：

1. Visit the storefront and enter the password.

2.Search ```shopify.theme``` in the web development tool of the browser to get the theme ID value.
{F1482354}

3.Replace the value of the ```preview_theme_id parameter```.
```
https://your-store.myshopify.com.myshopify.com/?_ab=0&_fd=0&_sc=1&preview_theme_id=xxxxxxxx
```

4. Access the preview link, when the storefront password is changed, the preview link is still valid.

5.Video:
{F1482355}

## Impact

After changing the storefront password, the preview link is still valid

## Attachments
- theme_id.png
- video.mp4
