import re
import ipaddress

# 定义正则表达式匹配IP地址和子网掩码
ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
mask_regex = r'/\d+'

# 打开输入和输出文件
with open('ip.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # 遍历输入文件中每一行
    for line in input_file:
        # 使用正则表达式查找匹配的IP网段
        matches = re.findall(ip_regex + mask_regex, line)

        # 遍历每个IP网段
        for match in matches:
            # 将网段转换为IPv4Network对象
            network = ipaddress.IPv4Network(match)

            # 将网络拆分为子网
            subnets = list(network.subnets())

            # 循环输出每个IP地址到输出文件
            for subnet in subnets:
                for host in subnet.hosts():
                    output_file.write(str(host) + '\n')
