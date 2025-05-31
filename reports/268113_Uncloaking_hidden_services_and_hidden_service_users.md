# Uncloaking hidden services and hidden service users

## Report Details
- **Report ID**: 268113
- **URL**: https://hackerone.com/reports/268113
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-13T16:26:52.466Z
- **Disclosed**: 2017-10-20T14:28:39.246Z

## Reporter
- **Username**: hackerfactor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
I believe I am currently seeing an effective attack that decloaks hidden services and their users.

Background
=========
Following some denial-of-service attacks, I modified my tor code to display every rendezvous site. E.g., in or/rendservice.c, I added:

Function rend_service_receive_introduction

Right after "Find the rendezvous point"
```
  /* Check if we'd refuse to talk to this router */
  if (options->StrictNodes &&
      routerset_contains_extendinfo(options->ExcludeNodes, rp)) {
    /* NAK: Log blocked rendezvous point */
    char TmpAddr[100];
    inet_ntop(rp->addr.family,&(rp->addr.addr.dummy_),TmpAddr,(socklen_t)100);
    log_warn(LD_REND, "Client asked to rendezvous at a relay that we "
             "exclude, and StrictNodes is set. Refusing service for [%s][%s].",rp->nickname,TmpAddr);
    reason = END_CIRC_REASON_INTERNAL; /* XXX might leak why we refused */
    goto err;
  }
```

Right after "Accepted intro; launching circuit"
```
  /** NAK: Log rendezvous point **/
  {
  char TmpAddr[100];
  inet_ntop(rp->addr.family,&(rp->addr.addr.dummy_),TmpAddr,(socklen_t)100);
  log_warn(LD_REND,"Rendezvous [%s] [%s]:%d", rp->nickname, TmpAddr, (int)(rp->port));
  }
```

This allows me to see if there are any common rendezvous sites during times when my server is under a DDoS. (It also allowed my to identify Russia as running a bunch of nodes that worked to attack sites.)

Current attack
=========
My logs normally show things like:
>Sep 13 08:44:45 Tor[32468]: Rendezvous [$747B7F0F60FB2A6625F05656EA74B42AB1DC966C] [138.197.147.223]:9001
>Sep 13 08:46:26 Tor[32468]: Rendezvous [$223A95DC4D09373BC18D61F56F3B18DAFF5FBA25] [31.171.155.29]:443
>Sep 13 08:46:27 Tor[32468]: Rendezvous [$1211AC1BBB8A1AF7CBA86BCE8689AA3146B86423] [95.85.8.226]:443
>Sep 13 08:48:04 Tor[32468]: Rendezvous [$35E8B344F661F4F2E68B17648F35798B44672D7E] [144.32.0.146]:9001
>Sep 13 08:49:27 Tor[32468]: Rendezvous [$51939625169E2C7E0DC83D38BAE628BDE67E9A22] [109.236.90.209]:443
>Sep 13 08:49:29 Tor[32468]: Rendezvous [$8C23B9DAFA7CC62B4C3ED72F1DBF7EC476704E1F] [167.114.219.61]:443

For these records, the fingerprint matches the IP address and port number found in cached-microdesc-consensus.

However, on rare occasions I receive a fingerprint that doesn't match the IP address.
In the above listing, "$35E8B344F661F4F2E68B17648F35798B44672D7E" is a valid fingerprint. According to atlas.torproject.org, it is associated with 146.0.32.144:9001 -- a different IP address than the one I was provided.

In fact, the IP address that I was provided (144.32.0.146) has no service running on port 9001.

