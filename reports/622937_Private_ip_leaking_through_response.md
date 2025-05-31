# Private ip leaking through response

## Report Details
- **Report ID**: 622937
- **URL**: https://hackerone.com/reports/622937
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-06-20T19:15:04.706Z
- **Disclosed**: 2021-06-16T10:08:28.062Z

## Reporter
- **Username**: t3chn0phil3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbancompany

## Vulnerability Information
**Name of Vulnerability:** Information desclosure
**User Details:** +91 ████
**Summary:** Private ip addresses are leaking through response in urban clap.

**Description:**
Hi team.
During my research i found some IP address from the response.After finding the origin of the ip i found that these ip addresses are belongs to a private network.I am not sure about the severity of the issue,If this is not a serious issue then close this report as informative,because i submitted this report only due to my curiosity.

Here is the ip
* █████
* ██████
* ██████

Here is the details obtain from whois command
##whois ██████

    NetRange:       172.16.0.0 - 172.31.255.255
    CIDR:           172.16.0.0/12
    NetName:        PRIVATE-ADDRESS-BBLK-RFC1918-IANA-RESERVED
    NetHandle:      NET-172-16-0-0-1
    Parent:         NET172 (NET-172-0-0-0-0)
    NetType:        IANA Special Use
    OriginAS:       
    Organization:   Internet Assigned Numbers Authority (IANA)
    RegDate:        1994-03-15
    Updated:        2013-08-30

##whois ██████████

>>


    Go to account settings and select security
    inetnum:        210.212.29.208 - 210.212.29.223
    netname:        COALTELNET
    descr:          COAL INDIA LIMITED
    descr:          COAL INDIA LTD HQ TELEPHONE DIV.
    descr:          10 N S ROAD
    descr:          KOLKATA - 700 001
    admin-c:        AKK4-AP
    tech-c:         KC1044-AP
    country:        IN
    admin-c:        NIK20-AP
    admin-c:        NC83-AP
    tech-c:         CDN1-AP
    mnt-by:         MAINT-IN-DOT
    status:         ASSIGNED NON-PORTABLE
    last-modified:  2008-09-04T07:11:55Z
    source:         APNIC

    role:           CGM Data Networks
    address:        CTS Compound
    address:        Netaji Nagar
    address:        New Delhi- 110 023
    country:        IN
    phone:          +91-11-24106782
    phone:          +91-11-24102119
    fax-no:         +91-11-26116783
    fax-no:         +91-11-26887888
    e-mail:         dnwplg@bsnl.in
    e-mail:         hostmaster@bsnl.in
    admin-c:        CGMD1-AP
    tech-c:         DT197-AP
    tech-c:         BH155-AP
    nic-hdl:        CDN1-AP
    mnt-by:         MAINT-IN-DOT
    last-modified:  2016-10-01T09:10:26Z
    source:         APNIC

    role:           NS Cell
    address:        Internet Cell  
    address:        Bharat Sanchar Nigam Limited
    address:        8th Floor,148-B Statesman House
    address:        Barakhamba Road, New Delhi - 110 001
    country:        IN 
    phone:          +91-11-23734057
    phone:          +91-11-23710183
    fax-no:         +91-11-23734052
    e-mail:         hostmaster@bsnl.in
    e-mail:         abuse@bsnl.in
    admin-c:        CGMD1-AP
    tech-c:         DT197-AP 
    nic-hdl:        NC83-AP
    mnt-by:         MAINT-IN-DOT
    last-modified:  2016-10-01T09:05:15Z
    source:         APNIC

    person:         A K KUSHARI
    nic-hdl:        AKK4-AP
    address:        COAL INDIA LTD HQ TELEPHONE DIV.
    address:        10 N S ROAD
    address:        KOLKATA - 700 001
    phone:          +91-33-22437001
    fax-no:         +91-33-22437001
    country:        IN
    e-mail:         kushariak@hotmail.com
    mnt-by:         MAINT-IN-PER-DOT
    last-modified:  2008-09-04T07:46:05Z
    source:         APNIC

    person:         KALYAN CHAUDHURI
    nic-hdl:        KC1044-AP
    address:        COAL INDIA LTD HQ TELEPHONE DIV.
    address:        10 N S ROAD
    address:        KOLKATA - 700 001
    phone:          +91-33-22131649
    fax-no:         +91-33-22131649
    country:        IN
    e-mail:         kalyan_chaudhuri@hotmail.com
    mnt-by:         MAINT-IN-PER-DOT
    last-modified:  2008-09-04T07:46:05Z
    source:         APNIC

    person:         Node Incharge KOLKATA
    nic-hdl:        NIK20-AP
    address:        NIB KOLKATA
    address:        2nd Floor, Telephone Bhawan, 34 B.B.D. Bag, Calcutta-1.
    phone:          +91-033-2108090
    fax-no:         +91-033-2109001
    country:        IN
    e-mail:         nib_kolkata@sancharnet.in
    mnt-by:         MAINT-IN-PER-DOT
    last-modified:  2008-09-04T07:33:09Z
    source:         APNIC

    % Information related to '210.212.16.0/20AS9829'

    route:          210.212.16.0/20
    descr:          BSNL Internet
    country:        IN
    origin:         AS9829
    mnt-lower:      MAINT-IN-DOT
    mnt-routes:     MAINT-IN-DOT
    mnt-by:         MAINT-IN-AS9829
    last-modified:  2008-09-04T07:54:45Z
    source:         APNIC
    



## Steps To Reproduce:


  1. Load https://www.urbanclap.com and open the response in Burp suite
  2. Check the response you will get these ip addresses 
  3. Search for ███████ 
  
## Supporting Material/References:

  * Images

Thank you

## Impact

Attacker get deatils about the ip.Also this information can help an attacker to identify other vulnerabilities in the future.

## Attachments
No attachments
