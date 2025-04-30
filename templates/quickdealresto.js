const restaurants = [
  {
    name: "Spice Kitchen",
    city: "Bhopal",
    rating: "4.5/5 (18K+)",
    services: [
      "Indian Cuisine", 
      "Breakfast, Lunch, Dinner", 
      "Wi-Fi", 
      "Live Music", 
      "Outdoor Seating", 
      "Parking", 
      "Pet Friendly"
    ],
    price: 500,
    image: "https://via.placeholder.com/300x200?text=Spice+Kitchen+Bhopal",
    tags: ["Family-Friendly", "Delivery Available"]
  },
  {
    name: "Indore Diner",
    city: "Indore",
    rating: "4.7/5 (22K+)",
    services: [
      "Mughlai Cuisine", 
      "Lunch, Dinner", 
      "Wi-Fi", 
      "Home Delivery", 
      "Bar", 
      "Air Conditioning"
    ],
    price: 600,
    image: "https://via.placeholder.com/300x200?text=Indore+Diner",
    tags: ["Pet Friendly", "Takeaway Available"]
  },
  {
    name: "Gwalior Heritage",
    city: "Gwalior",
    rating: "4.3/5 (15K+)",
    services: [
      "North Indian", 
      "Breakfast, Lunch, Dinner", 
      "Wi-Fi", 
      "Live Sports", 
      "Conference Hall", 
      "Outdoor Seating"
    ],
    price: 550,
    image: "https://via.placeholder.com/300x200?text=Gwalior+Heritage",
    tags: ["Romantic", "Valet Parking"]
  },
  {
    name: "Ujjain Treats",
    city: "Ujjain",
    rating: "4.4/5 (17K+)",
    services: [
      "Vegetarian Cuisine", 
      "Breakfast, Lunch", 
      "Wi-Fi", 
      "Chill Vibes", 
      "Takeaway", 
      "Family Friendly"
    ],
    price: 300,
    image: "https://via.placeholder.com/300x200?text=Ujjain+Treats",
    tags: ["Budget Friendly", "Vegetarian Only"]
  },
];

  var sum=''

  restaurants.forEach(function (elem) {
  sum += `
    <div class="h-[455px] w-[300px] bg-white shadow-lg ml-3 mt-[90px]">
      <img src="${elem.image}" alt="" class="h-[20vw] w-full ">

      <div class="flex items-center justify-evenly p-1">
        <h1 class="font-extrabold font-serif text-1xl ">${elem.name}</h1>
        <h4><i class="ri-star-fill text-yellow-400 text-1xl"></i>&nbsp;${elem.rating}</h4>
      </div>

      <h4 class="font-serif  text-center"><i class="">${elem.services[0]}</i></h4>
          
      <div class="flex items-center justify-evenly p-1">
       
        <i class="">${elem.services[1]}</i>
        <i class="">${elem.services[2]}</i>
        <button class="bg-black h-7 w-7 rounded-3xl text-white text-[14px] text-center">+${elem.services.length - 3}</button>
      </div>

      <div class="flex items-center justify-evenly p-1 mt-[3px]">
        <h1>₹${elem.price}/per person</h1>
        <button class="bg-black h-[35px] w-[90px] text-white text-[14px] text-center hover:bg-red-500 hover:text-white">Book Now</button>
      </div>
    </div>
  `;
});

  
  var select=document.querySelector('#hotelContainer2')
  select.innerHTML=sum

