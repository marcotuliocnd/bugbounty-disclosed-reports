# Binary output bypass

## Report Details
- **Report ID**: 1468962
- **URL**: https://hackerone.com/reports/1468962
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-02-03T02:22:00.749Z
- **Disclosed**: 2022-03-09T21:48:03.526Z

## Reporter
- **Username**: eliasknudsen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
Binary output check bypass

## Summary:
When curl outputs content, it checks for binary output. If the output is large enough, it bypasses the check for binary output. This can mess with the terminal.

## Steps To Reproduce:
1. Setup a server of your choice.
2. Create a function f with these arguments: char and num. Num is number of characters repeating.
3. Before serving at a given endpoint, create an offset f(".", 16384)
4. Create the payload with unicode 0x0 like this f("unicode 0x0", 1)
5. Make the server serve this at a given endpoint.
6. Run this command: curl "Accept: application/xml" -H "Content-Type: application/xml" http://localhost:8080/yourendpoint
7. Change the offset f(".", 16384) to f(".", 16383) to check if it worked.


 curlpayload.png is the code
execution.png is output for when it worked
failed.png is when it failed, when I changed the offset to 16383

## Impact

There could be some further impact by this exploit. As of now it can make the terminal really buggy at times, but further implementations could lead to something else.

## Attachments
- curlpayload.png
- execution.png
- failed.png
