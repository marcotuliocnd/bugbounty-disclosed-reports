# Incorrect IPv6 literal parsing leads to validated connection to unexpected https server.

## Report Details
- **Report ID**: 688048
- **URL**: https://hackerone.com/reports/688048
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-04T18:47:19.056Z
- **Disclosed**: 2021-01-12T13:11:23.513Z

## Reporter
- **Username**: thomas_v
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
The IPv6 ip address can be specified with square brackets like [fe80::3]. There can also be a zone id specified like [fe80::3%15]. A URL can specify its hostname with IPv6 literal,

It seems that the parsing in curl library is not complete. For instance, it is possible for particular IPv6 literals to trigger an http or https request on rather unexpected hostname.

See for instance the potentially misleading hostname:
`https://[ab.be%google.com]/query`

When used with the available online sample program 'simple.c', there is no error. The https request is performed on the Belgian website 'https://ab.be' and the SSL certificate is properly validated against 'ab.be', not 'google.com'.

## Steps To Reproduce:

  1. Build attached modified `simple.c`
  2. `gcc simple.c && ./a.out https://[ab.be%google.com]/query`
  3. Check with Wireshark actual DNS / IP traffic, actually is https and corresponds to 'ab.be'

- The command line 'curl' binary itself is performing sanities so the url above is rejected.
- The 'Host:' header field happens to contain square brackets. An attacker would have an http server handling that detail. Currently 'ab.be' responds with error 400 bad request.

## Supporting Material/References:
`simple.c`
```c
#include <stdio.h>
#include <curl/curl.h>
 
int main(int argc, char*argv[])
{
  CURL *curl;
  CURLcode res;
 
  curl = curl_easy_init();
  if(curl) {
    curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
    /* example.com is redirected, so we tell libcurl to follow redirection */ 
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
 
    /* Perform the request, res will get the return code */ 
    res = curl_easy_perform(curl);
    /* Check for errors */ 
    if(res != CURLE_OK)
      fprintf(stderr, "curl_easy_perform() failed: %s\n",
              curl_easy_strerror(res));
 
    /* always cleanup */ 
    curl_easy_cleanup(curl);
  }  
  return 0; 
}
```

## Impact

User might get confused and connect on the wrong hostname.

## Attachments
No attachments
