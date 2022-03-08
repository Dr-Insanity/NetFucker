# NetFucker

NetFucker: Denying all network packets/connections for your fellow network users


### A moment, please...
Don't rush in, now. I aimed to make this user-friendly. There's configuration to be done before using the application. I'll cover the steps later. So read this README.MD carefully.

## requirements
- [`Git`](https://git-scm.com/download/linux)
- [`Python 3.10+`](https://www.python.org/downloads/)

The rest is pretty much auto-installed.

## Installation

Clone this repository & CD into it.

```bash
git clone https://github.com/Dr-Insanity/NetFucker.git
cd NetFucker
```

## Usage
First, the configuration is needed. You need to tell NetFucker in `/Configuration/config.ini` what your IP range is. 

Here's an example
```ini
[DEFAULT]
ip_range = 192.168.0.0/24
; You're free to copy this and adjust the ip_range, if needed.


```
Once that's done, you may execute
```bash
sudo python3 nefilt_q.py
```

That is really required to be run as root, because:
- [`Scapy`](https://pypi.org/project/scapy/) needs to put your interface into monitor mode
- [`iptables`](https://linux.die.net/man/8/iptables) needs to be ran as root in order to write/execute.

It'll do some auto installing/updating of dependencies and pop up a nice banner, prompting you to continue. We're going to start sending ARP requests right after pressing enter

#### still have issues?
I have slightly tested this on a mobile device with [Termux](https://termux.com/). It turns out I had some errors while importing [`colorama`](https://pypi.org/project/colorama/) - It wasn't installed. If you get such errors, you could likely get around it by yourself. I haven't tested my application much on different platforms. I do know that Debian works fine, since I work on that.

Moving on with the usage of **NetFucker**:
```python
# I have to add that below details are completely generated. Purely for this example.
[1]       192.168.0.11        6C:45:03:6F:04:EE
[2]       192.168.0.14        51:31:D2:80:EA:1C
[3]       192.168.0.16        B6:60:EE:99:3B:B8
[4]       192.168.0.12        A7:27:D4:3F:DF:84
[5]       192.168.0.13        09:2B:EA:D5:D7:FC
[6]       192.168.0.17        D9:9D:79:2C:87:71
[7]       192.168.0.135       F1:E4:89:5A:F9:D8
[8]       192.168.0.121       86:B4:DC:57:BA:1D
[9]       192.168.0.18        99:73:50:69:04:A7
[10]      192.168.0.35        2A:02:49:EC:D8:35
[11]      192.168.0.15        38:A4:D8:EE:15:05
Pick a target by its number on the left
NetFucker>
```
Pick a target or more by typing the number next to your chosen target. If you wish to cancel multiple host's their packets type it like this
```
NetFucker>1, 5, 8, ... (and so on)
```

## Disclaimer
I do not condone illegal activities. I discourage non-ethical use of my application. I only developed this program. Anything that you do with this application is not done by me and therefore you're the only one responsible for any damage you cause. By using this application, you fully understood and agreed with what I just said and you understand you're on your own when you're charged or in a lawsuit, unless you got others rooting for you. It won't be me.

## Contributing
This project is __**NOT**__ open to contributions, but I thank you for your good intentions 🙏.