# Know whether private project name exists or not within a group using link comments

## Report Details
- **Report ID**: 495497
- **URL**: https://hackerone.com/reports/495497
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-13T19:02:16.247Z
- **Disclosed**: 2019-10-07T09:01:16.877Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:** 
Hello,

It is possible for anyone to know if private project exists or not in public/private groups if they can guess the project names correctly.


**Description:** 
Using markdown feature, we can form a comment which will allow us to know if the private project is exists within a group or not.



## Steps To Reproduce:
1. As any user, go to any issue/merge request and select the comment box
2. Select the link which will appear like `[](url)`
3. Now if you know the group name, just make a guess of the private project that may exists within that group. Lets say `PublicGroup` contains a `PrivateProject` but this user doesnt have any access to `PrivateProject`. 
4. This user can still know that this project exists if the user guess this name correctly
5. Just form a url like `[Click](https://gitlab.com/PublicGroup/PrivateProject/issues/1)` and comment.

6. Now hover over the **Click** link text. Notice the status bar (bottom left) of your browser. This will show you the link of your currect project with /click appended to the url.

7. Now just make a wrong guess `[Click](https://gitlab.com/PublicGroup/PrivateProject1/issues/2)`.

8. Now hover over again on **Click** link text and you will notice that the wrong link shows in the browser status bar as it is. 

9. So we can say, if we can guess the project name correctly, it shows current project link.

10. If we guess it wrong, the link appears as it is.

11. So the conclusion is, if link appears as it is on browser status bar, project DOES NOT exists in the group. If link appears of current project, then project Exists in the group!


Regards,
Ashish

## Impact

Know whether private project name exists within a group or not

## Attachments
No attachments
