# [Buddypress] Arbitrary File Deletion through bp_avatar_set

## Report Details
- **Report ID**: 183568
- **URL**: https://hackerone.com/reports/183568
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-20T06:36:56.932Z
- **Disclosed**: 2017-08-22T18:04:10.313Z

## Reporter
- **Username**: mopman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi,
The bp_avatar_set action in BuddyPress when cropping avatars allows an attacker to arbitrarily delete a file the webserver can delete through the 'original_file' parameter.

For example:

* Create a user on a Buddypress-powered Wordpress instance (any user is OK, doesn't need to be admin, just needs to have the ability to change it's own avatar in the Buddypress profile which is normal).
* Navigate to the avatar change URL for example /members/<username>/profile/change-avatar/ on my install.
* Click the button to upload an image and select any valid image. Allow the first request which uploads this image to submit as normal.
* Select the crop button, but do not allow the request to complete (I used Burp and enabled intercept mode). Modify the request to change the original_file parameter to point to a file you wish to delete, traversing up with ../.. if needed. So for example where my legitimate param was:

original_file=http%3A%2F%2Flocalhost%2F~sam%2Fwordpress%2Fwp-content%2Fuploads%2Favatars%2F2%2Fmy_ugly_face.jpg

Change to:

original_file=http%3A%2F%2Flocalhost%2F~sam%2Fwordpress%2Fwp-content%2Fuploads%2Favatars%2F2%2F../../../../../wp-config.php

Remember it will be in a numbered folder probably, so you need one more .. than expected from the URL. You can upload an image for real to see how the path ends up for guidance on this if you're an attacker and don't know the folder structure.

The wp-config.php file will be deleted when unlink() is called and the blog will then be unavailable, of course, in this case.

This path needs to be somehow validated such that it can only delete uploaded avatars (constraining to the upload directory would still allow you to delete, say, other users avatars, or other uploaded files, which would still make me sad :()

Let me know if you have any trouble reproducing or need any further info - I think I explained OK, but it is very late here. ;)

o/

## Attachments
No attachments
