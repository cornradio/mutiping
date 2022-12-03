import subprocess
import multiprocessing
import time

def check_alive(ip):
    #subprocess.call()的输出反馈有3个，分别是0，1，2。其中0代表正确执行，1和2都是错误执行，2通常是没有读取到文件，1的反馈目前未知。
    result = subprocess.call(f'ping  -c 3 {ip}', stdout=subprocess.PIPE, shell=True)
    if result == 0:
        print(f'{ip}\t\033[32m[ok]\033[0m\t--\t'.replace("\n","") )
    else:
        print(f'{ip}\t\033[31m[bad]\033[0m\t--\t'.replace("\n",""))


if __name__ == '__main__':
    print('结果使用tab分隔，可以拷贝到excel中，通过数据透视进行ip排序等')
    # 获取所有当前目录下的txt文件并存入 txtfile_list
    import os
    path = "./"
    file_name_list = os.listdir(path)
    txtfile_list = []
    for x in file_name_list:
        if x.__contains__('.'):
            if x.split('.')[1] == "txt":
                iin = input(f"发现txt：{x}，是否加入测试队列？（y/n）")
                if iin == "n":
                    continue
                else:
                    txtfile_list.append(x)
                    print("已加入！")
    print(txtfile_list)

    MUTIPROCESS = True

    for x in txtfile_list:
        print(f"scaning {x} :")
        x = path + x
        # input("enter 开始ping")
        with open(x, 'r') as f:  # xxx.txt 内容应该包含ip地址，每行一个，可以写#开头的备注
            print(f'ipaddress\t[ok]\tlatency\t'.replace("\n", ""))
            for line in f:
                # 识别ip地址,#可以作为备注
                if line.__contains__("#"):
                    # print("comment: " + line)
                    continue
                if len(line.split('.')) == 4:
                    if MUTIPROCESS: # 多线程模式
                        # print(line)
                        p = multiprocessing.Process(target=check_alive, args=(line,))
                        p.start()
                    else: #单线程模式
                        check_alive(line)


        # 等待多线程数量为0（ping均结束）后开启下一个txt的扫描
        while True:
            if len(multiprocessing.active_children()) == 0:
                # print('thread count: '+ str(len(multiprocessing.active_children())) +' ,scan complete\n\n')
                print("------------")
                break
            time.sleep(3)
