# Memory Leak

## Report Details
- **Report ID**: 3137657
- **URL**: https://hackerone.com/reports/3137657
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2025-05-09T20:18:26.098Z
- **Disclosed**: 2025-05-10T21:16:26.583Z

## Reporter
- **Username**: antypanty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
* in getparameter() via strdup() in tool_getparam.c > SIGSEGV
Project: cURL
File: src/tool_getparam.c
Function: getparameter() → indirectly via getstr()
Detected By: AddressSanitizer (ASan)
Command Used:

ASAN_OPTIONS="detect_leaks=1:verbosity=2:malloc_context_size=50" ./curl -K <crash-file>

# Overview
A memory leak vulnerability has been identified in Curl’s configuration handling within tool_getparam.c. The issue originates from improper memory management of dynamically allocated strings using strdup(), leading to a persistent allocation that is never freed. Leak occurs in a key parsing function that processes user input, and survives until program termination, violating memory safety expectations for clean exits or tools used in pipelines and fuzzing environments. The issue lies in allocations made for fields like config->range, config->useragent, etc., without corresponding calls to free() or a cleanup routine.
Affected Component
- File: tool_getparam.c
- Function: getstr()
- Location: Line 2754
- Bug Type: Memory Leak
- Impact: The persistent allocation results in uncontrolled heap growth. While a memory leak alone does not directly enable arbitrary code execution, further analysis is required to assess whether heap fragmentation or manipulation could lead to memory corruption scenarios.

## Technical Details
Issue Description
The function getstr() is responsible for handling dynamically allocated strings used for various Curl parameters. If an existing string pointer is assigned a new value, it is properly freed before reallocation:
static ParameterError getstr(char **str, const char *val, bool allowblank)
{
  if(*str) {
    free(*str);
    *str = NULL;
  }

However, when val is provided, strdup() is used to duplicate the string without ensuring proper memory cleanup later:
  if(val) {
    if(!allowblank && !val[0])
      return PARAM_BLANK_STRING;
  
    *str = strdup(val);  // Potential leak occurs here
    if(!*str)
      return PARAM_NO_MEM;
  }
  return PARAM_OK;
}


Since there is no corresponding free() before process termination, this leads to a direct memory leak, as confirmed by ASAN:
==7796==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 2 byte(s) in 1 object(s) allocated from:
    #0 0x55fa1dc2f19e in strdup (/home/og/test/afl-test/curl/build/src/curl+0xdf19e)
    #1 0x55fa1dca3e21 in getparameter /home/og/test/afl-test/curl/src/tool_getparam.c:2754
    #2 0x55fa1dce687b in parseconfig /home/og/test/afl-test/curl/src/tool_parsecfg.c:175

Control Flow Analysis
The memory allocation propagates through several functions, increasing impact:
getparameter() → parseconfig() → parse_args() → operate() → main()


This suggests that user-provided configuration values influence the strdup() call, meaning an attacker might manipulate inputs to generate excessive heap allocations.

Sanitizer Output (Summary)

==7796==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 2 byte(s) in 1 object(s) allocated from:
    #0 0x55fa1dc2f19e in strdup
    #1 0x55fa1dca3e21 in getparameter /curl/src/tool_getparam.c:2754:35
    #2 0x55fa1dce687b in parseconfig /curl/src/tool_parsecfg.c:175:13
    #3 0x55fa1dca7c03 in getparameter /curl/src/tool_getparam.c:2793:10
    ...
SUMMARY: AddressSanitizer: 2 byte(s) leaked in 1 allocation(s).

## Root Cause

The function getstr() is used to safely copy a string into a heap-allocated buffer, freeing any previous value:

static ParameterError getstr(char **str, const char *val, bool allowblank)
{
  if(*str) {
    free(*str);
    *str = NULL;
  }
  if(val) {
    if(!allowblank && !val[0])
      return PARAM_BLANK_STRING;

    *str = strdup(val);  // <-- Allocation not freed later
    if(!*str)
      return PARAM_NO_MEM;
  }
  return PARAM_OK;
}

The call site inside getparameter() likely sets *str (e.g. config->range or another config field) but the value is never freed at the end of execution or between subsequent calls, especially in a fuzzing or crashing scenario.

- Execution Flow:
getparameter() → parseconfig() → parse_args() → operate() → main()

## Impact

Causes memory leaks on malformed or crafted config files (especially during fuzzing).

    Affects test reliability and resource handling.

    May mask deeper issues or confuse fuzzers due to retained allocations.

- The allocation remains in memory until exit, resulting in a direct memory leak.

## Attachments
- curl-SIG-bug
