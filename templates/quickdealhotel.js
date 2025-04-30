const hotels = [
  {
    image: "https://pix8.agoda.net/hotelImages/9766179/-1/d4f43c4a3b97772267e55a71ff0c0d56.jpg?ca=9&ce=1&s=1024x",
    name: "The Grand Residency",
    city: "Bhopal",
    rating: "4.5 (22K+)",
    services: ["Bed", "Bath", "Parking", "WiFi", "AC"],
    price: 1800,
    location: { lat: 23.2599, lng: 77.4126 }
  },
  {
    image: "https://img-cdn.thepublive.com/fit-in/1200x675/hospibuz/media/post_attachments/wp-content/uploads/2022/02/S-Cafe-2-Sheraton-Grand-Palace-Indore.jpeg",
    name: "Indore Palace",
    city: "Indore",
    rating: "4.3 (18K+)",
    services: ["Bed", "Bath", "Parking", "Gym", "Restaurant"],
    price: 1600,
    location: { lat: 22.7196, lng: 75.8577 }
  },
  {
    image: "https://assets.simplotel.com/simplotel/image/upload/x_45,y_0,w_564,h_317,r_0,c_crop,q_80,fl_progressive/w_500,f_auto,c_fit/deo-bagh---17th-c-gwalior/View_Deo_Bagh_Gwalior_3_ngjts2",
    name: "Royal Heritage",
    city: "Gwalior",
    rating: "4.7 (20K+)",
    services: ["Bed", "Bath", "Parking", "Pool", "Spa"],
    price: 2100,
    location: { lat: 26.2183, lng: 78.1828 }
  },
  {
    image: "https://cf.bstatic.com/xdata/images/hotel/max1024x768/505799485.jpg?k=2a40dbca123bb4dad7b51cbaa11cf01cd521444d16ae876f7c1a9dc9b78b7a5f&o=&hp=1",
    name: "Ujjain Retreat",
    city: "Ujjain",
    rating: "4.2 (16K+)",
    services: ["Bed", "Bath", "Parking", "WiFi", "Restaurant"],
    price: 1400,
    location: { lat: 23.1793, lng: 75.7849 }
  },
  
];


  var sum=''

  hotels.forEach(function (elem) {
  sum += `
    <div class="h-[425px] w-[300px] bg-white shadow-lg ml-3 mt-[90px]">
      <img src="${elem.image}" alt="" class="h-[20vw] w-full ">

      <div class="flex items-center justify-evenly p-1">
      
        <a href="${elem.location}" class="no-underline">
  <h1 class="font-extrabold font-serif text-1xl">${elem.name}</h1>
</a>
        <h4><i class="ri-star-fill text-yellow-400 text-1xl"></i>&nbsp;${elem.rating}</h4>
      </div>

      <div class="flex items-center justify-evenly p-1">
        <i class="ri-hotel-bed-fill">&nbsp;${elem.services[0]}</i>
        <i class="ri-showers-line">&nbsp;${elem.services[1]}</i>
        <i class="ri-parking-box-fill">&nbsp;${elem.services[2]}</i>
        <button class="bg-black h-7 w-7 rounded-3xl text-white text-[14px] text-center">+${elem.services.length - 3}</button>
      </div>

      <div class="flex items-center justify-evenly p-1 mt-[3px]">
        <h1>₹${elem.price}/per night</h1>
        <button class="bg-black h-[35px] w-[90px] text-white text-[14px] text-center hover:bg-red-500 hover:text-white">Book Now</button>
      </div>
    </div>
  `;
});

  
  var select=document.querySelector('#hotelContainer')
  select.innerHTML=sum





