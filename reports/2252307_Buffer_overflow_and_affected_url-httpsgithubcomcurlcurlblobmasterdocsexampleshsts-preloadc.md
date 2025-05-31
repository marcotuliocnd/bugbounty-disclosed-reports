# Buffer overflow and affected url:-https://github.com/curl/curl/blob/master/docs/examples/hsts-preload.c

## Report Details
- **Report ID**: 2252307
- **URL**: https://hackerone.com/reports/2252307
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-11-15T01:23:19.099Z
- **Disclosed**: 2023-11-15T10:10:19.471Z

## Reporter
- **Username**: cyberguardianrd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
A buffer overflow, also known as a buffer overrun, occurs when a program or process attempts to write more data to a buffer than the buffer is allocated to hold. This can happen if the program does not properly check the length of the data before writing it to the buffer, or if the program allocates too little space for the buffer.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1. The hstsread function in the provided code does not properly check the length of the host string before copying it into the e->name buffer. This could lead to a buffer overflow, allowing an attacker to inject arbitrary code into the application.this could exploited by a malicious domain or website whose url should be long enough to overflow buffer as it's using strcpy function 
Condition a malicious preload host is required to exploit this if it's meet government can use it for zero click attack

Recommendation:

The hstsread function should be modified to check the length of the host string before copying it into the e->name buffer. If the string is too long, the function should return an error code

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

Affected url:-https://github.com/curl/curl/blob/master/docs/examples/hsts-preload.c
Here is the vulnerable code if attacker or government manipulate developer to add a very long domain name in  hsts_preload then this will result remote code execution 



#include <stdio.h>
#include <string.h>
#include <curl/curl.h>

struct entry {
  const char *name;
  const char *exp;
};

static const struct entry preload_hosts[] = {
  { "example.com", "20370320 01:02:03" },
  { "curl.se",     "20370320 03:02:01" },
  { NULL, NULL } /* end of list marker */
};

struct state {
  int index;
};

/* "read" is from the point of the library, it wants data from us. One domain
   entry per invoke. */
static CURLSTScode hstsread(CURL *easy, struct curl_hstsentry *e,
                            void *userp)
{
  const char *host;
  const char *expire;
  struct state *s = (struct state *)userp;
  (void)easy;
  host = preload_hosts[s->index].name;
  expire = preload_hosts[s->index++].exp;

  if(host && (strlen(host) < e->namelen)) {
    strcpy(e->name, host);
    e->includeSubDomains = 0;
    strcpy(e->expire, expire);
    fprintf(stderr, "HSTS preload '%s' until '%s'\n", host, expire);
  }
  else
    return CURLSTS_DONE;
  return CURLSTS_OK;
}

static CURLSTScode hstswrite(CURL *easy, struct curl_hstsentry *e,
                             struct curl_index *i, void *userp)
{
  (void)easy;
  (void)userp; /* we have no custom input */
  printf("[%u/%u] %s %s\n", (unsigned int)i->index, (unsigned int)i->total,
         e->name, e->expire);
  return CURLSTS_OK;
}

int main(void)
{
  CURL *curl;
  CURLcode res;

  curl = curl_easy_init();
  if(curl) {
    struct state st = {0};

    /* enable HSTS for this handle */
    curl_easy_setopt(curl, CURLOPT_HSTS_CTRL, (long)CURLHSTS_ENABLE);

    /* function to call at first to populate the cache before the transfer */
    curl_easy_setopt(curl, CURLOPT_HSTSREADFUNCTION, hstsread);
    curl_easy_setopt(curl, CURLOPT_HSTSREADDATA, &st);

    /* function to call after transfer to store the new state of the HSTS
       cache */
    curl_easy_setopt(curl, CURLOPT_HSTSWRITEFUNCTION, hstswrite);
    curl_easy_setopt(curl, CURLOPT_HSTSWRITEDATA, NULL);

    /* use the domain with HTTP but due to the preload, it should do the
       transfer using HTTPS */
    curl_easy_setopt(curl, CURLOPT_URL, "http://curl.se");

    curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);

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

## Impact

An attacker could exploit this vulnerability to inject arbitrary code into the application. This could allow the attacker to take control of the application and perform actions on behalf of the user.

## Attachments
No attachments
