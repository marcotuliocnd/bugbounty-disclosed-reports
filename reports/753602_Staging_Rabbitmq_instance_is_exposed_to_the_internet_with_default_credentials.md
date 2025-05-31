# Staging Rabbitmq instance is exposed to the internet with default credentials

## Report Details
- **Report ID**: 753602
- **URL**: https://hackerone.com/reports/753602
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-07T11:46:41.492Z
- **Disclosed**: 2019-12-09T06:46:47.374Z

## Reporter
- **Username**: albatraoz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
**Description:** 
RabbitMQ is an open-source message-broker software (sometimes called message-oriented middleware) that originally implemented the Advanced Message Queuing Protocol (AMQP) and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol (STOMP), Message Queuing Telemetry Transport (MQTT), and other protocols.

The instance of the rabbitmq of unikrn is exposed to the internet with the default credentials guest:guest which has an administrative access.

## Steps To Reproduce:
1. Visit ███████
2. Enter user as guest & password as guest.
3. Boom!! You are inside the management console of the rabbitmq of unikrn.

P.S I checked that the ssl certificates belong to domain *.dev.unikrn.space which proves that the instance belongs to unikrn and maybe used for production or development.

##Mitigation
Don't expose the rabbitmq console on the internet & remove the default credentials.

## Supporting Material/References:
Here is a screenshot of the list of queue
███

## Impact

The impact is critical as the attacker can get hell lot of details by dumping the queues as the queues are having confidential details like sso details & api details for different assets. Also the default credential has the administrative access which can help the attacker to add a new queue, modify or delete an existing queue etc.

## Attachments
No attachments
