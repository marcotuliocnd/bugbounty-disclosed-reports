# XSS [flow] - on www.paypal.com/paypalme/my/landing (requires user interaction)

## Report Details
- **Report ID**: 425200
- **URL**: https://hackerone.com/reports/425200
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-18T00:36:35.334Z
- **Disclosed**: 2018-11-06T16:40:59.057Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paypal

## Vulnerability Information
### Steps to reproduce
On _Chrome and Firefox_:
1. Go to `https://www.paypal.com/paypalme/my/landing?flow=cmV0dXJuVXJsPWphdmFzY3JpcFQ6UEFZUEFMLmNvbSUzZDEsbG9jYXRpb24lM2QnamF2YXNjcmlwdDpceDNjc3ZnXHgyMG9ubG9hZD1hbGVydFx4Mjhkb2N1bWVudC5kb21haW5ceDI5XHgzZScmY2FuY2VsVXJsPWphdmFzY3JpcFQ6UEFZUEFMLmNvbSUzZDEsbG9jYXRpb24lM2QnamF2YXNjcmlwdDpceDNjc3ZnXHgyMG9ubG9hZD1hbGVydFx4Mjhkb2N1bWVudC5kb21haW5ceDI5XHgzZSc=`
1. Click on the __X__ at the top right of the modal window

On _Safari_:
1. Go to `https://www.paypal.com/paypalme/my/landing?flow=cmV0dXJuVXJsPWphdmFzY3JpcFQ6UEFZUEFMLmNvbSUzZDEsbG9jYXRpb24lM2QnamF2YXNjcmlwdDphbGVydFx4Mjhkb2N1bWVudC5kb21haW5ceDI5JyZjYW5jZWxVcmw9amF2YXNjcmlwVDpQQVlQQUwuY29tJTNkMSxsb2NhdGlvbiUzZCdqYXZhc2NyaXB0OmFsZXJ0XHgyOGRvY3VtZW50LmRvbWFpblx4Mjkn`
1. Click on the __X__ at the top right of the modal window

### Explanation
The value of the paramter `flow` is a base64 value which decoded looks like this:
```
returnUrl={paypal_url}&cancelUrl={paypal_url}
```
`cancelUrl` is passed as the `href` value of the __X__ button at the top right of the modal window that appears. It doesn't matter if you already created a paypal.me address.
`returnUrl` is passed as the `href` value of the __Done__ button when you follow the instructions to create a paypal.me profile.

The problem is that `javascripT:paypal.com` is considered a valid value for `returnUrl` and `cancelUrl`. However, there a few restrictions already: you can't add a `%0a` character (or almost any special character, even using HTML encoding) and the URL has to start with `javascripT:*.paypal.com` or `javascripT:paypal.com` or `javascripT://paypal.com` or `javascripT://*.paypal.com`. 
First thing you have to take care of is about `paypal.com` because the object `paypal` doesn't exist, which will stop anything from working. The good thing is that `PAYPAL` does exist and `PAYPAL.com` is accepted as a valid value in the URL.
The second thing is that parentheses, quotes, semicolons and new lines are not allowed. But equal signs, commas and single quotes are allowed. So, you can set `PAYAPL.com` to any valid value you want like `PAYPAL.com=1`. Then you can use `location` and set it to something like `'javascript:alert\x28\x29'`. I encoded the invalid special characters in a encoding that Javascript understands and will decode before changing the `location`. Now you can put anything you want.

On Firefox and Chrome, the `location='javascript:alert\x28\x29'` writes `javascript:alert()` in the document, so I had to change it to make it work. Ended up with this: `location='javascript:\x3csvg\x20onload=alert\x28document.domain\x29\x3e'`.

## Impact

You could make actions as the authenticated user and probably more but I didn't tried.

## Attachments
No attachments
