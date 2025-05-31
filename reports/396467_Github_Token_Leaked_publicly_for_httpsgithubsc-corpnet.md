# Github Token Leaked publicly for https://github.sc-corp.net

## Report Details
- **Report ID**: 396467
- **URL**: https://hackerone.com/reports/396467
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-17T09:49:01.636Z
- **Disclosed**: 2018-10-08T12:57:23.028Z

## Reporter
- **Username**: th3g3nt3lman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
###Description :

GitHub is a truly awesome service but it is unwise to put any sensitive data in code that is hosted on GitHub and similar services as i was able to find github token indexed ***7 hours Ago*** by user ***██████ - Software Engineer - Snap Inc***

### Issue & POC :
You can find the leak in this link :
https://github.com/█████/leetcode/blob/0eec6434940a01e490d5eecea9baf4778836c54e/TopicMatch.py

````

import os
import requests
import sys
pull_number = 76793
pull_url = "https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/" + str(pull_number)
payload = {}
payload["Authorization"] = "token " + "9db9ca3440e535d90408a32a9c03d415979da910"
print payload
r = requests.get(pull_url,

```

## Impact

I didn't try anything with the token, and dont know what access it has, and i know that in order to login to https://github.sc-corp.net you need to have an email @snap but still i though it would be a good idea to share this finding with you in case it can be used in a way that i dont know.

Best Regards

## Attachments
No attachments
