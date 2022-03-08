'''

Написать функцию host_range_ping_tab(), возможности которой основаны на
функции из примера 2. Но в данном случае результат должен быть итоговым по
всем ip-адресам, представленным в табличном формате (использовать модуль
tabulate).

'''

import tabulate
from homework2 import host_range_ping


def host_range_ping_tab():

    available, not_available = host_range_ping()
    pr = {'available': [], 'not_available': []}
    for i in available:
        pr['available'].append(i)
    for i in not_available:
        pr['not_available'].append(i)

    print(tabulate.tabulate(pr, headers='keys', tablefmt='grid'))




if __name__ == '__main__':

    host_range_ping_tab()