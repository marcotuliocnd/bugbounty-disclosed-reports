# Insecure Bundler configuration fetching internal Gems (okra) from Rubygems.org

## Report Details
- **Report ID**: 1104874
- **URL**: https://hackerone.com/reports/1104874
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-16T17:13:18.507Z
- **Disclosed**: 2021-08-10T07:12:35.420Z

## Reporter
- **Username**: zofrex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
I believe (most likely) that one of your projects is not set up correctly to only pull internal gems from your internal gem server, and instead will pull gems from Rubygems.org if the version number there is higher.

Specifically, the "okra" gem.

At around 15:21 today (UTC) the okra gem that I wrote – https://rubygems.org/gems/okra – was installed on the machine with hostname "oscillatinghost" under the username "fernando" on your network.

This would be possible if the Gemfile either installs gems from global sources (thus allowing the version on Rubygems to 'trump' the internal version) or if the okra gem is depended on by another internal gem, and your version of Bundler is less than 2.2.10 – see here for details on that: https://bundler.io/blog/2021/02/15/a-more-secure-bundler-we-fixed-our-source-priorities.html

It is possible this is not correct, and instead, someone typed "gem install okra" without specifying where to fetch the Gem from. This would potentially also have fetched it from Rubygems.

Please note that the Gem I wrote does not do anything malicious, and only fetches the minimum information I need to filter out false positives and correctly identify organisations. You can verify this yourself by looking at the code for the gem "okra-90002.0" in your gems folder. I will delete all information relating to your organisation as soon as it is no longer needed.

## Impact

The impact is that an attacker could achieve arbitrary Remote Code Execution on any machines that will fetch the gem from the Rubygems repository.

Note that to achieve code execution, merely installing the Gem is enough, it does not have to be require'd or run.

## Attachments
No attachments
