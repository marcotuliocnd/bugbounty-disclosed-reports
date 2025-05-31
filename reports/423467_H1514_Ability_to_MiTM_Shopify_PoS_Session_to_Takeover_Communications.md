# H1514 Ability to MiTM Shopify PoS Session to Takeover Communications

## Report Details
- **Report ID**: 423467
- **URL**: https://hackerone.com/reports/423467
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-13T19:35:59.245Z
- **Disclosed**: 2019-11-04T01:07:32.970Z

## Reporter
- **Username**: teknogeek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi @iv-rodriguez,

After a decent amount more digging and research, I must disagree with you on the "expecting to work offline" portion. The code actually specifically listens on all local interfaces (`0.0.0.0`) and the wifi network address is specifically used in the QR code connection string, as shown here in `com.shopify.pos.customerview.server.CustomerViewWebSocketServer::getConnectionString()` in the `com.shopify.pos` app:

```java
private final String getConnectionString() {
    String initialPublicKey = this.crypto.initialPublicKey();
    String initialNonce = this.crypto.initialNonce();
    String currentWifiIpAddress = NetworkUtility.getCurrentWifiIpAddress(PosApplication.Companion.getInstance());
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append(this.protocol);
    stringBuilder.append("://");
    stringBuilder.append(currentWifiIpAddress);
    stringBuilder.append(':');
    stringBuilder.append(this.port);
    stringBuilder.append(';');
    stringBuilder.append(initialPublicKey);
    stringBuilder.append(';');
    stringBuilder.append(initialNonce);
    stringBuilder.append(';');
    PayloadManager payloadManager = this.payloadManager;
    if (payloadManager == null) {
        Intrinsics.throwUninitializedPropertyAccessException("payloadManager");
    }
    stringBuilder.append(payloadManager.getSchemaVersion());
    return stringBuilder.toString();
}
```
This can also be seen from netstat on the device:

```
vbox86p:/ # netstat -an | egrep 'LISTEN[^I]'
tcp        0      0 0.0.0.0:24800           0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:24801         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:27042         0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22468           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:24810           0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:24811         0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:5037          0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN
tcp        0      0 :::5000                 :::*                    LISTEN <---
tcp        0      0 :::24296                :::*                    LISTEN
tcp        0      0 :::6379                 :::*                    LISTEN
tcp        0      0 :::5555                 :::*                    LISTEN
```


In addition to this, the main point of this attack is to show how a merchant can abuse this functionality to cause extra charges to the customer, unknowingly. I was able to build a relay server for the WebSocket and could snoop on the raw messages without any issue.

Using an ARP spoofing attack it would be possible to MiTM the WebSocket between the real server and the customer while on the same network. At this point, you still need to obtain the initial public key that is in the QR code. This can be done by forcing the client to accept a new one by altering the message types to contain a new receiverPublicKey.

This faulty logic can be seen here in `com.shopify.pos.customerview.common.crypto.ClientCryptoProtocol::receiveMessageFromServer()` in the `com.shopify.pos.customerview` app:

```java
public void receiveMessageFromServer(String str, CryptoType cryptoType, String str2) {
    Intrinsics.checkParameterIsNotNull(str, "message");
    Intrinsics.checkParameterIsNotNull(cryptoType, "type");
    Intrinsics.checkParameterIsNotNull(str2, "publicKeyString");
    if (WhenMappings.$EnumSwitchMapping$0[cryptoType.ordinal()] != 1) {
        str = new Hex().decode(str);
        Intrinsics.checkExpressionValueIsNotNull(str, "decodedMessageString");
        str = handleIncomingMessage(str, cryptoType, str2);
        if (str != null) {
            getDecryptedMessageHandler().invoke(new String(str, Charsets.UTF_8));
            str = handleOutgoingMessage(CryptoConstant.ACK.encoded(), cryptoType);
            if (str != null) {
                str = new Hex().encode(str);
                Intrinsics.checkExpressionValueIsNotNull(str, "Hex().encode(cipherText)");
                String publicKey = getSenderKeyPair().getPublicKey().toString();
                Intrinsics.checkExpressionValueIsNotNull(publicKey, "senderKeyPair.publicKey.toString()");
                getEncryptedMessageHandler().invoke(new CryptoMessage(cryptoType, str, publicKey));
                return;
            }
            return;
        }
        return;
    }
    str = new Hex().decode(str2);
    Intrinsics.checkExpressionValueIsNotNull(str, "Hex().decode(publicKeyString)");
--->setReceiverPublicKey(str);
    onAckReceived();
}
```

