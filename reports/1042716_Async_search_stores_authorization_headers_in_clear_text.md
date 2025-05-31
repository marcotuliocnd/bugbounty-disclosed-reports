# Async search stores authorization headers in clear text

## Report Details
- **Report ID**: 1042716
- **URL**: https://hackerone.com/reports/1042716
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-24T21:45:59.222Z
- **Disclosed**: 2021-01-19T20:25:14.963Z

## Reporter
- **Username**: alexbrasetvik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:** The `.async-search` index stores the results of async searches. It also stores a copy of the requests authorization headers, in clear text. These clear text authorization headers are then available to anyone with access to `.async-search`, probably mostly super users.

**Description:**

While you have to be a superuser to read this index, there's potential for lateral movement or impersonating other users if credentials are re-used, which would be the case if e.g. LDAP or Active Directory integrations are used.

Kibana is understandably eager in its use of async-search. The default `waitForCompletionTimeout` is 100ms, so if you want to get the password of someone else on your cluster, then it's probably already there if they use Kibana. If not, send them a link to a Kibana dashboard that trigger searches that take longer than 100ms.

I first noticed this on a recent 8.0.0-snapshot, but 7.10.0 is the latest release containing it.

## Steps To Reproduce:

```
# This just triggers an async-search as yourself.
POST /_async_search?size=0&wait_for_completion_timeout=0
{
  "query": {
    "match_all": {}
  }
}

# This shows where the clear text authorization header is stored
POST /.async-search/_search
{
  "_source": "headers.*"
}
```

## Supporting Material/References:

 * Video walkthrough

## Impact

- Super users can get the clear text credentials of other users.
- An XSS with a superuser victim can now trivially get the authorization headers of its target.

## Attachments
No attachments
