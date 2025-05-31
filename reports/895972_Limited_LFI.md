# Limited LFI

## Report Details
- **Report ID**: 895972
- **URL**: https://hackerone.com/reports/895972
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-11T10:43:44.905Z
- **Disclosed**: 2020-07-09T01:13:41.082Z

## Reporter
- **Username**: mariuszdeepsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
## Summary:
Due to improper parameter sensitization  local file inclusion is possible. LFI is limited as we were not able to truncate the end of string.

## Description:
Application root is located at 
/var/www/dashboard/new/public

Due to URL Manipulation we are able to raed file from 
/var/www/dashboard/new/
Which should not be allowed.

Below we present function Index in Docs class -> parameter $page is set in URL  in below example "..%2fREADME" 
Path is constructed as follow $docs_path = $docs_path . $page . '.md'; then file is read in file_get_contents and returned in application GUI.
LFI is limited due to  " . '.md';" part, but may be bypassed in futures, we have not found a way to bypass it thats why the risk was set to low. In case of bugs combination , PHP bugs etc.. in future this may be escalated. User should  not control any part of "file_get_contents" function
```
 public function index($page = 'main')
    {

        $data = array();

        $docs_path = ($this->config->item('docs_path')) ? $this->config->item('docs_path') : 'https://raw.githubusercontent.com/GSA/project-open-data-dashboard/master/documentation/';
        $docs_path = $docs_path . $page . '.md';
        $docs = @file_get_contents($docs_path);
```

## Steps To Reproduce:
1. Read file from main root by calling URL:
https://labs.data.gov/dashboard/Docs/index/..%2fREADME

## POC

File README.md not exists in our current dir.
F863983

File README.md can be read due to LFI
https://labs.data.gov/dashboard/Docs/index/..%2fREADME
F863984

Confirmation:
File exact as:
https://github.com/GSA/project-open-data-dashboard/blob/master/README.md

## Impact

User have ability to control part of @file_get_contents function. This type of usage may lead to critical file read. In this scenario, we did not bypass the hardcoded ext so files was limited to ".md" and low risk was set.  This should be corrected in case of future PHP bugs, if attacker will truncate the .ext part any file read will be allowed.

## Attachments
- Zrzut_ekranu_2020-06-11_o_12.36.29.png
- Zrzut_ekranu_2020-06-11_o_12.37.51.png
