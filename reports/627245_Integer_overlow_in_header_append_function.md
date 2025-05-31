# Integer overlow in "header_append" function

## Report Details
- **Report ID**: 627245
- **URL**: https://hackerone.com/reports/627245
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-06-24T13:23:01.226Z
- **Disclosed**: 2021-02-08T07:53:07.503Z

## Reporter
- **Username**: invictus1306
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
The function header_append contains an integer overflow,  it can bypass the check on the length and can lead to a subsequent heap buffer overflow.

## Steps To Reproduce:
I don't have PoC, but here there is a little description of the problem (vulnerable code) 

```
static CURLcode header_append(struct Curl_easy *data,
                              struct SingleRequest *k,
                              size_t length)
{
  size_t newsize = k->hbuflen + length; // <-- here there is the point of the integer overflow (length is user controllable)
// the value of "newsize" will be small and minor than CURL_MAX_HTTP_HEADER
  if(newsize > CURL_MAX_HTTP_HEADER) {
    /* The reason to have a max limit for this is to avoid the risk of a bad
       server feeding libcurl with a never-ending header that will cause
       reallocs infinitely */
    failf(data, "Rejected %zu bytes header (max is %d)!", newsize,
          CURL_MAX_HTTP_HEADER);
    return CURLE_OUT_OF_MEMORY;
  }
...
// here the length is a big number, and it can lead in a heap overflow
  memcpy(k->hbufp, k->str_start, length);
  k->hbufp += length;
  k->hbuflen += length;
  *k->hbufp = 0;

  return CURLE_OK;
}
```

## Additional info
As I mentioned I don't have a PoC, but I saw that this function could be reached in different ways e.g., evil server, by running curl with a specific argument (extend the header size), curl API (but not sure).

## Impact

- It can lead on a RCE

## Attachments
No attachments
