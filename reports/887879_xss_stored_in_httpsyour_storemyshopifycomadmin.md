# xss stored in https://your store.myshopify.com/admin/

## Report Details
- **Report ID**: 887879
- **URL**: https://hackerone.com/reports/887879
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-31T12:27:24.446Z
- **Disclosed**: 2020-08-24T16:08:20.442Z

## Reporter
- **Username**: lbro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
hello , 
i fond xss stored in  https://your store.myshopify.com/admin/
steps ;
1. go to ```https://swqdewd.myshopify.com/admin/menus/new```
2. click in Add menu item
3. add name ```"><img src="x" onerror="alert(document.cookie)">``` AND any link 
4. now click add 
5. click in remove item 
6. alert 
7. watch the vedio poc for more information

## Impact

xss attack .....

## Attachments
- Enregistrement__4.mp4
