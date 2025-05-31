# Issues with uploading list images

## Report Details
- **Report ID**: 159820
- **URL**: https://hackerone.com/reports/159820
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-16T18:46:47.530Z
- **Disclosed**: 2016-09-26T20:14:17.710Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hi,

There are several issues with uploading images for a list, i.e. with a PUT request to `https://www.instacart.com/api/v2/lists/153253` and passing `list[remote_image_url]`.

First, information about open ports and SSH information can be disclosed via different urls. For example, PUT-ing localhost:80 will return a 404 error, but localhost:1010 will return a connection refused error. PUT-ing localhost:22 will, return `"Image could not download file: wrong status line: 'SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.3'"`, showing that OpenSSH version 6.6.1p1 is being used, which is outdated and may be vulnerable to published exploits.

Passing a value such as `http://google.com` will show that rmagick is being used, with an error: `"Image must be a JPEG or PNG","Image Failed to manipulate with rmagick, maybe it is not an image? Original Error: unable to open file `/tmp/magick-ezcF8DGU': No such file or directory @ error/constitute.c/ReadImage/583"`

Finally, uploading a JPG such as in [https://hackerone.com/reports/390] makes the server timeout and returns a 502 error, overflowing the memory. I have attached the image below.

Thanks for your time, and please let me know if you need any more information.

## Attachments
- image.jpg
