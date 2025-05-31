# [glance] Access unlisted internal files/folders revealing sensitive information

## Report Details
- **Report ID**: 490379
- **URL**: https://hackerone.com/reports/490379
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-02T15:32:02.524Z
- **Disclosed**: 2019-02-28T19:25:51.550Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report sensitive information disclosure in `glance`.
Similar to #486933 in ways

# Module

**module name:** glance
**version:** 3.0.5
**npm page:** `https://www.npmjs.com/package/glance`

## Module Description

a quick disposable http server for static files

## Module Stats

**weekly downloads**
41

# Vulnerability

## Vulnerability Description

The `glance` modules allows directory browsing and to serve static files through the browser.
The config option `nodot` can be used to prevent serving sensitive folders such as `.git` or `.DS_Store` 
refer: https://github.com/jarofghosts/glance#command-line-options
This rule can be bypassed using the technique below which can lead to sensitive information disclosure (An interesting example: https://smitka.me/).

## Steps To Reproduce:

- Install `glance`
```
$ npm install -g glance
```

- Inside a project directory, initialise `git`.
```
$ git init
```

- Add rule to ignore dotfiles in `.glance.json`
```json
{
  "nodot": true
}
```

- Start `glance` in current directory.
```
$ glance --verbose
glance serving /project/directory on port 8080
```

- Now, current directory will be served by serve with the exception of folder `.git` and file `.gitignore`.
- If we try to curl .`git` or `.gitignore` we get a Not Found error
```
$ curl --path-as-is 127.0.0.1:8080/.git
...
<title>File Not Found</title>
...
```

- Although if we try to fetch files/folders inside a forbidden [dot]folder there is no problem at all and most of it's content can be extracted successfully  (except dotfiles itself).
```
$ curl --path-as-is 127.0.0.1:8080/.git/HEAD      
ref: refs/heads/master
```

>The structure of git repository is well known, so it is possible to found references to the objects/packs in the repository, download them via direct requests and reconstruct the repository and obtain your files – not only the current ones, but also the past files. 

## Supporting Material/References:

- Ubuntu 16.04
- node v11.3.0
- npm 6.7.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N]
- I opened an issue in the related repository: [N] 

>Hunter's comments and funny memes goes here

{F416786}

## Impact

The essentially bypasses the `nodot` feature and allows an attacker to read from a directory that the victim has not allowed access to.

References:
- https://github.com/jarofghosts/glance#command-line-options
- https://smitka.me/

## Attachments
- meme.png
