# Field Day With Protocol Handlers

## Report Details
- **Report ID**: 416040
- **URL**: https://hackerone.com/reports/416040
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-29T06:41:48.353Z
- **Disclosed**: 2018-12-17T19:36:57.398Z

## Reporter
- **Username**: dudetechitout
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Summary
=====================

When launching a protocol such as ```mailto:```, ```SEARCH:```, or ```bitcoin:```, Brave only asks to allow the protocol to be opened by an external application. You can select on whether or not to remember the decision or not and to allow or deny it. The issue is that upon selecting "Remember this decision" and allowing the launching of an external application, it will launch the selected external application on any and all websites - regardless of permissions.

## Version Information: 

Brave	0.24.0
V8	6.9.427.23
rev	f657f15
Muon	8.1.6
OS Release	10.0.16299
Update Channel	Release
OS Architecture	x64
OS Platform	Microsoft Windows
Node.js	7.9.0
Brave Sync	v1.4.2
libchromiumcontent	69.0.3497.100


But First
=====================

Before I get started, I'd like to let you know there are a multitude of issues that will be covered in this report using this as a baseline. As basically this can be used for malicious intent and I'd like to get as many of them expressed as I can. *The most juicy one is "Completely Bypass Brave's Protocol Permissions".*

Opening Bitcoin Hardware Wallet Automatically
---------------------
The below steps will allow you to open a Bitcoin hardware wallet automatically with information already filled in.

## Steps To Reproduce:

 * Open the "wallet_landing.html" file.
 * Click "Click here to enable the bitcoin protocol in Brave."
 * Select "Remember this decision" and click "Allow".
 * Once the hardware wallet has launched, be sure to close it.
 * Click "Click here to send me some bitcoin."

As you can see upon navigating to the second page, it doesn't ask for confirmation. It automatically launches the hardware wallet with the address to send and amount to send as well; both of which are changeable.

## Video

Be sure to watch the video of this in action, it's attached as "bitcoin_wallet.mp4".

## Impact

Allowing the launching of a protocol across a multitude of domains is dangerous. For example, going to BitPay to make a payment with bitcoin, setting it to remember and navigating to another website, the hardware wallet would launch, all information already filled out, that could result in an accidental amount of bitcoin being sent to a nameless address.

Crashing the Brave Browser & OS
---------------------
With a few altercations of the code, you can launch a multitude of bitcoin wallets that would eventually result in a complete crash of the OS and browser.

Delete the code ```clearInterval(window.refreesh);``` on line 56 in file ```landing_run.html``` and launch it.

It will now launch the hardware wallet every 300 milliseconds.

You can of course change it to the ```mailto:``` protocol by changing the code ```window.open("bitcoin:" + address + "?amount=" + amount, "loader");``` to ```window.open("mailto:" + address + "?amount=" + amount, "loader");``` in the ```landing_run.html```, which will open up the users' default e-mail client every 300 milliseconds.

## Impact

Simply causing the operating system and browser to overload itself, which can cause loss of work or even permanent system damage depending on the user's reaction. For example, if the system overloads and completely freezes, the user will have no other choice but to do a hard shutdown. hard shutdowns can defiantly result in loss of work and if the user is unlucky, even system damage could accrue due to system file corruption at the time of shutdown.

Completely Bypass Brave's Protocol Permissions
---------------------
This is an interesting one and shouldn't be taken lightly. What makes it so interesting is that Brave only asks to use the ```url:``` protocol. Any other protocol after that, you can launch without Brave even asking. For example, if I wanted to open the ```mailto:``` protocol, I don't have to allow it through Brace. This same trick works with the ```sms:```, ```bitcoin:```, ```acrobat:```, ```search:``` and many more - basically anything that's listed in your "default apps by protocol".

Let's mess with the ```mailto:``` protocol by changing the code ```window.open("bitcoin:" + address + "?amount=" + amount, "loader");``` in ```landing_run.html``` to ```window.open("url:mailto:" + address + "?amount=" + amount, "loader");```.

Now launch ```landing_run.html``` and allow Brave to launch the ```url:``` protocol.

Once allowed, your e-mail client will now open!

## Video

__It is highly suggested to watch the video attached as "bypass_permissions.mp4".__

Keep in mind that my default browser is set as Internet Explorer.

If you'd like to see ```telnet:``` in action, check out the "telnet.mp4" video.

## Impact

The impact of this is that basically any protocol is free game - system wide. I've tried to run this same scenario in FireFox, Internet Explorer, and Google Chrome, but all three of them ignore it.

End
=====================

Hopefully I filled out this report right. If you have any questions at all, feel free to ask and I'll assist.

## Impact

Open bitcoin hardware wallet across multiple domains, crash OS and Brave, and bypass protocol permissions.

## Attachments
- bitcoin_wallet.mp4
- bypass_permissions.mp4
- telnet.mp4
- wallet_landing.html
- landing_run.html
