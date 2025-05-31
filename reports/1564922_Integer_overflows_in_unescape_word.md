# Integer overflows in unescape_word()

## Report Details
- **Report ID**: 1564922
- **URL**: https://hackerone.com/reports/1564922
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-10T16:10:48.939Z
- **Disclosed**: 2022-06-09T07:10:02.710Z

## Reporter
- **Username**: ddme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
A similiar issue to [CVE-2019-5435](https://hackerone.com/reports/547630)

## Steps To Reproduce:
### analysis
DICT protocol can use one url like "dict://localhost:3306", and  function unescape_word() is used to deal with the character in url like this comment
```c
    /* According to RFC2229 section 2.2, these letters need to be escaped with
       \[letter] */
      if((ch <= 32) || (ch == 127) ||
          (ch == '\'') || (ch == '\"') || (ch == '\\')) {
        dictp[olen++] = '\\';
      }
```

and the bug case here /curl/lib/dict.c

```c
static char *unescape_word(const char *inputbuff)
{
  char *newp = NULL;
  char *dictp;
  size_t len;

  CURLcode result = Curl_urldecode(inputbuff, 0, &newp, &len,          <------------- get len
                                   REJECT_NADA);
  if(!newp || result)
    return NULL;

  dictp = malloc(len*2 + 1);    <------------ overflow here
//.....
}
```

In my analysis(maybe wrong), the `inputbuff` in DICT url is "dict:[inputbuff]", for example "//localhost:3306" in  "dict://localhost:3306", and `len` is the length of `inputbuff`.

And the length of `inputbuff` multiplied by 2 and then passed to malloc. This may lead to a integer overflow on a 32bit OS when the inputbuff is longer than 2GB

`unescape_word` was called by dict_do(), If someone use libcurl to code, and call dict_do() with a extreme long url, it might be triggered.

## Impact

It might leads to a crash or some other impact.

## Attachments
No attachments
