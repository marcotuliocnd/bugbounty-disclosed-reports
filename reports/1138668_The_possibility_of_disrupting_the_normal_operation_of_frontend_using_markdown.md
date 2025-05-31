# The possibility of disrupting the normal operation of frontend using markdown

## Report Details
- **Report ID**: 1138668
- **URL**: https://hackerone.com/reports/1138668
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-29T07:00:33.027Z
- **Disclosed**: 2021-08-24T03:19:23.715Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hi team,

Our team noticed that using some string construction in markdown may cause it to fail and output error 502. Thus, disrupting the UI process. This may affect the work in places where there is a GraphQL attribute output.

For example:

* `User` object in GraphQL : `intro_html` attribute
* `Report` object in GraphQL: `vulnerability_information_html` attribute
and other objects with attributes that output this data

We believe that there are two things here, both a partial dos attack and a negative effect in the work. For example, the hackerone_triage team, which checks a lot of reports, will constantly have problems opening the report and will ask the engineering team to change the state of the report to edit the message in markdown. Or you are a collaborator in one of the reports that is being prepared for disclosure. But we are able to respond in such cases. In this way, we can send a message and the report will not be shown, but instead error 502 will be called. Which will also lead to many calls to the support team to resolve these issues

These are just some of the attack vectors, but we believe there could be many more.



## Steps To Reproduce:

```
[[[[[[[[[[[[[[[[][l]][l]][l]][l]][l]`][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]
[l]:ht0tp%3A%2F%2FdwqNo%0A+fg
```

I put this in the code so that my PoC wouldn't work. You just need to paste it just by copying it. To be sure, try inserting it into a report created in the sandbox
 Our team believes that it makes sense to fix this error.

## Impact

* DoS
* Disruption of normal operation

## Attachments
No attachments
