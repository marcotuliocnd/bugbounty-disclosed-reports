# Arbitrary Code Injection in ownCloud’s Windows Client

## Report Details
- **Report ID**: 155657
- **URL**: https://hackerone.com/reports/155657
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-31T19:00:09.481Z
- **Disclosed**: 2016-11-23T18:45:41.271Z

## Reporter
- **Username**: fbogner
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
The current ownCloud Windows Desktop client is prone to an arbitrary code injection vulnerability.

The underlying issue is that the ownCloud desktop client tries to load QT extensions from C:\usr\i686-w64-mingw32\sys-root\mingw\lib\qt5\plugins.

As any authenticated user on Windows is allowed to create new folders within C:, the expected folder structure can be created.

What that means is that a local attacker can create a malicious QT extensions that gets automatically loaded on the next launch of the ownCloud Desktop client.

To verify the issue I first tried to simply create a new QT imageformats plugin. However I failed! Have you ever tried to install QT? So I decided to simply modify an existing DLL.

Hence, I used Hopper to disassemble the qwindows.dll platform’s library to learn more about its entry points. With that knowledge I planned to modify the DLL so that it shows a simply message box. The necessary shellcode was created with Metasploit:

msfvenom -a x86 --platform windows -p windows/messagebox TEXT="DLL Loaded" EXTIFUNC=process -f raw > shellcode
cat shellcode |xxd -p

I then overwrote some bytes after one of the previously identified DLL entry points with the shellcode.

After placing the modified payload DLL into C:\usr\i686-w64-mingw32\sys-root\mingw\lib\qt5\plugins\platforms the shellcode got executed after launching the ownCloud desktop client.

Please see the attached PDF for some images documenting the process.
Furthermore I created a private screen capture: https://owncloud.bogner.sh/s/Ik8AYJ9FfY5Rkyq

## Attachments
- Arbitrary_Code_Injection_in_ownCloud_s_Windows_Client___bogner.pdf
