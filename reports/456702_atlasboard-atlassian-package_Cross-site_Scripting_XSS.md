# [atlasboard-atlassian-package] Cross-site Scripting (XSS)

## Report Details
- **Report ID**: 456702
- **URL**: https://hackerone.com/reports/456702
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-06T01:23:27.941Z
- **Disclosed**: 2020-01-04T22:09:05.070Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report XSS in `atlasboard-atlassian-package`
It allows to inject clientside javascript (or HTML) in cases when attacker has opportunity to create or modify issues on JIRA server (e.g bug tracker) which is configured to work with application from module.

# Module

**module name:** atlasboard-atlassian-package
**version:** 0.0.2
**npm page:** `https://www.npmjs.com/package/atlasboard-atlassian-package`

## Module Description

> this is a package ready to be used with Atlasboard. It contains dashboards, widgets and jobs related to Atlassian products.

## Module Stats

1 downloads in the last day
9 downloads in the last week
20 downloads in the last month

# Vulnerability

## Vulnerability Description

> `atlasboard-atlassian-package` is a collection of widgets for `atlasboard` which is another package and a dashboard framework, 'blockers' widget dedicated to show issues from JIRA with 'Blocked' status (which actually can be used to show any kind of issues because it uses configurable JQL query for requesting data from Jira server) doesn't have proper incoming data sanitization.

## Steps To Reproduce:

First of all it requires `atlasboard` installed
that is why steps a from https://www.npmjs.com/package/atlasboard#installation
install `atlasboard`
```
npm install -g atlasboard
```
create your dashboard
```
atlasboard new mywallboard
```
go to dashboard directory and install `atlasboard-atlassian-package`
```
cd mywallboard/
git init
git submodule add https://bitbucket.org/atlassian/atlasboard-atlassian-package packages/atlassian
```
then configure packages/atlassian/dashboards/example1.json to use Jira server,
```
...
  "config": {
    "confluence-blockers": {
      "timeout": 30000,
      "retryOnErrorTimes": 3,
      "interval": 120000,
      "jira_server": "https://your-jira-portal.atlassian.net",
      "jql": "project = \"YOUR-PROJECT\" ORDER BY priority DESC"
    },
...
```
where `jira_server` - url of your Jira portal
`jql` - query that you want to use for getting jira issues list

then create a ticket in Jira with summary containing payload e.g. ```test<script>alert(1)</script>```
F386186

then start your dashboard
```
atlasboard start
```
or
```
node start.js
```

url `dashboard-server:port/example1` will contain payload
where `dashboard-server` - your server location where you host the dashboard
`port` - port of your server where you host the dashboard
by default it's `localhost:3000`

source:
https://bitbucket.org/atlassian/atlasboard-atlassian-package/src/289092d890fa764983282d92730f4709a2038be5/widgets/blockers/blockers.js?at=master&fileviewer=file-view-default#blockers.js-44

```javascript
var $summary = $("<div/>").addClass("issue-summary").append(blocker.summary).appendTo(listItem);
```
blocker is an issue object recieved from Jira

if an attacker has access for changing issues summary in Jira any kind of markup (HTML / JS) can be injected on the dashboard

## Patch

I suppose it's better to use 'text' instead of 'append' here
```javascript
var $summary = $("<div/>").addClass("issue-summary").text(blocker.summary).appendTo(listItem);
```
## Supporting Material/References:

- Linux Mint current
- Node.js 8.11.1
- NPM 6.4.0

# Wrap up

- I contacted the maintainer to let them know:N
- I opened an issue in the related repository: N

Didn't do a patch myself because I'm not familiar with bitbucket and don't have account there, didn't contacted the maintainer for the same reason.
It's obviously has a low level impact but I guess this is important due to the fact that this package is presented as a good place to start creating your own dashboards for atlasboard  https://www.npmjs.com/package/atlasboard#importing-your-first-package
May be it won't affect somebody directly, but as long as this package is created by well known company (Atlassian) it can be a bad example of how to not sanitize your inputs

## Impact

Cross-site Scripting

## Attachments
- issue-summary.png
