# Information Exposure Through Directory Listing

## Report Details
- **Report ID**: 1948562
- **URL**: https://hackerone.com/reports/1948562
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-15T18:35:12.441Z
- **Disclosed**: 2023-06-23T14:57:45.264Z

## Reporter
- **Username**: mo3giza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Summary:

Directory listing is a web server function that displays the directory contents when there is no index file in a specific website directory. It is dangerous to leave this function turned on for the web server because it leads to information disclosure.

## Steps To Reproduce:

Go to this URL:  ███
You can see logs files
████
████████

## PoC:
```
██████████ - - [█████:████ +0000] "GET /api/live/ws HTTP/1.1" 400 3325 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
█████ - - [█████:████ +0000] "GET /api/live/ws HTTP/1.1" 400 3325 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
█████ - - [██████████:██████████ +0000] "GET /api/live/ws HTTP/1.1" 400 872 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
```
```
[███ █████ █████████████] [core:error] [pid 8186:tid 140028348987136] [client ███:47058] AH00126: Invalid URI in request GET /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/hosts HTTP/1.1
[██████ ████████████ ██████████] [authz_core:error] [pid 8186:tid 140027803723520] [client ██████████:47426] AH01630: client denied by server configuration: proxy:███████████
[████ ████████████ ██████████] [ssl:error] [pid 11243:tid ████] [client ████████:42490] AH02042: rejecting client initiated renegotiation
[█████ ████ ████] [proxy:error] [pid 4547:tid 140029011683072] (111)Connection refused: AH00957: HTTP: attempt to connect to ████:3000 (████████████) failed
```

## Impact

Information Disclosure

## Attachments
No attachments
