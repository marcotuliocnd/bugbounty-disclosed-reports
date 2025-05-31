# Frameset(Frame) html tag is allowed in html editor.(can lead to clickjacking)

## Report Details
- **Report ID**: 285609
- **URL**: https://hackerone.com/reports/285609
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-02T11:36:15.558Z
- **Disclosed**: 2018-02-14T16:36:31.535Z

## Reporter
- **Username**: na5ne3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hello Sir/Mam ,
I was using the html editor in computer programming section , which allowed me to design a webpage. When i use the iframe tag , object tag and embed tag it show me the message that these tags are not allowed for security reasons(may be cause of clickjacking attack or something) but when i used frameset n frame tag it does not showed any message and allows them. 
The  X-frame option is set to same-origin. So, it allowed to load the user setting page in a frameset tag , (i also recorded the video too)which can lead to clickjacking attack. If there is restriction on iframe , object n embed tag then there should also be restriction on frameset(frame). 
P.S:The poc video is also attached below.

## Attachments
No attachments
