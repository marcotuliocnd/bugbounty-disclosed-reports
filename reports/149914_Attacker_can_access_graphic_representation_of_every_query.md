# Attacker can access graphic representation of every query

## Report Details
- **Report ID**: 149914
- **URL**: https://hackerone.com/reports/149914
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-08T04:45:38.324Z
- **Disclosed**: 2016-07-27T15:00:23.962Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bime

## Vulnerability Information
# Vulnerability details
On a dashboard, widgets can be added to show a graphic representation of a query. These queries come from datasources. When creating a widget, a query ID is given. This query ID can be changed in order to obtain the results of the dataset through a scheduled email. This leaks (sensitive) information of other customers their dataset.

# Proof of concept
Sign in as a normal user - I used my personal email address on the https://h1-bugbounty.bime.io domain. After creating your first dashboard, a `POST` request is sent to the `/widgets.json` endpoint. It'll look something like this:

```
POST /widgets.json HTTP/1.1
Host: h1-bugbounty.bime.io
...

{"title":"SUM(Dynamic Count) per ID","height":0,"position_x":0,"position_y":0,"width":0,"query_id":1052531,"tab_id":612224,"visualisation_type":"none","configuration":"<Properties><Config name=\"borderColor\" value=\"#787c82\"/><Config name=\"headerBackgroundColor\" value=\"#787c82\"/><Config name=\"headerColor\" value=\"#ffffff\"/><Config name=\"headerFontItalic\" value=\"false\"/><Config name=\"headerFontSize\" value=\"16\"/><Config name=\"headerFontUnderline\" value=\"false\"/><Config name=\"headerFontWeight\" value=\"false\"/><Config name=\"hidden\" value=\"false\"/><Config name=\"hideHeader\" value=\"false\"/><Config name=\"hideLoaders\" value=\"false\"/><Config name=\"hideWindowBorder\" value=\"false\"/><Config name=\"layout\" value=\"vertical\"/><Config name=\"numberOfLineHeader\" value=\"2\"/><Config name=\"position\" value=\"absolute\"/><Config name=\"roundedEdges\" value=\"0\"/><Config name=\"textForTextWidget\" value=\"\"/><Config name=\"textFontSize\" value=\"16\"/><Config name=\"zOrder\" value=\"0\"/></Properties>"}
```

Notice the `query_id` in the request. Change this ID to the query object that you want to see the data of. Now go to the web application and click on Dashboards in the left column. It'll look something like this:

{F103809}

As you can see, there's an empty widget. This is caused by the fact that the user is not authorized to view the data. This is good. I tried exporting the data by clicking the Export button at the bottom. However, this does not leak the data, the images and PDFs I downloaded show up empty. This is also good. But when I scheduled an email reminder for every 5 minutes, and I waited 5 minutes, I received a PDF and image in my inbox that contained the actual data:

{F103811}

It seems that the authorization / authentication is implemented differently when executed asynchronous, which allows an attacker to obtain actual data from other customers' datasources and queries. Let me know if you need more information!

## Attachments
- Screen_Shot_2016-07-07_at_21.41.00.png
- Screen_Shot_2016-07-07_at_21.43.48.png
