import math

def ip_to_int(ip: str):
    a = ip.split(".")
    v = 0
    v += int(a[0]) << 24
    v += int(a[1]) << 16
    v += int(a[2]) << 8
    v += int(a[3])
    return v


def int_mask_to_ip(intmask: int):
    str = ""
    for i in range(4):
        count = max(0, 8 - intmask)
        str += "%d." % ((255 >> count) << count)
        intmask -= 8
    return str[:-1]


def ip_str_to_sub_mask(ipstr: str):
    ipstr = ipstr.replace("\n", "")
    ips = ipstr.split(" ")

    left = ip_to_int(ips[0])
    right = ip_to_int(ips[1])
    int_mask = 32 - int(math.log2(right + 1 - left))
    return "route %s %s net_gateway\n" % (ips[0], int_mask_to_ip(int_mask))


path = "chn_ip.txt"
string = ""
with open(path, "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        string += ip_str_to_sub_mask(line)

f = open("openvpn.txt", "w")
f.write(string)