Normally, when the customer view initially connects to the server, the public key and nonce from the QR code are stored from the `com.shopify.pos.customerview.common.crypto.ClientCryptoProtocol::start()` method in the `com.shopify.pos.customerview` app:

```java
public void start(String str, String str2, Function0<Unit> function0) {
    Intrinsics.checkParameterIsNotNull(str, "publicKeyString");
    Intrinsics.checkParameterIsNotNull(str2, "randomString");
    Intrinsics.checkParameterIsNotNull(function0, "startCompletion");
    setSenderKeyPair(getCrypto().generateKeyPair());
    setReceiverKeyPair(getCrypto().generateKeyPair());
    str = new Hex().decode(str);
    str2 = new Hex().decode(str2);
    Intrinsics.checkExpressionValueIsNotNull(str, "publicKey");
--->setReceiverPublicKey(str);
    Intrinsics.checkExpressionValueIsNotNull(str2, "random");
    byte[] encrypt = encrypt(str2, getSenderKeyPair(), str);
    str = encrypt(str2, getReceiverKeyPair(), str);
    if (encrypt != null) {
        if (str != null) {
            CryptoType cryptoType = CryptoType.SENDER_INIT;
            String encode = new Hex().encode(encrypt);
            Intrinsics.checkExpressionValueIsNotNull(encode, "Hex().encode(sCiphertext)");
            String publicKey = getSenderKeyPair().getPublicKey().toString();
            Intrinsics.checkExpressionValueIsNotNull(publicKey, "senderKeyPair.publicKey.toString()");
            getEncryptedMessageHandler().invoke(new CryptoMessage(cryptoType, encode, publicKey));
            CryptoType cryptoType2 = CryptoType.RECEIVER_INIT;
            str = new Hex().encode(str);
            Intrinsics.checkExpressionValueIsNotNull(str, "Hex().encode(rCiphertext)");
            String publicKey2 = getReceiverKeyPair().getPublicKey().toString();
            Intrinsics.checkExpressionValueIsNotNull(publicKey2, "receiverKeyPair.publicKey.toString()");
            getEncryptedMessageHandler().invoke(new CryptoMessage(cryptoType2, str, publicKey2));
            function0.invoke();
        }
    }
}
```

As you can see in the code above, the same `setReceiverPublicKey(...)` method is used in the start method as well as the receiveMessageFromServer method. This is the public key that is later used to encrypt the messages with Curve25519 before being sent to and from the server. As a result, when the message type satisfies the if statement below, the rest of the logic is skipped, and the receiver public key can be overridden:

```java
public void receiveMessageFromServer(String str, CryptoType cryptoType, String str2) {
    Intrinsics.checkParameterIsNotNull(str, "message");
    Intrinsics.checkParameterIsNotNull(cryptoType, "type");
    Intrinsics.checkParameterIsNotNull(str2, "publicKeyString");
--->if (WhenMappings.$EnumSwitchMapping$0[cryptoType.ordinal()] != 1) {
        str = new Hex().decode(str);
        Intrinsics.checkExpressionValueIsNotNull(str, "decodedMessageString");
...
    }
    str = new Hex().decode(str2);
    Intrinsics.checkExpressionValueIsNotNull(str, "Hex().decode(publicKeyString)");
    setReceiverPublicKey(str);
    onAckReceived();
}
```

Combining this together...

- the device listens on `0.0.0.0:5000` but instructs clients to connect to the wifi IP address
- the communications between the customer view and pos apps happens over a normal `ws://` connection with no encryption outside the Curve25519 box
- there is an initial communication process that occurs, allowing the attacker to know the next valid public key to sign messages with in order to continue communication with the legitimate server
- since each portion of the communication stems off of the initial QR code public key, overriding this would grant full control to the session
- as a result, an attacker can override the initial receiver public key to fully take-over the session during a MiTM attack


Thanks, @teknogeek


P.S. This is a copy of my comment from #423378 which I was asked to re-submit as a new bug

## Impact

An attacker can take-over a session by performing a MiTM attack on a PoS customer view session.

## Attachments
No attachments
