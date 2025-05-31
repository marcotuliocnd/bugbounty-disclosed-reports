# Parallel upload hangs curl if upload file not found

## Report Details
- **Report ID**: 1019372
- **URL**: https://hackerone.com/reports/1019372
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-10-26T21:42:14.324Z
- **Disclosed**: 2020-10-29T16:24:29.914Z

## Reporter
- **Username**: brumbrum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
Attempting to upload (-T) a not found file with parallel (-Z) flag present, will cause curl to get stuck and never terminate, potentially stalling scripts that make use of this particular flags. 

curl -T blabla-notexists -Z upload.example.com www.google.com www.cnn.com www.apple.com


Same issue occurs if using -Z or --parallel flags.


$ curl -T blabla-notexists -Z upload.example.com www.google.com www.cnn.com www.apple.com
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
DL% UL%  Dled  Uled  Xfers  Live   Qd Total     Current  Left    Speed
--  --      0     0     1     0     1 --:--:--  0:00:01 --:--:--     0      curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information



Doesn't happen with --parallel-max or --parallel-immediate flags.

Observing the network with tcpdump, shows NO traffic at all.


I suspect this is just an ordinary bug, but reporting it in case there is a security angle that might be present. Really the only obvious security issue is that curl will block possibly forever, and if curl tool is used inside a script or binary (via system() for example) could cause that script/binary to stop/block/hang.  In some cases, this could lead to a bad situation, leading to denial of service or loss of service availability for program/process/server/service using curl in such a way.

Not 100% sure, but I suspect that libcurl does not have this issue.  I could be wrong.


Steps to Reproduce:
Upload (-T) a file with curl while in parallel mode (-Z) and the upload file must not exist locally.

curl -T blabla-notexists -Z upload.example.com www.google.com www.cnn.com www.apple.com

## Impact

curl hangs leading to denial of service or loss of service availablity for script or binary using curl CLI tool.


Mitigation:
Don't use -Z parallel flag with -T upload flag.

## Attachments
No attachments
