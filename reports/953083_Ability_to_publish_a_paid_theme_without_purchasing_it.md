# Ability to publish a paid theme without purchasing it.

## Report Details
- **Report ID**: 953083
- **URL**: https://hackerone.com/reports/953083
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-07T05:20:04.866Z
- **Disclosed**: 2020-08-27T19:42:54.950Z

## Reporter
- **Username**: saltymermaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

##Description
I kept looking for alternatives to my report #927567 and I found another way to publish a paid theme without having to purchase it. This time the trick is to send "*ThemePublishLegacy*"  XHR request while the theme is being installed.

##Requirements
1. Google Chrome suggested because that's what I use to describe my steps

##Steps to reproduce
1. Make sure you have the default theme installed and that it is published
2. Install any free theme
3. Publish the free theme you just installed
4. From your developper tool, copy the `ThemePublishLegacy` XHR request as fetch and paste it in your developper tool console and keep it for later.

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

5. Now, in a new tab, visit https://themes.shopify.com/ and **leave the admin/themes tab open**
6. Choose any paid theme, which should bring you to the selected theme page (e.g. https://themes.shopify.com/themes/mr-parker)
7. Click the "**Try theme**" button to launch the installation
 7.1 **From here, the next steps have to be done as fast as you can, before the theme gets fully installed**
8. Quickly go back  to the **admin/themes** tab you left open at ***step #5*** and refresh the page (your developper tool should still be active for that tab).
 8.1 Once the page is reloaded, you should see in the "*Theme library*" section that the theme is being installed (a spinner animation is shown)
9. Now in your developper tool, open the XHR tab and select the first graphql request that is made to `ThemesProcessingLegacy`
10. Once its selected, open the response preview tab and l look for `data > onlineStore > themes > edges > [0] > node > id`
 11.1 The ID of the theme being installed is the one at the first index
12. Copy the theme ID `gid://shopify/OnlineStoreTheme/[THEME_ID]`
13. Go back to your developper tool console and in the request you saved at ***step #4***, replace the theme ID with the one you just copied at ***step #11*** and send the request (**before the theme installation is complete!**)
14. Once the theme installation is complete, refresh the page and you will see that the paid theme is now publish.

I will be attaching a POC video with this report. You will see in the video that the first time I sent the request, it did not work because of an error (***Role can't be set to main: missing required file layout/theme.liquid***). I believe this attack has to be timed at the right moment for it to work all the time. It seems like for this to work properly, the `ThemePublishLegacy` request should be sent right before the installation is complete, just before the last `ThemesProcessingLegacy` request is made. This could probably be improved and automated with a script.

Also, again, after the theme is published, it seems like we own it. So, at this point, if you publish another theme (the free one), you should see that the the yellow "Theme trial" badge is missing and that you can rename, edit and download the theme files.

## Impact

Ability to install paid theme without purchasing it could lead to content stealing and lost of profit. There is also some unwanted information disclosure since we can edit the theme code and download the files after its published.

If you need extra details, please let me know!

Thank you!

## Attachments
No attachments
