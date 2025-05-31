# Bedrock Guardrails Evasion with Prompt Formatting

## Report Details
- **Report ID**: 3056937
- **URL**: https://hackerone.com/reports/3056937
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-03-25T15:38:21.747Z
- **Disclosed**: 2025-05-15T16:12:27.643Z

## Reporter
- **Username**: nkirk-nrlabs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
## Description

Greetings, my name is ██████ and I am a Director here at NR Labs. We recently completed disclosure of this vulnerability by working with ████ and the AWS Security team. We are submitting this issue to the AWS VDP to create an official record of the issue with AWS in preparation for a blog post detailing the issue that will be released shortly. Below is a description of this issue based on an excerpt from the upcoming blog post:

First, a Bedrock AI service leveraging a set of mock data was created, as detailed in the attached document. The mock data used as the knowledge base for the Client service contained several fields of PII, including first names, last names, and email addresses. NR Labs configured the Client service with the Guardrails Sensitive information filter “Name” option enabled with the “Mask” behavior, as shown below:
 ████
Figure 1: Configuration of “Sensitive information filters” functionality within Guardrails that was used for testing
NR Labs then attempted to bypass this filter by modifying the output returned by the AI model. Since names do not typically contain numbers, NR Labs began by instructing the Client service to append the number “123” to the end of each user’s last name. While natural language attempts to have the Client service modify the output in this manner were ineffective, queries that leveraged programmatic-like instructions were successful. 
In the below screenshot, the first response from the Claude 3.5 Sonnet AI model shows Guardrails effectively sanitizing the PII data returned from the associated query, while the second query leveraged the prompt formatting technique to append the number “123” to each last name, causing the affected portion of the response to bypass the Guardrails Sensitive information filter:
 ████████
Figure 2: Evidence of bypassing the Guardrails “Sensitive Information Filter” for Names by leveraging the prompt formatting technique to append the number “123” to each name. 
In addition to appending numbers, NR Labs determined that the AI model would interpret more advanced programmatic commands for PII that required additional manipulation to successfully exfiltrate. In the example below, the Python slice notation was used to exfiltrate the first four characters of each user’s email addresses with the Guardrails Sensitive information filter “Email” option enabled:
 ██████
Figure 3: Example of leveraging the prompt formatting technique with the Python slice notation
By leveraging multiple queries, an attacker could use the above technique to extract sensitive information from a diverse number of sensitive information types.
It was determined that the prompt formatting technique was most effective when the column names of the mock data were used as a reference, such as “first_name” and “last_name”. 
This technique did not appear to be affected when additional Guardrail controls were present, such as the “Grounding check”, “Prompt attacks filter”, and “Relevance check” options. Other AI models within Bedrock, such as Command R+, were also found to be affected by the prompt formatting technique.

## Impact

This issue could allow an attacker to exfiltrate sensitive data from an AI service that leverages the Guardrails "Sensitive information filters" feature of Guardrails. The impact of this issue can be mitigated through the use of effective System Prompt engineering, which will be presented in our upcoming blog post.

## Disclosure

We would like to have this report publicly disclosed, and our usernames revealed, to ensure attribution between our upcoming blog post and an official AWS acknowledgement of the issue. If you have any questions or concerns, please reach out to myself or ████, thanks. 


## Attachments
No attachments
