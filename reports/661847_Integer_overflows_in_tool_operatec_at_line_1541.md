# Integer overflows in tool_operate.c at line 1541

## Report Details
- **Report ID**: 661847
- **URL**: https://hackerone.com/reports/661847
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-27T15:07:00.843Z
- **Disclosed**: 2021-01-01T15:40:09.134Z

## Reporter
- **Username**: cjun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
[add summary of the vulnerability]
In tool_operate.c at line 1541, if --retry-delay>18446744073709552, config->retry_delay*1000 > 2^64 results in integer overflows, on 64 bit architectures; 
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. [add step]
Tool_operate.c add a "printf" at line 1538 as following:
printf("config->retry_delay*1000L = %ld\n", config->retry_delay*1000L);
  2. [add step]
make
  1. [add step]
run command:  
./src/curl --retry-delay 18446744073709552 -v 192.168.222.1:8080/test.html
output:
config->retry_delay*1000L = 384

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

The flaw exists on 32&64 bit architectures, it results in retry-delay is invalid.

## Attachments
No attachments
