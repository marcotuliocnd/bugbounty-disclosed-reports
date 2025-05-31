# Some build dependencies are downloaded over an insecure channel (without subsequent integrity checks)

## Report Details
- **Report ID**: 1039504
- **URL**: https://hackerone.com/reports/1039504
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-20T12:12:33.260Z
- **Disclosed**: 2020-12-04T18:57:34.720Z

## Reporter
- **Username**: jub0bs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:

Build jobs [`mingw64 | openssl-1.1.1d`](https://github.com/OpenVPN/openvpn/blob/master/.travis.yml#L87) and [`mingw32 | openssl-1.0.2u`](https://github.com/OpenVPN/openvpn/blob/master/.travis.yml#L91) download dependencies from `build.openvpn.net` and `www.oberhumer.com`over an insecure channel (`http`, _not_ `https`) and do not check their integrity in any way.

This opens the door to person-in-the-middle attacks, whereby an attacker controlling an intermediate node on the network path between Travis CI's build servers and those two servers could manipulate traffic and inject his own malicious code into the artifacts produced by the two jobs in question.

## Steps To Reproduce:

The `install` phase of the `.travis.yml` file [unconditionally executes](https://github.com/openvpn/openvpn/blob/master/.travis.yml#L120) the `.travis/build-deps.sh` script. If the following three conditions are satisfied,

1. [the OS be other than `windows`](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L4),
2. [environment variable `SSLLIB` be set to `openssl`](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L148), and
3. [environment variable `CHOST` be set](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L161),

(they are only satisfied for build jobs [`mingw64 | openssl-1.1.1d`](https://github.com/OpenVPN/openvpn/blob/master/.travis.yml#L87) and [`mingw32 | openssl-1.0.2u`](https://github.com/OpenVPN/openvpn/blob/master/.travis.yml#L91)), then shell functions `download_tap_windows` and `download_lzo` are executed [one](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L162) after the [other](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L165).

Shell functions `download_tap_windows` and `download_lzo` are defined above ([here](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L18) and [here](https://github.com/OpenVPN/openvpn/blob/master/.travis/build-deps.sh#L18), respectively) in `.travis/build-deps.sh`:

```shell
download_tap_windows () {
    if [ ! -f "download-cache/tap-windows-${TAP_WINDOWS_VERSION}.zip" ]; then
       wget -P download-cache/ \
           "http://build.openvpn.net/downloads/releases/tap-windows-${TAP_WINDOWS_VERSION}.zip"
    fi
}

download_lzo () {
    if [ ! -f "download-cache/lzo-${LZO_VERSION}.tar.gz" ]; then
        wget -P download-cache/ \
            "http://www.oberhumer.com/opensource/lzo/download/lzo-${LZO_VERSION}.tar.gz"
    fi
}
```

Note that both `wget` commands use `http` as opposed to `https` ( though using `https` is readily possible, since both  domains `build.openvpn.net` and `www.oberhumer.com` support `https` and have valid TLS certificates) .

## Supporting Material/References:

To be added in a comment below when my custom build of OpenVPN/openvpn finishes on travis-ci.org (it's taking a while...).

## Impact

The two dependencies are downloaded over an insecure channel and, therefore, can be intercepted and tampered with by a person in the middle (controlling an intermediate node on the network path between Travis CI's build servers).

Moreover, as no integrity checks seem to be performed after download, a person-in-the-middle attack would go undetected and could seriously compromise the integrity of the artifacts produced by those two build jobs.

Please do not dismiss the possibility of such an attack too quickly, as it is [not as far-fetched as one would think](https://medium.com/bugbountywriteup/want-to-take-over-the-java-ecosystem-all-you-need-is-a-mitm-1fc329d898fb).

## Attachments
No attachments
