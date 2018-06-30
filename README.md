# USB Connection Logger
This is a program that record USB device connection entries to your computer.

This can be used for investigations for logging if an external threat tried/has exfilitrated data or inputted a [malicious USB device](https://hakshop.com/products/usb-rubber-ducky-deluxe).

## Install
You will need to have python3 install along with the [libusb driver](https://libusb.info) for your operating system.

Then
```
pip3 install libusb1
```
## Compiling
If you want the program to run in the background without a the python console running, you will need to have pyinstaller installed.

Then
```
pyinstaller usbLogger.py --onefile --no-window --noconsole
```

## Example Log:
```python
2018-06-30 01:49:26: "Bus 020 Device 033: ID 154b:005b" has CONNECTED 
2018-06-30 01:49:30: "Bus 020 Device 033: ID 154b:005b" has DISCONNECTED 
2018-06-30 01:49:35: "Bus 020 Device 034: ID 1050:0116" has CONNECTED 
2018-06-30 01:49:36: "Bus 020 Device 034: ID 1050:0116" has DISCONNECTED 
2018-06-30 01:49:53: "Bus 020 Device 035: ID 05e3:0610" has CONNECTED 
2018-06-30 01:49:53: "Bus 000 Device 001: ID 05e3:0616" has CONNECTED 
2018-06-30 01:49:55: "Bus 000 Device 001: ID 05e3:0616" has DISCONNECTED 
2018-06-30 01:49:55: "Bus 000 Device 002: ID 05e3:0616" has CONNECTED 
2018-06-30 01:50:06: "Bus 020 Device 036: ID 154b:005b" has CONNECTED 
2018-06-30 01:50:12: "Bus 020 Device 037: ID 1050:0116" has CONNECTED 
2018-06-30 01:50:16: "Bus 020 Device 035: ID 05e3:0610" has DISCONNECTED 
2018-06-30 01:50:16: "Bus 020 Device 036: ID 154b:005b" has DISCONNECTED 
2018-06-30 01:50:16: "Bus 000 Device 002: ID 05e3:0616" has DISCONNECTED 
2018-06-30 01:50:17: "Bus 020 Device 037: ID 1050:0116" has DISCONNECTED 
```
