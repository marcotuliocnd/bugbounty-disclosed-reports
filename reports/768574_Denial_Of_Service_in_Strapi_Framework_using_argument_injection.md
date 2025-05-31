# Denial Of Service in Strapi Framework using argument injection

## Report Details
- **Report ID**: 768574
- **URL**: https://hackerone.com/reports/768574
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-05T21:45:31.668Z
- **Disclosed**: 2020-01-28T20:10:50.459Z

## Reporter
- **Username**: princechaddha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Denial Of Service in Strapi Framework.It allows attacker to force restart the server using argument injection.

# Module

**module name:** strapi
**version:** 3.0.0-beta.18.3 and earlier
**npm page:** `https://www.npmjs.com/package/strapi`

## Module Description

> The Strapi HTTP layer sits on top of Koa. Its ensemble of small modules work together to provide simplicity, maintainability, and structural conventions to Node.js applications.

## Module Stats

[1] weekly downloads 8,508

# Vulnerability

## Vulnerability Description

>  While reviewing source code i found that "installPlugin" and "uninstallPlugin" handler functions for the admin panel (https://github.com/strapi/strapi/blob/master/packages/strapi-admin/controllers/Admin.js) is using regex on line 70 & 110 i.e `/^[A-Za-z0-9_-]+$/` before passing user input to `execa()` on line 77 & 117 to prevent command injection but the regex allows `-` character.Using this attacker can pass valid arguments like "-h" "-v" "--help" which will add after the command `npm run strapi -- install <user-input>` & `npm run strapi -- uninstall <user-input>` and leads the serve to restart.

## Steps To Reproduce:

> Create a new strapi project and start the server by using yarn.
> Login to admin panel by visiting http://172.16.129.155:1337/admin/
> Goto http://172.16.129.155:1337/admin/marketplace & click on download while intercepting the request.
> Change value of plugin to "-h",  "--help", "-v" or "--version"
> Check console the server will restart everytime we send the request using valid strapi arguments. 

## Patch

> Instead of `strapi.reload();` after executing the command there should be a check to validate if a valid plugin is installed or uninstalled.Many user uses `_` & `-` in plugin names so blacklisting the above 4 inputs will fix this issue instead of removing `_` & `-` from the regex

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] N
- I opened an issue in the related repository: [Y/N] N


#####Also, It looks like an intented behaviour to restart server after uninstalling or installing a valid plugin but by just passing the valid arguments we can restart the server.

## Impact

Attacker can cause the server to restart even without installing or uninstalling a valid plugin.

## Attachments
No attachments
