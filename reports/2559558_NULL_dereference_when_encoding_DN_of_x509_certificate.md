# NULL dereference when encoding DN of x509 certificate

## Report Details
- **Report ID**: 2559558
- **URL**: https://hackerone.com/reports/2559558
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-19T00:38:04.026Z
- **Disclosed**: 2024-06-19T12:03:07.768Z

## Reporter
- **Username**: z2_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
libcurl at commit [04739054cdac5a0614fb94e3655e313c03399f35](https://github.com/curl/curl/tree/04739054cdac5a0614fb94e3655e313c03399f35) contains a NULL-dereference in function `encodeDN()` when parsing the certificate of a server during the TLS connect-phase.

The vulnerable code is in [lib/vtls/x509asn1.c:701](https://github.com/curl/curl/blob/04739054cdac5a0614fb94e3655e313c03399f35/lib/vtls/x509asn1.c#L701):
```c
static CURLcode encodeDN(struct dynbuf *store, struct Curl_asn1Element *dn)
{
    struct dynbuf temp;
    Curl_dyn_init(&temp, MAX_X509_STR);
    
    for(p1 = dn->beg; p1 < dn->end;) {
        for(p2 = rdn.beg; p2 < rdn.end;) {
            // --- snip ---
            
            Curl_dyn_reset(&temp);
            result = ASN1tostr(&temp, &oid, 0);
            if(result)
                goto error;

            str = Curl_dyn_ptr(&temp);

            /* Encode delimiter.
                If attribute has a short uppercase name, delimiter is ", ". */
            for(p3 = str; ISUPPER(*p3); p3++)
                ;
        }
    }
}
```

When the `oid` that `ASN1tostr` tries to convert to a string is an element that is constructed such that `oid.constructed` is 1
`ASN1tostr` returns without touching the dynbuf `temp`. The following `Curl_dyn_ptr()` returns NULL and `ISUPPER(*p3)` causes
the application to crash.

# Exploit scenario
The following exploit scenario demonstrates how to terminate an application using libcurl with the NULL dereference from above:

1. Setup a malicious server with a TLS certificate that triggers the crash
2. When a client connects over TLS, send the invalid certificate. This causes the client to terminate and no longer serve its purpose

## Impact

The null dereference causes a DOS on applications using libcurl to do TLS-encrypted connections.
It requires no special setup to trigger the crash, since it is triggered during the connect-phase of the
connection. Thus I chose severity "Low".

## Attachments
No attachments
