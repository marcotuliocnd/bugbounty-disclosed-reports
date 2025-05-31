# Open Redirect on www.redditinc.com via `failed` query param bypass after fixed bug #1257753

## Report Details
- **Report ID**: 1285081
- **URL**: https://hackerone.com/reports/1285081
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-30T17:02:26.822Z
- **Disclosed**: 2022-09-30T15:11:07.620Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
hello dear support

i have found bypass to open redirect this submission #1257753 after the fixed by sec team 
{F1394378}
old open redirect it;s fixed and not working  this url 
https://www.redditinc.com/ama?action=zendesk%2fdefault%2fsubmit&redirect=74bcbfb4f9c047fb4e467dd203ca3b30f2b31216551ab9db2bf44911c029d506thank-you%2fama-form-step-1&success=thank-you%2fama-form-step-1&failed=http://evil.com&ticket_form_id=360000307211&subject=AMA+Request&name=%27%22%3e%3c%2fscript%3e%3cimg+src%3dx+onerror%3dalert%28%29%3e%7b%7b7*7%7d%7d&email=wehifyyis@solarunited.net&email_confirm=wehifyyis@solarunited.net&participants=%27%22%3e%3c%2fscript%3e%3cimg+src%3dx+onerror%3dalert%28%29%3e%7b%7b7*7%7d%7d&description=%27%22%3e%3c%2fscript%3e%3cimg+src%3dx+onerror%3dalert%28%29%3e%7b%7b7*7%7d%7d&organization=%27%22%3e%3c%2fscript%3e%3cimg+src%3dx+onerror%3dalert%28%29%3e%7b%7b7*7%7d%7d&timeframe=next-week&timezone=%28GMT-05%3a00%29+Eastern+Time+%28US+%26+Canada%29&g-recaptcha-response=03AGdBq26GE8j1nvvxRFyoLySXC_sqwwVN0y8SUOy5Dt_EpgjZ_NcTluixasj63r4R-p88FygQDqWM_xAD2usiKGStmYqRt6o7DKUbfFAoJYH_e2RQnymyCPuln8k3AKMBLEVZ_aGU0hoCqzivt7ZaZWKARPDhrSOacKG4M5O7KD7LIbDAq28NtmuK7ByV0oHsM2uUQOwSv8kfsGRh5pXjLo4No1X2tlQUmj1cy7vEPQ0TJvpWzCLnc8vmhl3tjraPCqIXYkrMuf1nqAPx_0mnggUk_jUAy21JSJVGHJroH3asn70y3wOfCr_nYNAyfWo2mm3Ar5iXNwBOkq7ERaltBj9ZSaZdcOBMTq8tfKrR1mZ0h82owoCQTno3ZXHplZ7XHhegeJDOw5F4dcLHSKmiZfUNDkRqSuCO0HfDxov2ty0FWn_y9RR45fdABD--c0dqITZEUcWqJrkx&agreement=yes
this old  submission

and bypass here  

https://www.redditinc.com/ama?action=zendesk%2fdefault%2fsubmit&redirect=74bcbfb4f9c047fb4e467dd203ca3b30f2b31216551ab9db2bf44911c029d506thank-you%2fama-form-step-1&success=thank-you%2fama-form-step-1&failed=//evil.com&ticket_form_id=360000307211&subject=AMA+Request&name=ergergerg&email=tzzyspu@northsixty.com&email_confirm=tzzyspu@northsixty.com&participants=ergerg&description=ergerg&organization=ergerg&timeframe=month-plus&timezone=%28GMT-07%3a00%29+Arizona&g-recaptcha-response=03AGdBq27Lwm_f_tiYnQMq03oi7u4iTRuxyKgIuJd80Atn2dslKRSRtojLo4zmE7bxWVskHfPWbwB1jhB_nFFnONPa8m3h1ad16G4olvmuj8uTGQEW_LpXhKG3bJqVepH4OVWkZTSo7-sCuhI6ZmyZDa03Ai3zrUvGUeJDUoQGDWW4WgdglWO3TqBzQt_lDcizkX2yGHxasyCkNiifMuarK2Bp6oH52kTUtdnSHoVELj6qDIw0-B1ytpJzKBodibN7txKqSA7-airAZUH7oGU6HZHlH5BW54kJluRlAbGWsL_pMoj6hwYwVFZ7xZzmktYtyHgn5e3TYvd4lUTwmMTReE1v4X0WIID41KgSj9Fcn8KYGo85w5pXY72o-BKWxirNxs_2lh9-WIITsqEL3eTIttbPueaZ5aIb7PS5R51r8nhnTygrWv6_NI8Y5LroEgATxHEch6bWq6-5&agreement=yes


i bypass and i add this //evil.com to  failed=

{F1394382}

{F1394384}

## Impact

Open Redirect and bypass

## Attachments
- 455.PNG
- 777.PNG
- bandicam_2021-07-30_19-59-52-170.mp4
