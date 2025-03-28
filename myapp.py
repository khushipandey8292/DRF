import requests
import json



# URL="http://127.0.0.1:8000/stuinfo/"
# r=requests.get(url=URL)
# data=r.json()
# print(data)


#create data
# URL="http://127.0.0.1:8000/stucreate/"
# data={
#     'name':'naveen',
#     'roll':104,
#     'city':'Siwan'
# }
# json_data=json.dumps(data)
# r=requests.post(url=URL,data=json_data)
# data=r.json()
# print(data)


URL="http://127.0.0.1:8000/stuupdate/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
get_data()