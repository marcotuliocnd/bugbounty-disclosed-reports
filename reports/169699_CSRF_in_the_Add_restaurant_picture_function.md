# CSRF in the "Add restaurant picture" function

## Report Details
- **Report ID**: 169699
- **URL**: https://hackerone.com/reports/169699
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-16T00:08:43.021Z
- **Disclosed**: 2017-09-14T22:57:21.979Z

## Reporter
- **Username**: 0xamir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
##Overview  
I found a CSRF vulnerability within the process responsible for adding photos for a restaurant which can lead to tricking victims into adding arbitrary photos to their restaurant's page.  
##Details  
The CSRF vulnerability exists due to a misconfiguration on your part in which your `X-CSRF-TOKEN` header is set to "Undefined" which leads to any request being accepted and processed.  
Uploading a picture to your restaurant is a two step process, when you start the process you first have to upload a picture off your device to the server, after that you'll be presented with another form which will allow you to add any captions or descriptions you want to the photo. The misconfiguration in question resides in the first request (The photo upload request) which allows attackers to forge a picture upload request to the server, however the photo will not be added to the restaurant's page unless the second request from the second form (the captions and description form)  is also submitted.  
It's also worth noting that there're no CSRF protections in place on the second form.  
##PoC  
To carry out a successful attack the attacker needs to obtain two values which will tie the requests to the victim's account. these values are namely `res_id` and `user_id`. After obtaining these two values (Which are publicly available for any user and restaurant) all the attacker will have to do is to fill these values in the GET parameters in the first request with the values of the victim and the `res_id` parameter in the body of the second POST request. I'll provide a PoC HTML file below in order to make it easier for you to reproduce the flaw, the PoC couldn't be included here due to the huge size of it (because the first request has the binary form of the photo being uploaded in the code itself.)  
After modifying the values in the two requests, click the button that says "Request 1" to submit the first request and then "Request 2" the submit the second. By this point you can now visit the photos page in your restaurant's page and you'll find a picture of a star added there.  
##PoC Code:  
[You can download the exploit code from Mega.nz here](https://mega.nz/#!0wpkhLJL!Xkjm37fvqhcl7Ybp8yPBugnaRz0ruLU0eWS26icsz7s), The file is protected so there's no need to worry about accidental disclosure.  

## Attachments
No attachments
