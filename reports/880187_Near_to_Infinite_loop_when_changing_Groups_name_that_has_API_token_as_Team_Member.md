# Near to Infinite loop when changing Group's name that has API token as Team Member

## Report Details
- **Report ID**: 880187
- **URL**: https://hackerone.com/reports/880187
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-22T02:43:54.512Z
- **Disclosed**: 2020-07-23T21:54:16.366Z

## Reporter
- **Username**: wlucenasec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

The  `https://hackerone.com` contains an iteration or loop with an exit condition that is near to infinite loop. If the loop can be influenced by an attacker, this weakness could allow attackers to consume excessive resources such as CPU or memory and even a DoS attack.

**Description:**
Hello Security team,

I  have a test Enterprise Program `https://hackerone.com/tonight_ptdkf` enabled in my second H1 account. Last days I have been hunting on the program features and I have founded a weird behavior that can consume excessive resources on the platform.

Under the `group management` feature the program administrator can add a new `group` to segregate the permissions. The website runs the following function to create the group on the platform.

```javascript
{
            Object(u.a)(a, e);
            var t = Object(c.a)(a);
            function a() {
                var e;
                return Object(o.a)(this, a),
                (e = t.call(this)).teamMemberGroups = new bO,
                e.teamMemberGroup = new fO,
                e.availablePermissions = [],
                e.currentTeam = new Lf,
                e.teamMembers = new PO,
                e.fetched = !1,
                e.savingTeamMemberGroupMembers = !1,
                e.selectedTeamMemberGroups = {},
                e
            }
```
```javascript
{
                key: "new",
                value: function(e) {
                    var t = this;
                    this.loadResources(e).always((function() {
                        t.fetched = !0,
                        t.teamMemberGroup = new fO,
                        t.availablePermissions = t.currentTeam.get("available_permissions"),
                        t.trigger("change")
                    }
                    ))
                }

```
 Once the group is created its can be read in `JSON` format throuhg the page `https://hackerone.com/[YOUR_PROGRAM]/groups.json`, as example below:

```javascript
{
	"id":95038,
	"key":null,
	"name":"Testing",
	"team_members_count":0,
	"permissions":[
	],
	"immutable":false,
	"team_member_ids":[
	]
}
```
{F838205}

From the `group management` page the program administrator can add only users to that group, can't add API token to that group from there.

{F838206}

But the API token can be added to that group through `https://hackerone.com/[YOUR_PROGRAM]/api`.

{F838209}

Clicking on **Manage groups** is possible to add this API token to the previously created group.

{F838210}

Once you save that, you can read this API token permission/groups in `JSON` format too, just goint to `https://hackerone.com/[Your_Program]/team_members/[The team member ID of your API toke].json`

Just like before, the same data will be displayed.

```javascript
{
	"id":95038,
	"key":null,
	"name":"Testing",
	"team_members_count":0,
	"permissions":[
	],
	"immutable":false,
	"team_member_ids":[
	]
}
```
Also, the `group` will be displayed under API Token page.

{F838211}

The issue comes when we `change` this `group` name that is linked to the API Token. So, in my test I changed from `Testing` to `AAABC2`.

More than `500` repeated JSON key `{"id":95004,"key":null,"name":"AAABC2","team_members_count":0,"permissions":[],"immutable":false,"team_member_ids":[]}` due to the loop issue.

{F838226}

As far as I understood from a static code analysis, the loop that is causing this issue is:

```javascript
!function(e) {
    function t(t) {
        for (var n, s, l = t[0], o = t[1], c = t[2], m = 0, d = []; m < l.length; m++)
            s = l[m],
            Object.prototype.hasOwnProperty.call(r, s) && r[s] && d.push(r[s][0]),
            r[s] = 0;
        for (n in o)
            Object.prototype.hasOwnProperty.call(o, n) && (e[n] = o[n]);
        for (u && u(t); d.length; )
            d.shift()();
        return i.push.apply(i, c || []),
        a()
    }
```
{F838219}
### Steps To Reproduce

* Add a new group under group management of your program
* Under the API Token, link your API to the group created in the previous step 
* Go back to the group management and change the group name

Note: Sometimes that server will not be able to handle the large repeated infomation in this loop when changing the group name and will response `500`.

{F838230}

## Impact

If the loop can be influenced by an attacker, this weakness could allow attackers to consume excessive resources such as CPU or memory and even a DoS attack.

## Attachments
- group_management.JPG
- members.JPG
- API_Tokens.JPG
- members_2.JPG
- API_Token_Member.JPG
- function_loop.JPG
- loop_json.JPG
- response_500.JPG
