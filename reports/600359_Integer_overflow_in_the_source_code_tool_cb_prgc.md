# Integer overflow in the source code tool_cb_prg.c

## Report Details
- **Report ID**: 600359
- **URL**: https://hackerone.com/reports/600359
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-06-05T13:22:01.791Z
- **Disclosed**: 2021-02-08T07:52:50.813Z

## Reporter
- **Username**: sfpskywood
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Integer overflow in the source code tool_cb_prg.c

## Steps To Reproduce:

Review the source code of tool_cb_prg.c
In the function fly, pay attention to Line 80, 82, 84

```C
69 static void fly(struct ProgressData *bar, bool moved)
70 {
71   char buf[256];
72   int pos;
73   int check = bar->width - 2;
74 
75   msnprintf(buf, sizeof(buf), "%*s\r", bar->width-1, " ");
76   memcpy(&buf[bar->bar], "-=O=-", 5);
77
78  pos = sinus[bar->tick%200] / (10000 / check);
79  buf[pos] = '#';
80  pos = sinus[(bar->tick + 5)%200] / (10000 / check);
81  buf[pos] = '#';
82  pos = sinus[(bar->tick + 10)%200] / (10000 / check);
83  buf[pos] = '#';
84  pos = sinus[(bar->tick + 15)%200] / (10000 / check);
85  buf[pos] = '#';
```

in Line 80, Line 82, Line 84, there are integer overflow issues.
the type of 'tick' is 'unsigned int'
bar->tick could be a large value, then bar->tick + 5 may revert to a small value.
Here no big impact and only logic error.

I think maybe a logic like this is better to avoid integer overflow.
`pos = sinus[((bar->tick)%200 + 5)%200] / (10000 / check);`

I am not sure if I directly create this issue on github is the correct way, so I report it here.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

The output of the my self-development code scan tool:
[Scanning] /home/a/Data/curl/src/tool_cb_prg.c
Integer Overflow found in file: /home/a/Data/curl/src/tool_cb_prg.c, Line: 80, Column: 28
pos = sinus[(bar->tick + 5)%200] / (10000 / check);
Integer Overflow found in file: /home/a/Data/curl/src/tool_cb_prg.c, Line: 82, Column: 28
pos = sinus[(bar->tick + 10)%200] / (10000 / check);
Integer Overflow found in file: /home/a/Data/curl/src/tool_cb_prg.c, Line: 84, Column: 28
pos = sinus[(bar->tick + 15)%200] / (10000 / check);

## Impact

This integer overflow has no big impact and only may cause business logic error.

## Attachments
No attachments
