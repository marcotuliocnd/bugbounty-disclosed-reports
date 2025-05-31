# Use of Unsafe function || Strcpy

## Report Details
- **Report ID**: 1485379
- **URL**: https://hackerone.com/reports/1485379
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-02-18T18:51:47.568Z
- **Disclosed**: 2022-03-09T21:48:14.205Z

## Reporter
- **Username**: shobhit2401200
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
It was observed that application is using strcpy() function which may cause buffer overflow attacks.

#Affected Code
https://github.com/curl/curl

# Affected Lines
1. Line 195 of curl-master\tests\libtest\stub_gssapi.c
2. Line 204,212,216 curl-master\tests\server\socksd.c

## Steps To Reproduce:
Lets first discuss what is the issue with strcpy function. basically it takes 2 arguments 1 dst 2 source. the issue is if the dst size is small and the source size is more without a null terminating value so it will overwrite the memory. so in these case 1 got the several lines about strcpy function. but i'm discussing 1 with you rest with remain the same.

        else if(!strcmp(key, "backend")) {
          strcpy(config.addr, value);

        else if(!strcmp(key, "password")) {
          strcpy(config.password, value);

  char addr[32]; /* backend IPv4 numerical */
  char user[256];
  char password[256];

here it is copying the value into config.addr and the size of addr is 32 and same goes for password is  256. now let suppose the value of value is more than 32 in case of add and in case of password it is more than 256. than it can be buffer overflow attack here. so here it will be secure if you use the functions like snprintf , strlcpy. or dynamically assign the size to the array.

## Supporting Material/References:
https://cwe.mitre.org/data/definitions/676.html
https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/

# Recommendation:
It is recommended to use below mentioned functions to avoid buffer overflow attacks
1. snprintf
2. strlcpy

  * [attachment / reference]
Please find the attached screenshots for your reference.

## Impact

The strcpy() function does not specify the size of the destination array, so buffer overrun is often a risk. Using strcpy() function to copy a large character array into a smaller one is dangerous, but if the string will fit, then it will not be worth the risk. If the destination string is not large enough to store the source string then the behavior of strcpy() is unspecified or undefined.

## Attachments
- Screenshot_(640).png
- Screenshot_(641).png
