# Invalid URL parsing '#'

## Report Details
- **Report ID**: 341634
- **URL**: https://hackerone.com/reports/341634
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-04-21T19:23:14.376Z
- **Disclosed**: 2018-05-01T14:47:21.018Z

## Reporter
- **Username**: mrtc0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
`URI` is not correctly parsed when "#" is included in the URL.
Therefore, could instead be tricked into connecting to a different host. 

### PoC

```bash
$ ruby --version
ruby 2.4.1p111 (2017-03-22 revision 58053) [x86_64-darwin16]
```

```ruby
require 'uri'
uri = URI("http://www.example.com#@test.evil.com/test")
# => #<URI::HTTP http://www.example.com.evil.com/test>
p uri.hostname
# => "www.example.com.evil.com"
```

But, does not happen if use single quotes,  like this.

```ruby
uri = URI.parse('http://www.example.com#@evil.com/test')
p uri.hostname
# => www.example.com
```

However, in RFC 3986 it is defined that after "#" it is interpreted as a fragment.
Therefore, this behavior is contrary to the user's intuition and easy to overlook.

## Impact

The user may connect to an unintended host.

## Attachments
No attachments
