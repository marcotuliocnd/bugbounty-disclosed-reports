# Malformed Skybox .TGA in Half-Life (GoldSRC) leads to Access Violation

## Report Details
- **Report ID**: 351016
- **URL**: https://hackerone.com/reports/351016
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-13T01:14:32.363Z
- **Disclosed**: 2018-08-28T23:37:17.517Z

## Reporter
- **Username**: chippy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
A malformed .TGA when loaded as a Skybox on a map in a GoldSRC engine game (Half-Life) can lead to arbitrary code execution on a remote client.

###Reproduction Steps

Load the attached map + resources on a local Half-Life listen server. The game will crash with an Access Violation as soon as the map with the malicious skybox is loaded.

###Exploitability

Since anyone can host a map with custom assets, and the custom assets are loaded onto a remote clients computer, a malicious server can distribute malformed skybox assets (.TGA's) that could cause remote code execution on clients. The inclusion of .DLL's on Steam without ASLR make exploitablility of this bug via ROP quite trivial.

## Impact

###Impact

A malicious server could infect hundreds or perhaps thousands of clients with this bug. This bug could also be used in targeted attacks for the theft / compromise of high-value Steam accounts by attacking their Half-Life client.

## Attachments
- crossfire.tga.zip
