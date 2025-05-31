# Stored XSS in Headline TextControl element in Express forms [ concrete5 8.1.0 ]

## Report Details
- **Report ID**: 230278
- **URL**: https://hackerone.com/reports/230278
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-20T17:20:31.913Z
- **Disclosed**: 2017-07-14T06:49:11.977Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
## Intro

Luke, I am your Crayons!


__Type of issue__: Core CMS issue
__Level of severity__: Internal Attack Vector
__Concrete5 version__: 8.1.0

## Summary

There is Stored XSS vulnerability in __Headline__ element of __TextControl__ Express element. This vulnerability allows malicious user to embed JavaScript code and execute it in the website.
Sample concrete5 installation contains *Contact* page, where contact form is present. I present PoC of this vulnerability on this page.

## Steps to reproduce

#### Injection

- login into concrete5 instance
- go to index.php/dashboard/system/express/entities, then select Contact form

{F186592}

- select Forms, then Form from the left

{F186591}

- in (Text) Core Property click Edit (a pen) icon
- in dialog popup, enter following payload in __Headline__ text input:

```
<p>These are not the payloads you're looking for... </p><script>console.error('Stored XSS, browser:', navigator.appVersion)</script>
```

- save changes

#### Execution

Go to website and visit __Contact__ page. JavaScript payload is executed without any user interaction. WebKit/Blink-based browsers XSS Auditor is not able to detect and prevents this attack (in general, XSS Auditor fails against Stored XSS)

{F186593}



## Technical details

Vulnerability exists, because ```GetControlLabel()``` method from ```TextControl``` class returns ```Headline``` value without any sanitization (line 75, concrete/src/Entity/Express/Control/TextControl.php):

```php
public function getControlLabel()
    {
        if ($this->getHeadline()) {
            $label = $this->getHeadline();              // line 75
        } else if ($this->getBody()) {
            $text = \Core::make('helper/text');
            $label = $text->sanitize($this->getBody(), 32);
        }

        $label .= ' ' . t('(Text)');
        return $label;
    }
```


## Impact

This vulnerability gives malicious user a possibility to inject JavaScript and executes client side attack against any user which visits Contact page (or any other page where form with __TextControl__ element is present).

> Internal Attack Vector - A bug that requires someone already have some type of administrative access to the CMS. This might just change the experience of the CMS, or __be part of a more complicated attack that might hypothetically gain more access than they should have__. These are considered important to clean up over time.


## Testing environment

System:

- Concrete5 version 8.1.0, installed localy
- PHP ver. 5.6.30
- Apache HTTP Server 2.4.25 for macOS
- MySQL ver. 5.7.13 for macOS

This vulnerability was tested on macOS Sierra 10.12.5 with following browsers:

- Chrome 58
- Chromium build 60.0.3104.0
- Safari 10.1.1


## Wrap up

I hope my report will help keep Concrete5 safe in the future.

Best Regards,

Rafal 'bl4de' Janicki

## Attachments
- tc2.png
- tc1.png
- tc3.png