In the last day, I have received the following non-Tor addresses:
>Sep 11 23:17:53 Tor[32468]: Rendezvous [$683EBDCAA47D33AE3A2C7D2C7A502C39C006794B] [218.214.136.107]:443
>Sep 12 00:27:25 Tor[32468]: Rendezvous [$DAB5784E3874F8B8119832642E7C292708E95B32] [91.137.230.173]:9001
>Sep 12 03:34:02 Tor[32468]: Rendezvous [$B4CA5FDB58A06914689BA23ED2C5FED79CFB3950] [9.192.32.178]:443
>Sep 12 05:00:11 Tor[32468]: Rendezvous [$38A42B8D7C0E6346F4A4821617740AEE86EA885B] [202.35.220.37]:9001
>Sep 12 09:58:33 Tor[32468]: Rendezvous [$56DCA89A6B41ADA30E891EF65FDCC071DC05079B] [50.118.92.96]:9001
>Sep 12 09:58:33 Tor[32468]: Rendezvous [$8AD8B31171063B7D524F01DC310628BC85772D6A] [146.22.95.192]:443
>Sep 12 09:58:35 Tor[32468]: Rendezvous [$25990FC54D7268C914170A118EE4EE75025451DA] [176.33.39.5]:9001
>Sep 12 09:58:35 Tor[32468]: Rendezvous [$3D44A0A9DCEE0C66F4DF121A64C3424EFAE06864] [16.63.69.158]:443
>Sep 12 09:58:35 Tor[32468]: Rendezvous [$91516595837183D9ECD1318D00723A8676F4731C] [208.254.217.144]:9001
>Sep 12 09:58:35 Tor[32468]: Rendezvous [$CD43574ADF4B706DEB72F820DEA6784979AA213A] [173.160.191.37]:443
>Sep 12 09:58:36 Tor[32468]: Rendezvous [$49E7AD01BB96F6FE3AB8C3B15BD2470B150354DF] [195.194.165.188]:9001
>Sep 12 09:58:38 Tor[32468]: Rendezvous [$F540C7C2E49904D351771BC889DD0D6A5985F352] [133.73.15.51]:9001
>Sep 12 10:57:34 Tor[32468]: Rendezvous [$73779046CB0B393F1E66C1A48E919E925C5FA3C8] [17.252.192.206]:9001
>Sep 12 10:57:36 Tor[32468]: Rendezvous [$005D5C2B6B7638730366298AD6455A784749A26A] [34.16.80.151]:9077
>Sep 12 10:57:39 Tor[32468]: Rendezvous [$7A6873B86D82BC8B4F0E790828626107820F7B9E] [50.77.0.146]:443
>Sep 12 10:57:42 Tor[32468]: Rendezvous [$7383AFD3241269E630DB421AB79F0E8CCD57E90D] [215.120.31.176]:9001
>Sep 12 10:57:44 Tor[32468]: Rendezvous [$5D7D8E6CB9F57303D9437ED4DE46EA14CED3B16B] [76.203.75.62]:443
>Sep 12 12:37:51 Tor[32468]: Rendezvous [$1C90D3AEADFF3BCD079810632C8B85637924A58E] [84.53.172.163]:21
>Sep 12 12:37:57 Tor[32468]: Rendezvous [$86C281AD135058238D7A337D546C902BE8505DDE] [29.88.96.185]:443
>Sep 12 17:52:39 Tor[32468]: Rendezvous [$374830F04945D9847255D98EC93DFB2E9951BD29] [193.125.149.83]:15026
>Sep 12 17:52:41 Tor[32468]: Rendezvous [$125769539D9DAE4053926A897331050B9BE90D51] [198.107.170.107]:443
>Sep 12 17:52:42 Tor[32468]: Rendezvous [$94B0AC1151F5611E801A04AEE29D7D65C3B1A5F5] [33.250.201.138]:9011
>Sep 12 17:52:43 Tor[32468]: Rendezvous [$8AAD1E7D6271B7172A4BC800945302B63A817CB8] [98.30.214.188]:443
>Sep 12 17:52:53 Tor[32468]: Rendezvous [$DF0CB83B662A3F775872D1513946E589FF07E991] [210.189.43.179]:15446
>Sep 12 18:33:28 Tor[32468]: Rendezvous [$775B0FAFDE71AADC23FFC8782B7BEB1D5A92733E] [64.23.196.5]:9001
>Sep 12 18:33:30 Tor[32468]: Rendezvous [$2521B270112C5A6B1631EAE2855B7EE3FE86F616] [154.106.137.79]:443
>Sep 12 18:33:32 Tor[32468]: Rendezvous [$D8D7734AE90F936B13A7347A957A266EEB1CFE37] [164.210.163.89]:443
>Sep 12 18:33:33 Tor[32468]: Rendezvous [$2DE7F6294336C47C0BDF8F10856F548348B2FB63] [44.183.143.79]:9001
>Sep 12 18:41:16 Tor[32468]: Rendezvous [$512F5C68632F4FD64B4A114BC9ACED1CFF76085D] [199.152.37.193]:9001
>Sep 12 18:41:21 Tor[32468]: Rendezvous [$9F3AAF54952400DC016DF17437D2A77D7C47511B] [12.6.169.83]:9001
>Sep 12 18:41:23 Tor[32468]: Rendezvous [$9735D88B8345E57DFB07BE0DAEEBD217E9003E87] [51.70.229.38]:443
>Sep 12 18:41:27 Tor[32468]: Rendezvous [$E248C3A604E196137A3175D4B2E4328922178B47] [35.124.205.137]:1720
>Sep 12 18:41:29 Tor[32468]: Rendezvous [$07DCBC2E00617AF70F411B7CD2A8CE355A6E9668] [19.42.15.51]:9001
>Sep 12 18:41:31 Tor[32468]: Rendezvous [$0CD5EBCD07CE9422CF6FC59793683D6002A83C61] [202.10.99.192]:9001
>Sep 12 23:10:06 Tor[32468]: Rendezvous [$F9EF1F29654CF20F51A30D4BCF04E7D1012F7FDE] [38.106.104.5]:9001
>Sep 13 01:58:49 Tor[32468]: Rendezvous [$52BFADA8BEAA01BA46C8F767F83C18E2FE50C1B9] [65.159.25.85]:80
>Sep 13 03:02:31 Tor[32468]: Rendezvous [$FA4C63169898945DAFF1E682992F1562374B3237] [33.134.87.90]:9666
>Sep 13 08:48:04 Tor[32468]: Rendezvous [$35E8B344F661F4F2E68B17648F35798B44672D7E] [144.32.0.146]:9001
>Sep 13 09:39:28 Tor[32468]: Rendezvous [$F65E0196C94DFFF48AFBF2F5F9E3E19AAE583FD0] [23.246.242.94]:9001

