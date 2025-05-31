# Arbitrary file download due to bad handling of Redirects in WebTorrent

## Report Details
- **Report ID**: 975514
- **URL**: https://hackerone.com/reports/975514
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-06T04:58:16.107Z
- **Disclosed**: 2022-06-30T17:46:38.080Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Previously I reported  #963155 how an attacker can trick user into downloading malicious files using ".save torrent" feature, In this report I am going to reproduce the same behavior but by abusing a different feature.

## Description

While I was testing webtorrent on brave I noticed that whenever webtorrent detects a torrent file a request is made to the following extension scheme 
```
chrome-extension://lgjmpdmojkpocjcopdikifhejkkjglho/extension/brave_webtorrent.html?{torrent_url/magnet_link}
```

WebTorrent also consider a URL a valid torrent file if a URI starts with a `magnet:` scheme or if it ends with a `.torrent` extension for example:-

```
chrome-extension://lgjmpdmojkpocjcopdikifhejkkjglho/extension/brave_webtorrent.html?http://xyz.com?x=.torrent
chrome-extension://lgjmpdmojkpocjcopdikifhejkkjglho/extension/brave_webtorrent.html?magnet%3Ablahblah
```
Both the above URIs will be considered as a valid torrent file by WebTorrent (Refer below SS).

{F977576}

Another behavior that I observed was, when opening a URL `http://xyz.com?x=.torrent` will serve a normal response but one can force it to be opened with WebTorrent using the extensions scheme `chrome-extension://lgjmpdmojkpocjcopdikifhejkkjglho/extension/brave_webtorrent.html?http://xyz.com?x=.torrent`

Also, if a website for example, `http://xyz.com` redirects to `http://abc.com` then one can interrupt the redirection and can force it to open the source site via webtorrent before the redirection takes place. This behavior can be leveraged by an attacker to redirect a user to a malicious website or can force user to download a malicious file onto their system (for more better understanding please refer the Steps-to-Reproduce section) .

## Tested on

* Brave Version 1.12.114 Chromium: 84.0.4147.135 (Windows)

## Steps To Reproduce:

* Visit https://php-demo-app-shibli.cfapps.io/brave/brave-poc.html
* Click on "Save .torrent file" option
* "Poison.bat" file will be downloaded onto your machine

An attacker can also use this to redirect the user to a malicious webpage. See below POC video

{F977593}

## Impact

Remote Code Execution
Remote JavaScript execution
Installing malware on client's machine
Phishing

## Attachments
- ss1.PNG
- bandicam_2020-09-06_10-23-10-265.mp4
