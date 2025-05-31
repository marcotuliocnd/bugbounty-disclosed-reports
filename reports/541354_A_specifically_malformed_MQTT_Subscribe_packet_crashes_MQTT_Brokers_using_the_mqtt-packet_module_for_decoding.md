# A specifically malformed MQTT Subscribe packet crashes MQTT Brokers using the mqtt-packet module for decoding  

## Report Details
- **Report ID**: 541354
- **URL**: https://hackerone.com/reports/541354
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-17T15:00:31.503Z
- **Disclosed**: 2019-04-28T07:36:31.109Z

## Reporter
- **Username**: lxndr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a buffer over-read in mqtt-packet respectively BufferList module.
It allows triggering an out of range read on a buffer which throws a RangeError. MQTT Brokers like mosca and aedes using this module can be forced to crash by sending a specifically malformed MQTT Subscribe packet. 

# Module

**module name:** mqtt-packet
**version:** 6.1.1
**npm page:** `https://www.npmjs.com/package/mqtt-packet`

## Module Description

Encode and Decode MQTT 3.1.1, 5.0 packets the node way.

## Module Stats

114,635 weekly downloads

# Vulnerability

## Vulnerability Description

From the original E-Mail to the Author:
*Hey Matteo,
while playing around with mosca/aedes and our fuzzing approach from IoT-Testware, I discovered some flaws which cause mosca/aedes to crash. Though, I assume the reasons originate from the mqtt-packet respectively bl modules. 
I didn't open an issue because the issue is IMHO quite critical. One could try to abuse to crash mosca/aedes without requiring any credentials, thus might lead to easy DoS attacks.
The malformed Subscribe Packet crashes mosca (v2.8.3) and aedes (v0.37.0), no valid credentials required.*

## Steps To Reproduce:

> Detailed steps to reproduce with all required references/steps/commands. If there is any exploit code or reference to the package source code this is the place where it should be put.

1. start either mosca or aedes MQTT Broker
2. shoot the following command against the Broker (on localhost)
  * `echo -ne '\x104\x00\x04MQTT\x04\xc2\x00\xff\x00\x19alicedoesnotneedaclientid\x00\x05alice\x00\x06secret\x82\x19\xa5\xa6\x00\x15hello/topic/of/alice\x00' | nc localhost 1883`
  * the sent byte string contains 2 accumulated MQTT Packets. The second packet is a subscribe packet and is processed in any case and the Broker's Auth mechanisms are undermined.

## Patch

Please find a GitHub patch attached.

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Ubuntu 18.04.2 LTS
- nodejs -v `v6.17.1`
- npm -v `3.10.10`

# Wrap up

- I contacted the maintainer to let them know: [Y] 
- I opened an issue in the related repository: [N]

## Impact

An attacker can harm the availability of MQTT services which are using these modules.

## Attachments
- fix_malformed_subscribe_crash.patch
