# Lack of quarantine meta-attribute for downloaded files leads to GateKeeper bypass

## Report Details
- **Report ID**: 374106
- **URL**: https://hackerone.com/reports/374106
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-30T01:04:45.729Z
- **Disclosed**: 2019-09-12T16:34:06.053Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Executable files downloaded through Brave don't have quarantine attribute. 
That means it's possible to launch any executable bypassing codesigning + quarantine.

However, later I found that Brave has already [tracked similar report](https://github.com/brave/browser-laptop/issues/13088) but only in the context of `.pkg` files. 

Additionally, Brave is allowed to run apps in Terminal. It was already shown in [369185](https://hackerone.com/reports/369185) that Brave has more permissions on Terminal than it should have => It is possible to execute downloaded files in Terminal by click(double click) in Brave "Downloads" toolbar.

macOS doesn't have executable files that could be launched without installation after downloading from the web. Files like `.command` and `.tool` could be executed in Terminal and only if they have `-x`, but these files downloaded from the web have only `-rw`.

However, it's possible to download and launch Java archives, because they're archives => executable after downloading.

> As far as I know, Java isn't installed by default. That means only macOS users with Java installed are affected by this problem.

## Products affected: 

Brave: 0.23.19 
V8: 6.7.288.46 
rev: 178c3fbc045a0cbdbe098db08307503cce952081 
Muon: 7.1.3 
OS Release: 17.6.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Tor: 0.3.3.7 (git-035a35178c92da94) 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.87

## Steps To Reproduce:

### Chrome/<etc>

#### Apps from unknown publishers disallowed (screencast):

Download `test.jar` using Chrome -> launch it from Downloads toolbar -> macOS warns that this executable published by an unknown developer -> manually allow running the app from Settings-> app launches.

#### Apps from anywhere allowed:

Download `test.jar` using Chrome -> launch it from Downloads toolbar -> macOS warns that this Java archive was downloaded from the web  -> allow -> app launches.

#### Apps from anywhere + downloaded executables allowed:

Download `test.jar` using Chrome -> launch it from Downloads toolbar -> macOS warns that Chrome can't run files in Terminal.

### Brave (unknown publishers disallowed, screencast)

Download `test.jar` using Brave -> launch it from Downloads toolbar (double click) -> no warnings, Java archive launches.

## Supporting Material/References:

[Live PoC + jar + screencast](https://brave-jar-nqzdybbsgw.now.sh/)

## Impact

> Java isn't installed on macOS by default (as I know), that's why it's not critical.

Users with installed Java could run any downloaded through Brave java archive from Downloads toolbar bypassing quarantine + code-signing checks in one click (double click).

I think this isn't a duplicate, because this attack scenario leverages two vulnerabilities (quarantine + Brave permissions over Terminal).

> The fact that downloaded files aren't in quarantine by itself doesn't show that it's possible to execute any app by click. However, Brave's permissions over Terminal introduce that.

## Attachments
- exploit.html
- brave-jar.mp4
- hello.jar
