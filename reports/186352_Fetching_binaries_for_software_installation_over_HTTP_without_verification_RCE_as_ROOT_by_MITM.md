# Fetching binaries (for software installation) over HTTP without verification (RCE as ROOT by MITM)

## Report Details
- **Report ID**: 186352
- **URL**: https://hackerone.com/reports/186352
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-29T12:22:47.340Z
- **Disclosed**: 2016-12-29T20:19:52.031Z

## Reporter
- **Username**: e3amn2l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
From: https://secure.phabricator.com/book/phabricator/article/installation_guide/
> Installing Required Components
If you are installing on Ubuntu or an RedHat derivative, there are install scripts available which should handle most of the things discussed in this document for you:
RedHat Derivatives: install_rhel-derivs.sh
Ubuntu: install_ubuntu.sh

The install_rhel-derivs.sh file download binaries over plain HTTP and run/install them using sudo without verification (checksum / GPG), thus:

* active MITM attacker can modify the binaries with malicious code.
* malformed target server infrastructure can deliver malicious code (server hacked/DNS hijacked/etc..)

The malicious code will run under ROOT.

for example in 1, a downloaded file over HTTP will be run as php using sudo (the script won't run without root/sudo rights)
https://github.com/phacility/phabricator/blob/master/scripts/install/install_rhel-derivs.sh#L49-L58
>echo "ERROR: You must be able to sudo to run this script, or run it as root.";

1\. https://github.com/phacility/phabricator/blob/master/scripts/install/install_rhel-derivs.sh#L95
```
  echo "Attempting to install PEAR"
  wget http://pear.php.net/go-pear.phar
  $SUDO php go-pear.phar && $SUDO pecl install apc
```

2\. https://github.com/phacility/phabricator/blob/master/scripts/install/install_rhel-derivs.sh#L68-L70
```
    echo "It doesn't look like you have the EPEL repo enabled. We are to add it"
    echo "for you, so that we can install git."
    $SUDO rpm -Uvh http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
```

fix:

1\. use https:// instead of http:// (the used URLs support HTTPS)
2\. implement verification (sha256 on static files, such as if specific version is used) & GPG on dynamic files (verify signatures of signed files, such as downloading latest version of software).

misc: safe word "mongoose" or mongoose to indicate that I read the rules.

## Attachments
No attachments