When my service undergoes a denial of service attack (someone attempted on Sept 11-12), I see many more of these fake IP addresses.

The IP addresses are fake.  Some of the IP addresses are not even valid for network routing. For example:
>Sep 12 09:58:34 Tor[32468]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$4558E7A6B8AD56C93526BA046F248E3A877A115D][251.190.172.217].
>Sep 12 09:58:35 Tor[32468]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$AC66FFA4AB35A59EBBF5BF4C70008BF24D8A7A5C][243.164.154.195].
>Sep 12 16:32:57 Tor[32468]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$93DB9554195667032CFDCF15274E826C6779C1F7][228.219.41.31].
>Sep 12 17:52:51 Tor[32468]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$D9E01D8505FFFE439FE61765459E4AE055A8F054][228.27.23.94].
>Sep 12 18:41:20 Tor[32468]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$907F03F43E976A73B1573D68631D0C5CA7CDB2D8][254.2.123.176].
>Sep 11 09:37:25 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$E738E4C5ACE5C015DED9D1A7787C0A6AEB10E5D8][246.190.220.85].
>Sep 11 09:42:33 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$AEC96C88D703D6E2E65ABCE107AB969B748C59AC][238.50.255.51].
>Sep 11 09:42:33 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$AEC96C88D703D6E2E65ABCE107AB969B748C59AC][238.50.255.51].
>Sep 11 09:42:54 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$55793F726CDF6E4AFC46F64661D6BC09DCD082DF][252.146.50.198].
>Sep 11 09:43:13 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$1A4488A367D89D0EFDA88116059FEBCACF0F508A][242.223.56.149].
>Sep 11 09:43:19 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$7231159DCA5BAD27ECA16A0908A753BC886D5FE2][232.146.172.163].
>Sep 11 11:49:53 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$AF36942955DF80849EE646642B36DC4F5909B223][244.82.210.62].
>Sep 11 12:40:41 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$74F1390FA4784387EFD5758F327A5EDF87CF6AA5][240.167.217.144].
>Sep 11 13:24:55 Tor[21819]: Client asked to rendezvous at a relay that we exclude, and StrictNodes is set. Refusing service for [$205ECC49B5BB5230BA0D2F5A0FC1117E391F9825][254.110.107.86].

Each of these IP addresses are Class-D or Class-E (private; reserved for future use).  They should NEVER appear as rendezvous points.

How this appears to be used for decloaking
=========

Most of the time I receive a valid rendezvous address:port.  It's only on rare cases that they are not known Tor nodes.

For these rare cases, as far as I can tell, these IP addresses are fake. There is no Tor-related service running on those ports, and often there is no server regardless of port.

And yet... the connection from the Tor tunnel to the rendezvous point usually succeeds.

Here is what I think is going on:
1. A hostile hsdir negotiates a rendezvous point.  It supplies a valid fingerprint, but an invalid IP address. The IP address is nothing more than a tracking flag.

2. If the hidden service uses a guard before accessing the rendezvous point, then the hostile guard (working in conjunction with the hostile hsdir) reroutes traffic to the correct IP. The hidden service never knows that this rerouting occurred. The attacker now knows the hidden service's real IP address.

3. If the hidden service uses a guard and relay before accessing the rendezvous point, then the attacker needs to control three evil nodes: hsdir, relay, and guard. If the attacker doesn't own the guard, then the attacker still does the rerouting to the correct IP, but doesn't know the hidden service's address due to the guard.  NOTE: There are enough Tor nodes with unspecified owners and unspecified families (or with defined families that claim to be unrelated but actually have the same owners) that this attack is still very plausible.

4. If the attacker does not own the guard or relay, then the IP address does not get rerouted to the correct address.  The connection fails and the user's system renegotiates a different rendezvous point.  NOTE: I have seen connections to these bad addresses fail and a follow-up negotiation for a different (working) rendezvous point.

Besides uncloaking hidden services, this same technique could also uncloak users to the hidden services.

Solution
=========
The solution to this attack is pretty simple... If the signature, IP, and port does not exist in the cached-microdesc-consensus, then don't even attempt to connect. The rendezvous point should be rejected as invalid.

## Attachments
No attachments
