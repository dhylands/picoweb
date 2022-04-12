import network
import wifi_config

def do_connect(ssid, pwd):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to {} ...'.format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('Network Config:', sta_if.ifconfig())

# Attempt to connect to WiFi network
do_connect(wifi_config.ssid, wifi_config.password)
