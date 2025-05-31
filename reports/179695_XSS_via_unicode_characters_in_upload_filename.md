# XSS via unicode characters in upload filename

## Report Details
- **Report ID**: 179695
- **URL**: https://hackerone.com/reports/179695
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-11-02T17:06:33.182Z
- **Disclosed**: 2020-08-28T16:43:32.278Z

## Reporter
- **Username**: kahoots
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Wordpress has a vulnerability that could lead to javascript execution and (thus) privileged escalation via an admin visiting the wrong page via specially crafted JavaScript. Unicode characters are escaped by javascript but they are not escaped serverside. I've checked the latest version (4.6.1) at the time of writing this report and it is vulnerable.

Steps to reproduce: 

1. You will need a way to bypass javacsript in a post request. For purposes of this report I'll assume the free firefox plugin tamperdata is used.
2. You will need an installation of wordpress with the capability of uploading files.
3. Create a blank image file with a javascript alert i.e <script> alert('XSS') </script> and name the file a valid image extension such as .png
4. In wordpress, go to the file upload screen on the side bar (Media -> Add new). Activate tamperdata and click upload. Use a special Unicode character at the begining of the filename. Note that for this step all that is required is upload privileged - see https://codex.wordpress.org/Roles_and_Capabilities
5. The image page will be called "-1" visit that page. It will render as HTML.

Note that an image could be specially crafted with a 0-sized iframe and upon an administrator visiting the page could redirect via javascript to create another user account leading to privilege escalation.

Here is my explanation for the bug:

Unicode characters are not escaped server-side, but they appear to be escaped client side which can be bypassed. This can be shown by trying to upload a file with a unicode character and seeing the "Â" character before it. For example: "±myfile.png" would become "Â±myfile.png" - this was tested with tamperdata by watching the image field.

In wordpress\wp-admin\includes\file.php there is a function called "_wp_handle_upload" Ideally, this is where special characters should be escaped or dealt with. That functon calls "wp_unique_filename" which then calls "sanitize_file_name" which the return value is a number instead of a filename. 

If a file with a valid file extension is given such as "myfile.png" intended behavior is that it will save the file. If it is given twice, then it will be named myfile-1.png and so on. However, because a special character can make a return value of 0 from the unique_filename function, it will result in "-1" being the file name. If another file is uploaded it will be called "-2" if it is in the same year and month folder. For example: "wordpress\wp-content\uploads\2016\10" if there is already a "-1" file there and a month passes -1 would go in the next folder. "wordpress\wp-content\uploads\2016\11"

Apache normally prevents javascript execution from images, however a filename such as "-1" will render text which can execute javascript. 

The best mitigation would be to check for special characters in the _wp_handle_upload function.

(I'm new to writing hackerone reports, hopefully this is clear enough.)

## Attachments
- example.png
