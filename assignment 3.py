# 1) Fetch all Urls from the dict
# 2) Add new entity in flow_3
# 3) Update url in all flow
# 4) Delete the entity in flow_1


flow_1 = {
    "intent": "product_info",
    "entities": [{"entity": "product", "prompt": "can you please enter what are you searching ?"},
                 {"entity": "location", "prompt": "Please enter your location ?"}],
    "api_data": {"url": "https://rasatest.free.beeceptor.com/"}
          }
flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}


def flow_url(a):
    print(a["api_data"]["url"])
               
    
    
def add_entity():                           
    new_entity={}
    n=int(input("Number of elements to add new entity: "))

    for i in range(n):
        k=input("Enter key: ")
        v=input("Enter value: ")
        new_entity.update({k:v})
    flow_3["entities"][0].update(new_entity)
    print("Updated Dictionary is ",flow_3)
            


def update_url(flow):
    floww=flow
    print(f"Old url is",flow["api_data"]["url"])
    u=input("Enter new url: ")
    flow["api_data"]["url"]=u
    print("New url is: ",flow["api_data"]["url"])
    print("Updated dictionary: ",flow)
    


def del_entity(flow):
    print("Orignal dictionary: ",flow)
    del flow["entities"][0]["entity"]
    print("\nUpdate dict: ",flow)

    
    
choice=int(input("""Press->
1. For Fetch all Urls from the dict.
2. For Add new entity in flow_3
3. For  Update url in all flow
4. For Delete the entity in flow_1
Enter your choice here: """))

if choice==1:                           # 1) Fetch Url from the dict
    print("\nFrom flow_1: ")
    flow_url(flow_1)    
    print("\nFrom flow_2: ")
    flow_url(flow_2) 
    print("\nFrom flow_3: ")
    flow_url(flow_3)
elif choice==2:                         # 2) Add new entity in flow_3
        print("\nFor flow_3: ")
        add_entity()
elif choice==3:                         # 3) Update url in all flow
    print("\nFor flow_1: ")
    update_url(flow_1) 
    print("\nFor flow_2: ")
    update_url(flow_2) 
    print("\nFor flow_3: ")
    update_url(flow_3) 
elif choice==4:                         # 4) Delete the entity in flow_1
        print("\nFor flow_1: ")
        del_entity(flow_1)
else:
    print("Invalid Input!!")