# NULL Pointer dereference in idn.c

## Report Details
- **Report ID**: 2171309
- **URL**: https://hackerone.com/reports/2171309
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-09-19T09:41:20.922Z
- **Disclosed**: 2023-09-20T12:07:26.974Z

## Reporter
- **Username**: s0urc3_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
A NULL Pointer dereference vulnerability is present in idn.c source code.
This module is responsible of handling international domain name.
This issue was found performing manual source code review of Curl which took >20 hours.

## Steps To Reproduce:
Find below a detailed and commented execution flow / code snippet explanation.

## Impact 
In some circumstances writing or reading memory is possible, which may lead to code execution. 

###  Code Snippet
```c
static CURLcode idn_decode(const char *input, char **output)
{

char *decoded = NULL;
/* 4. 'decoded' initialized to a null pointer value	*/

CURLcode result = CURLE_OK;
#ifdef USE_LIBIDN2
if(idn2_check_version(IDN2_VERSION)) {
	
/* 5. Assuming the condition is false	*/
/* 6. Taking false branch	*/

int flags = IDN2_NFC_INPUT
#if IDN2_VERSION_NUMBER >= 0x00140000 | IDN2_NONTRANSITIONAL
#endif;
int rc = IDN2_LOOKUP(input, &decoded, flags);
if(rc != IDN2_OK)
rc = IDN2_LOOKUP(input, &decoded, IDN2_TRANSITIONAL);
if(rc != IDN2_OK)
result = CURLE_URL_MALFORMAT;
}
#elif defined(USE_WIN32_IDN)
result = win32_idn_to_ascii(input, &decoded);
#endif

if(!result)
/* 7. Taking true branch */
*output = decoded;
/* 8. Null pointer value stored to 'decoded'	*/
return result;
/* 9. Returning zero (loaded from 'result'), which participates in a condition later */

...

#ifdef USE_IDN

if(!Curl_is_ASCII_name(host->name)) {
/* 1. Assuming condition is True */
char *decoded;

/* 2  Calling idn_decode */
CURLcode result = idn_decode(host->name, &decoded); 

/* 10. Returning from idn_decode*/
if(!result) 
/* 11. Taking True branch */
{
    if(!*decoded) 
    {
	/* 12.  Dereference of null pointer (loaded from variable 'decoded') */
    Curl_idn_free(decoded);
    return CURLE_URL_MALFORMAT;
	}

host->encalloc = decoded;
host->name = host->encalloc;
}
else
    return result;
}
#endif
return CURLE_OK;
 }
```
## Remediation
Implement sanity checks to never dereference null pointer.

## References
- https://cwe.mitre.org/data/definitions/476.html
- https://0x00sec.org/t/kernel-exploitation-dereferencing-a-null-pointer/3850
- https://www.abatchy.com/2018/01/kernel-exploitation-6
- https://access.redhat.com/articles/20484

## Impact

- Crash or Segmentation Fault: If the decoded pointer is dereferenced when it is still NULL, it will lead to a crash or segmentation fault. This can disrupt the normal operation of the program.
    - Exploitation Scenario: An attacker can send specially crafted input data to trigger the vulnerable code path, causing the program to crash. While this doesn't directly lead to a security breach, it can be used as part of a larger attack to disrupt a service or application.

- Denial of Service (DoS): A null pointer dereference can be exploited to cause a DoS attack by repeatedly triggering the vulnerable code path, causing the application to crash and become unavailable.
    - Exploitation Scenario: An attacker could send a high volume of malicious requests that exploit the vulnerability, causing the service to crash repeatedly. This results in a DoS condition, making the service unavailable to legitimate users.

-   Remote Code Execution (Rare): In some cases, null pointer dereferences can potentially be leveraged for remote code execution if the attacker can control the data that leads to the dereference and can influence the program's control flow.
    *  Exploitation Scenario: An attacker would need to have a deep understanding of the program's memory layout and control flow to craft input that not only triggers the null pointer dereference but also redirects program execution to attacker-controlled code. This scenario is less likely but more severe.

## Attachments
No attachments
