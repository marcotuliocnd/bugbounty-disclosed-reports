# Steal collateral during `end` process, by earning DSR interest after `flow`.

## Report Details
- **Report ID**: 672664
- **URL**: https://hackerone.com/reports/672664
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-13T21:21:36.953Z
- **Disclosed**: 2019-09-09T16:50:17.991Z

## Reporter
- **Username**: lucash-dev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: makerdao_bbp

## Vulnerability Information
## Summary:

The `end` contract in MCD controls the process of shutting down
the MCD contracts and allowing for users to redeem their DAI for
collateral -- presumably to migrate to a new implementation of DAI.
The process, however, doesn't prevent the continued functioniong
of DAI savings accounts (`pot` contract), which allows for continued
minting of DAI after all other contracts have been "caged", resulting
in theft (possibly involuntary) of collateral.

## Detailed Description

The `end` contract is responsible for orchestrating the complex sequence
of steps for shutting down the MCD eco-system, settling all existing DAI
into collateral during the process.

The first step in the process is the method `cage`, which ensures that other
MCD contracts stop operating in the normal way, and enter a "not-live" mode.
In particular, the `vat` contract is updated to prevent the creation of new
CDP's, and also prevents the accrual of interest (`vat.fold`). This is obtained by
calling the `cage` method in the `vat` contract.

Puzzingly, however, the `end.cage` method doesn't affect the state of the `pot`
(savings account) contract, allowing for interests to be continuously earned
-- and new DAI to be minted --indefinitely during all the phases of the `end`
process. Most significantly, it allows a user to mint new DAI even after the
final DAI/collateral rate has been fixed (`end.flow`).

The consequence is that it's possible to inflate the DAI supply so that there
isn't enough collateral for all of it to be redeemed. In that case the last
users to try to redeem will have their collateral stolen by the faster ones, as
they might well be unable to redeem any DAI at all.

An example might help clarify the problem:

- Suppose there are two users, Ali and Bob, who each control 50% percent of the
DAI supply, lets say 10 DAI each.

- Now let's assume the `end` process is initiated and proceeds as usual --
eventually reaching the `flow` stage, with a fixed exchange rate of 1 DAI / ETH.

- Let's also assume that there is a DSR rate of 100% a month (unrealistic, but makes
the numbers easier).

- After the `end.flow` is called, Ali notices that the he can still use `pot` to earn
interests, so he deposits all his DAI in `pot`. Meanwhile Bob can't do the same
as his funds are locked inside a Dapp (let's say an Augur market).

- After one month, Ali calls `pot.exit` and gets back 20 DAI. That corresponds to
the total original supply of DAI before `end.flow` was called. So, Ali calls
`end.pack` and `end.cash` to convert his 20 DAI into 20 ETH -- all the collateral
in the MCD contracts.

- When Bob tries to redeem his DAI, there is no collateral left. His `end.cash`
calls fail and he ends up with no tokens -- DAI or ETH -- at all.

## Steps to Reproduce

I've attached to this report a version of `end.t.sol` that adds a test scenario
(`test_steal_collateral_using_dsr_after_thaw`) to reproduce this attack (in fact, the example above).

Please don't hesitate to contact me if you need more help reproducing it.

## Possible Remediation

The issue could be completely prevented by introducing a `cage` functionality into
the `pot` contract, and not allowing the `pot.drip` method to be called when
not in live mode.

Please note that the above solution is provided as proof that the reported issue
is fixable. I make no claim that the above is the best available solution.


## Impact

Please refer to the "Impact Analysis" field for more details.

## Final Note

Please don't hesitate to contact me if you need any further clarification around
this issue, or help reproducing and evaluating it.

## Impact

## Impact Analysis

As clearly demonstrated above, the reported bug can be used to steal collateral
from the `end` contract. Even more disturbingly, the bug can likely cause users
that own DSR deposits to unwittingly steal collateral in case of a shutdown.

Let's evaluate how much collateral can be stolen in this scenarios. The amount
stolen depends on three factors:

1 - DSR savings rate.
2 - Portion of DAI kept in DSR deposits.
3 - Time distribution of users calling `end.pack`.

It's impossible to know beforehand either. But we can make educated guesses
about a worst-case scenario.

It's possible that the DSR rate will be set at a high value at some point.
Considering that the previous incarnation of DAI saw a the CDP rate reach
25% at some point, it's definitely possible for DSR to reach a slightly lower
rate, say 20%. Furthermore, it's likely all users (including Dapps) will keep
their DAI holdings in DSR deposits, doing so has a possible upside, and minimal
gas costs.

As for the time-distribution of users redeeming their DAI, it's again entirely
possible that a large portion of the DAI supply will be used to interact with
Dapps rather than held speculatively. Augur V2, for example, has plans to use
DAI for making bets on prediction markets. Since these markets might take
quite a long time to be resolved -- up to several months -- it's unlikely
that a DAI shutdown would cause an immediate withdrawal of DAI by Augur users
-- if the reported vulnerability isn't known.

Other Dapps might well have similar characteristics, though it's again impossible
to know beforehand.

Given the above -- DSR rates up to 20% and most of DAI locked in DSR deposits
inside Dapps for months -- it's perfectly possible that the bug leads to
a loss of 10% or more of the collateral in the MCD contracts.

That scenario might happen even without an intentional attack.

## Attachments
- end.t.sol
