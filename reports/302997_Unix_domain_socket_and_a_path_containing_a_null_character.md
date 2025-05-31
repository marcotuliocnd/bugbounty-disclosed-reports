# Unix domain socket and a path containing a null character

## Report Details
- **Report ID**: 302997
- **URL**: https://hackerone.com/reports/302997
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-01-07T09:18:54.893Z
- **Disclosed**: 2018-03-31T05:38:52.892Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Some methods on UNIX domain socket are not checked for null characters.

```
[vagrant@localhost ~]$ ls /tmp
[vagrant@localhost ~]$ irb
irb(main):001:0> require 'socket'
=> true

irb(main):002:0> UNIXServer.open("/tmp/socket\0ruby") {|serv|
irb(main):003:1*   c = UNIXSocket.open("/tmp/socket\0sapphire")
irb(main):004:1>   s = serv.accept
irb(main):005:1>   s.write "from server"
irb(main):006:1>   c.write "from client"
irb(main):007:1>   p c.recv(20)
irb(main):008:1>   p s.recv(20)
irb(main):009:1> }
"from server"
"from client"
=> "from client"

irb(main):010:0> UNIXServer.open("/tmp/socket2") {|serv|
irb(main):011:1*   c = Socket.unix("/tmp/socket2\0emerald")
irb(main):012:1>   s = serv.accept
irb(main):013:1>   s.write "from server"
irb(main):014:1>   p c.recv(20)
irb(main):015:1> }
"from server"
=> "from server"

# safe
irb(main):016:0> Socket.unix_server_loop("/tmp/socket3\0yellow")
Traceback (most recent call last):
        5: from /home/vagrant/.rbenv/versions/2.5.0/bin/irb:11:in `<main>'
        4: from (irb):16
        3: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/socket.rb:1163:in `unix_server_loop'
        2: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/socket.rb:1108:in `unix_server_socket'
        1: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/socket.rb:1108:in `lstat'
ArgumentError (path name contains null byte)
irb(main):017:0> Socket.unix_server_socket("/tmp/socket3\0yellow")
Traceback (most recent call last):
        4: from /home/vagrant/.rbenv/versions/2.5.0/bin/irb:11:in `<main>'
        3: from (irb):17
        2: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/socket.rb:1108:in `unix_server_socket'
        1: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/socket.rb:1108:in `lstat'
ArgumentError (path name contains null byte)
```

## Impact

It may be connected to an unintended socket.

## Attachments
No attachments
