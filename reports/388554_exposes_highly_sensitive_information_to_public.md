# ████ █████ exposes highly sensitive information to public

## Report Details
- **Report ID**: 388554
- **URL**: https://hackerone.com/reports/388554
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-07-30T17:57:24.019Z
- **Disclosed**: 2020-05-11T16:43:33.681Z

## Reporter
- **Username**: cablej_dds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

www.██████ is a system used by ██████ for vendors to upload details of their technology for review by ███. Due to an insecure direct object reference vulnerability, all vendor uploads are accessible to the public, without authentication. This includes `Unclass//FOUO` documents, documents labeled `ITAR RESTRICTED / EXPORT CONTROLLED DATA`, and confidential / proprietary data of the respective vendors. These documents include detailed specifications on military technology, including weapons systems, surveillance systems, missiles and ballistics, and other confidential technology.

For instance, several documents contained had labeled criminal penalties for foreign export:

```
WARNING – This document contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C., Sec 2751 et seq.) or the Export Administration Act of 1979, (Title 50, U.S.C., App. 2401 et seq.), as amended. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.
```

Although I did not identify any classified documents, there is a possibility that classified information is also uploaded here.

## Step-by-step Reproduction Instructions

1. Visit `https://www.███/api/document/x`, replacing `x` with any numerical ID. These go into the low tens of thousands.
2. Observe that the document will be downloaded, provided it exists.
3. Observe that this can be repeated for tens of thousands of documents.

Some screenshots of evidence of sensitive information attached.

## Impact

This exposes highly sensitive information of both the DoD (ITAR restricted) and proprietary/confidential company information.

## Attachments
No attachments
