# Leaking Rockset API key on Github

## Report Details
- **Report ID**: 1094151
- **URL**: https://hackerone.com/reports/1094151
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-03T17:54:12.674Z
- **Disclosed**: 2021-03-02T16:02:20.439Z

## Reporter
- **Username**: fonte
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockset

## Vulnerability Information
## Summary:
We all know that Github is great, but it runs the risk of some credentials being revealed by mistake. In this case I found a Rockset API key, This API key is not in the current code, but it is visible in an old commit.

## Steps To Reproduce:
You can find the leak in this link : https://github.com/rockset/recipes/pull/19/files

```
        /* Getting the distance covered by each vehicle using the latest and oldest locations */
        distance_for_vehicles AS (
        SELECT
            ST_DISTANCE(
@@ -128,7 +147,7 @@
    'q4': query4 
}

api_key = "skZMJRZSXLZZj5HAdBjNxUfZbarWV5dLqfVO6U623zW5KROzfY0vNRa22ToZfRRe"
```

Then I visited the documentation of Rockset ( https://docs.rockset.com/rest-api/ ) and I found this way to check if the API key is revoke or not
```
curl --request GET \
    --url https://api.rs2.usw2.rockset.com/v1/orgs/self/users/self/apikeys \
    -H 'Authorization: ApiKey skZMJRZSXLZZj5HAdBjNxUfZbarWV5dLqfVO6U623zW5KROzfY0vNRa22ToZfRRe'
```
and I got this answer:
```
{"data":[{"created_at":"2019-10-22T06:08:37Z","name":"K1","key":"skZMJRZSXLZZj5HAdBjNxUfZbarWV5dLqfVO6U623zW5KROzfY0vNRa22ToZfRRe","last_access_time":null,"created_by":null}]}
```
So I could verify that it was not revoked

## Impact

I just checked that the key was not revoked. I didn't try anything with the token  to be prudent, and I don't know the real impact of this, But I think it is a good idea to share this with you, to avoid any risk that may grow.

Regards!

## Attachments
No attachments
