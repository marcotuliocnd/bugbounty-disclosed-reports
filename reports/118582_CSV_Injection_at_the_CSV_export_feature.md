# CSV Injection at the CSV export feature

## Report Details
- **Report ID**: 118582
- **URL**: https://hackerone.com/reports/118582
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-02-24T20:06:33.317Z
- **Disclosed**: 2019-04-08T19:03:12.316Z

## Reporter
- **Username**: niemand_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi there, I have find a way to bypass the mitigation done in [#72785](https://hackerone.com/reports/72785) and [#111192](https://hackerone.com/reports/111192).


What happens if an attacker creates a Ticket with the Tittle `":";-3+3+cmd|' /C calc'!D2`. The ; will break the field making excel think that there are two fields. Although, you are using "" to encapsulate a field and , to separate them, its possible to break one field in two.

Normal case:
`118470,333333,open,new,Denial of Service,2016-02-24 17:43:52 UTC,,,,,,perra,,no,,`

Case where the field is splitted:
`118555,"'"":"";-3+3+cmd|' /C calc'!D2",open,new,"Design Issue,Missing Best Practice",2016-02-24 19:31:14 UTC,,,,,,perra,,no,,`

Once the CSV is create excel will ignore the " and split the field into two by taking into account the ;.

I have tried in:

* Excel Office 2013 on W8.1
* Excel Office 2016 on windows 10
In all cases the code got executed. 


I attach one picture with the executed code.

To Reproduce the issue:

1- Create a Ticket with the following name `":";-3+3+cmd|' /C calc'!D2`. 
2- Export it to CSV
3- Open the CSV. Check attached picture to see the executed code.


If you have further question do not hesitate to ask me.

Best,
███████


## Attachments
- alert.png
