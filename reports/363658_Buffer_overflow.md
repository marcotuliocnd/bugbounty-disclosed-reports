# Buffer overflow

## Report Details
- **Report ID**: 363658
- **URL**: https://hackerone.com/reports/363658
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-09T06:51:22.024Z
- **Disclosed**: 2018-06-10T06:06:40.411Z

## Reporter
- **Username**: kaushalag29
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
A buffer overflow condition exists when a program attempts to put more data in a buffer than it can hold or when a program attempts to put data in a memory area past a buffer. In this case, a buffer is a sequential section of memory allocated to contain anything from a character string to an array of integers. Writing outside the bounds of a block of allocated memory can corrupt data, crash the program, or cause the execution of malicious code. 
For better refernce:
https://www.owasp.org/index.php/Buffer_Overflow

POC:
Go to
https://liberapay.com/sign-up
Now type(copy and paste using python) email address of size more than 100mb or in gbs and sign up.
After signing up for few times u will receive this error as shown in sent pic.

Steps to resolve:
Restrict size limit on input parameter.

## Impact

Category:Availability: Buffer overflows generally lead to crashes. Other attacks leading to lack of availability are possible, including putting the program into an infinite loop.
    Access control (instruction processing): Buffer overflows often can be used to execute arbitrary code, which is usually outside the scope of a program’s implicit security policy.
    Other: When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Attachments
- Screenshot_from_2018-06-09_12-15-18.png
