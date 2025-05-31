# Tabnabbing via Window.Opener @Mavenlink

## Report Details
- **Report ID**: 220737
- **URL**: https://hackerone.com/reports/220737
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-13T11:34:41.678Z
- **Disclosed**: 2017-05-09T19:19:11.434Z

## Reporter
- **Username**: chols
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mavenlink

## Vulnerability Information
Details:
When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

POC: 
Edit your website in work sample, with the website URL of http://daniel-tomescu.com/hackerone/landpage.php, which has the following code.

<html>
<script>
window.opener.location.replace('http://daniel-tomescu.com/hackerone/scampage.php');
</script>

My cool page with some funny cat pictures.<br> <br>

<img style="height:400px; width:300px;" src="http://static.tumblr.com/81b6d42b4064def5e9062d5f4410c820/betml74/Yl5ml0lia/tumblr_static_impress.jpg">
</html>

Create a work sample, and add that website, but make sure to publicize your profile, in order for other users to see,  you can then click on the link to the website. This opens in a new tab, and the existing tab is silently redirected to the a website without asking the user. In a real life example, this would redirect to a phishing site to try gain credentials for users.

The javascript code that does all the magic: 
window.opener.location.replace(newURL);

Ways to solve this:

Don't open links in new tabs using the target="_blank"
Add attribute rel="noreferrer" which also disables referrer
Set the window.opener attribute to null on the new tab before redirecting, like this: <script>var w=window.open(url, "target=_blank");w.opener=null;</script>
I hope you see why this is dangerous: this method has huge potential for tricking users that click on external links from this site to be a victim of a scam page because the redirecting is made in the background, while the user is focused on another tab.

More then that, some browsers like Mozilla for Android don't even display the URL, just the page title, so the user has no way of knowing that he was redirected to a scam page.

Note that the target page doesn't have to be in the same-origin policy, so can be an entirely different domain, and the redirect happens silently while user is viewing another page.

Hope that all helps, let me know if you need more information. I can provide screenshots and/or screencasts if necessary.

Wonder if this is eligible for a bounty? :)
Hope you'll triaged this.

Kind Regards,
Jolan Saluria

## Attachments
- 5db38cb3-6727-49c6-ba49-0733fa06b668.png
