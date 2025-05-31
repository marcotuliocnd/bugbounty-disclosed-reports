# Possibility of DOS Through logging System

## Report Details
- **Report ID**: 242489
- **URL**: https://hackerone.com/reports/242489
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-23T01:02:34.052Z
- **Disclosed**: 2017-08-16T22:07:42.178Z

## Reporter
- **Username**: imran-parray
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
The Quora is using HTTP post method to send logs to the Quora Server and save the logs on the server 
Which is not Validating the size of the log data and directly storing a large amount of data on the server.
i mean when the logs are sended to the server a bad guy can use the same HTTP POST method and same Parameter to send a large amount of data to your server because there is no Mechanism to Test incoming logs size and attacker can  fill a large amount of space  on the server.

How To Reproduce:

Normal HTTP Request:

POST https://log.quora.com/ajax/batched_log_POST HTTP/1.1
Connection: keep-alive
Content-Length: 1328
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://www.quora.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.quora.com/
Accept-Language: en-gb
Cookie: m-b="HmerlxRPKlY2P8ZetSoJRA\075\075"; m-s="fApMTrywJ0FDK7OlbICFPg\075\075"; m-css_v=d4987ef9da8d042b; m-login=1; m-early_v=ad51054ba26a785a; m-tz=-330; m-wf-loaded=q-icons-q_serif; _ga=GA1.2.1732973717.1498176387; _gid=GA1.2.1110816896.1498176387
Host: log.quora.com

json=%7B%22args%22%3A%5B%5D%2C%22kwargs%22%3A%7B%22messages%22%3A%5B%7B%22category%22%3A%22action_data%22%2C%22data%22%3A%7B%22data%22%3A%7B%22url%22%3A%22%2Fwebnode2%2Fserver_call_POST%3F_v%3DT8XhSYsCyYcwrs%26_m%3Dget_next_page%22%2C%22vcon%22%3A%5B%22T8XhSYsCyYcwrs%22%5D%2C%22method%22%3A%22get_next_page%22%2C%22args%22%3Anull%2C%22kwargs%22%3Anull%2C%22startTime%22%3A1498176435253%2C%22id%22%3A%22er24r3s3oi%22%2C%22controller%22%3A%22webnode2%22%2C%22action%22%3A%22server_call_POST%22%2C%22standard%22%3A%7B%7D%2C%22serverTime%22%3A2552628%2C%22endTime%22%3A1498176439423%7D%7D%2C%22time%22%3A1498176439423000%7D%2C%7B%22category%22%3A%22perf%2Fpost_e2e%22%2C%22data%22%3A%7B%22vcon%22%3A%5B%22T8XhSYsCyYcwrs%22%5D%2C%22method%22%3A%22get_next_page%22%2C%22type%22%3A%22web%22%2C%22duration%22%3A4436%7D%2C%22time%22%3A1498176439690000%7D%2C%7B%22category%22%3A%22perf%2Fpost_e2e%22%2C%22data%22%3A%7B%22vcon%22%3A%5B%22T8XhSYsCyYcwrs%22%5D%2C%22method%22%3A%22get_next_page%22%2C%22type%22%3A%22user_perceived%22%2C%22duration%22%3A4436%7D%2C%22time%22%3A1498176439690000%7D%5D%2C%22nid%22%3A0%7D%7D&revision=7a0b4942858186e883835568054f3089311f25c1&formkey=c990bafe6dcaaf22d5939994fc0a2bca&postkey=42e50148a09db5abeef10502c90ea3ce&window_id=dep3101-4180021445674349298&referring_controller=index&referring_action=index

-->End of The Request<--

the Parameter json= carries a data which is url encoded

Attacker can encode His Payload of large size [say 2.0 MB ] and paste in the HTTP Request and send to the server and server is Successfully Accepting the Request and Saveing his large amount of data [2.0 mb] on your server.
This time the hacker can send this http request 1000000 times to fill up whole memory on the server and cause the server to crash or slow down.


POC

in Video i have showed a little Description how Hackers can Perform a Delicious Attack using quora Log System !


## Attachments
- POC.avi
