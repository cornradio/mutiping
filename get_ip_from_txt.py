iplist = []
# 打开文件
with open('ip.txt', 'r',encoding = 'utf-8') as file:
    # 逐行读取文件内容并打印
    for line in file:
        if not (line.strip() == '') and not (line.startswith('#')): #如果line是 # 开头 或者是空行 则不要
            iplist.append(line.strip())# 使用strip()方法删除行尾的换行符

iplist = list(set(iplist)) # 通过set转换，去重

print(len(set(iplist)))


# 过滤一些ip到ipfilt_list
ipfilt_list = []
for ip in iplist:
    if ip.startswith('10.') or ip.startswith('192.168.14.'):
        ipfilt_list.append(ip)

# 通过set计算反转list获取其他的ip
ipfilt_reverse = list(set(iplist) - set(ipfilt_list))

for ip in ipfilt_reverse:
    print(ip)
