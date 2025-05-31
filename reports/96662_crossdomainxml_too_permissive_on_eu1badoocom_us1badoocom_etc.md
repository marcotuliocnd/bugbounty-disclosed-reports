# crossdomain.xml too permissive on eu1.badoo.com, us1.badoo.com, etc.

## Report Details
- **Report ID**: 96662
- **URL**: https://hackerone.com/reports/96662
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-10-29T23:54:41.876Z
- **Disclosed**: 2017-08-31T10:20:34.330Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
__Description__

The file _crossdomain.xml_ that is hosted at https://[eu1,us1,etc].badoo.com/crossdomain.xml is too permissive in the scope of allowed domains to access the content in the domain using Flash.
When you contact Badoo via https://us1.badoo.com/feedback/, you can upload a file. This file can be a Flash file. This file is hosted at https://static-*.badoo.com which is an allowed domain because of the line `<allow-access-from domain="*.badoo.com"/>` in the _crossdomain.xml_ file.
The problem is that an attacker can upload a malicious Flash file and load it from an external website. This allows to read and update information of the current logged in user.

__Proof of concept__

1. Download the file _bug.jpg_ that I attached (the source code is attached too).
2. Go to https://us1.badoo.com/feedback/.
3. Click on _General question_.
4. Fill the required fields.
5. Click _Attach screenshot_.
6. Select the file you downloaded in step 1 and click _Open_.
7. When the upload is finished, click _Send message_.
8. Go to the inbox of the email address that you entered for _Email address_.
9. Open the email with the subject "We've received your query", sent by Badoo Support Team.
10. Click on the link that appears (like: https://us1.badoo.com/support.phtml?rid=11761766:noX7xh7DgCDiU80B).
11. Click on the name of the file that you uploaded (_bug.jpg_). Appears below the message you wrote.
12. Right click on the black box that is shown, and find the `<img alt="" class="pv-big" id="big_photo">` element.
13. Save the `src` value of the element (it looks like https://static-us2.badoo.com/file/36140042.0?signature=41918aa731579d62a601d6391ac793f1&amp;dt=9tKskfyuTrlkjvLg).
14. Download the file _bug.html_ that I attached.
15. Open the file _bug.html_ in a text editor. Change the value of the attribute `src` of the element `<embed>` to the value that you saved in step 13.
16. Serve the file _bug.html_ from a server (can be local, like `php -S 0.0.0.0:8000`).
17. Verify that you are logged in Badoo.
18. Open the file _bug.html_ from the server using the web browser (like http://localhost:8000/bug.html).
19. The content of the endpoint https://us1.badoo.com/settings is showed in the `<textarea>`.

This is a simple proof of concept, but it's possible to make POST requests too.

Let me know if something is not well explained.

## Attachments
- bug.as
- bug.jpg
- bug.html
