# Credential leak when use two url

## Report Details
- **Report ID**: 1569926
- **URL**: https://hackerone.com/reports/1569926
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-13T19:09:41.178Z
- **Disclosed**: 2022-06-27T06:55:01.273Z

## Reporter
- **Username**: liang1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Curl can leak user credentials if use two url.

## Steps To Reproduce:


  1. curl -I -v -u aaa:bbb hackerone.com curl.se
  2. the output is:
> Connected to hackerone.com (104.16.100.52) port 80 (#0)                                                
> Server auth using Basic with user 'aaa'                                                                   
> HEAD / HTTP/1.1                                                                                           
> Host: hackerone.com                                                                                       
> Authorization: Basic YWFhOmJiYg==                                                                        
 > User-Agent: curl/7.83.1                                                                                  
 > Accept: */*

> Connection #0 to host hackerone.com left intact                                                         
>Trying 151.101.65.91:80...                                                                             
> Connected to curl.se (151.101.65.91) port 80 (#1)                                                        
>Server auth using Basic with user 'aaa'                                                                  
 > HEAD / HTTP/1.1                                                                                          
 > Host: curl.se                                                                                            
 > Authorization: Basic YWFhOmJiYg==                                                                         
> User-Agent: curl/7.83.1                                                                                   
> Accept: */*
                                                                                                       
  3. from the output we can see, the second url get the same credentials

## Impact

Leak of confidential information (user credential)

## Attachments
No attachments
