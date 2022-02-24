'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет
проверяться доступность сетевых узлов. Аргументом функции является список,
в котором каждый сетевой узел должен быть представлен именем хоста или
ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность
 с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
 При этом ip-адрес сетевого узла должен создаваться с помощью функции
 ip_address().
'''
import ipaddress
import socket
import subprocess



def host_post(ip_list):
    result = []
    not_result = []
    for ip in ip_list:
        try:
            ipv4 = str(ipaddress.ip_address(ip))
        except ValueError:
            ipv4 = str(socket.gethostbyname(ip))
        ping_result = subprocess.Popen(['ping', ipv4], shell=True,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
        ping_result.wait()

        if ping_result.returncode == 1:
            # print(ip, ' - узел доступен')
            result.append(ip)
        else:
            # print(ip, ' - узел недоступен')
            not_result.append(ip)

    return (result, not_result,)


if __name__ == '__main__':

    list_ip = [
        'yandex.ru',
        '8.8.8.8',
        '0.0.0.0',
    ]

    host_post(list_ip)



