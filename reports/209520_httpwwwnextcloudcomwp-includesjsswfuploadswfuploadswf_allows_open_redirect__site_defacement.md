# http://www.nextcloud.com/wp-includes/js/swfupload/swfupload.swf allows open redirect / site defacement

## Report Details
- **Report ID**: 209520
- **URL**: https://hackerone.com/reports/209520
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-28T07:12:50.139Z
- **Disclosed**: 2020-03-07T21:55:51.808Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information

Good day, I truly hope it treats you well on your side of the screen :)

I have found that your website uses the flash file: swfupload.swf to allow your users to upload files.

The tl;dr version of this bug report is it allows an open redirect to any site a non kind person may want to exploit or website defacement with the option to put any image on your site to share with others.  If not greatly in scope I understand, just wanted to help you be more secure :)

The link in question is:

http://www.nextcloud.com/wp-includes/js/swfupload/swfupload.swf?debugEn%xabled=true&buttonImag%xeURL=https://████████/PugOfConcept/pugOfConcept.swf

Friendly url shorted version:

https://tinyurl.com/zduxnhz

I've already created a fancy animated gif of the exploit in action so you can click, watch, and hopefully see a cute POC surprise on video end.

https://www.dropbox.com/s/0343g6qgjdz1y1r/nextcloud.com_swf_upload_open_redirect_2_27_2017.gif?dl=0

Defacement Link

http://www.nextcloud.com/wp-includes/js/swfupload/swfupload.swf?debug%%Enabled=true&buttonTe%%xt=&buttonImag%%eURL=http://██████████/PugOfConcept/nopuppies.jpg


Full report details:

a) Why Open Redirects can be harmful for your users and your company:
   https://www.owasp.org/index.php/Top_10_2010-A10-Unvalidated_Redirects_and_Forwards

b) The source of the most recent version of swfupload.swf is here:
   https://github.com/WordPress/secure-swfupload

The bad news is the newest version is vulnerable to the exploit (I will be reporting it to wordpress to fix hopefully)

They strongly suggest updating to a newer move secure version:
http://www.plupload.com/


c) How the exploit works:

When you visit a swf, query string parameters (what appears after the ?) can be passed along in the request:

http://myawesomewebsite.com/wp-includes/js/swfupload/swfupload.swf?   <debugEn%xabled=true?&buttonImag%xeURL=https://█████/PugOfConcept/pugOfConcept.swf>
	
Flash reads in these variables via a special variable: root.loaderInfo.parameters

The intended solution is that they tried to filter out if query string parameters were passed along in the request by checking for them and if the were passed to delete them.
   
	for(key in params)
	{
			if(query.hasOwnProperty(Utils.trim(key)))
		{
			delete params[key];
		}
	}


The trick is that Flash will filter and non valid url encoded variables from a string, so %00-%FF are valid ascii encoded strings, a = %61 b = %62 etc
I tricked the system with the variable passed "?debugEnabled=true" normally would be filtered, but with debugEn%xabled=true, the %x is a non valid hex string :)  Since Hex counts from 0-F There is no valid %x.

May you be well on your side of the screen :)

-Eric

Also vulnerable:



## Attachments
No attachments
