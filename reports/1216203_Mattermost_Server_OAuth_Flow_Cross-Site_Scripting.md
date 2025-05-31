# Mattermost Server OAuth Flow Cross-Site Scripting

## Report Details
- **Report ID**: 1216203
- **URL**: https://hackerone.com/reports/1216203
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-03T08:56:19.005Z
- **Disclosed**: 2021-08-06T14:01:32.171Z

## Reporter
- **Username**: shielder
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
The vulnerability is a reflected Cross-Site Scripting (XSS) via the OAuth flow. A victim clicking a malicious link pointing to the target Mattermost host will trigger the XSS. If the victim is a regular user, it is possible to obtain all of their Mattermost chat contents; if it’s an administrator, it is possible to create a new administrator.

## Root Cause Analysis:
The application fails to sanitize an HTTP query parameter before reflecting it within the HTML response during the OAuth flow.

```go=280
        if props != nil {
                action = props["action"]
                isMobile = action == model.OAUTH_ACTION_MOBILE
                if val, ok := props["redirect_to"]; ok {
[1]                     redirectURL = val
                        hasRedirectURL = redirectURL != ""
                }
        }
        renderError := func(err *model.AppError) {
                if isMobile && hasRedirectURL {
[2]                     utils.RenderMobileError(c.App.Config(), w, err, redirectURL)
                } else {
                        utils.RenderWebAppError(c.App.Config(), w, r, err, c.App.AsymmetricSigningKey())
                }
        }
```

The file "/web/oauth.go" (https://github.com/mattermost/mattermost-server/blob/master/web/oauth.go) contains the function "completeOAuth" which on line 284 values the variable "redirectURL" with the parameter "redirect_to" [1] of the query string of the HTTP GET request. Subsequently always inside of the same function to the line 291 comes called the function "utils.RenderMobileError" to which it comes passed like argument the variable "redirectURL" [2].

```go=103
func RenderMobileError(config *model.Config, w http.ResponseWriter, err *model.AppError, redirectURL string) {
        RenderMobileMessage(w, `
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" style="width: 64px; height: 64px; fill: #ccc">
                        <!-- Font Awesome Free 5.15.3 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) -->
                        <path d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"/>
                </svg>
                <h2> `+i18n.T("error")+` </h2>
                <p> `+err.Message+` </p>
[1]                <a href="`+redirectURL+`">
                        `+i18n.T("api.back_to_app", map[string]interface{}{"SiteName": config.TeamSettings.SiteName})+`
                </a>
        `)
}
```

The function "RenderMobileError" is contained within the file "utils/api.go" (https://github.com/mattermost/mattermost-server/blob/master/utils/api.go) at line 103, and the fourth argument of this function is "redirectURL". At line 104 the "RenderMobileMessage" function is called and at line 111 the variable "redirectURL" is concatenated (without being sanitised) with another string argument of the "RenderMobileMessage" function [1].

```go=157
[...]
                        </head>
                        <body>
                                <!-- mobile app message -->
                                <div class="message-container">
[1]                                     `+message+`
                                </div>
                        </body>
                </html>
        `)
```

Inside the "RenderMobileMessage" function (declared at line 117 of utils/api.go) "fmt.Fprintln" is called to print the HTTP response and the HTML page is dynamically built concatenating the "message" variable [1] (second argument of the function).

Call graph:
completeOAuth -(redirectURL=redirect_to)-> util.RenderMobileError(*,redirectURL) -(message=string+redirectURL)-> RenderMobileMessage(*,message) -> fmt.Fprintln(string+message)

Since the HTTP GET request parameter "redirect_to" is never sanitized and is appended to the HTML page, it is possible to trigger a reflected XSS.

## Steps To Reproduce:
1. Visit the following URL after replacing <mattermost_url> with the domain/ip of the mattermost server instance:
https://<mattermost_url>/oauth/shielder/mobile_login?redirect_to=%22%3E%3Cimg%20src=%22%22%20onerror=%22alert(%27zi0Black%20@%20Shielder%27)%22%3E

2. Notice the JavaScript's generated pop-up

## Supporting Material/References:
  * [attachment / F1324661]

## Impact

The following attack scenarios have been identified:
- If the victim is a regular user, the attacker could read the messages sent and received by the user.
- If the victim is an administrative user, the attacker could change the server settings (e.g. add a new administrative user).

## Attachments
- upload_43235b1bc0e676092457868cc1e2c7fe.png
