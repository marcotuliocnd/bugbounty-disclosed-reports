# Gratipay rails secret token (secret_key_base) publicly exposed in GitHub

## Report Details
- **Report ID**: 262620
- **URL**: https://hackerone.com/reports/262620
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-23T16:40:01.692Z
- **Disclosed**: 2017-08-23T17:04:45.686Z

## Reporter
- **Username**: sp4rrow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary
Gratipay's Rails secret token is publicly exposed on GitHub. Knowing the secret token allows an attacker to impersonate any user in the application.

Thanks to EdOverflow for sharing the tips for finding security issues in GitHub projects, below is the referenced github for the analysis. 

# Description
The `secret_token.rb` file's content includes a long randomized string which is used to verify the integrity of signed cookies (such as user sessions when people are signed into your web app).
[Documentation](http://edgeguides.rubyonrails.org/upgrading_ruby_on_rails.html) says:
> Use your existing `secret_key_base` from the `secret_token.rb` initializer to set the `SECRET_KEY_BASE` environment variable for whichever users run the Rails app in production mode. Alternately, you can simply copy the existing `secret_key_base` from the `secret_token.rb` initializer to `secrets.yml` under the production section, replacing `<%= ENV["SECRET_KEY_BASE"] %>`.
> Make sure your secret_key_base is kept private
if you're sharing your code publicly.

**Further Details:**
Knowing the secret token allows an attacker to impersonate any user in the application.

# Steps To Reproduce
Go to the Gratipay "Access Dashboard" project (https://github.com/gratipay/access-dashboard/blob/rails-recode/config/initializers)
In the `secret_token.rb` file the `secret_key_base` is publicly disclosed.
As per the comments in the code as well as the documentation the key should always be kept private, looks like the developer forgot to remove the token. Happens! Too much work sometimes and the expected delivery deadlines :)

# Patch
Removing the secret key would do the work!

# Supporting Material/References:
Thanks to EdOverflow for sharing the tips for finding security issues in GitHub projects. :)
(https://gist.github.com/EdOverflow/922549f610b258f459b219a32f92d10b)

Please let me know if any further information is needed on this.

BR,
null

## Attachments
No attachments
