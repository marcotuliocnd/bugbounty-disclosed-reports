# CryptoNote: remote node DoS

## Report Details
- **Report ID**: 506595
- **URL**: https://hackerone.com/reports/506595
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-08T03:01:48.309Z
- **Disclosed**: 2019-07-03T00:20:02.687Z

## Reporter
- **Username**: anonimal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:

Remote node DoS. See patch below.

## Releases Affected:

All Monero versions, including the recent v0.14.0.2. Possibly all CryptoNote implementations that aren't Zano.

## Steps To Reproduce:

Since this is *currently* a theoretical attack, non-code PoC detailed in the patch below.

## Supporting Material/References:

Based against current `master` `49afbd0c53d29656689f319c7d3543204ead4e59`:

```diff
commit 6620d099800d8935596f59834ce389868b2851f0 (HEAD -> cryptonote)
gpg: Signature made Fri 08 Mar 2019 02:57:58 AM UTC
gpg:                using RSA key 12186272CD48E2539E2DD29B66A76ECF914409F1
gpg: using pgp trust model
gpg: Good signature from "anonimal <anonimal@getmonero.org>" [ultimate]
gpg:                 aka "anonimal <anonimal@kovri.io>" [ultimate]
gpg:                 aka "anonimal <anonimal@sekreta.org>" [ultimate]
gpg: binary signature, digest algorithm SHA256, key algorithm rsa4096
Author: anonimal <anonimal@getmonero.org>
Date:   Fri Mar 8 02:21:38 2019 +0000

    cryptonote_protocol_handler: prevent potential DoS
    
    Essentially, one can send such a large amount of IDs that core exhausts
    all free memory. This issue can theoretically be exploited using very
    large CN blockchains, such as Monero.
    
    Credit given to CryptoNote author 'cryptozoidberg' for the fix.

diff --git a/src/cryptonote_protocol/cryptonote_protocol_handler.h b/src/cryptonote_protocol/cryptonote_protocol_handler.h
index efd986b53..c9e35d2d9 100644
--- a/src/cryptonote_protocol/cryptonote_protocol_handler.h
+++ b/src/cryptonote_protocol/cryptonote_protocol_handler.h
@@ -52,6 +52,7 @@ PUSH_WARNINGS
 DISABLE_VS_WARNINGS(4355)
 
 #define LOCALHOST_INT 2130706433
+#define CURRENCY_PROTOCOL_MAX_BLOCKS_REQUEST_COUNT 500
 
 namespace cryptonote
 {
diff --git a/src/cryptonote_protocol/cryptonote_protocol_handler.inl b/src/cryptonote_protocol/cryptonote_protocol_handler.inl
index c8b43fb91..023d1b457 100644
--- a/src/cryptonote_protocol/cryptonote_protocol_handler.inl
+++ b/src/cryptonote_protocol/cryptonote_protocol_handler.inl
@@ -889,6 +889,16 @@ namespace cryptonote
   int t_cryptonote_protocol_handler<t_core>::handle_request_get_objects(int command, NOTIFY_REQUEST_GET_OBJECTS::request& arg, cryptonote_connection_context& context)
   {
     MLOG_P2P_MESSAGE("Received NOTIFY_REQUEST_GET_OBJECTS (" << arg.blocks.size() << " blocks, " << arg.txs.size() << " txes)");
+
+    if (arg.blocks.size() > CURRENCY_PROTOCOL_MAX_BLOCKS_REQUEST_COUNT)
+      {
+        LOG_ERROR_CCONTEXT(
+            "Requested objects count is too big ("
+            << arg.blocks.size() << ") expected not more then "
+            << CURRENCY_PROTOCOL_MAX_BLOCKS_REQUEST_COUNT);
+        drop_connection(context, false, false);
+      }
+
     NOTIFY_RESPONSE_GET_OBJECTS::request rsp;
     if(!m_core.handle_get_objects(arg, rsp, context))
     {
```

This is essentially from https://github.com/hyle-team/zano/blob/master/src/currency_protocol/currency_protocol_handler.inl#L364 and confirmation will be needed that Monero doesn't already mitigate this elsewhere.

I have the above patch in my branch ready for PR but if you want to create your own patch, please give credit to cryptozoidberg and myself (anonimal). Thank you.

## Impact

Remote node DoS.

## Attachments
No attachments
