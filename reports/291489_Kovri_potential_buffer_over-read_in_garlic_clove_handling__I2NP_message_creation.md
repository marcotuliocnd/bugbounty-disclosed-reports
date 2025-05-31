# Kovri: potential buffer over-read in garlic clove handling + I2NP message creation

## Report Details
- **Report ID**: 291489
- **URL**: https://hackerone.com/reports/291489
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-18T12:42:53.852Z
- **Disclosed**: 2017-12-05T06:09:37.460Z

## Reporter
- **Username**: aerodudrizzt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Brief
-----
There is a lack of sanitation checks when handling Garlic messages in the kovri I2P router. Sending a specially crafted Garlic message can cause the router to send onward an I2P message containing leaked RAM data, triggering a massive information leakage.

Technical Details:
===========
* Code Version: Taken from Github on the 18th of November 2017 - commit 5aafe6608519d31e537c97b24ea7b23aa372dd5b
* Vulnerable File: src\core\router\garlic.h
* Vulnerable Function: GarlicDestination::HandleGarlicPayload

The function is responsible to parse and handle Garlic Payloads: several independent Garlic Cloves.
When handling a clove with a delivery type of "DeliveryTypeTunnel" there are insufficient checks on the message, before it is wrapped and sent onward:
```cpp
    GarlicDeliveryType delivery_type = (GarlicDeliveryType)((flag >> 5) & 0x03);
    switch (delivery_type) {
      case eGarlicDeliveryTypeLocal:
        LOG(debug) << "GarlicDestination: Garlic type local";
        HandleI2NPMessage(buf, len, from);
      break;
      case eGarlicDeliveryTypeDestination:
        LOG(debug) << "GarlicDestination: Garlic type destination";
        buf += 32;  // destination. check it later or for multiple destinations
        HandleI2NPMessage(buf, len, from);
      break;
      case eGarlicDeliveryTypeTunnel: {
        LOG(debug) << "GarlicDestination: Garlic type tunnel";
        // gateway_hash and gateway_tunnel sequence is reverted
        std::uint8_t* gateway_hash = buf;
        buf += 32;
        std::uint32_t gateway_tunnel = bufbe32toh(buf);
        buf += 4;
        std::shared_ptr<kovri::core::OutboundTunnel> tunnel;
        if (from && from->GetTunnelPool())
          tunnel = from->GetTunnelPool()->GetNextOutboundTunnel();
        // EI [BUG-TRACE] : The payload length is based on an unchecked length field
        // EI             : from the just found I2NP message contained in the clove.
        // EI	          : When creating and sending this message onward we may leak
        // EI             : heap memory data to the destination node [18/11/2017]
        if (tunnel) {  // we have send it through an outbound tunnel
          auto msg = CreateI2NPMessage(buf, kovri::core::GetI2NPMessageLength(buf), from);
          tunnel->SendTunnelDataMsg(gateway_hash, gateway_tunnel, msg);
        } else {
          LOG(debug)
            << "GarlicDestination: no outbound tunnels available for garlic clove";
        }
        break;
      }
      case eGarlicDeliveryTypeRouter:
        LOG(warning) << "GarlicDestination: Garlic type router not supported";
        buf += 32;
      break;
      default:
        LOG(error)
          << "GarlicDestination: unknown garlic delivery type "
          << static_cast<int>(delivery_type);
    }
    buf += kovri::core::GetI2NPMessageLength(buf);  // I2NP
    buf += 4;  // CloveID
    buf += 8;  // Date
    buf += 3;  // Certificate
    // EI [BUG_TRACE] : This check is too late since the I2NP message was already sent. [18/11/2017]
    if (buf - buf1  > static_cast<int>(len)) {
      LOG(error) << "GarlicDestination: clove is too long";
      break;
    }
```

Proposed Fix
---------------
The inner I2NP message is parsed and forwarded using it's own length field BEFORE this field is checked for consistency. There is a good sanitation check in the bottom of the function, but the check is preformed only AFTER the message is sent.

The proposed fix is to copy the current code check to the vulnerable case, and to preform it before the new message is created:
```cpp
    case eGarlicDeliveryTypeTunnel: {
        LOG(debug) << "GarlicDestination: Garlic type tunnel";
        // gateway_hash and gateway_tunnel sequence is reverted
        std::uint8_t* gateway_hash = buf;
        buf += 32;
        std::uint32_t gateway_tunnel = bufbe32toh(buf);
        buf += 4;
        std::shared_ptr<kovri::core::OutboundTunnel> tunnel;
        if (from && from->GetTunnelPool())
          tunnel = from->GetTunnelPool()->GetNextOutboundTunnel();
        // EI [BUG-FIX] : added this new check
        if (buf + kovri::core::GetI2NPMessageLength(buf) + 4 + 8 + 3 - buf1  > static_cast<int>(len)) {
          LOG(error) << "GarlicDestination: clove is too long";
          break;
        }
        if (tunnel) {  // we have send it through an outbound tunnel
          auto msg = CreateI2NPMessage(buf, kovri::core::GetI2NPMessageLength(buf), from);
          tunnel->SendTunnelDataMsg(gateway_hash, gateway_tunnel, msg);
        } else {
          LOG(debug)
            << "GarlicDestination: no outbound tunnels available for garlic clove";
        }
        break;
      }
```

Implications
--------------
Since the original message is allocated on the heap, this message can **leak massive amounts of heap data** to the receiving node (message lengths can be even 32KB). This data contains previous messages, currently treated messages, and many other sensitive data-structures of the I2P router.

In case there are any questions regarding my findings I will be more than happy to help.

## Attachments
No attachments
