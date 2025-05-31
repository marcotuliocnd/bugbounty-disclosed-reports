# Possibility to freeze/crash the host system of all Slack Desktop users easily

## Report Details
- **Report ID**: 392728
- **URL**: https://hackerone.com/reports/392728
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-10T11:09:25.530Z
- **Disclosed**: 2020-11-10T20:18:19.225Z

## Reporter
- **Username**: freesec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hello,

I report here what I suspect to be a critical issue for all your users using the Slack Desktop app.
Please find below my research way and the corresponding POC result:

First, I started by exploring the content of the file **app.asar** of the Slack Dresktop application.
I was firstly attrackted by the file **parse-protocol-url.js** and more particularly on the following lines:

```javascript
const expressionsToMatch = [{
  regex: /devEnv=(dev\d*|staging|qa\d*)/,
  onMatch: (match) => ({ devMode: true, devEnv: match[1] })
}
```
I immediately tried the URL `slack://open?devEnv=staging` in my browser and it was working as expected:

{F330966}

The issue started whan I noted the fact that if I reload my browser, I will have a second Slack Desktop process with a second interface. This is not the case when I use the url `slack://open` openning the normal prod interface. So, even if I can imagine this behavior as practical for your developers (having two Slack Desktop applications at the same time, one one the production environment and one on the staging/dev/qa environment), the fact to be able to launch infinite Slack Desktop application should be forbidden.

I click 9 times on **F5** in my browser and below was the result:

{F330971}
{F330972}

You can test this fact on your side with the simple POC page in attachment : {F330973}

On my side, with 32Go of RAM and a i7-6820HQ CPU 2.70, I freezed my PC easily with the test **100 Slack Apps - Not Funny!**

You will not have this issue if you use the url `slack://open` where only the CPU can be used at 100% depending of how many requests you launch:

{F330972}

With the url  `slack://open?devEnv=staging` you will have quickly % of CPU usage and a memory usage increasing quickly.

The security aspect here is on the availability of the application.

## Impact

An attacker can use this lack of control in order and through a simple link ( or a batch file for windows or a script for linux, etc ... ) can crash and/or freeze all customers using your Slack Desktop application. I did not test on Linux or Mac but I suspect that the effects are the same.

I recommand you to put in place the same control that the one on production environment: if one slack desktop application is already launched on the staging/dev[xxx]/qa[xxx] platform, do not launch a second one but just give the focus on the existing one.

What do you think?

## Attachments
- staging.png
- multislackapp-1.png
- multislackapp-2.png
- MultiSlackApps.html
- multislackapp-cpu.png
