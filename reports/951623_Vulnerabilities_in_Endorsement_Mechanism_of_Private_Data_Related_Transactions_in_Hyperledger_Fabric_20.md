# Vulnerabilities in Endorsement Mechanism of Private Data Related Transactions in Hyperledger Fabric 2.0

## Report Details
- **Report ID**: 951623
- **URL**: https://hackerone.com/reports/951623
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-05T14:09:07.148Z
- **Disclosed**: 2021-03-30T20:29:49.355Z

## Reporter
- **Username**: swang1994
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
To whom it may concern,

We report design flaws that can be exploited by private data collection non-member organizations to forge endorsements of read-related transactions and return fake values to a user.  

When a user issues a read-only transaction proposal to a endorser in the private data collection, if the user has the privilege to read private data, the endorser returns a read set storing <key, version> and a null write set. The value of the key is returned in the "payload" field of the transaction. 

When the user issues a read-only transaction proposal to an endorser which is not a member of private data collection, the <key, version> and the value can not be found in the endorser's world state. Therefore, a private data collection non-member endorser cannot endorse such read-related transactions.

However, we find a malicious private data non-member endorser can endorse a read-only transaction proposal for private data and pass the validation by all peers if this non-member endorser colludes with other endorsers, which can be either a private data collection member or non-member endorsers. These malicious endorsers can just return the same read set and payload, which can collaboratively fabricated by these malicious endorsers. Since the validation process does not check if the endorsers have the private data, the transaction will be written into the ledger as valid. 

The damage of this attack is the malicious endorsers can return fake values to the user.

Please let me know if you have any questions or concerns. If you think it is necessary, we can give you a briefing on the issues. Look forward to your reply!

Best Regards,

Shan Wang, Southeast University (Email: shanwang1994@gmail.com)
Yue Zhang, Jinan University
Xinwen Fu, University of Massachusetts, Lowell

## Impact

The damage of this attack is the malicious endorsers can return fake values to the user.

## Attachments
No attachments
