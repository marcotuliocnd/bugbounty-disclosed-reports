# Found Origin IP's Lead To Access To [ Grafana Instance , PgHero Instance [ Can SQL Injection ]  

## Report Details
- **Report ID**: 687908
- **URL**: https://hackerone.com/reports/687908
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-04T16:34:19.924Z
- **Disclosed**: 2019-10-09T04:04:01.563Z

## Reporter
- **Username**: elmahdi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
####Hello through `RECON` for on go.exchange i found origin ip's on https://censys.io/ipv4?q=go.exchange That's allow to the attacker to access to Many Instances Like ( Grafana [ But Need Crediantles ]  And Access To PgHero and TokenModel · GO.Exchange  where the attacker can use pghero to Execute postgresql Queries ]

###Origin Ip's : 
####1.  35.244.190.123
####2.  35.227.254.117
####3.  35.240.155.199
####4.  35.201.99.84
####5.  35.244.200.254 - pghero.dev-go.exchange [ PgHero Instance ]
####6.  34.96.94.220 - token-model.dev-go.exchange [ TokenModel · GO.Exchange ]
####7.  35.244.144.67  - yourtrack.dev-go.exchange [ Your Track Instance ]
####8.  35.241.6.32 - grafana.dev-go.exchange [ Grafana Instance ]
####9.  35.190.7.180
####10. 35.241.27.91
####11.  35.187.241.152

###PgHero Instance : 
`curl -i -s -k  -X $'GET' \
    -H $'Host: pghero.dev-go.exchange' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H $'Sec-Fetch-Site: same-origin' -H $'Referer: https://35.244.200.254/explain' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.' \
    $'https://35.244.200.254/'`
###Or Go To Burp suite > Options > Replace&Match
####1. Set Header request And 
`Host: 35.244.200.254
Host: pghero.dev-go.exchange` 
####And do the action with other Instances

## Impact

####Access To Instances for origin server's

## Attachments
No attachments
