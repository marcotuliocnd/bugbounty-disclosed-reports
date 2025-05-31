# Information Disclosure

## Report Details
- **Report ID**: 143064
- **URL**: https://hackerone.com/reports/143064
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-04T14:00:12.596Z
- **Disclosed**: 2016-07-31T07:58:12.924Z

## Reporter
- **Username**: mugeesahmed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
Hey, 

I found Following Security issue on your site.

Information Disclosure :-

your Wordpress installation in Disclosing its version Number in https://drchrono.com/blog/readme.html 
This can a hacker in speeding up the process or information gathering though discovering your wordpress version number a attacker could use specific exploits made just for your version.

Missing Best Practice :- 

There are Two outdated plugins in your Wordpress site

                 1.  Wordpress-importer
                  2.  Wufoo-shortcode

This could Serve as a Potential Thread to your site because outdated plugins are often Vulnerable to attacks 
and could also be vulnerable to 0days 

The Website Plugins Should be update regularly to prevent your site from getting attacked.

Prove of Concept :-

https://drchrono.com/blog/wp-content/plugins/wufoo-shortcode/readme.txt
https://drchrono.com/blog/wp-content/plugins/wordpress-importer/readme.txt



## Attachments
- readme.png
