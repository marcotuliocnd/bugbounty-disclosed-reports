# User object in GraphQL exposes number of trial reports for External Programs that also have a Private Program

## Report Details
- **Report ID**: 350964
- **URL**: https://hackerone.com/reports/350964
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-05-12T19:42:58.521Z
- **Disclosed**: 2018-06-27T03:31:46.792Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

For this vulnerability to work, it is necessary that you should be Admin/member of atleast one sandbox team and running a GraphQL node can tell you if the external programs exist on directory page running a private program on hackerone or not

`https://hackerone.com/directory?query=type%3Aexternal&sort=name%3Aascending&page=1`


**Description:**

 By running a below graphQL, it is possible to know wether external program running a private program or not

```
{"query":"query Report_submission_page{\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  me {\n    username,\n    _remaining_reports3zrc4S:remaining_reports(team_handle:\"█████\")\n  },\n  id\n}","variables":{"first_0":100}}
```

And the response will be 

```
{"data":{"query":{"id":"Z2lkOi8vaGFja2Vyb25lL09iamVjdHM6OlF1ZXJ5L3N0YXRpYw==","me":{"username":"acc1","_remaining_reports3zrc4S":1}}}}
```


As you can see in response, `"_remaining_reports3zrc4S":1`

The response is always `1` for external programs if private program exist or else, it will be `null`

For eg i have verified that following program are running private program and i am getting response as 1

███████
██████████
████
██████

Where as following program gives me null

██████
███████
██████
████

Also, for some public programs like `Security` , i get `5` . I am not sure what this remaining report is about but it atleast helps you tell that if external program exist on h1 or not 


### Steps To Reproduce

1.  Register any sandbox program
2. Run above graphQL query
3.  If you get `"_remaining_reports3zrc4S":1`  in response, that means external program is running private program on hackerone
4. If you get `"_remaining_reports3zrc4S":null` , that means it doesn't exist on hackerone!


Regards,
Ashish

## Impact

Know wether external programs running private programs on hackerone or not

## Attachments
No attachments
