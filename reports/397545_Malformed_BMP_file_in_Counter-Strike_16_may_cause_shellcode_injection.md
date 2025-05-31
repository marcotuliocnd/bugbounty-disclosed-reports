# Malformed .BMP file in Counter-Strike 1.6 may cause shellcode injection

## Report Details
- **Report ID**: 397545
- **URL**: https://hackerone.com/reports/397545
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-21T06:33:12.777Z
- **Disclosed**: 2020-02-27T18:43:10.663Z

## Reporter
- **Username**: kohtep2010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
With the vulnerability of the GoldSource Engine, the server is able to perform remote code execution on the client, overwriting the stack when reading the BMP file. The problem is in the LoadBMP8 function, which is executed when the player connects to the server, by loading the "overviews\%MAPNAME%.bmp" file. If we send a badly formed file to this function, then we will be able to rewrite the stack of the function by setting the own code in the stack and passing program control to it.

I've wrote a program that compiles file like that. The shellcode, which runs on the stack, starts the "calc.exe" process with the WinExec function.

For the client to execute this file, the server must send this file to the client. The server can do this if map that is not present on the client is launched. The server must load a map with random name, for example, "definitely_missing_client_map.bsp". In this case, the name of the BMP file must also be "definitely_missing_client_map.bmp" and it must be in "overviews" folder. You also must create the "overviews\definitely_missing_client_map.txt" file, which is overview description. The nonstandard name of the map prompts the client to download the missing files (bsp, bmp and txt). Upon completion, when the client is able to see the map, the BMP file will be loaded and the binary code from BMP file will be executed on the stack.

I've attached the source code of "compiler" to the message. You can find more detailed instructions in the code comments. You need to compile this project in "Release" configuration and then start this project. After that, malformed "de_dust2.bmp" file will be produced.

## Impact

An attacker can execute remote code on the client's machine.

## Attachments
- HL1-BmpSploit.zip
