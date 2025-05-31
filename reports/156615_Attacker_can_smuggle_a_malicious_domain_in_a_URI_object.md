# Attacker can smuggle a malicious domain in a URI object.

## Report Details
- **Report ID**: 156615
- **URL**: https://hackerone.com/reports/156615
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-05T01:03:25.537Z
- **Disclosed**: 2022-12-13T20:39:21.428Z

## Reporter
- **Username**: djspinmonkey
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Simple example:
```
user_provided_redirect_uri = "http:////malware.com/real/path"
evil_uri = URI.parse(user_provided_redirect_uri)
evil_uri.host          # => nil
evil_uri.to_s          # => "http://malware.com/real/path"
```

In many common URI-validation scenarios, the target system will likely parse a user provided URI, and then check the host against some internal validation criteria, eg, that it's a host owned by that system. Seeing a blank hostname will often cause the system to assume that the link only contains a path, not a domain,  so any validation or checking of that domain won't happen.

However, if the URI object is turned back into a string, the resulting URI contains the malicious domain, as you can see above. The actual behavior is to remove two of the leading slashes, so starting with 4 leading slashes will give you 2 leading slashes in the output, which is a well-formed (and in this case malicious) URL.

In addition, most browsers (all that I checked on) will allow multiple slashes before the domain name -- type "http:////google.com" in to your browser, and you will go to google. So, using the original string will also result in a redirection to the malicious host.

Bottom line, this bug is almost certainly the cause of a large number of open redirect vulnerabilities in Ruby based web apps. The most obvious use would be to craft malicious URIs for phishing purposes, but it could be used to potentially circumvent any host-checking logic in a URI validator.

The cause of the bug can be seen here: https://github.com/ruby/ruby/blob/trunk/lib/uri/rfc3986_parser.rb#L6 (if you can spot it in there). The real smoking gun is comment on the line above it that says the regex is modified from the RFC to allow empty host names. A little consideration will show why this causes the above behavior, and why it ends up stripping the initial two leading slashes.

## Attachments
No attachments
