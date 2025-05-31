# [flintcms] Account takeover due to blind MongoDB injection in password reset

## Report Details
- **Report ID**: 386807
- **URL**: https://hackerone.com/reports/386807
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-07-25T20:41:49.826Z
- **Disclosed**: 2018-08-15T14:17:31.426Z

## Reporter
- **Username**: becojo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a privilege escalation vulnerability in flintcms.
It allows to reset a known user password, extract its password reset token and reset its password to then access the account.

# Module

**module name:** flintcms
**version:** v.1.1.9
**npm page:** `https://www.npmjs.com/package/flintcms`

## Module Description

Flint is a CMS built to be easy to use and super flexible. Your content needs to fit into more layouts and environments than anyone but you can plan for, so Flint enables you to make the templates you need and fill it with your content. It's a CMS that is built for those who want to fully design the front-end of their website without wanting to deal with static site generators or older content management systems (that are slow and use outdated technology).

## Module Stats

7 downloads in the last week

# Vulnerability

## Vulnerability Description

The vulnerability is caused by the lack of user input sanitization in the route that verifies the password reset token. The value from the parameter is directly sent to the Mongoose API which allows a user to insert MongoDB query operators. These operators can be used to extract the value of the field _blindly_ in the same manner of a blind SQL injection. In this case, the `$regex` operator is used to guess each character of the token from the start.

Vulnerable code:

```js
  router.get('/verify', async (req, res) => {
    const token = req.query.t

    const user = await User.findOne({ token })

    if (!user) {
      res.redirect('/admin')
      return
    }

    res.redirect(`/admin/sp/${token}`)
  })
```
You can tell the different behavior when visiting these pages (assuming one of the user has reset their password):
- http://localhost:4000/admin/verify?t[$ne]=something redirects to http://localhost:4000/admin/sp/[object%20Object]
- While http://localhost:4000/admin/verify?t[$eq]=something redirects to http://localhost:4000/admin/login?p=/admin/

To take over an account, the following are required:
1. Reset the password of the targeted account (the email of the target user must be know)
2. Use the password reset page to extract the token using the blind MongoDB injection
3. Use the token to reset the password and log in 

---

To lift the requirements to know the email, it is also possible to find the emails of the users because the password reset form is also vulnerable to blind MongoDB injection. In the same manner as previously, each character of the email can be guessed using the `$regex` MongoDB operator.

Vulnerable code:
```js
  router.post('/forgotpassword', async (req, res) => {
    const { email } = req.body
    const user = await User.findOne({ email })

    if (!user) {
      res.status(400).end('There is no user with that email.')
      return
    }
    // [...]
```

## Steps To Reproduce:

1. Follow the install guide https://flintcms.co/docs/installation/
2. Create the admin user at http://localhost:4000/admin/install
3. Log out
4. Proceed to reset the password of the admin. Let's say the email configured was `admin@localhost.com`
5. Run the provided Python script
6. Visit the reset URL that the script finds
7. Reset the user password
8. You are now logged in

## Patch
The request parameters should be converted to string before being sent to the Mongoose API. Adding `.toString()` to the parameters should be enough to prevent objects being passed to Mongoose. For example:

```js
    const { email } = req.body
    const user = await User.findOne({ email: email.toString() })
```

```js
    const token = req.query.t.toString()
```

Further sanitization should be added to other endpoints. 

## Supporting Material/References:

- Ubuntu 16.04.3 LTS
- v8.4.0
- 5.3.0
- For the script: Python 2.7.12 and the `requests` package

# Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker could take over the website, delete data or server malicious content.

## Attachments
- exploit.py
