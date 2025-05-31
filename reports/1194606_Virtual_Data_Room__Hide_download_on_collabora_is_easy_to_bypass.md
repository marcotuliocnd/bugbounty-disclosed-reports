# Virtual Data Room / Hide download on collabora is easy to bypass

## Report Details
- **Report ID**: 1194606
- **URL**: https://hackerone.com/reports/1194606
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-12T18:27:06.135Z
- **Disclosed**: 2021-08-07T14:28:34.326Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So, let me start with saying I'm not sure if this is a security issue or if it is by design. The reason I'm reporting it here is since Nextcloud promotes this Virtual Data Room a lot.

https://nextcloud.com/blog/nextcloud-announces-virtual-data-room-solution-for-ultimate-protection-of-data-during-sensitive-dealmaking/
https://nextcloud.com/virtual-data-room/

And let me just quote: "configure Secure View ensure the users can still read and (when shared with editing rights) modify documents, while the documents are watermarked when on screen."

"With secure view, our online office solutions can be configured to open PDF files, images and text files, making these files available in a watermark-protected way, while downloads and other apps are disabled using File Access Control. This setup is useful when data has to be protected from leaking but still has to be made available for review, as in a virtual data room scenario."

Both of these claims are false. 

Minimal proof of concept.

1. Setup Nextcloud with Collabora
2. Setup sercure view & file access control to disallow the download of the files
3. Share a document, lets say `vdr.odt` by public link and mark as hide download
4. Copy the link

Now the point here is that anybody you send the link will only see the watermarked file. Not being able to download or copy data. And of course making a picture of these things is useless as it shows the watermark.

5. attacker opens their network tab in the developer tools
6. attacker opens the link
7. attacker filters on WOPISRC
8. Attacker finds a link like

```
wss://collabora.server/https%3A%2F%2Fserver%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F1234_abcd%3Faccess_token%3efgh%26access_token_ttl%3D0/ws?WOPISrc=https%3A%2F%2Fserver%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F1234_abcd&compat=/ws
```

As far as I understand the WOPI spec this is us sending the collabora server the WOPI endpoint they have to call. Which in this case is

`https://server/index.php/apps/richdocument/wopi/files/1234_abcd`
The `1234_abcd` seems to be the `fileid` and the `instance id`

And the access token is also there in the url. In this case `efgh`.

Now if an attacker just does the following curl command

```
curl https://server/index.php/apps/richdocument/wopi/files/1234_abcd?access_token=efgh -o stolen.odt
```

You will see that they have the unwatermarked version of the data. This is even easier than copying everything over or making photographs.

## Impact

Your Virtual Data Room is inherently broken. And the claims you make on your website are at best misleading.
However as said I'm not sure if this may be intentional as the feature is called hide download in the UI.

In any case. Maybe a good idea would be to have a secret configured on both collabora and the Nextcloud host. Which gets send. So that in case of hide download a client that doesn't know the secret token can't download the file.

I do not have access to a setup with Only Office. But I believe that to be vulnerable to a similar attack.

## Attachments
No attachments
