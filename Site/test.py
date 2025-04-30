import os

if __name__ == '__main__':
    path = os.path.join('../static/plans','Bhopal')
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
        di = {}
        di['day_number'] = i[0]
        di['description'] = i[1]
        di['image_url'] = i[3]
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