# The react-marked-markdown module allows XSS injection in href values.

## Report Details
- **Report ID**: 344069
- **URL**: https://hackerone.com/reports/344069
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-27T19:35:19.912Z
- **Disclosed**: 2018-05-13T17:11:10.683Z

## Reporter
- **Username**: ronperris
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report XSS in react-marked-markdown.
The react-marked-markdown module incorrectly sanitizes href values and allows arbitrary code injection (XSS) via user provided Markdown.

# Module

**module name:** react-marked-markdown
**version:** 1.4.6
**npm page:** `https://www.npmjs.com/package/1.4.6`

## Module Description

A react components package that helps you use Markdown easily.

## Module Stats

> Replace stats below with numbers from npm’s module page:

133 downloads in the last day
935 downloads in the last week
4207 downloads in the last month

# Vulnerability

## Vulnerability Description

The React component created with react-marked-markdown contains XSS in link values even when the sanitize option is set to true.

The react-marked-markdown module uses marked.Render() but overwrites the link method with a custom version that doesn't correctly escape values passed to the href prop of anchor components.

## Steps To Reproduce:

import React from 'react'
import ReactDOM from 'react-dom'
import { MarkdownPreview } from 'react-marked-markdown'

ReactDOM.render(
  <MarkdownPreview
    markedOptions={{ sanitize: true }}
    value={'[XSS](javascript: alert`1`)'}
  />,
  document.getElementById('root')
)

## Patch

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- macOS 10.13
- Node.js 8.11.1
- npm 6.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: Y 
- I opened an issue in the related repository: Y 

https://github.com/Vincent-P/react-marked-markdown/issues/61

## Impact

The software does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users. This allows attackes to add malicious scripts to the page via Markdown.

## Attachments
No attachments
