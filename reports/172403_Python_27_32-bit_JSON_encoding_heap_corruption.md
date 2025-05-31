# Python 2.7 32-bit JSON encoding heap corruption

## Report Details
- **Report ID**: 172403
- **URL**: https://hackerone.com/reports/172403
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-09-27T13:20:03.357Z
- **Disclosed**: 2019-10-13T13:01:19.623Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.python.org/issue28284
https://hg.python.org/cpython/rev/9375c8834448

Among other things this vulnerability will be triggered when JSON-encoding a dict with a very large key:
```
python -c 'import json; json.dumps({chr(0x22)*0x2AAAAAAB:0})'
```

## Attachments
No attachments
