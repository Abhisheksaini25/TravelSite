import os

if __name__ == '__main__':
    path = os.path.join('../static/data','restaurants')
    data = open(path, "r")
    hotel_string = data.read()
    hotel_ls = hotel_string.split('\n')
    hotel_list=[]

    for i in hotel_ls:
        hotel_list.append(i.split(','))
    hotel_data=[]
    for i in hotel_list:
        print(i)
        di={}
        di['name']=i[0]
        di['city']=i[1]
        di['rating']=i[2]
        di['services']=[i[3],i[4],i[5],i[6]]
        di['price']=i[7]
        di['image_url']=i[8]
        hotel_data.append(di)
    print(hotel_data)

    '''{
        "name": "Spice Garden",
        "city": "Delhi",
        "rating": "4.5",
        "services": ["Indian", "Buffet", "Wi-Fi"],
        "price": 450,
        "image_url": "https://via.placeholder.com/300x200.png?text=Spice+Garden",
    },'''