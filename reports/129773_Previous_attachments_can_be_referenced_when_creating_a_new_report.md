# Previous attachments can be referenced when creating a new report

## Report Details
- **Report ID**: 129773
- **URL**: https://hackerone.com/reports/129773
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-04-11T08:00:54.434Z
- **Disclosed**: 2019-04-12T16:21:26.587Z

## Reporter
- **Username**: kusl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello
When user upload file in comment to report, user can find file ID by two ways:
1. In preview mode - In response to POST method `https://hackerone.com/attachments` , answer will be something like this:
-`{"id":84577,"name":"mytestfile.png","size":32397}` where file_ID = 84577 (for example)
2. If user post comment - At link to hackerone-attachments.s3.amazonaws.com, where file_ID is part of the link 
.../production/000/084/579/2b912875c3e8856c300dad535b732500f3c42c25/...
In this case file_ID = 84579

When user post new report to some company on page:
https://hackerone.com/[some_company]/reports/new
in this page user's draft autosave by POST request:
https://hackerone.com/security/reports/draft_sync

So if user post comment to report_1 and get file_ID_1, then he go to post new report to another company
and generate autosave POST request by himself and change file_ID_new_report to  file_ID_1
For example:
`report%5Btitle%5D=&report%5Bvulnerability_information%5D=Ffile_ID_1&report%5Battachment_ids%5D%5B%5D= file_ID_1&report%5Bforce%5D=false`
And, as you can see, set in param `vulnerability_information` Ffile_ID_1 (for example F84577)

Then user reload page with new report (F5), there two issues:
1. After Markdown parse he have direct link to file in comment (in our case file_ID_1 ): where comment to another report and another company.
I think it's not so critical, but same experiment with file, which uploaded directly in initial report_1, is fail.
2. More Strange - file_1 in comment to report_1 is deleted! No more link to file in this comment.

My same experiment with file uploaded by another user (I make test account : @dkusliy_test) also is fail.
Luckily)) 

Thanks and Best!

## Attachments
No attachments
