# Node.js: TLS session reuse can lead to hostname verification bypass

## Report Details
- **Report ID**: 811502
- **URL**: https://hackerone.com/reports/811502
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-05T17:30:12.121Z
- **Disclosed**: 2020-06-03T06:55:54.149Z

## Reporter
- **Username**: fwilhelm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
The Node.js TLS library supports client side reuse of TLS sessions when multiple connections to the same server are opened.

Code that wants to use this feature can listen for the 'session' event (https://nodejs.org/api/tls.html#tls_event_session) on a tls.TLSSocket to get notified of newly created TLS sessions. The documentation for this event explicitly mentions that the passed sessions "can be used immediately or later".

The problem with this design is that 'session' events are triggered even if verification of the server certificate hostname in onConnectSecure fails. (https://github.com/nodejs/node/blob/b1d4c13430c92e94920f0c8c9ba1295c075c9e89/lib/_tls_wrap.js#L1502):

onConnectSecure is triggered by the OpenSSL info callback (with the flag SSL_CB_HANDSHAKE_DONE) after a TLS handshake. The 'session' event is triggered by OpenSSLs get_session_cb, which can happen before the info callback in TLS 1.2 and after in TLS 1.3 and which is triggered regardless of the result of onConnectSecure.

This means that sessions where the server presented an invalid certificate, or one with a wrong hostname, will trigger the session event and can end up being reused or stored in a cache.

That behavior is insecure, because resumed sessions will not be subjected to another hostname verification check as long as they are CA signed:

// Verify that server's identity matches it's certificate's names
// Unless server has resumed our existing session
if (!verifyError && !this.isSessionReused()) {
    const hostname = options.servername ||
                   options.host ||
                   (options.socket && options.socket._host) ||
                   'localhost';
    const cert = this.getPeerCertificate(true);
    verifyError = options.checkServerIdentity(hostname, cert);
}


In practice, this means that the immediate reuse described in the API documentation is always insecure and that session caches are at risk of storing insecure sessions. The most important implementation of a session cache is in the https library (https://github.com/nodejs/node/blob/b1d4c13430c92e94920f0c8c9ba1295c075c9e89/lib/https.js#L130): New sessions are stored in the cache when the ‘session’ event is triggered and are evicted once a tls socket is closed with an error. 

 if (options._agentKey) {
    // Cache new session for reuse
    socket.on('session', (session) => {
      this._cacheSession(options._agentKey, session);
    });

    // Evict session on error
    socket.once('close', (err) => {
      if (err)
        this._evictSession(options._agentKey);
    });
  }

This opens a small race window where an invalid session can be used by other HTTPs requests to the same host. The attached proof-of-concept wins the race reliably against a local server using a setImmediate() callback, but there are probably other ways this could be exploited in real world applications. I also did not fully investigate if there is a way to trigger the socket ‘close’ event with no error which would skip the session eviction and turn this into a 100% reliable bypass.


The POC requires a target server with a valid CA signed certificate (for an arbitrary hostname) and support for TLS resumption. I’ve attached a minimal golang https server that worked for me.

[fwilhelm@fwilhelm node]$ ../node/node-v13.9.0-linux-x64/bin/node poc.js
[!] First request failed:Host: nodejs.org. is not in the cert's altnames: DNS:loca.host
[x] Starting second request
[x] Dumping globalAgent._sessionCache.map:
{
  'nodejs.org:8444:::::::::::::::::TLSv1_2_method:': <Buffer 30 82 06 2f 02 01 01 02 02 03 04 04 02 13 01 04 20 cd b7 17 84 ac 9f 31 6f 1c cc 73 de 31 05 eb dc 60 62 df c7 c5 d5 8c b4 75 cc a7 28 1f d9 c0 22 04 ... 1537 more bytes>
}
[!] Bypassed hostname verification. Server response: 200
{
  date: 'Thu, 05 Mar 2020 17:08:24 GMT',
  'content-length': '29',
  'content-type': 'text/plain; charset=utf-8',
  connection: 'close'
}


This bug is subject to a 90 day disclosure deadline. After 90 days elapse,
the bug report will become visible to the public. The scheduled disclosure
date is 2020-06-03. Disclosure at an earlier date is also possible if
agreed upon by all parties.

## Impact

MitM of TLS connections

## Attachments
- poc.js
- server.go
