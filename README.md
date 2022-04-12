# picoweb
All of the picoweb files collected together in one place

I started playing with the Pyboard D (in particular the SF2) and wanted
to get some web services up and running. Looking at the forum, using
picoweb seemed like the best way forward.

I was unable to get upip installed since it needs Python2 and my machine
no longer has that installed.

So I downloaded the appropiate packages from PyPi.org and collected them
altogether in this repository.

I also added wifi.py and a wifi_config.py that you'll need to edit with
your own SSID and password.

You need to copy all of the files to /flash on your pyboard D. Using rshell you
can use:
```
cp -r * /flash
```
Then from the REPL, you can do:
```
>>> import wifi
Connecting to YOUR-SSID ...
Network Config: ('192.168.0.239', '255.255.255.0', '192.168.0.1', '192.168.0.1')
>>> from picoweb import example_webapp
* Running on http://0.0.0.0:80/
INFO:picoweb:703032636.642 <HTTPRequest object at 20011210> <Stream object at 20010740> "GET /"
INFO:picoweb:703032684.326 <HTTPRequest object at 20014980> <Stream object at 20014780> "GET /file"
INFO:picoweb:703032684.326 <HTTPRequest object at 200197c0> <Stream object at 20014540> "GET /squares"
```

