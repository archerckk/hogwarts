import yaml
import json





# def get_config_data():
#     with open('D:\hogwarts\mitmproxy_hw\config.yml')as f:
#         data=yaml.safe_load(f)
#     return data
#
#
#
#
#
# data = get_config_data()
#
# for i in data['pararms_del']:
#     print(i)

import json
json_data= '{"content":{"text_content":{"content":"iuuuu"}},"peer_id":872471,"type":1,"seq_id":1612691290284,"nick":"English man"}'
new_data=json.loads(json_data)


result = ['test: ','test2: ','test3: ','test3: 123','test4: 12345']

def json_to_str(dict_data:dict):
    if isinstance(dict_data,dict):
        for key,value in dict_data.items():
            if isinstance(value,dict):
                result.append(f'{key}: ')
                json_to_str(value)
            else:
                result.append(f"{key}: {value}")
    else:
        result.append(dict_data)

    return result
    # print(result)

# new_result=[]
def format_list(list_data:list):
    new_result=[]
    deep=1
    for i in list_data:
        if i[-1]==' ' and list_data.index(i)==0 :
            new_result.append(i)
        elif i[-1]==' ' and list_data.index(i)!=0:
            tab_str='\t'*deep
            i=f'{tab_str}{i}'
            deep+=1
            new_result.append(i)
        else:
            new_result.append(i)

    return new_result
# json_to_str(new_data)
new_result=format_list(result)
print(new_result)

# print('结果为',result)
