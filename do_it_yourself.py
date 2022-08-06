

def reader(filename):
    list_success_devices = {}
    list_fail_devices = []
    with open(filename) as f:

        for line in f:

            if 'BIG' in line:
                st = line.split(";")
                if st[-2] == '02':
                    if st[2] in list_success_devices:
                        count = list_success_devices.get(st[2]) + 1
                        list_success_devices.update({st[2]: count})
                    else:
                        list_success_devices.update({st[2]: 1})
                else:
                    if st[2] not in list_fail_devices:
                        list_fail_devices.append(st[2])

        for key in list_fail_devices:
            if key in list_success_devices:
                del list_success_devices[key]
        print(f'__________________Failed test {len(list_fail_devices)}_________________')
        for i in list_fail_devices:
            print(f'Device {i} was removed')
        print(f'__________________Failed test {len(list_success_devices)}_________________')
        for key, value in list_success_devices.items():
            print(f'Device {key} sent {value} statuses')


if __name__ == '__main__':
    reader('app_2.py')
