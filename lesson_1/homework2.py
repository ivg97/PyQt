'''

Написать функцию host_range_ping() для перебора ip-адресов из заданного
диапазона. Меняться должен только последний октет каждого адреса. По
результатам проверки должно выводиться соответствующее сообщение.
'''
import homework

def host_range_ping():

    ip1 = input('Input Address: ')
    # ip1 = '192.168.0.1'
    range_ip = int(input('Input range: '))
    # range_ip = 5
    ip_list = []
    for i in range(1, range_ip):
        try:
            oct_3 = int(ip1.split('.')[3])

            if int(oct_3) == range_ip:
                break
            else:
                oct_3 += 1
                ip1 = ip1.split('.')[:3]
                ip1.append(str(oct_3))
                ip1 = '.'.join(ip1)
                ip_list.append(ip1)

        except Exception as err:
            print(err)
    # print(ip_list)
    result = homework.host_post(ip_list)
    return result


if __name__ == '__main__':

    host_range_ping()
