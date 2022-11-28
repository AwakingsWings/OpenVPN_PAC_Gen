# OpenVPN_PAC_Gen
从网段生成OpenVPN识别的子网掩码启动参数.
(Generating the OpenVPN-recognized subnet mask startup parameters from the network segment.)

# Step 1
将网段文件chn_ip.txt放置在同目录下，其格式为多行 首ip+空格+尾ip

# Step 2
运行gen.py,需要python3

# Step 3
将其复制到.ovpn客户端中，并删除block-outside-dns（如果openvpn版本较低，可能还需要添加
