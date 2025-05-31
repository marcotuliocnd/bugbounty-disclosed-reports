# Lack of URL normalization renders Blocked-Previews feature ineffectual

## Report Details
- **Report ID**: 1102764
- **URL**: https://hackerone.com/reports/1102764
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-13T15:32:54.223Z
- **Disclosed**: 2022-01-16T07:48:02.719Z

## Reporter
- **Username**: jub0bs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Slack has a feature known as [_Blocked Previews_][blocked-previews], which allows Workspace Owners and Admins to specify a list of URLs for which no link preview should occur. The point of this feature is to reduce clutter and prevent harmful content from getting embedded in the workspace.

However, when a URL is posted on Slack, the backend evidently doesn't perform any preliminary URL normalization on it. This lack of URL normalization enables easy bypasses of a workspace's list of blocked previews.

(In what follows, I'll use the link `https://jub0bs.com/posts/2021-01-29-great-samesite-confusion/` as an example.)

# Bypassing blocked previews for all links from a domain

If all previews from `jub0bs.com` have been blocked, posting `https://jub0bs.com/posts/2021-01-29-great-samesite-confusion/` (note the trailing period after the host part) will trigger a link preview. Note: posting such a URL to Slack requires an intercepting proxy, such as Burp. Here is a video PoC:

{F1194569}

# Bypassing Blocked Previews for a specific link or all links under a domain subdirectory

If previews for

* specific link `https://jub0bs.com/posts/2021-01-29-great-samesite-confusion/`, or
* all links under `jub0bs.com/posts`

have been blocked, posting a URL of the form `https://jub0bs.com/ARBITRARY_PATH_SEGMENT/../posts/2021-01-29-great-samesite-confusion/` (note the non-normalized path) will trigger a link preview. Here is a video PoC:

{F1194567}

[blocked-previews]: https://slack.com/intl/en-fr/help/articles/360001502048-Manage-link-previews-for-your-workspace

## Impact

Workspace Owners and Admins cannot easily block link previews in a reliable fashion. The trailing-period bypass requires them to duplicate create an additional rule for each blocked domain, and the path-normalization bypass completely defeats the blocking of specific links or all links under a domain subdirectory. As a result, malicious actors are able to get their links to preview in Slack regardless of the workspace's list of blocked previews.

Please note that the "attack" scenario isn't limited to "team member against team member", because links may come from Slack integrations (e.g. with [Microsoft Outlook](https://hackerone.com/redirect?url=https%3A%2F%2Fslackhq.com%2Fincrease-everyday-productivity-with-office-365-apps-for-slack)). In this connection, see report #481472.

## Attachments
- slack_bypassing_blocked_previews_non_normalized_path.mov
- slack_bypassing_blocked_previews_trailing_period.mov
