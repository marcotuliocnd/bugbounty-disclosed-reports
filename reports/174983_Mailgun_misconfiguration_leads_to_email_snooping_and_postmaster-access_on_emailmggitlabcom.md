# Mailgun misconfiguration leads to email snooping and postmaster@-access on email.mg.gitlab.com

## Report Details
- **Report ID**: 174983
- **URL**: https://hackerone.com/reports/174983
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-10T18:19:32.283Z
- **Disclosed**: 2016-12-06T00:57:56.300Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

Previously a blog post went out about Uber's Sendgrid issues: http://blog.pentestnepal.tech/post/149985438982/reading-ubers-internal-emails-uber-bug-bounty

Also, a report from @uranium238 went out due to a similar issue with Slack (that I know uses Mailgun): https://hackerone.com/reports/163938

Now, by reasons I do not know, this actually has some issues still unpatched by Mailgun, which in combination with a misconfiguration, currently exposes at least `email.mg.gitlab.com`.

The problem lies in this issue:
1. You add the domain `mg.gitlab.com` to Mailgun
2. Mailgun asks you to add a MX record to `mg.gitlab.com`
3. You add that, then Mailgun also tells you that to get tracking you need to add a CNAME from `email.mg.gitlab.com` to mailgun.org as well. 
4. What is missing here, is for you to actually add `email.mg.gitlab.com` to your account as a separate domain by itself. By not doing this, anyone can add this domain to their account.
5. You probably later on remove the MX from `mg.gitlab.com` again, but the CNAME is still there for `email.mg.gitlab.com`

The problem with missing out on #4 above is how DNS CNAMEs works. If you have a CNAME pointing to another domain, this CNAME will actually inherit the MX-records from the other domain. This basically means that your `email.mg.gitlab.com` is now listed with MX-records from Mailgun:

```
$ host email.mg.gitlab.com
email.mg.gitlab.com is an alias for mailgun.org.
mailgun.org has address 173.203.37.113
mailgun.org mail is handled by 10 mxb.mailgun.org.
mailgun.org mail is handled by 10 mxa.mailgun.org.
```

Due to this, I can claim this domain as mine in Mailgun:
{F127024}

And due to this, I can now create a mailing list called `postmaster@email.mg.gitlab.com` with Access-level: `everyone`:
{F127025}

I'll add my own email as a recipient:
{F127026}

I'll now try and see if I can receive emails to `postmaster@email.mg.gitlab.com`:
{F127027}

The logs of Mailgun will show me the routing:
{F127028}

And my inbox now have the emails sent to `postmaster@email.mg.gitlab.com`:
{F127029}

Since postmaster can be used to issue certificates for these domains, and since no one but you should have access to the whitelisted SSL-issuing aliases (ref: https://wiki.mozilla.org/CA:Problematic_Practices#Email_Address_Prefixes_for_DV_Certs)  
I recommend that you:

1. Add the both domains `email.mg.gitlab.com` to your Mailgun account. **I have removed it again so you can take it back, remember that anyone can right now claim it themselves.**. 
2. Keep in mind that all domains pointing to Mailgun (MX/CNAME) needs to be claimed by you, even the sub sub domains of the ones already in Mailgun. So make sure that no other domains pointing to Mailgun are missing inside your Mailgun account.

Regards,
Frans

## Attachments
- Screen_Shot_2016-10-10_at_20.13.53.png
- Screen_Shot_2016-10-10_at_20.14.05.png
- Screen_Shot_2016-10-10_at_20.14.10.png
- Screen_Shot_2016-10-10_at_20.14.38.png
- Screen_Shot_2016-10-10_at_20.15.05.png
- Screen_Shot_2016-10-10_at_20.15.13.png
