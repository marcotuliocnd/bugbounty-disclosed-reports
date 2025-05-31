# Access Projects And create projects in gitlab pre production server

## Report Details
- **Report ID**: 540711
- **URL**: https://hackerone.com/reports/540711
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-17T05:06:45.523Z
- **Disclosed**: 2019-08-28T17:49:17.235Z

## Reporter
- **Username**: rockrzhackr9z
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Steps to reproduce

Go to https://pre.gitlab.com

Here any one can register and can view the pre production projects of gitlab developers.


I have registered in https://pre.gitlab.com/users/sign_in

and have created one test group and test project 

go to https://pre.gitlab.com/explore/groups

i have created one test group 

{F470509}

And i have created one test project

{F470510}

I went to look for gitlab project members https://pre.gitlab.com/qa-perf-testing/gitlabhq/project_members


I have seen it was created by your gitlab employee Ramya Authappan 

https://pre.gitlab.com/rauthappan


The attacker not only access the internal projects of gitlab but he can also create groups and projects in pre production server of gitlab.

## Impact

Attacker will access the pre production server of gitlab and he access the groups and projects created by gitlab employees.

Attacker will also create the projects and groups in pre production server of gitlab.

## Attachments
- pre_gitlab_groups.png
- pre_gitlab_projects.png
