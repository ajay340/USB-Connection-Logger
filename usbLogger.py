import usb1
from datetime import datetime
import os
import sys

current_time = str((datetime.now()))

log_first ="USB Connection "
log_extension = (".log")
log_date = str(datetime.now())[0:16]
log_middle = log_first.__add__(log_date)
log_name = log_middle.__add__(log_extension)

def hotplug_callback(context, device, event):

    print('%s: "%s" %s \n' % (
        str(datetime.now())[0:19],
        device,
        {
            usb1.HOTPLUG_EVENT_DEVICE_ARRIVED: 'has CONNECTED',
            usb1.HOTPLUG_EVENT_DEVICE_LEFT: 'has DISCONNECTED',
        }[event],
    ))
    with open(log_name, "a") as log:
        log.write(
        '%s: "%s" %s \n' % (
            str(datetime.now())[0:19],
            device,
            {
                usb1.HOTPLUG_EVENT_DEVICE_ARRIVED: 'has CONNECTED',
                usb1.HOTPLUG_EVENT_DEVICE_LEFT: 'has DISCONNECTED',
                }[event],))



def main():
    with usb1.USBContext() as context:
        if not context.hasCapability(usb1.CAP_HAS_HOTPLUG):
            print('Hotplug support is missing. Please update your libusb version.')
            return

        print('Checking if libusb driver is installed...')
        print('Driver is installed, now monitoring usb connections to device...\n')
        opaque = context.hotplugRegisterCallback(hotplug_callback)

        try:
            while True:
                context.handleEvents()

        except (KeyboardInterrupt, SystemExit):
            print('Exiting')


if __name__ == '__main__':

    main()
