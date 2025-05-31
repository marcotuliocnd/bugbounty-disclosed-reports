# Node Installer Local Privilege Escalation 

## Report Details
- **Report ID**: 1211160
- **URL**: https://hackerone.com/reports/1211160
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-28T00:40:41.036Z
- **Disclosed**: 2021-07-01T20:00:57.517Z

## Reporter
- **Username**: deepsurface-robert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
Node is vulnerable to local privilege escalation attacks under certain conditions on Windows platforms. More specifically, improper configuration of permissions in the installation directory allows an attacker to perform two different escalation attacks: PATH and DLL hijacking.  

To demonstrate this flaw, we first download the latest version of Node from https://nodejs.org/en/download/. At the time of writing, this was node version 14.17.0. 

We follow the standard installation steps, except for the installation directory, which we change to `C:\tools`. This directory can either be created through the installer GUI, or through `mkdir C:\tools`. 

{F1318095}

We also select the option in a later step to “automatically install the necessary tools”. 

In the screenshot below, note the improper permissions, `BUILTIN\Users Allow *`, on the installation directory, which are inherited from the drive root. This gives any local user the ability to create arbitrary files in the installation directory. 

{F1318096}

This unprotected directory has also been added to the system `PATH` variable, allowing an attacker to drop malicious executables in that directory and have them executed by other users in certain circumstances. (Note that you may have to start a new powershell instance to see the `PATH` change.)

{F1318097}

To fully demonstrate the implications of this vulnerability, first create a new unprivileged user. Then, as this user, drop a malicious exe into the `C:\tools` directory and rename it to `npm.exe`. For testing purposes, you can simply do `cp node.exe npm.exe`. Note that the same could be done for `npx`. 

Windows will search for a program with the `.exe` extension first, meaning that the malicious npm.exe will take precedence over `npm.cmd`. 

Now, as the privileged user, try running `npm`. This should drop you into the node shell, demonstrating how an attacker could run a malicious executable. 

{F1318098}

A writable PATH directory would also allow an attacker to hijack the execution of any commands that come later in the path. From the default node installation, this would include chocolatey, a software management tool for Windows. However, such a vulnerability could also affect all programs installed in the future as well. 

Aside from the `PATH` vulnerability, the insecure permissions configured could also allow an attacker to perform a DLL hijacking attack against the `node.exe`. Using [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon), we can confirm that node attempts to load a number of DLLs from the unprotected folder. 

{F1318099}

For more information on DLL hijacking attacks, see our [blog post](https://deepsurface.com/deepsurface-security-advisory-local-privilege-escalation-in-erlang-on-windows-cve-2021-29221/). 

It is worth noting that a very similar problem was discovered in RabbitMQ and reported by the DeepSurface Security research team. The RabbitMQ team fixed this issue in May 2021. For more information, see: [CVE-2021-22117](https://tanzu.vmware.com/security/cve-2021-22117).

## Impact

A locally  unprivileged attacker could perform a local privilege escalation attack through PATH and DLL hijacking.

## Attachments
- image1.png
- image4.png
- image5.png
- image2.png
- image3.png
