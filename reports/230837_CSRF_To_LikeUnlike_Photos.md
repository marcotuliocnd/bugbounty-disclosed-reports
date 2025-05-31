# CSRF To Like/Unlike Photos

## Report Details
- **Report ID**: 230837
- **URL**: https://hackerone.com/reports/230837
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-22T17:59:33.758Z
- **Disclosed**: 2017-06-30T04:51:38.579Z

## Reporter
- **Username**: pabster
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Description:
There is a CSRF vulnerability allowing an attacker to trick a user into visiting his/her site and to forge a request to zomato.com that will in turn like or unlike the photos of the attacker's choosing.

The vulnerable page is https://www.zomato.com/php/photoViewerActionsHandler.php , which doesn't need a csrf token or anything like that in a POST request to like or unlike photos. The request looks like this: 
POST /php/photoViewerActionsHandler.php
Parameters: 
type = UNLIKE_PHOTO (Or LIKE_PHOTO)
photo_id = [photo id]

To get the photo id you just have to click on the photo you want the victim to like or unlike, then when you look at the url it should look something like: /es/photos/pv-res-18342981-r_2MzMzNTg1NzIwO      the last section will be /pv-res-[number]-[photo id]

Once you have the photo id you can perform the CSRF attack easily.

Steps to reproduce:
1. Deploy a webserver with an index.html file:

<form name="x" action="https://www.zomato.com//php/photoViewerActionsHandler.php" method="post">
<input type="hidden" name='type' value="LIKE_PHOTO">
<input type="hidden" name='photo_id' value="r_2MzMzNTg1NzIwO">
</form>
<script>document.x.submit();</script>

(Change the value attribute for the input tag with the name attribute of photo_id with the target photo's id and the input tag with the name attribute of type with UNLIKE_PHOTO if you want the victim to unlike a photo.
2. Get a victim to visit the webserver.

When done in large numbers you can easily get a photo to get 100's of likes. You can also damage a restaurant's reputation by using this attack to decrease their likes, and improve your own restaurant's reputation by using this attack to increase their likes.

Hope it helps.
Sincerely,
Pablo


## Attachments
No attachments
