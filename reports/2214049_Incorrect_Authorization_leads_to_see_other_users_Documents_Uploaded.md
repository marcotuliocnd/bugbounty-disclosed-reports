# Incorrect Authorization leads to see other users Documents Uploaded

## Report Details
- **Report ID**: 2214049
- **URL**: https://hackerone.com/reports/2214049
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-18T09:24:45.156Z
- **Disclosed**: 2023-11-30T15:45:03.044Z

## Reporter
- **Username**: mohs3n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
## Summary:
Hi team,
when user upload document, other user can see this docs only with link

## Steps To Reproduce:
1. loign to portal with user A : https://qcn.mytva.com
2. go to admin section and upload a document.
{F2782891}

3. click on link to see uploaded image. [like](https://qcn.mytva.com/Admin/FileHandler?ENC=RUFBQUFITmtabk00TjJGa1ptRTVNV0Z6TW5JMHV0S2hNTHNYR1J1SDNMMFBqeElLajlTNGNjTHcxVUhqcHhuL1R1cUxyVkxoS0RSRUFqUjRDTlFEd2E4S1diUkNYMlhGNFdSTDRrdE1yUUgvNkVhYWtUR251RjVYc1V6RDdwZkZXdTlCV0tZY2JmWGlVSkNjcHEyK0VvQU1Fc2R2RklDQW1MM25kNEZMTStxMTlhRnBrdStuOGs4N3lTU1Q1R2FsQ1ZrTHhnPT0)

{F2782892}

4. login to portal with user B
5. go to above url, we can see and download user A document.

{F2782896}

## Impact

any login user can see other user documents

## Attachments
- Screenshot_from_2023-10-18_12-49-20.png
- Screenshot_from_2023-10-18_12-50-36.png
- Screenshot_from_2023-10-18_12-52-38.png
