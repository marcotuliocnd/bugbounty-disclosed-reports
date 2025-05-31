# full path disclosure at hosted.weblate.org/admin/accounts/profile/ 

## Report Details
- **Report ID**: 225495
- **URL**: https://hackerone.com/reports/225495
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-02T08:38:53.634Z
- **Disclosed**: 2017-05-17T14:07:42.355Z

## Reporter
- **Username**: geekdad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Browsing this link https://hosted.weblate.org/admin/accounts/profile/  will ask for admin username and password as asked  when browsing https://hosted.weblate.org/admin/accounts/ or https://hosted.weblate.org/admin/ hence disclosing the directory path of forbidden area.
screenshot : path.png

also it is found that there is no rate limiting enforced at https://hosted.weblate.org/admin/login/?next=/admin/  hence attacker can break into staffs account by brute forcing. 
screenshot : login.png

## Attachments
- path.png
- login.png
