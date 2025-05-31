# Able to View other users income history

## Report Details
- **Report ID**: 361133
- **URL**: https://hackerone.com/reports/361133
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T17:06:09.641Z
- **Disclosed**: 2018-06-02T17:29:23.173Z

## Reporter
- **Username**: amaljacob
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello,

I found an IDOR that i was able to view income history of other users,

Steps to reproduce issue,
1. Login into account and fire up Burpsuite
2.  The got to profile page and click on view income history
3. Then you can see a request like
```
GET /Liberapay/charts.json HTTP/1.1
Host: liberapay.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Referer: https://liberapay.com/~107258/
Cookie: cookie
Connection: close
```

Response,

```
[
    {
        "date": "2018-05-30",
        "npatrons": 639,
        "receipts": {
            "amount": "261.68",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-05-23",
        "npatrons": 632,
        "receipts": {
            "amount": "259.93",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-05-16",
        "npatrons": 638,
        "receipts": {
            "amount": "210.93",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-05-09",
        "npatrons": 614,
        "receipts": {
            "amount": "209.83",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-05-02",
        "npatrons": 602,
        "receipts": {
            "amount": "208.99",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-04-25",
        "npatrons": 583,
        "receipts": {
            "amount": "206.15",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-04-18",
        "npatrons": 568,
        "receipts": {
            "amount": "133.39",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-04-11",
        "npatrons": 550,
        "receipts": {
            "amount": "171.99",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-04-04",
        "npatrons": 541,
        "receipts": {
            "amount": "171.92",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-03-28",
        "npatrons": 535,
        "receipts": {
            "amount": "168.50",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-03-21",
        "npatrons": 522,
        "receipts": {
            "amount": "169.75",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-03-14",
        "npatrons": 478,
        "receipts": {
            "amount": "163.06",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-03-07",
        "npatrons": 466,
        "receipts": {
            "amount": "169.64",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-02-28",
        "npatrons": 475,
        "receipts": {
            "amount": "166.92",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-02-21",
        "npatrons": 470,
        "receipts": {
            "amount": "225.92",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-02-14",
        "npatrons": 470,
        "receipts": {
            "amount": "151.92",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-02-07",
        "npatrons": 461,
        "receipts": {
            "amount": "139.19",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-01-31",
        "npatrons": 444,
        "receipts": {
            "amount": "139.19",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-01-24",
        "npatrons": 438,
        "receipts": {
            "amount": "139.19",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-01-17",
        "npatrons": 428,
        "receipts": {
            "amount": "141.01",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-01-10",
        "npatrons": 419,
        "receipts": {
            "amount": "136.62",
            "currency": "EUR"
        }
    },
    {
        "date": "2018-01-03",
        "npatrons": 403,
        "receipts": {
            "amount": "136.42",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-12-27",
        "npatrons": 386,
        "receipts": {
            "amount": "136.67",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-12-20",
        "npatrons": 369,
        "receipts": {
            "amount": "150.26",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-12-13",
        "npatrons": 332,
        "receipts": {
            "amount": "133.44",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-12-06",
        "npatrons": 207,
        "receipts": {
            "amount": "92.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-11-29",
        "npatrons": 204,
        "receipts": {
            "amount": "90.15",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-11-22",
        "npatrons": 199,
        "receipts": {
            "amount": "79.93",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-11-15",
        "npatrons": 196,
        "receipts": {
            "amount": "70.33",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-11-08",
        "npatrons": 191,
        "receipts": {
            "amount": "71.33",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-11-01",
        "npatrons": 178,
        "receipts": {
            "amount": "69.22",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-10-25",
        "npatrons": 172,
        "receipts": {
            "amount": "69.12",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-10-18",
        "npatrons": 169,
        "receipts": {
            "amount": "67.35",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-10-11",
        "npatrons": 165,
        "receipts": {
            "amount": "66.25",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-10-04",
        "npatrons": 162,
        "receipts": {
            "amount": "66.02",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-09-27",
        "npatrons": 152,
        "receipts": {
            "amount": "63.32",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-09-20",
        "npatrons": 149,
        "receipts": {
            "amount": "62.92",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-09-13",
        "npatrons": 136,
        "receipts": {
            "amount": "59.72",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-09-06",
        "npatrons": 127,
        "receipts": {
            "amount": "57.86",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-08-30",
        "npatrons": 123,
        "receipts": {
            "amount": "57.86",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-08-23",
        "npatrons": 113,
        "receipts": {
            "amount": "47.86",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-08-16",
        "npatrons": 111,
        "receipts": {
            "amount": "45.41",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-08-09",
        "npatrons": 104,
        "receipts": {
            "amount": "43.36",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-08-02",
        "npatrons": 101,
        "receipts": {
            "amount": "43.91",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-07-26",
        "npatrons": 95,
        "receipts": {
            "amount": "41.24",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-07-19",
        "npatrons": 91,
        "receipts": {
            "amount": "39.22",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-07-12",
        "npatrons": 87,
        "receipts": {
            "amount": "39.61",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-07-06",
        "npatrons": 80,
        "receipts": {
            "amount": "38.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-06-28",
        "npatrons": 76,
        "receipts": {
            "amount": "36.01",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-06-21",
        "npatrons": 76,
        "receipts": {
            "amount": "39.03",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-06-14",
        "npatrons": 71,
        "receipts": {
            "amount": "38.61",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-06-07",
        "npatrons": 69,
        "receipts": {
            "amount": "40.11",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-05-31",
        "npatrons": 70,
        "receipts": {
            "amount": "36.11",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-05-24",
        "npatrons": 69,
        "receipts": {
            "amount": "34.86",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-05-17",
        "npatrons": 68,
        "receipts": {
            "amount": "35.71",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-05-10",
        "npatrons": 69,
        "receipts": {
            "amount": "32.71",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-05-03",
        "npatrons": 68,
        "receipts": {
            "amount": "32.66",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-04-26",
        "npatrons": 61,
        "receipts": {
            "amount": "30.21",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-04-19",
        "npatrons": 53,
        "receipts": {
            "amount": "21.21",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-04-12",
        "npatrons": 47,
        "receipts": {
            "amount": "22.01",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-04-05",
        "npatrons": 47,
        "receipts": {
            "amount": "23.71",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-03-29",
        "npatrons": 47,
        "receipts": {
            "amount": "24.21",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-03-22",
        "npatrons": 46,
        "receipts": {
            "amount": "24.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-03-15",
        "npatrons": 47,
        "receipts": {
            "amount": "24.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-03-08",
        "npatrons": 48,
        "receipts": {
            "amount": "22.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-03-01",
        "npatrons": 45,
        "receipts": {
            "amount": "19.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-02-22",
        "npatrons": 43,
        "receipts": {
            "amount": "19.49",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-02-15",
        "npatrons": 42,
        "receipts": {
            "amount": "19.91",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-02-08",
        "npatrons": 42,
        "receipts": {
            "amount": "19.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-02-01",
        "npatrons": 42,
        "receipts": {
            "amount": "19.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-01-25",
        "npatrons": 40,
        "receipts": {
            "amount": "19.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-01-18",
        "npatrons": 43,
        "receipts": {
            "amount": "20.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-01-11",
        "npatrons": 40,
        "receipts": {
            "amount": "18.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2017-01-04",
        "npatrons": 35,
        "receipts": {
            "amount": "18.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-12-28",
        "npatrons": 33,
        "receipts": {
            "amount": "17.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-12-21",
        "npatrons": 34,
        "receipts": {
            "amount": "17.06",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-12-14",
        "npatrons": 32,
        "receipts": {
            "amount": "17.06",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-12-07",
        "npatrons": 34,
        "receipts": {
            "amount": "18.50",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-11-30",
        "npatrons": 30,
        "receipts": {
            "amount": "19.95",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-11-23",
        "npatrons": 31,
        "receipts": {
            "amount": "20.95",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-11-16",
        "npatrons": 30,
        "receipts": {
            "amount": "22.95",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-11-09",
        "npatrons": 31,
        "receipts": {
            "amount": "24.22",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-11-02",
        "npatrons": 31,
        "receipts": {
            "amount": "24.91",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-10-26",
        "npatrons": 30,
        "receipts": {
            "amount": "24.91",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-10-19",
        "npatrons": 27,
        "receipts": {
            "amount": "18.43",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-10-12",
        "npatrons": 29,
        "receipts": {
            "amount": "18.93",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-10-05",
        "npatrons": 27,
        "receipts": {
            "amount": "18.67",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-09-28",
        "npatrons": 28,
        "receipts": {
            "amount": "22.92",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-09-21",
        "npatrons": 30,
        "receipts": {
            "amount": "24.42",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-09-14",
        "npatrons": 28,
        "receipts": {
            "amount": "19.17",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-09-07",
        "npatrons": 28,
        "receipts": {
            "amount": "15.32",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-08-31",
        "npatrons": 28,
        "receipts": {
            "amount": "15.32",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-08-24",
        "npatrons": 28,
        "receipts": {
            "amount": "15.32",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-08-17",
        "npatrons": 28,
        "receipts": {
            "amount": "18.32",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-08-10",
        "npatrons": 29,
        "receipts": {
            "amount": "18.33",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-08-03",
        "npatrons": 31,
        "receipts": {
            "amount": "19.43",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-07-27",
        "npatrons": 31,
        "receipts": {
            "amount": "21.47",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-07-20",
        "npatrons": 30,
        "receipts": {
            "amount": "21.22",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-07-13",
        "npatrons": 36,
        "receipts": {
            "amount": "27.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-07-06",
        "npatrons": 36,
        "receipts": {
            "amount": "27.16",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-06-29",
        "npatrons": 47,
        "receipts": {
            "amount": "29.94",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-06-22",
        "npatrons": 46,
        "receipts": {
            "amount": "28.94",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-06-15",
        "npatrons": 47,
        "receipts": {
            "amount": "28.36",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-06-08",
        "npatrons": 31,
        "receipts": {
            "amount": "16.54",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-06-01",
        "npatrons": 30,
        "receipts": {
            "amount": "22.64",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-05-25",
        "npatrons": 23,
        "receipts": {
            "amount": "11.93",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-05-18",
        "npatrons": 20,
        "receipts": {
            "amount": "11.93",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-05-11",
        "npatrons": 18,
        "receipts": {
            "amount": "10.52",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-05-04",
        "npatrons": 17,
        "receipts": {
            "amount": "10.01",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-04-27",
        "npatrons": 14,
        "receipts": {
            "amount": "8.26",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-04-20",
        "npatrons": 13,
        "receipts": {
            "amount": "8.26",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-04-13",
        "npatrons": 13,
        "receipts": {
            "amount": "8.31",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-04-06",
        "npatrons": 11,
        "receipts": {
            "amount": "7.03",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-03-30",
        "npatrons": 10,
        "receipts": {
            "amount": "6.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-03-23",
        "npatrons": 9,
        "receipts": {
            "amount": "5.26",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-03-16",
        "npatrons": 9,
        "receipts": {
            "amount": "5.01",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-03-09",
        "npatrons": 9,
        "receipts": {
            "amount": "4.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-03-02",
        "npatrons": 8,
        "receipts": {
            "amount": "4.51",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-02-24",
        "npatrons": 6,
        "receipts": {
            "amount": "4.26",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-02-17",
        "npatrons": 5,
        "receipts": {
            "amount": "2.76",
            "currency": "EUR"
        }
    },
    {
        "date": "2016-02-10",
        "npatrons": 3,
        "receipts": {
            "amount": "1.76",
            "currency": "EUR"
        }
    }
]
```

i have taken Liberapay username for PoC for 

If we change the username then we can see that users income history

## Impact

Able to view income history of other users

## Attachments
No attachments
