import subprocess
import multiprocessing
import  time

def check_alive(ip):
    result = subprocess.call(f'ping -w 1000 -n 2 {ip}', stdout=subprocess.PIPE, shell=True)
    # 等待超时时间1000ms ， 测试次数 2次
    if result == 0:
        h = subprocess.getoutput('ping ' + ip)
        returnnum = h.split('平均 = ')[1]
        print(f'{ip}\t\033[32m[ok]\033[0m\t{returnnum}\t'.replace("\n","") )
    else:
        print(f'{ip}\t\033[31m[bad]\033[0m'.replace("\n",""))


if __name__ == '__main__':
    print('结果使用tab分隔，可以拷贝到excel中，通过数据透视进行ip排序等')
    # 获取所有当前目录下的txt文件并存入 txtfile_list
    import os
    path = "."
    file_name_list = os.listdir(path)
    txtfile_list = []
    for x in file_name_list:
        if x.__contains__('.'):
            if x.split('.')[1] == "txt":
                txtfile_list.append(x)
    print(txtfile_list)

    MUTIPROCESS = True

    for x in txtfile_list:
        print(f"scaning {x} :")
        # input("enter 开始ping")
        with open(x, 'r') as f:  # xxx.txt 内容应该包含ip地址，每行一个，可以写备注因为下面会
            print(f'ipaddress\t[ok]\tlatency\t'.replace("\n", ""))
            for line in f:
                # 识别ip地址
                if len(line.split('.')) == 4:
                    if MUTIPROCESS: # 多线程模式
                        p = multiprocessing.Process(target=check_alive, args=(line,))
                        p.start()
                    else: #单线程模式
                        check_alive(line)
                # 展示非ip行内容
                # else:   print(line)

        # 等待多线程数量为0（ping均结束）后开启下一个txt的扫描
        while True:
            if len(multiprocessing.active_children()) == 0:
                # print('thread count: '+ str(len(multiprocessing.active_children())) +' ,scan complete\n\n')
                print("------------")
                break
            time.sleep(3)