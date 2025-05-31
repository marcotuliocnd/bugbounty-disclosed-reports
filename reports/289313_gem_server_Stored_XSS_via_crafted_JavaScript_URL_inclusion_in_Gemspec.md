# [gem server] Stored XSS via crafted JavaScript URL inclusion in Gemspec

## Report Details
- **Report ID**: 289313
- **URL**: https://hackerone.com/reports/289313
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-10T23:06:18.960Z
- **Disclosed**: 2018-02-22T06:30:28.542Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Hi,

A JavaScript URL injection in the `homepage` field within a Gemspec file can be leveraged to achieve stored XSS on the default `gem server` web interface, referenced [here](http://guides.rubygems.org/run-your-own-gem-server/).

> When you install RubyGems, it adds the gem server command to your system. This is the fastest way to start hosting gems.

As such, a carefully crafted Ruby gem can be installed to exploit this vulnerability against the [gem server](https://github.com/rubygems/rubygems/blob/master/lib/rubygems/server.rb).

## Prerequisite steps

First, please create a new Gemspec file (e.g. "securitytest.gemspec") with the following contents:

```
Gem::Specification.new do |s|
  s.name = 'securitytest'
  s.version = '0.1.0'
  s.date = '2017-11-10'
  s.summary = "This is a proof-of-concept gem"
    s.description = "Select the WWW hyperlink."
    s.authors = ["Author Name"]
  s.homepage = 'javascript:confirm(document.domain)'
end
```

After saving this Gemspec file, please execute `gem build securitytest.gemspec` and locate the resultant Gem file ahead of the following steps.

## Steps to reproduce

1. Please install the newly created Gem ("securitytest-0.1.0.gem") on your system.
2. Next, execute `gem server` to launch the built-in hosting interface.
3. Access the RubyGems Documentation Index via the applicable port.
4. Finally, locate the `securitytest` gem and select the `[www]` link to execute the JavaScript payload.

### Supporting evidence

{F238563}

Please let me know if you require any additional information regarding this issue.

Thanks

Yasin

## Attachments
- Gem_Server_XSS.png
