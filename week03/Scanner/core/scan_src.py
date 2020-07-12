import socket
import time
import os
import struct
import select
import argparse
from multiprocessing.pool import Pool
from multiprocessing import Queue,Process
from logging import config,getLogger
import json

from conf import settings

config.dictConfig(settings.LOGGING_DIC)
log = getLogger('ipcheck')
log_port = getLogger('portcheck')

ICMP_ECHO_REQUEST=8
class IPCheck:
    success_ip = Queue()  # 存放可用ip
    timeout = 10
    sequence_id = 1 # icmp报文 序列号

    def __init__(self, dst_ip):
        self.dst_ip = dst_ip
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        self.pid = os.getpid()
        self.sequence_id += 1

    def run(self):
        log.debug('IPCheck run()')
        '''发送回显请求,读取回显应答'''
        self.send()
        self.read()

    def send(self):
        log.debug('IPCheck send() 发送icmp报文到{}'.format(self.dst_ip))
        header= struct.pack("BBHHH", 8, 0, 0, self.pid, self.sequence_id)  # 构建一个空header
        data = struct.pack("d",time.time())  # icmp 的数据

        cksum = self.check_sum(header + data)  # 头和数据 校验和

        header= struct.pack("BBHHH", 8, 0, socket.htons(cksum), self.pid, self.sequence_id)  # 主机字节序转换成网络序

        packet = header + data

        self.my_socket.sendto(packet, (self.dst_ip, 80))

    def check_port(self, start_port, end_port):
        log.debug('IPCheck check_port')
        port_list = []

        for port in range(start_port, end_port + 1):
            log.info('[{}]:port[{}] 检测'.format(self.dst_ip, port))
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)    #这一句用来设置超时
            status = sock.connect_ex((self.dst_ip, port))
            time.sleep(0.5)
            if status == 0:
                port_list.append(port)
                # print(port)
                log.info('[{}]:port[{}] 开放'.format(self.dst_ip, port))
            else:
                log.info('[{}]:port[{}] 关闭'.format(self.dst_ip, port))
            sock.close()
        # print('ip[{}] 端口开放的有:{}'.format(self.dst_ip, port_list))
        log_port.info('ip[{}] 端口开放的有:{}'.format(self.dst_ip, port_list))

    def read(self):
        log.debug('IPCheck read() 从{}读取数据'.format(self.dst_ip))
        while True:
            started_select = time.time()
            what_ready = select.select([self.my_socket], [], [], self.timeout)
            wait_for_time = (time.time() - started_select)
            if what_ready[0] == []:  # Timeout
                raise Exception('{} 连接超时'.format(self.dst_ip))
            time_received = time.time()
            received_packet, addr = self.my_socket.recvfrom(1024)
            icmpheader = received_packet[20:28]
            # 一个ICMP报文包括IP头部（20字节）、ICMP头部（8字节）前20个字节是ip头部
            m_type, code, checknum, process_id, sequence = struct.unpack("BBHHH",icmpheader)
            if process_id == self.pid:
                log.info('收到来自 {} 的回复'.format(addr[0]))
                time_sent=struct.unpack("d",received_packet[28:])[0]
                self.success_ip.put((self.dst_ip, started_select - time_sent))
                log.info('{} put to queue'.format((self.dst_ip, started_select - time_sent)))
                break

    def check_sum(self, data):
        '''校验和计算'''
        n = len(data)
        m = n % 2
        sum = 0
        # 字节长度可能是奇数,单独拿出来最后一个之值
        for i in range(0, n - m ,2):
            sum += (data[i]) + ((data[i+1]) << 8)  # 传入data以每两个字节（十六进制)，第一字节在低位，第二个字节在高位
        if m:
            sum += (data[-1])
        # 将高于16位与低16位相加
        sum = (sum >> 16) + (sum & 0xffff)
        sum += (sum >> 16)  # 如果还有高于16位，将继续与低16位相加
        answer = ~sum & 0xffff
        # 主机字节序转网络字节序列（参考小端序转大端序）
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

