# Senseitive data Related to Shopify Host -> https://shopify.zendesk.com/

## Report Details
- **Report ID**: 1298809
- **URL**: https://hackerone.com/reports/1298809
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-08-11T02:05:14.977Z
- **Disclosed**: 2021-11-08T15:12:32.366Z

## Reporter
- **Username**: sam_exploit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
###Description :
Github is truly awesome service but its unwise to put sensitive data in public repo as i was found a repo committed ***1 houre ago*** contain ***Senseitive data (Credentials && ZRT_API_KEY && JWT_SECRET*** related to ***this Host -> https://shopify.zendesk.com/*** leaked publicly in github, and clearly this is not intended to be public.


###Explanation :

While searching in github repos for sub-domains realted to ***Zendesk***, I found this a ***Shopify*** Sub domains -> ***https://shopify.zendesk.com/***


https://github.com/█████/extension/manifest.json
```
        {
            "matches": ["https://shopify.zendesk.com/agent/tickets/*"],
            "js": ["contentScript/contentScript.js"]
        }

    "options_page": "popup/options/options.html",
    "host_permissions": [
        "http://localhost:4000/*",
        "http://127.0.0.1/*"
```

https://github.com/█████████/extension/background.js
```
    // chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
    //     const tab = tabs[0];
    //     const url = new URL(tab.url);
    //     const domain = url.hostname;
    //     if (domain === 'shopify.zendesk.com') {
    //         chrome.action.enable();
    //     } else {
    //         chrome.action.disable();
    //     }
    // });

    /*
    const checkDomain = () => {
        chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
            const activeTab = tabs[0];
            const url = new URL(activeTab.url);
            const domain = url.hostname;
            if (domain === 'shopify.zendesk.com') {
                chrome.action.enable();
            } else {
                chrome.action.disable();
            }


async function fetchPostCall(type, path, bodyData, callback) {
    const url = `http://localhost:4000/${path}`
 
    fetch(url, {
        method: type,
        body: JSON.stringify(bodyData),
        headers: {    
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8'
        }
        }).then(resp => resp.json())
        .then(data => {
            chrome.cookies.set({
                url: 'http://localhost:4000/extension/login',
                name: 'token',
                value: data.token,
                httpOnly: true
              });
            callback(data)
        })
```

https://github.com/█████/extension/popup/public/js/controls.js
```
    if (domain === 'shopify.zendesk.com') {
      chrome.storage.local.set({
        ticketInitiated: true,
        isRunning: true,
        isNotified: false
      });

    const url = `http://localhost:4000/ticket`;

    fetch(url, {
      method: 'POST',
      body: JSON.stringify(bodyData),
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
```


as you see in the Repo above the user mentined for ***localhost site and Token*** for connection, ***But digging more in the user repo i found a Senseitive data (Credentials && ZRT_API_KEY && JWT_SECRET***


https://github.com/██████████
```
PORT=4000
NODE_ENV=DEVELOPMENT

DB_LOCAL_URI=mongodb://127.0.0.1:27017/TicketTracker

SENDGRID_API_KEY=███████
SENDGRID_FROM_EMAIL=████████
WELCOME_USER_TEMPLATE=███████
RESET_PASSWORD_TEMPLATE=█████

BCRYPT_SALT=10
CRYPTO_SECRET=███

JWT_SECRET=████
JWT_EXPIRE_TIME=30d
COOKIE_SECRET=██████
COOKIE_EXPIRE_TIME=30
ZRT_API_KEY=█████████
```

## Impact

Such information is intended to private not public, it's highly recommended to check and revoke this repo after your assessment.

## Attachments
No attachments
