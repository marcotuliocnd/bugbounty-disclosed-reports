# After the upload of an private file, using transformations, the file becomes public without the possibility of changing it.

## Report Details
- **Report ID**: 1984060
- **URL**: https://hackerone.com/reports/1984060
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-11T14:54:33.393Z
- **Disclosed**: 2023-10-20T09:37:30.009Z

## Reporter
- **Username**: limusec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
When an user uploads a private file, ex (Screenshot 1), where only he has access to. Using the "View transformations" function can generate different kinds of image transformations (Screenshot 2). But after the generation of that transformation for example clicking on  the regenerate button next to profile. The function will create a cropped public image, where the user is unable to edit or modify his own generated image (Screenshot 3). 

Issue: You have a picture with you smiling and your passport holding in your hand (An example would be a "know you customer purpose" selfie). You like that picture on how you look, so you upload it on phabricator, privately, assuming nobody can view it. You click on view transformations, to modify and crop that picture, to get rid of the sensitive data passport you are holding in your hand, so only the face remains. After you clicked on the regenerate next to profile, you realize the crop doesn't work as intended and your passport data is still in there. So you want to modify/delete that picture but you cant. And what's worse that picture visible to anyone and you don't have access to remove it nor to modify it.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

 1.Upload a private picture here: https://phabricator.allizom.org/file/upload/
 2.Change the visibility to no one or just you.
 3. After the upload, click on "View Transformations" on the right.
 4. There you can create different transformations when you click on regenerate.
 5. After that you, you get a new preview to your generated picture. 
 6. Now go back, to the transforms page, and you get a new link on phabricator, that is public, and can't be changed.

I've added a video that showcases this behavior. 


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
I've added screenshots and a video to showcase this issue.
  * [attachment / reference]

## Impact

The user is assuming that he can upload private data securely. Not knowing that the transform feature will make his uploaded files public with no way to delete it, could in worst case leak PII information.

## Attachments
- 1.PNG
- 2.PNG
- 3.PNG
- 2023-05-11_16-48-42.mp4
