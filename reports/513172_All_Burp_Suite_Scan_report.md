# All Burp Suite Scan report

## Report Details
- **Report ID**: 513172
- **URL**: https://hackerone.com/reports/513172
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-21T14:29:02.220Z
- **Disclosed**: 2019-03-22T14:05:15.675Z

## Reporter
- **Username**: punitcingh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
## Summary:
[1. Detected Deserialization RCE: Jackson
1.1. https://lgtm-com.pentesting.semmle.net/blog/ [lgtm_short_session cookie]
1.2. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getSuggestedProjects [apiVersion parameter]
2. Session token in URL
3. CSP: Inline scripts can be inserted
3.1. https://lgtm-com.pentesting.semmle.net/
3.2. https://lgtm-com.pentesting.semmle.net/admin
3.3. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876)
3.4. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876)%3C/
3.5. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876)%3C/script%3E
3.6. https://lgtm-com.pentesting.semmle.net/blog
3.7. https://lgtm-com.pentesting.semmle.net/blog/
3.8. https://lgtm-com.pentesting.semmle.net/blog/images/
3.9. https://lgtm-com.pentesting.semmle.net/blog/images/announcing_project_badges/
3.10. https://lgtm-com.pentesting.semmle.net/blog/images/bsides_wrap_up/
3.11. https://lgtm-com.pentesting.semmle.net/blog/images/does_review_improve_quality/
3.12. https://lgtm-com.pentesting.semmle.net/blog/images/ghostscript_2018/
3.13. https://lgtm-com.pentesting.semmle.net/blog/images/how_lgtm_builds_cplusplus/
3.14. https://lgtm-com.pentesting.semmle.net/blog/images/introducing_dataflow_path_exploration/
3.15. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getProjectLatestStateStats
4. Vulnerable version of the library 'jquery' found
4.1. https://lgtm-com.pentesting.semmle.net/static/site/scripts/vendor-jquery.41f697b3f15739940f70.js
4.2. https://lgtm-com.pentesting.semmle.net/static/site/scripts/vendor-jquery.41f697b3f15739940f70.js
5. [SSL Scanner] Sweet32
6. Interesting input handling: Magic value: none
7. Strict Transport Security Misconfiguration
8. CSP: Libraries using eval or setTimeout are allow
8.1. https://lgtm-com.pentesting.semmle.net/
8.2. https://lgtm-com.pentesting.semmle.net/admin
8.3. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876)
8.4. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getActivePRIntegrations
8.5. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getAuthenticationProviders
8.6. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getAvailableProjects
8.7. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getBlogPosts
8.8. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getDist
8.9. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getDocumentationArticle
8.10. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getProjectLatestStateStats
8.11. https://lgtm-com.pentesting.semmle.net/tos
9. [Vulners] Vulnerable Software detected
9.1. https://lgtm-com.pentesting.semmle.net/static/site/scripts/vendor-jquery.41f697b3f15739940f70.js
9.2. https://lgtm-com.pentesting.semmle.net/static/site/scripts/vendor-jquery.41f697b3f15739940f70.js
10. Detected Deserialization RCE: JSON-IO
11. Interesting input handling: Magic value: null
12. Link manipulation (DOM-based)
12.1. https://lgtm-com.pentesting.semmle.net/
12.2. https://lgtm-com.pentesting.semmle.net/
12.3. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876)%3C/
12.4. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876)%3C/script%3E
12.5. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876);%3C/
12.6. https://lgtm-com.pentesting.semmle.net/admin%3Cscript%3Ealert(9876);%3C/script%3E
12.7. https://lgtm-com.pentesting.semmle.net/blog/
12.8. https://lgtm-com.pentesting.semmle.net/blog/images/
12.9. https://lgtm-com.pentesting.semmle.net/blog/images/announcing_project_badges/
12.10. https://lgtm-com.pentesting.semmle.net/blog/images/bsides_wrap_up/
12.11. https://lgtm-com.pentesting.semmle.net/favicon.ico
12.12. https://lgtm-com.pentesting.semmle.net/help/
13. Lack or Misconfiguration of Security Header(s)
14. [SSL Scanner] LUCKY13
15. Interesting Header(s)
16. Software Version Numbers Revealed
16.1. https://lgtm-com.pentesting.semmle.net/qlapi-fast/getqlparser
16.2. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
16.3. https://lgtm-com.pentesting.semmle.net/static/site/scripts/vendor-jquery.41f697b3f15739940f70.js
16.4. https://lgtm-com.pentesting.semmle.net/static/site/scripts/vendor-lodash.57a18b08a24a9b344412.js
17. J2EEScan - Information Disclosure - Jetty 9.4.11.
17.1. https://lgtm-com.pentesting.semmle.net/qlapi-fast/
17.2. https://lgtm-com.pentesting.semmle.net/qlapi-fast/getqlparser
17.3. https://lgtm-com.pentesting.semmle.net/qlapi-fast/getqlparser
17.4. https://lgtm-com.pentesting.semmle.net/qlapi-fast/getqlparser
17.5. https://lgtm-com.pentesting.semmle.net/qlapi-slow/
17.6. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
17.7. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
17.8. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
17.9. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
17.10. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
18. Detailed Error Messages Revealed
18.1. https://lgtm-com.pentesting.semmle.net/help/ql/locations
18.2. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getPersonBySlug
18.3. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getPersonHistoryStats
18.4. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getProjectLatestStateStats
18.5. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/getSearchSuggestions
18.6. https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/performSearch
18.7. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
19. Cross-domain Referer leakage
19.1. https://lgtm-com.pentesting.semmle.net/login/
19.2. https://lgtm-com.pentesting.semmle.net/search
20. Frameable response (potential Clickjacking)
20.1. https://lgtm-com.pentesting.semmle.net/qlapi-fast/
20.2. https://lgtm-com.pentesting.semmle.net/qlapi-fast/getqlparser
20.3. https://lgtm-com.pentesting.semmle.net/qlapi-slow/
20.4. https://lgtm-com.pentesting.semmle.net/qlapi-slow/checkerrors
21. SSL certificate
22. [SSL Scanner] Supported Cipher Suites
23. [SSL Scanner] 3DES Cipher (Medium)]

## Steps To Reproduce:
[Look In Attached report]

## Impact

The issues reported here as i had done burp scan so wanted to share complete report.

## Attachments
- lgtm-com.pentesting.semmle.net_-_Semmle_Burp.html
