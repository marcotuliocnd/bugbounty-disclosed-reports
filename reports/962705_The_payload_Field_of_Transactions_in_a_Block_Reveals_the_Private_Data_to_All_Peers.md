# The “payload” Field of Transactions in a Block Reveals the Private Data to All Peers 

## Report Details
- **Report ID**: 962705
- **URL**: https://hackerone.com/reports/962705
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-19T18:48:25.281Z
- **Disclosed**: 2021-03-30T20:30:07.046Z

## Reporter
- **Username**: swang1994
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
To whom it may concern, 
 
We are a research group conducting research on Hyperledger Fabric 2.0. We find a design flaw about the “payload” field of transactions, which can reveal the Private Data to all peers in one channel.  
 
When a client invokes a function to read the private data, the <key, version> is stored in the read set and the value is returned in the “payload” field of transactions. In the private data related transaction workflow, to avoid revealing private data, only the hash of the read-write set is stored in transactions. However, we find that the “payload” in a transaction holds the original value of the private data. Since all transactions will be bundled into blocks and distributed to all peers in one channel, all peers including private data collection non-member peers can see the private data by fetching the specific transaction. This seriously violates the design principles of the private data collection which is shared by only a subset of peers in one channel. 
 
We test the private data example “marbles02_private” in official documents [1]. In this example, only peer0.org1 is the member of PDC “collectionMarblePrivateDetails”. Peer0.org1 invokes the function readMarblePrivateDetails(). The generated transaction has a “payload” containing the private data {"docType":"marblePrivateDetails","name":"marble1","price":99} and is stored into the blockchain. Peer0.org2 is not the owner of this private data, but can find the actual private data in its local blockchain. Please note that we use the ‘invoke’ CLI, not the ‘query’ CLI. 
 
We recommend that original values of private data should not appear in transactions. More restrictions on “payload” are needed. 
 
References 
 
[1] Hyperledger Fabric Official Docs, Tutorials>> Using Private Data in Fabric, https://hyperledger-fabric.readthedocs.io/en/release-2.0/private_data_tutorial.html?highlight=using%20private%20data 
 
Please let me know if you have any questions or concerns. If you think it is necessary, we can give you a briefing on the issues. Look forward to your reply! 
 
Best Regards, 
 
Shan Wang, Southeast University, University of Massachusetts Lowell , email: shanwang1994@gmail.com
Yue Zhang, Jinan University, University of Massachusetts Lowell 
Xinwen Fu, University of Massachusetts Lowell

## Impact

This design flaw seriously violates the design principles of the private data collection which is shared by only a subset of peers in one channel.

## Attachments
No attachments