def check_ip(ip):
    '''
    进程入口函数,每一个进程对应一个IPCheck对象,做ping检测
    '''
    # print('{}:检测开始'.format(ip))
    log.info('{}:检测开始'.format(ip))
    ck = IPCheck(ip)
    try:
        time.sleep(0.5)
        ck.run()
    except Exception as e:
        log.warning('{} 连接超时, ip不可用'.format(ip))
        # print(e)
    # print('{}:检测结束'.format(ip))
    log.info('{}:检测结束'.format(ip))


def product_ip(ip_scope):
    # ip_scope 是一个字符串表示的范围需要拆分,'192.168.0.1-192.168.0.100'
    start_ip, end_ip = ip_scope.split('-')
    start_ip_pos_a, start_ip_pos_b, start_ip_pos_c, start_ip_pos_d =\
        start_ip.split('.')

    end_ip_pos_a, end_ip_pos_b, end_ip_pos_c, end_ip_pos_d =\
        end_ip.split('.')

    # str->int
    start_ip_pos_a = int(start_ip_pos_a)
    start_ip_pos_b = int(start_ip_pos_b)
    start_ip_pos_c = int(start_ip_pos_c)
    start_ip_pos_d = int(start_ip_pos_d)
    end_ip_pos_a = int(end_ip_pos_a)
    end_ip_pos_b = int(end_ip_pos_b)
    end_ip_pos_c = int(end_ip_pos_c)
    end_ip_pos_d = int(end_ip_pos_d)

    while True:
        if (start_ip_pos_a == end_ip_pos_a and\
            start_ip_pos_b == end_ip_pos_b and\
            start_ip_pos_c == end_ip_pos_c and\
            start_ip_pos_d == end_ip_pos_d):
            break

        # 逢 255 进到上一个字段
        if start_ip_pos_d == 255:
            start_ip_pos_b += 1
            start_ip_pos_d = 0
        if start_ip_pos_b == 255:
            start_ip_pos_c += 1
            start_ip_pos_b = 0
        if start_ip_pos_c == 255:
            start_ip_pos_d += 1
            start_ip_pos_c = 0
        if start_ip_pos_d == 255:
            print('ip error')
            break

        ip_addr = '{}.{}.{}.{}'.format(start_ip_pos_a,\
                                   start_ip_pos_b,\
                                   start_ip_pos_c,\
                                   start_ip_pos_d)
        start_ip_pos_d += 1
        yield ip_addr
    yield end_ip


def start():
    parser = argparse.ArgumentParser(description='scanner')
    parser.add_argument('-n', type=int, default=12, help='number of concurrent')
    parser.add_argument('-f', choices=['ping', 'tcp'], default='tcp', help='ping or tcp protocol')
    parser.add_argument('-ip', type=str, required=True, help='ip range 192.168.0.1-192.168.0.100')
    # parser.add_argument('-w', action='count', default=0, help='save to file')
    parser.add_argument('-w', '--write', dest='file_out',
                        default='', type=str, help='target Write to File')
    parser.add_argument('-m', choices=['proc', 'thread'], default='proc', help='multiprocess or multithread',
                        required=False)
    parser.add_argument('-v', action='count', default=0, help='show elapsed time')
    args = parser.parse_args()

    if 'ping' == args.f:
        with Pool(processes = args.n) as pool:
            it = pool.imap(check_ip, product_ip(args.ip))
            for _ in it:
                # print(i)
                pass
        success_ip_dic = {'success_ip': []}
        while True:
            try:
                ip_time =IPCheck.success_ip.get(timeout = 10)
                log.info('成功的ip:{}'.format(ip_time))
                success_ip_dic['success_ip'].append(ip_time)
            except Exception as e:
                # print(e)
                if args.file_out:
                    # 保存到指定文件
                    with open(os.path.join(settings.LOG_DIR, args.file_out), mode = 'wt', encoding = 'utf-8') as log_file:
                        json.dump(success_ip_dic, log_file)
                print(e,success_ip_dic)
                log.warning('队列为空, 等待超时')
                break

    elif 'tcp' == args.f:
        # 端口扫描
        ck = IPCheck(args.ip)
        ck.check_port(1, 1024)

