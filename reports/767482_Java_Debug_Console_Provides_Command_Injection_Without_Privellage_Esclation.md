# Java Debug Console Provides Command Injection Without Privellage Esclation

## Report Details
- **Report ID**: 767482
- **URL**: https://hackerone.com/reports/767482
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-03T05:59:05.336Z
- **Disclosed**: 2020-07-23T17:03:55.662Z

## Reporter
- **Username**: rpbeast33
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

   I intially found the debug console as a tool to insert arbitrary html/xss bugs, however after further probing the debug console it has some serious security flaws to allow arbitrary java code to be executed. My intial report of a seperate bug using this console, https://hackerone.com/reports/767077, uses the out.print functionality to write html code into the jsp page to perform a XSS attack. This intself is a dangerous bug for compromising users of the webapp. However, what is even more dangerous is allowing any abritratry java code to be executed on the server that an attacker controls. This is exactly what the debug console allows. The console spawns calls the execute.jsp page and then spawns a new .jsp page to give back to the user. Within this scope, the java code that the user/attacker writes is excuted on the server with the privellages given to the new .jsp file under the auspcies of the execute.jsp file. What does this mean? Well, an attacker can write custom .jsp files with native java code to do all sorts of malicous things, which includes Local File Inclusion and overwriting/changing source code - among other attacks. 


## Steps To Reproduce:


  1. Visit: http://ptldynamicgame.mtn.sd/portal-api/tools/debug_console/index.jsp
  2. Write any java code you want to be excuted:


####PoC Java Code:
out.print("LOCAL FILE DATA");
out.print(":");%>
<%@ page import="java.util.Random"%>
<%@ page import="java.io.*"%>
<%
out.println("\n");
File file = new File("/etc/mime.types"); 
BufferedReader br = new BufferedReader(new FileReader(file)); 
String st;
while ((st = br.readLine()) != null)  
{ out.println(st); };%>
<% out.println("Exit");

        Here please note the custom import of java.io.* for file reading purposes.
        As you can see, you can directly import native java code into the .jsp file by closing your opening tag %> and then using 
        your own custom <% %> tags afterwords. At the end also note the <% to ensure the floating tag from the template jsp is closed

## Supporting Material/References:

As stated in my intro, this is similar to my other reported bug found here https://hackerone.com/reports/767077 , but is actually quite different in its attack vector and impact. This represents a uniquely different bug due to the fact you are able to execute java code on the server and thus you are attacking the server rather than performing an XSS attack to target clients of the webapp. Overall, in my opinion these are two distinct bugs that just use the same console as its source. Also what is key to note is you do not have to get the current runtime enviroment of java to execute malicous commands, which in itself would be another crtical bug.

## Impact

Overall the impact for this is critical. In my PoC I demonstrated how you can run attacker controlled java code to read local files, which in itself is a huge bug. However, the power of this bug comes from the ability to really craft the payload to do whatever an attacker desires on your site. Overall, this bug leads to Remote Code Execution which is critical to compromising a server.

## Attachments
No attachments
