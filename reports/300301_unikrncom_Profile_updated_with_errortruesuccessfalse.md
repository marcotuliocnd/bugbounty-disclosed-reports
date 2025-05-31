# [unikrn.com] Profile updated with error":true,"success":false"

## Report Details
- **Report ID**: 300301
- **URL**: https://hackerone.com/reports/300301
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-24T07:25:43.434Z
- **Disclosed**: 2019-06-12T16:27:00.075Z

## Reporter
- **Username**: rbcafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Greetings,

We noticed that even if the https://unikrn.com/apiv2/user/updateprofile gave an answer that the code is on error , the post is proceeded :

PoC :
--

    curl 'https://unikrn.com/apiv2/user/updateprofile' -XPOST -H 'Referer: https://unikrn.com/profile' -H 'Content-Type: application/json' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7' -H 'Origin: https://unikrn.com' -H 'DNT: 1' -H 'Accept: application/json, text/plain, */*' -H 'Application-Version: v3.9.1-1743-g043d784' --data-binary '{"firstname":"RBCA","lastname":"RBCA","nickname":"Rbcafe","street":"","suburb":"","state":"","shipcountry":null,"postcode":"","telephone":null,"phone_cc":"fr","email":"bounty-1@rbcafe.com","city":"","avatar":"https://www.gravatar.com/avatar/0f2219216ab1e07d370b387d028a6535","session_id":"bb6ig4dqkest1cbp3t11g4mpppjka56m"}'

Result :
--

    {"ver":"2.0","error":true,"success":false,"msg":"file_wrong","msg_trans":"file_wrong","data":[],"code":0,"flds":null,"flds_errors":null}

Video :
--

{F249242}

Impact :
--

Bypass the answer of the post and update a profile.

Fix :
--

If the answer is success false, the POST should not be proceeded.

Best regards.

Rbcafe

## Impact

- Bypass the answer of the post and update a profile.
- Lack of control.

## Attachments
- unikrn.mov
