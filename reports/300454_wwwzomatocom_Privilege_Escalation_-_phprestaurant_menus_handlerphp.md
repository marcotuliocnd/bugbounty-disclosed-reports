# [www.zomato.com] Privilege Escalation - /php/restaurant_menus_handler.php

## Report Details
- **Report ID**: 300454
- **URL**: https://hackerone.com/reports/300454
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-25T13:27:52.919Z
- **Disclosed**: 2018-03-29T17:00:35.760Z

## Reporter
- **Username**: gerben_javado
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
#Introduction
In the following ██████████ the endpoint `/php/restaurant_menus_handler.php` was found. This endpoint is meant solely to be accessible for admins, however due to insufficient protections normal users can access this endpoint too. This results in any Zomato user being able to edit and remove menu's from any restaurant. The following actions have been found in the JS file but there might be more: `menu_collected`, `toggle-res-menu-type`, `clear_menu_tool`, `change-menu-type`.

#POC
Toggle-res-menu-type will be used in the POC since it switches between text and image menu's which makes it very easy to see the change happen on the page of the restaurant. When switching to text the images of the menu will disapear (and reappear when enabled).

Go to https://www.zomato.com/████ and view the images under the menu section. After that submit the following JS code in the developers console. After this reload the page and the menu images should be gone. Do it once more and the images should reappear again.

```js
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:██████}
```

## Impact

Any user can delete and edit any menu of any restaurant. The reason is that an admin endpoint has insufficient access protection.

## Attachments
No attachments
