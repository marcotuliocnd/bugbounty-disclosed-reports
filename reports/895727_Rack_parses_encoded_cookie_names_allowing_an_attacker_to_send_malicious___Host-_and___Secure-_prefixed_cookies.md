# Rack parses encoded cookie names allowing an attacker to send malicious `__Host-` and `__Secure-` prefixed cookies

## Report Details
- **Report ID**: 895727
- **URL**: https://hackerone.com/reports/895727
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-10T23:58:33.703Z
- **Disclosed**: 2020-06-16T13:27:52.001Z

## Reporter
- **Username**: fletchto99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
The [rack cookie parser](https://github.com/rack/rack/blob/c9ff9709afa70ca0e427aa06643c851f498359dc/lib/rack/utils.rb#L215) parses the cookie string using [`unescape`](https://github.com/rack/rack/blob/c9ff9709afa70ca0e427aa06643c851f498359dc/lib/rack/utils.rb#L215). This allows a malicious attacker to set a second cookie with the name being percent encoded. Typically it would be expected that we cannot trust cookies and in _most_ cases that's true. However in a couple of cases certain expectations are set. Cookies allow for [cookie prefixes](https://textslashplain.com/2015/10/09/duct-tape-and-baling-wirecookie-prefixes/) on the cookie name to indicate to the browser certain attributes. In this case there are 2 special attributes we care about: `__Secure-` and `__Host-`. When the browser sends these cookies to the server certain [assumptions](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Attributes) are be made around these cookies:

1. `__Secure-` prefix: Cookies names starting with `__Secure-` (dash is part of the prefix) must be set with the secure flag from a secure page (HTTPS).
2. `__Host-` prefix: Cookies with names starting with `__Host-` must be set with the secure flag, must be from a secure page (HTTPS), must not have a domain specified (and therefore aren't sent to subdomains) and the path must be `/`

The flaw in Rack allows for a `__%48ost-` or `__%53ecure-` cookie to be set **without** the required attributes (I.e. set without HTTPS, from root domain, or from a secure page). This means a malicious cookie set by an attacker could set a `__%48ost-` cookie from a subdomain knowing that Rack would parse it as `__Host-`. Furthermore, since the browser won't enforce the `HostOnly` attribute to `__%48ost-` cookies an attacker could control the `__Host-` prefixed cookie from a subdomain by setting a wildcard domain on the `__%48ost-` cookie.

It should be noted that while the [cookie spec](https://tools.ietf.org/html/rfc6265#section-4.1.1) recommends encoding for the value of a cookie it doesn't make any suggestions around the encoding of the name of a cookie.

Here's a simple PoC test case which fails :

```ruby
# frozen_string_literal: true

require_relative 'helper'

describe Rack::Utils, "malicious cookie" do
  # Fails and __Host-evil reads the malicious value and sets it as the cookie
  # rather than reading the actual __Host cookie
  #
  # Furthermore, browsers enforce HostOnly for `__Host-` cookies but they would
  # not enforce it for "__%48ost" cookies so a malicious script could potentially
  # set this cookie knowing it would be parsed as the `__Host-` cookie
  #
  # Lastly, when the cookie is made it could be set with the `.example.com` domain
  # wildcard, thus a malicious script on a subdomain could set the cookie and it
  # would be parsed by the root domain
  #
  # This is due to the cookie being unescaped, thus:
  # URI.unescape("__%48ost-evil") => "__Host-evil"
  #
  # Currently fails, should be passing
  it "doesnt parse malicious __Host cookie" do
    env = Rack::MockRequest.env_for("", "HTTP_COOKIE" => "__%48ost-evil=evil;__Host-evil=abc")
    cookies = Rack::Utils.parse_cookies(env)
    cookies.must_equal({ "__%48ost-evil" => "evil", "__Host-evil" => "abc"  })
  end

  # Less of a security issue and more of a bug
  it "generic foo=bar example" do
    env = Rack::MockRequest.env_for("", "HTTP_COOKIE" => "%66oo=baz;foo=bar")
    cookies = Rack::Utils.parse_cookies(env)
    cookies.must_equal({ "%66oo" => "baz", "foo" => "bar" })
  end
end
```

An attacker could potentially set the cookie from a malicious script on a subdomain like so, bypassing any expectations around the attributes of the cookie:
```
document.cookie = "__%48ost-evil=evil; domain=.example.com";
```

I should note I work for GitHub, I'm not sure if there's any conflict with payouts in this case (and I certainly don't want/need a payout), however should you chose to payout for this I'd like the money to be donated to charity. If possible could it please be donated to [NAACP Legal Defense and Education Fund](https://www.naacpldf.org/support/fiscal-responsibility/) their donaiton page can be found [here](https://org2.salsalabs.com/o/6857/p/salsa/donation/common/public/?donate_page_KEY=15780&_ga=2.63873391.1784282200.1591830687-771342060.1591210817).

## Impact

An attacker can control cookies by encoding creating a second cookie with the name url encoded. This means that the `__Host-` and `__Secure-` prefixed cookies can be controlled. Furthermore, a malicious attacker could set this cookie from a subdomain and have it apply to the root domain, in which case the Rack would parse the attackers cookie.

## Attachments
No attachments
