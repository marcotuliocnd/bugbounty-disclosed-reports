# ShopifyAPI is vulnerable to timing attacks.

## Report Details
- **Report ID**: 224096
- **URL**: https://hackerone.com/reports/224096
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-26T16:31:49.207Z
- **Disclosed**: 2017-06-23T15:36:23.392Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Dear Shopify bug bounty team,

The [Python ShopifyAPI](https://github.com/Shopify/shopify_python_api) library is vulnerable to timing attacks, because the `validate_hmac()` falls back to a non-constant time comparison when `hmac.compare_digest()` is not available. I am perfectly aware that this issue is out of scope, but your Shopify Guru (Jack P.) kindly advised me to report this issue here.

# Summary
---

Timing attacks are a type of side channel attack where one can discover valuable information by recording the time it takes for a cryptographic algorithm to execute.

The issue lies in `shopify/session.py`'s `validate_hmac()` function:

~~~
# Try to use compare_digest() to reduce vulnerability to timing attacks.
# If it's not available, just fall back to regular string comparison.
try:
    return hmac.compare_digest(hmac_calculated, hmac_to_verify)
except AttributeError:
    return hmac_calculated == hmac_to_verify
~~~

The `==` operator does a byte-by-byte comparison of two values and as soon as the two differentiate it terminates. This means the longer it takes until the operation returns, the more correct characters the attacker has guessed. It is important to note that this issue really only affects users using Python versions prior to 2.7.7.

Link to source code: https://github.com/Shopify/shopify_python_api/blob/master/shopify/session.py#L115-L120

# PoC
---

Here is a quick and messy PoC to demonstrate the issue:

~~~python
import time, hmac


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def timing_attack_diff():
    s1 = "100000000000000000000000000000000"
    s2 = "000000000000000000000000000000001"
    for i in range(200):
        if not s1 == s2:
            print i

@timing
def timing_attack_same():
    s1 = "100000000000000000000000000000000"
    s2 = "100000000000000000000000000000000"
    for i in range(200):
        if s1 == s2:
            print i

@timing
def constant_time_diff():
    s1 = b"100000000000000000000000000000000"
    s2 = b"000000000000000010000000000000000"
    for i in range(200):
        if not hmac.compare_digest(s1, s2):
            print i
        
@timing
def constant_time_same():
    s1 = b"100000000000000000000000000000000"
    s2 = b"100000000000000000000000000000000"
    for i in range(200):
        if hmac.compare_digest(s1, s2):
            print i

timing_attack_diff()
timing_attack_same()
constant_time_diff()
constant_time_same()
~~~

The results are quite significant:

| Round   | timing_attack_diff | timing_attack_same | constant_time_diff | constant_time_same |
|---------|---------------------------|---------------------------|---------------------------|---------------------------|
| Round 1 | 2463 ms                   | 2365 ms                   | 2310 ms                   | 2329 ms                   |
| Round 2 | 2219 ms                   | 2175 ms                   | 2156 ms                   | 2188 ms                   |

# How can this be fixed?
---

~~~python
# Try to use compare_digest() to reduce vulnerability to timing attacks.
try:
    return hmac.compare_digest(hmac_calculated, hmac_to_verify)
except AttributeError:
    def fallback_constant_time(hmac_calculated, hmac_to_verify):
    if len(hmac_calculated) != len(hmac_to_verify):
        return False
    
    result = 0
    for x, y in zip(hmac_calculated, hmac_to_verify):
        result |= x ^ y
    return result == 0
~~~

This fallback does not terminate as soon as two bytes are not the same. I am willing to submit a PR to solve this issue, but I need your permission first.

# Just one more little thing
---

The "Verify the request" section over in the [docs](https://help.shopify.com/api/tutorials/building-public-app) is also vulnerable to timing attacks:

~~~ruby
if not (hmac == digest)
    return [403, "Authentication failed. Digest provided was: #{digest}"]
end
~~~

Best regards,
Ed

## Attachments
- shopify_timing_attack_poc.py
