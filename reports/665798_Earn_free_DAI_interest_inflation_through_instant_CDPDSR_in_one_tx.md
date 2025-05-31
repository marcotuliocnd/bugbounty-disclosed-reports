# Earn free DAI interest (inflation) through instant CDP+DSR in one tx

## Report Details
- **Report ID**: 665798
- **URL**: https://hackerone.com/reports/665798
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-02T08:11:11.902Z
- **Disclosed**: 2019-08-12T23:44:52.395Z

## Reporter
- **Username**: lucash-dev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: makerdao_bbp

## Vulnerability Information
## Summary:
The MCD contracts contain different mechanisms for accumulating rates in different
contracts, namely `pot` and `jug` corresponding to the cost of a loan and interest
earned on savings. Because these rates are not synchronised, and depend on the
call to the `drip` method to be calculated, it's possible to game the system
to obtain returns on DAI "savings" that exist only within a transaction.
This means all holders of ETH/gems can costlessly and risklessly earn interest
from the `pot` contract without ever holding DAI for any amount of time.
This leads to inflation of the DAI supply and transfer of value to attackers.

## Detailed Description of the Attack Mechanism

One of the novel features introduced in the MC contracts is the concept of DSR
(DAI Savings Rate) which incentivises investors to hold DAI, by allowing them
to earn interest on DAI deposits in the `pot` contract.
Normally that doesn't result in overall inflation of the DAI supply,
as the only ways of obtaining the DAI to deposit on the "savings account" is by
either acquiring a CDP (Collateralised Debt Position) or buying DAI from someone
else. As repaying a CDP will require an amount of DAI increasing with time, the
overall economic effect is a net increase in DAI value.

In practice, however, both the Stability Fee rates and the DSR rate accrue at discrete
moments in time (rather than continuously), whenever a user calls the method
`drip` on the `jug` or `pot` contracts. As these methods are not synchronised
between the `jug` and `pot` contracts it is possible, by carefully sequencing
method calls to perform a transaction with the following steps:

1. Transform the ETH/token into gem balance, using the `join` contract.
2. Create a CDP urn (vat.frob), obtaining the maximum amount of DAI from the gem balance.
3. Deposit the resulting DAI balance into `pot` (`join` method).
4. Update accumulated DSR rate (`pot.drip`).
5. Withdraw DAI from `pot` (`exit` method), obtaining the DAI deposited in 3 plus
interest.
6. Repay CDP (again, `vat.frob`), getting back the gem balance.
7. Transform back the gem balance into ETH/token.

At first glance the attack might not seem very practical, since there's no way
to guarantee that no other transaction with call `pot.drip` in the same block, and
that the time between calls to drip might be just a few seconds, earning a minimal
amount of interest.
In practice, a balance of several million USD worth of tokens would be enough to
obtain interest payments larget than the gas cost of each call -- this could be
easily crowdsourced in a trustless contract that splits the profits according to
size of ETH/token deposits by participants, or easily obtained by some individual
investors (e.g. exchanges).
Even if the attack doesn't earn an interest in every instance (due to `pot.drip`
having already been called in the same block), a random portion of successful
occurrences would be enough to make executing it repeatedly profitable. Moreover,
the crowdsourcing contract could obtain miner collaboration by paying them a portion of profits or
extremely high fees.

If a crowdsourced attacker is correctly built and publicised, nothing prevents
every single ETH/token holder from depositing their holdings in it, and profitably
participating (with minimal cost and no risk) in a continuous attack on the MCD contracts,
earning interest on a total balance worth billions USD -- and considerably inflating
the DAI supply.

The attack will become clearer by inspecting a concrete example.


## Reproducing the Attack - Example Crowdsourcer Contract

Please find attached the file `antivat.t.sol` which includes an example crowdsourcer
contract (AntiVat) capable of accepting ETH deposits from users, and executing
the CDP+DSR attack (`grabFreeDai` method). The contract also distributes profits
proportionally between contributors.

The contract could be easily extended to support other gems and to provide an
incentive to the miner.

Please note that this attacker contract is provided merely as an example for
helping in reproducing the bug.

## Possible Fix

As a suggested fix, calling `pot.drip` from within the call to `vat.frob` would
render the attack impossible (interest would always be zero).

Please note that I make no claim that the above is the best way of fixing the issue.
The suggested fix is provided only as proof that this is a fixable bug in the
contracts.

## Impact Analysis

Please refer to the "Impact Analysis" field below for a detailed analysis.

## Impact

This section will proceed to demonstrate that this is a critical bug that meets
(and exceeds) the requirements stated in the policy.

In the description above I've already made the points that:
1 - The issue reported is fixable.
2 - The attack has minimal cost when performed by a crowdsourced contract (or
high-balance attacker).

I'll proceed to show that:
3 - It's possible to steal 10% (or more) of the value of the collateral in the
system.

The attack described consists of repeatedly obtaining DAI interest over large
balances in ETH/token that could be used for collateral, but without increasing
the overall collateral locked in the system. As the DAI interest is paid for with
newly created DAI, this corresponds to a continuous inflation of the DAI supply,
transferring value continuously from legitimate holders of DAI.

Ultimately, given enough time, virtually all the DAI market cap could be in the hands of
the attackers. The only limiting factor is time, and the rate at which value can
be stolen is a function of the value of ETH and collateral tokens available to the
attackers (which could well be the economic majority in the ETH ecosystem), the
DSR rate, and the "Line" limit.

Assuming, as an example, that the DSR rate is 2% a year, that the available ETH
supply is 20x that of the collateral in the MCD contracts, and that the "Line" limit
is higher than that -- after one year (assuming successful attack in most blocks)
the attackers would have inflated the DAI
supply in 40%, transfering much more than 10% of collateral value to themselves.

It's impossible to know beforehand what values the DSR rate and the "Line" limit
will have, but all they can do without breaking the contract functionality is
to slow down the theft. (a DSR rate of 0% would effectively kill the DAI savings
functionality, and low "Line" values that prevent DAI from being created in the
attack would also affect the possibility of new legitimate users joining the system)

# Final Note

I understand this is an involved attack, exploiting an issue in the interaction
between several contracts, and with complex economic consequences.
Please don't hesitate in contacting me for further explanations or to provide
any information that can help you reproduce and evaluate the issue.

## Attachments
- antivat.t.sol
