# FAKE-X1C

Fake the broadcasts of a Bambu Lab X1 Carbon 3D printer so you can use it via VPN.

## Why?

The bambu lab X1C emits a broadcast containing its IP address and name regularly.
The Orca-Slicer plugin for the X1C will only show printers in the "Device" tab when
it receives those broadcasts. 

If your computer is not connected to the same LAN (e.g. you are connected via VPN or 
you are in a different subnet) then the slicer will not be able to send the print
data to the printer. Entering the IP address directly is not possible.

This little script is a proof-of-concept. It immitates the broadcast messages from the
printer and sends them out on your local machine for the slicer to receive.

## Important notice

This was last tested in March 2024. Please use wireshark to sniff broadcast from the X1C
and check if the `ANNOUNCEMENT_TEMPLATE` variable still is compatible with the 
announcements the X1C is broadcasting. 

## Usage

```
usage: fake_x1c.py [-h] printerip printername [bind_addr]

positional arguments:
  printerip    IPv4 address of the Bambu X1C printer (in LAN mode), e.g. 192.168.1.42
  printername  printer name as it appears in the device pane of OrcaSlicer/Bambustudio
  bind_addr    the address to bind to when sending the broadcast message

options:
  -h, --help   show this help message and exit
```

Example: `fake_x1c/fake_x1c.py 10.0.0.217 EXA-MPL-EXX`

## Using sniff_x1c.py to decode the SSDP discovery broadcast:

In order to find out the values for `printerip` and `printername` above, there is a
small helper program called `sniff_x1c.py`. This script will listen for UDP broadcasts
of the X1C and print the on the screen. You can copy+paste the output of `sniff_x1c.py`
into `fake_x1c.py` to make sure your fake messages look exactly like the ones from your
X1C.

You need to be on the same network and be able to receive the broadcasts for this to work.

## Usage of sniff_x1c.py

```
usage: sniff_x1x.py [-h] [bind_addr]

positional arguments:
  bind_addr   IP address to bind the listening socket to.

options:
  -h, --help  show this help message and exit
```