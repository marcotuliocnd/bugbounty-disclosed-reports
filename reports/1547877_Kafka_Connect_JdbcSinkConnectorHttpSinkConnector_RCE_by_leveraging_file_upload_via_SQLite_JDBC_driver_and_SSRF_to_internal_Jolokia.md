# [Kafka Connect] [JdbcSinkConnector][HttpSinkConnector] RCE by leveraging file upload via SQLite JDBC driver and SSRF to internal Jolokia

## Report Details
- **Report ID**: 1547877
- **URL**: https://hackerone.com/reports/1547877
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-04-22T12:20:17.422Z
- **Disclosed**: 2022-11-08T06:29:22.109Z

## Reporter
- **Username**: jarij
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aiven_ltd

## Vulnerability Information
## Summary:
The Aiven JDBC sink includes the SQLite JDBC Driver. This JDBC driver can be used to upload SQLite database files onto the server. The HTTP sink connector allows sending HTTP requests to localhost. There is unprotected Jolokia listening on `localhost:6725`.  JMX exports the `com.sun.management:type=DiagnosticCommand` MBean, which contains the `jvmtiAgentLoad` operation. This operation can be used to execute the SQLite database as JVM Agent by embedding the JVM Agent JAR file inside the SQLite database as an BLOB field in a table.

## Steps To Reproduce:

{F1703051}

  1. Login into my VPS: `ssh ████`, password: `█████████@`
  1. Execute `nc -nlvp 4446`
  1. cd to `jdbc-sqlite-jolokia-rce` and run `python3 poc.py` (if running locally, install kafka-python using pip first).
  1. Reverse shell connection should now be established to my test instance

## Impact

RCE on the Kafka Connect server

## Attachments
- 2022-04-22_15-14-04.mp4
- java-agent-reverse-shell-src.zip
