# NET::Ftp allows command injection in filenames

## Report Details
- **Report ID**: 294462
- **URL**: https://hackerone.com/reports/294462
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-02T11:33:02.750Z
- **Disclosed**: 2017-12-19T06:25:23.383Z

## Reporter
- **Username**: staaldraad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hi

While using NET::Ftp I realised you could get command execution through "malicious" file names. 

The problem lies in the `gettextfile(remotefile, localfile = File.basename(remotefile))` method.
When looking at the source code, you'll note:
```
def gettextfile(remotefile, localfile = File.basename(remotefile),
                &block) # :yield: line
  f = nil
  result = nil
  if localfile
    f = open(localfile, "w") # Vulnerable code here. open("| os command","w")
  elsif !block_given?
    result = String.new
  end
```
The `localfile` value will trigger command execution if the value is `| os command`. In general use, most users would likely provide their own localfile value and would not rely on the default of `File.basename(remotefile)`; however, in some situations, such as listing and downloading all files in a FTP share, the `remotefile` value would be controlled by the remote host and could thus be manipulated into causing RCE. Since the file path is simply a string returned by the server (either `ls -l` style for the `LIST` command, or filenames for `NLIST`), there is no need/guarantee that filename will be a valid filename.

I have attached a sample server that can be used to trigger this vulnerability, as well as a sample client which is vulnerable.

**Usage:**
Change the `host` and `port` values in both *ftpserver.rb* and *client.rb*

Start the server: `ruby ftpserver.rb`
Run the client: `ruby client.rb`

Observe that a new file has been created in the CWD of the *client.rb*. The file will be called `pang` and contain the output of the `id` command. As seen in screenshot1.png

The provided attack example is a little contrived and assumes the user is accepting the file names provided by the server, rather than their own. However, since there is no clear indication in the documentation or an expectation that filenames could lead to RCE, users may be caught unaware. It would probably be best to not use `open` in NET::Ftp, but rather something like `File.open`, maintaining both expected behaviour and security.

## Impact

Remote code execution through command injection. As a user of the NET::Ftp is expecting normal file creation behaviour, they might not be sanitising file paths.

## Attachments
- screenshot1.png
- client.rb
- ftpserv.rb
