# Nextcloud 10.0 privilege escalation issue - Normal user can mask external storage shared by admin    

## Report Details
- **Report ID**: 165229
- **URL**: https://hackerone.com/reports/165229
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-09-02T09:43:42.725Z
- **Disclosed**: 2020-03-01T15:01:32.178Z

## Reporter
- **Username**: egrep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information

Normal user(Non-privileged) can mask external storage shared by admin.
 
 
Scenario :
Created three users "admin", "attacker", "victim"
Created group "samplegroup" containing all the three users with "victim" as group admin
 
 
Steps:
1) User "admin" created external storage named "localstrg"(note: name is the attack vector) with properties:
 
Folder Name : localstrg
External Storage : Local
Authentication : None
Configuration : /
Available for : "samplegroup","admin" - groups
Settings : Enable sharing
 
2) On seeing this , user "attacker" created one more external storage with the same name "localstrg" with properties:
 
Folder Name : localstrg
External Storage : SFTP
Authentication : Username and Password
Configuration : Fill "Host", "Root" ," Username" ,"Password"
Settings : Enable sharing
 
3) After that, user "attacker" shared created external storage with group "samplegroup" which is having other two users
 
4) If suppose, user "victim" visits the external storage "localstrg" in his profile, he is only shown with files shared by user "attacker"
 
Prerequisite : Both attacker and victim should be in the same group
 
Using this vulnerability, non-privilged user can mask the external storage shared by admin to other users
 
 

## Attachments
No attachments
