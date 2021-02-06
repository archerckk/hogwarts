import yaml


def get_config_data():
    with open('D:\hogwarts\mitmproxy_hw\config.yml')as f:
        data=yaml.safe_load(f)
    return data





data = get_config_data()

for i in data['pararms_del']:
    print(i)
