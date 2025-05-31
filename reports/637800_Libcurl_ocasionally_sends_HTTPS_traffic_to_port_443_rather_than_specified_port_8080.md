# Libcurl ocasionally sends HTTPS traffic to port 443 rather than specified port 8080

## Report Details
- **Report ID**: 637800
- **URL**: https://hackerone.com/reports/637800
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-08T17:08:00.783Z
- **Disclosed**: 2021-02-03T07:50:50.073Z

## Reporter
- **Username**: omdr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
We have encountered an issue with libcurl where, under certain network conditions, the library will attempt to submit data to an incorrect port as was set by CURLOPT_PORT. As information is sent to an unauthorised port, we consider this an information disclosure issue.

Our security software encompasses a Windows application (an agent) that runs as a Windows service. Its purpose is to collect custom metrics from the machine, such as IO operations (file reads, file writes, ...), process start/stops, user login, and some other forensic info. We use libcurl to communicate with a server over HTTPS.

A customer with ~5000 our agents raised an issue that approx 0.5% of all traffic is sent to port 443. In our application, we only use port 8080. Each request is made with source code (nearly identical) to the one I attach to this report.

This client uses Windows DNS load balancing. An agent will make a request to a local DNS server and the server will return an IP of one of the 5 servers based on round-robin. All servers have a web server running and our server-side application working on port 8080. 

We were unable to pin-point exactly which network conditions trigger this issue reliably, however, we have been able to reproduce it in a production environment with logging enabled. This could potentially be triggered by a slow server response or when the web server is down.

## Steps To Reproduce:

  1. Configure a round-robin DNS load balancing
  2. Make a high number of small HTTPS request to port 8080
  3. [Potentially] Server fails to handle a response [exact conditions were not established]
  4. Approx 0.5% of all traffic will be directed to port 443, under the hood, without application instructions

## Supporting Material/References:

- Example source code
- Log sample showing the `primary port` is changed to 443

## Versions
- OS: Windows 10 x64

Libraries
- curl:x86-windows-static                            7.61.1-7        
- curl[http2]:x86-windows-static                                     
- curl[openssl]:x86-windows-static                                   
- curl[ssl]:x86-windows-static                                       
- curl[winssl]:x86-windows-static                                    
- fmt:x86-windows-static                             5.3.0-1         
- gtest:x86-windows-static                           2019-01-04-2    
- nghttp2:x86-windows-static                         1.35.0          
- nlohmann-json:x86-windows-static                   3.6.1           
- openssl-windows:x86-windows-static                 1.0.2q-2        
- openssl:x86-windows-static                         0               
- rapidcheck:x86-windows-static                      2018-11-05-1    
- rapidxml:x86-windows-static                        1.13            
- spdlog:x86-windows-static                          1.3.1           
- zlib:x86-windows-static                            1.2.11-5

## Impact

An attacker must have access to the authorised server, for example, be a local admin. 

The server is expected to run a web app on a port other than 443, for example, port 8080. 

A client application will send traffic to only port 8080. But libcurl will occasionally send traffic to port 443. 

If an attacker set up a web app on port 443, they will receive some traffic (0.5%) that was supposed to be sent to a different port.

## Attachments
- log_sample.txt
- code.c
