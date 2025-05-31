# Reflected XSS in the shared note view on https://evernote.com

## Report Details
- **Report ID**: 1518343
- **URL**: https://hackerone.com/reports/1518343
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-22T03:38:49.646Z
- **Disclosed**: 2022-04-20T19:37:48.052Z

## Reporter
- **Username**: sarka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: evernote

## Vulnerability Information
## Summary:

There is a reflected XSS vulnerability on https://evernote.com, in the shared web note view, triggered through the ```view``` and ```ionUrl``` parameters of the ***/shard/s[SHARD_NUMBER]/client/snv*** endpoint.

## Description:


When a user creates a note and shares it, it is stored in the following endpoint, being accessible by its ```GUID``` and generated ```KEY```: ***https://www.evernote.com/shard/s[SHARD_NUMBER]/sh/[NOTE_GUID]/[NOTE_KEY]***.

The above link redirects to another generated link this is going to be used to access the ressource in the web note viewer, and has the following format:
***https://www.evernote.com/shard/s[SHARD_NUMBER]/client/snv?noteGuid=[NOTE_GUID]&noteKey=[NOTE_KEY]&sn=[PREVIOUS_LINK]&title=[NOTE_TITLE]***

When accessing from this web note viewer link, a script named ***main.68d4af6d45d9dcaab6e6.js*** is fetched from ***https://dashboard.svc.www.evernote.com/app/nv/***, used to format and display the note properly.

After analyzing this file, we can observe at line 3353 of this script (beautify the script first) a function named ```renderWithContext()``` that handles different ways of rendering the note:

```javascript
renderWithContext() {
    switch (this.view) {
		case "content-unavailable":
			return this.renderContentUnavailable({
				header: this.state.i18n.t("SharedNote.contentUnavailable.info"),
				body: this.state.i18n.t("SharedNote.contentUnavailable.downloadInfo")
			});
		case "saved":
			return this.renderContentUnavailable({
				header: this.state.i18n.t("SharedNote.contentUnavailable.savedOnMobile.info"),
				body: this.state.i18n.t("SharedNote.contentUnavailable.savedOnMobile.downloadInfo")
			});
		case "notelink":
			return this.renderNoteLinkView();
		case "after-save-note":
			return this.renderAfterSaveNoteView()
	}
	const { embedMode: e } = this.state;
	return e ? this.renderContent() : o.createElement("div", {
		className: Gn.appContainer
	}, this.renderHeader(), this.renderContent())
}
```

Since the ```this``` object represent the current URL parameters, the switch statement ```switch (this.view)``` gives away that we can reach this function by adding a ```view``` parameter in the URL. 

The vulnerable case here is ```after-save-note```. Here is what the ```renderAfterSaveNoteView()``` function looks like:

```javascript
renderAfterSaveNoteView() {
	if (W())
		if (R.isMobile) {
			const e = oe(R.isMobile);
			e && (window.location.href = e)
		} else {
			const e = function () {
				const e = W();
				let n = e && e.ionUrl;
				return n && -1 === n.indexOf(J.baseUrl) ? null : n
			}();
			e && (window.location.href = e)
		}
	return null
}
```

We can observe line 12 that this script sets the ```window.location.href ``` attribute to the variable ```e```.  As line 9 shows, we also control this variable ```e``` as it represents an additional parameter we have to add in the URL: ```ionUrl```.

However, we can see at line 10 a security measure that will try to prevent attacker from setting the ```window.location.href``` attribute to anything outside evernote.com: ```J.baseUrl``` contains the value "https://www.evernote.com/". This line basically checks if the substring "https://www.evernote.com/" is present in the provided ```ionUrl``` URL parameter.

That's where the vulnerability resides; it only checks if the substring "https://www.evernote.com/" is in the provided ```ionUrl``` URL parameter, but not that it starts by it.

**I was then able to execute javascript by passing the following payload to ```ionUrl``` : ```javascript:alert(document.cookie)//https://www.evernote.com/```, using javascript comments to comment-out the evernote link (and setting ```view``` to ```after-save-note``` in order to reach this function).**

Here is the POC that will display current cookies in an alert box:
https://www.evernote.com/shard/s1/client/snv?view=after-save-note&ionUrl=javascript:alert(document.cookie)//https://www.evernote.com/

***The link to the note doesn't have to valid, only the view and ionUrl parameters matter. An attacker could also have a valid note link that is properly displayed, and still execute the javascript silently. He can also force the user to sign-in beforehand to make sure to get his cookies.***

This has been tested  and working on up-to-date Firefox and up-to-date Chrome.
This exploit works on the latest version of Evernote.

## Steps To Reproduce:

  1. Click on the following link: https://www.evernote.com/shard/s1/client/snv?view=after-save-note&ionUrl=javascript:alert(document.cookie)//https://www.evernote.com/

## Supporting Material/References:

  {F1663424}   {F1663430}

## Impact

An attacker can execute script in a victim's browser, making him able to take over accounts of victims, make victims perform action without their consent, steal their private data, install malware, and so on.

## Attachments
- POC_Firefox.png
- POC_Chrome.png
