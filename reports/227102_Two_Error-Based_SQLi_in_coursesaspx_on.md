# Two Error-Based SQLi in courses.aspx on ██████████

## Report Details
- **Report ID**: 227102
- **URL**: https://hackerone.com/reports/227102
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-09T06:13:58.202Z
- **Disclosed**: 2019-12-02T18:54:52.174Z

## Reporter
- **Username**: tcpiplab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The server at ████ contains two SQL injection vulnerabilities in the `courses.aspx` file. These are error-based SQLi vulnerabilities. The resulting errors reveal seven lines of C# code, including inline SQL which reveals internal database information. Note that this is one of two reports I'm going to submit for error-based SQLi; I'm grouping them by their vulnerable source code file.

**Description:**
The `crs_id` parameter, when sent with a `GET` to `courses.aspx`, triggers an **Unhandled Exception** if its value is set to either `%0a` or `0`. The vulnerable code is on lines 174 and 177, respectively.

## Impact
1. Leakage of:
   * Database table names and column names.
   * Seven lines of C# code, including inline SQL.
   * Server and framework version information.
1. Unhandled exceptions containing SQL errors are attractive indicators that hackers look for. Even though these vulnerabilities do not allow an attacker to execute arbitrary SQL, the errors do make for a much larger and more promising attack surface. Combining parts of the two error outputs reveals seven lines of C# code, with some inline SQL:
   
   ```c
Line 173:        sqlcrs = CCommonServices.GetCourseSQL(Request.QueryString("crs_id"))
Line 174:        rscrs.open(sqlcrs, connectionString)
Line 175:        sqlCrcf = "SELECT Career_Field.CF_Name FROM Career_CORE_PLUS Join Career_Field on Career_Field.CF_ID = Career_CORE_PLUS.CF_ID join CRS_Detail on CRS_Detail.ID = Career_CORE_PLUS.CRS_ID where Career_CORE_PLUS.CRS_ID =" + Request.QueryString("crs_id")
Line 176:        rsCrcf.Open(sqlCrcf, ConfigurationManager.ConnectionStrings("VbConnect").ToString())
Line 177:        crs = rscrs("crs_header").value
Line 178:        crs_id_print = Request.QueryString("crs_id")
Line 179:        rsData = oCommonServices.getCLPbyCOURSE(Request.QueryString("crs_id"))
```

   The SQL from line 175, revealing the names of tables and columns, is most interesting to an attacker:
   ```sql
   SELECT Career_Field.CF_Name
   FROM Career_CORE_PLUS
   Join Career_Field on Career_Field.CF_ID = Career_CORE_PLUS.CF_ID
   join CRS_Detail on CRS_Detail.ID = Career_CORE_PLUS.CRS_ID
   where Career_CORE_PLUS.CRS_ID =
   ```

## Step-by-step Reproduction Instructions

1. Send a `GET` request to `http://████████/onlinecatalog/courses.aspx?crs_id=%0a`
1. The server returns the following error: `Error converting data type varchar to numeric.` and indicates line 174 of `C:\Web_Data\iCatalog\onlinecatalog\courses.aspx`.
   ██████
1. Send a `GET` request to `http://██████/onlinecatalog/courses.aspx?crs_id=0`
1. The server returns the following error: `Either BOF or EOF is True, or the current record has been deleted. Requested operation requires a current record.` and indicates line 177 of the same file.
   ███

## Product, Version, and Configuration (If applicable)
* Microsoft .NET Framework Version:4.0.30319
* ASP.NET Version:4.6.1590.0 
* IIS 7.5

## Suggested Mitigation/Remediation Actions
1. Add code to validate that the value of the `crs_id` parameter is an integer.
1. Add code to return a `404` error page if the value of the `crs_id` parameter does not reference a valid object. Alternatively, you could set a default value to that of a known-good object reference.
1. Add code to return something other than the familiar `Invalid name parameter` error when the `crs_id` parameter is set to an invalid character. E.g., setting the value to `ä`:

   `http://██████████/onlinecatalog/courses.aspx?crs_id=%C3%A4`

Returns this terse error:
```
Invalid name parameterä
```
Although seemingly a less sensitive error message, I found this behavior useful. It gave me a fourth option when distinguishing between various behaviors based on my fuzzing of the aforementioned parameter:
* `200/OK` and a proper page render when the parameter is set to a valid value.
* TCP reset sent when the web application firewall (WAF) blocks a known-malicious value like `ORDER BY`.
* Unhandled exceptions by the application code (as shown above).
* Invalid input caught and appended to the `Invalid name parameter` message.

My recommendations, generally, are that you modify the source code of the `courses.aspx` file so that you can eliminate these latter two behaviors.

Please let me know if you have any questions.

## Attachments
No attachments
