# Second-order SOQL injection through email and campaign name parameter in Salesforce lead submission

## Report Details
- **Report ID**: 1039821
- **URL**: https://hackerone.com/reports/1039821
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-20T19:38:47.882Z
- **Disclosed**: 2021-06-18T19:15:55.475Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
The HackerOne directory contains profiles of bug bounty and vulnerability disclosure programs that aren't managed on HackerOne. These profiles can be claimed by the organization that manages it. As part of this flow, they will need to enter an email address to confirm that affiliation with the company. This email address will then be used to look up potential duplicate leads in SFDC. A lead can also be submitted through the `https://hackerone.com/leads` endpoint. The vulnerability will be demonstrated with the Leads endpoint with the campaign name, since the duplicate detection requires a duplicate to be matched in the SFDC backend before it can be exploited.

```
POST /leads HTTP/1.1
Host: hackerone.com
...

campaign_name='&name=A&company_name=B&title=C&phone=D&website=https://e.com
```

When submitting the request above, a lead will be created in HackerOne's SFDC account. The campaign name is matched against the SFDC backend first to obtain the ID that belongs to the campaign name. It does so using the following code:

```ruby
def find_campaign_id_by_name(campaign_name)
  campaign_record = Salesforce::SalesforceClient.new.soql_query(
    "SELECT Id FROM Campaign WHERE Name = '#{campaign_name}'",
  )&.first

  campaign_record['Id'] unless campaign_record.nil?
end
```

The `campaign_name` is passed directly into the SOQL query, resulting in the ability to inject arbitrary SOQL commands. The lead is created asynchronously, which makes this a second-order SOQL injection. In case the SOQL query syntax is invalid, an exception will be thrown as such:

```
Restforce::ErrorCode::MalformedQuery
MALFORMED_QUERY: 
Id FROM Campaign WHERE Name = '''
                                ^
ERROR at Row:1:Column:40
line 1:40 mismatched character '<EOF>' expecting '''
```

## Impact

Due to the [limited functionality of SOQL](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm), this doesn't seem to lead to any immediate risks. However, string interpolation in any kind of query should be discouraged.

## Attachments
No attachments
