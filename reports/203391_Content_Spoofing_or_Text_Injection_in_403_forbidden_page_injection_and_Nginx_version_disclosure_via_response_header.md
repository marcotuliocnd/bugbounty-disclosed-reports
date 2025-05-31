# Content Spoofing or Text Injection in (403 forbidden page injection) and Nginx version disclosure via response header

## Report Details
- **Report ID**: 203391
- **URL**: https://hackerone.com/reports/203391
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-04T12:10:11.032Z
- **Disclosed**: 2017-04-03T12:41:15.519Z

## Reporter
- **Username**: demo--hacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
### Hello there, 
I know that this is Non-critical issue  but i want you guys to be aware of it.


###1.) I have found a Content Spoofing or Text Injection in This url [http://dl-origin.ubnt.com/](http://dl-origin.ubnt.com/)

Go to this url [http://dl-origin.ubnt.com/has%20been%20changed%20by%20a%20new%20one%20https://www.ATTACKER.com%20so%20go%20to%20the%20new%20one%20since%20this%20one](http://dl-origin.ubnt.com/has%20been%20changed%20by%20a%20new%20one%20https://www.ATTACKER.com%20so%20go%20to%20the%20new%20one%20since%20this%20one)

See the text injection in the attached picture {F157352} 

See text injection similar reports here #134388

###2.) I have noticed in the response header of [https://www.ubnt.com/](https://www.ubnt.com/) shows Ngnix server version!

As you can see in the attached picture {F157353}



### Impact
An attacker can be used this for further analyzation of the target application.

###-It is a good practice not to disclose your Ngnix server version.

See server version disclosure similar reports here #179217 #183245 #141125

Thanks for taking the time to read my reports.


Regards,
###Rey Mark


## Attachments
- text_injection.png
- ubnt_Ngnix_Server_version_disclosure.png
