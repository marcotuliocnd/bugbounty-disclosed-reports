# Information / sensitive data disclosure on some endpoints

## Report Details
- **Report ID**: 273726
- **URL**: https://hackerone.com/reports/273726
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-02T09:31:58.011Z
- **Disclosed**: 2018-08-22T14:39:06.155Z

## Reporter
- **Username**: europa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello team!
While doing a preliminary recon on *.wordpress.org I've come across a few sensitive files that should not be facing the public web; I'll leave you a list organized by criticality and some proof.


### High priority
[.travis.yml](https://codex.wordpress.org/.travis.yml) configuration file with credentials
```
php maintenance/install.php testwiki admin
--pass travis
--dbname traviswiki
--dbuser travis
--dbpass ""
--scriptpath "/w"
```


### Medium priority
[.htaccess](https://munin-lax.wordpress.org/.htaccess) file for **munin-lax.wordpress.org**
```
AuthUserFile /usr/local/etc/munin-htpasswd
AuthName "Munin"
AuthType Basic
require valid-user
```

### Low priority
one `.bash_history` file accessible from multiple production vhosts:
```
http://iphone.git.wordpress.org/.bash_history
http://meta.git.wordpress.org/.bash_history
http://wordpress.git.wordpress.org/.bash_history
http://bbpress.git.wordpress.org/.bash_history
http://buddypress.git.wordpress.org/.bash_history
http://core.git.wordpress.org/.bash_history
http://android.git.wordpress.org/.bash_history
http://ios.git.wordpress.org/.bash_history
http://wordcamp.git.wordpress.org/.bash_history
http://develop.git.wordpress.org/.bash_history
http://evelop.git.wordpress.org/.bash_history
```

one ssh `known_hosts` file accessible from multiple production vhosts:
```
http://wordcamp.git.wordpress.org/.ssh/known_hosts
http://ios.git.wordpress.org/.ssh/known_hosts
http://android.git.wordpress.org/.ssh/known_hosts
http://core.git.wordpress.org/.ssh/known_hosts
http://buddypress.git.wordpress.org/.ssh/known_hosts
http://bbpress.git.wordpress.org/.ssh/known_hosts
http://wordpress.git.wordpress.org/.ssh/known_hosts
http://meta.git.wordpress.org/.ssh/known_hosts
http://iphone.git.wordpress.org/.ssh/known_hosts
http://develop.git.wordpress.org/.ssh/known_hosts
http://evelop.git.wordpress.org/.ssh/known_hosts
```


### Impact
Obviously there's no critical priority here—there could've been juicer stuff in the `.bash_history` but there wasn't; the publicly accessible `.htaccess` and `.travis.yml` might be serious as long as those credentials are really being used somewhere (and it seems to me the DBMS isn't facing the public internet anyway). The real impact is that finding such files always grabs the attention of a threat actor, which might give up not so easily influenced by the fact that there might be "more".


### (minor) bonus round: host header injection on wordpress.org
Probably *informational* but you might still want to look into that: **wordpress.org** is susceptible to "host header injection", you can read more about it [here](http://carlos.bueno.org/2008/06/host-header-injection.html) and [here](http://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html). Essentially, depending on your internal configuration, this flaw ranges from a self-inflicted open-redirect (wow, such threat), to password reset request hijack, to cache poisoning.

**PoC for the self-inflicted open-redirect (why though)**:

```
❯ curl -v -H "Host: z.xss.ro" "https://wordpress.org/themes/search"
> GET /themes/search HTTP/2
> Host: z.xss.ro
> User-Agent: curl/7.55.1
> Accept: */*
> 
< HTTP/2 301 
< server: nginx
< date: Mon, 02 Oct 2017 09:12:59 GMT
< content-type: text/html
< content-length: 178
< location: https://z.xss.ro/themes/search/
< x-frame-options: SAMEORIGIN
< x-nc: MISS lax 250
< 
<html>
<head><title>301 Moved Permanently</title></head>
```
this is also going down on plain HTTP so maybe a MitM scenario is possible in an already compromised business environment / hosting partner but then again, it's pretty low priority.

I obviously can't test the password reset scenario, you might want to test that as follows:

1. go to wordpress.org and begin the procedure to reset your password
2. intercept the request on Burp
3. change the host header to evil.com
4. send the request and check your e-mail

if the threat is real, the password reset link will be generated with evil.com instead of wordpress.org; otherwise it's all good (which should be, as this doesn't work on wordpress.com)

## Attachments
No attachments
