# Information Disclosure .htaccess accesible for public

## Report Details
- **Report ID**: 1241849
- **URL**: https://hackerone.com/reports/1241849
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-23T10:18:26.191Z
- **Disclosed**: 2021-07-18T14:00:57.599Z

## Reporter
- **Username**: aloneh1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Hello team!
While doing a preliminary recon on the sub domain of  "launchpad.37signals.com"  I've come across a few sensitive files that should not be facing the public web; I'll leave you a list organized by criticality and some proof.

Information disclosure of path .htaccess on the subdomain of https://launchpad.37signals.com/

POC url : https://_domainkey.launchpad.37signals.com/.htaccess

Medium priority
.htaccess file for https://_domainkey.launchpad.37signals.com 

Options +ExecCGI +MultiViews +FollowSymLinks
AddHandler cgi-script .cgi
php_value include_path "include:../include"
RewriteEngine on
RewriteCond sprockets.js !-f
RewriteRule ^sprockets\.js /nph-sprockets.cgi [P,L]

# Uncomment the next line to enable Sprockets caching
# SetEnv sprockets_generate_output_file true

step to reproduce :

go to the url :https://_domainkey.launchpad.37signals.com/
after add .htacces to the endpoint of url 

like https://_domainkey.launchpad.37signals.com/.htaccess


the page says download the content of .htaccess as a popup.

## Impact

The publicly accessible .htaccess  might be serious as long as those credentials are really being used somewhere (and it seems to me the DBMS isn't facing the public internet anyway). The real impact is that finding such files always grabs the attention of a threat actor, which might give up not so easily influenced by the fact that there might be "more".

## Attachments
- Screenshot_from_2021-06-23_15-45-21.png
- Screenshot_from_2021-06-23_15-45-55.png
