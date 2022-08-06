import re


def reader(filename):
    count = 0
    list_success_devices = {}
    list_fail_devices = []
    with open(filename) as f:
        # log = f.readline()

        # regexp = re.findall(r'02', log, re.I)

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
            # print(key)
            if key in list_success_devices:
                del list_success_devices[key]
                # print(key)



    print(f'Device {list_success_devices} status {list_fail_devices} \n fail {list_fail_devices}')
    # print(log)


if __name__ == '__main__':
    reader('app_2.py')
