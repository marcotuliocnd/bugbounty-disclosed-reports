# IDOR in TalentMAP API can be abused to enumerate personal information of all the users

## Report Details
- **Report ID**: 1848176
- **URL**: https://hackerone.com/reports/1848176
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-01-26T19:13:04.200Z
- **Disclosed**: 2023-04-11T01:49:37.950Z

## Reporter
- **Username**: nhx1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
## Summary:

I hope you're having a good day. Before starting to describe this vulnerability, I would like to thank the HackerOne triage team for doing the difficult job of triaging all these issues. 

I observed an IDOR vulnerability in one of the endpoints in the Talentmap API. This vulnerability is similar to #1809328. In this report I will demonstrate ways to enumerate all user accounts in the Talentmap API logged in as a guest user. To triage this vulnerability, you need to manually build it in your system, the build instructions can be accessed in the report #1809328 where HackerOne team has successfully built the Talentmap API. However, if you're having issues building it, drop a message!

After building the API, please go inside the docker container and run the following commands to create_seeded_users.

1. `$ python manage.py create_demo_environment` 
2.  `$ python manage.py create_seeded_users`

Also, go into the docker container and create some test users:
1. `$ python manage.py create_user normalUser normaluser@gmail.com normalUser123 Normal User`
2.  `$ python manage.py create_user normalUser1 normaluser1@gmail.com normalUser123 Normal User`
3. `$ python manage.py create_user normalUser2 normaluser2@gmail.com normalUser123 Normal User`

** Some details: **
i. The vulnerable endpoint = http://localhost:8000/api/v1/permission/user/{USER_ID}/  

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. After running the API, browse `http://localhost:8000` and login using the credentials `username: guest , password: guestpassword ` , and copy the token obtained in the respones

{F2139636}

{F2139638}

  2. Send the following request to http://localhost:8000. Replace {USER_ID} to the user id of the user you want to enumerate information of. Replace {token} to the token you obtained in step 1

```
GET /api/v1/permission/user/{USER_ID}/ HTTP/1.1

Host: localhost:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost:8000/
JWT: {token}
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
```

  3. Observe user information returned in the response

Additionally, you could also use Burp intruder to cycle through user-ids from 1 to 100 to get information of all users in the database.

{F2139641}

##Remediation Guidance

Implement access control mechanism. Allow the user to only fetch their information.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

A malicious actor could fetch information of all users and cause a data breach

## Attachments
- image.png
- image.png
- image.png
