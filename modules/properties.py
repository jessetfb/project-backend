from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Property(BaseModel):
    id: int
    image: str
    description: str
    price: float

# Define your list of properties as a global variable
properties = [
    Property(id=1,
             image="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/f8/52/08/lounge.jpg?w=700&h=-1&s=1", 
             description="Prime Living Luxury Apartments",
             price=100.0),
    Property(id=2, 
             image="https://res.cloudinary.com/sentral/image/upload/w_1000,h_1000,q_auto:eco,c_fill/f_auto/v1684782440/miro_hero_building_exterior_2000x1125.jpg", 
             description="Luxury Apartments Sentral", 
             price=200.0),
    Property(id=3,
             image="https://www.aveliving.com/AVE/media/Property_Images/Florham%20Park/hero/flor-apt-living-(2)-hero.jpg?ext=.jpg", 
             description="Beautiful Resort apt", 
             price=300.0),
    Property(id=4, 
             image="https://cf.bstatic.com/xdata/images/hotel/max1024x768/524964658.jpg?k=c6f3073a77b8c22957c71c50160dd9526afcb6bccdf96779b0082824bf0e345d&o=&hp=1", 
             description="Astoria Luxury Apartments",
             price=400.0),
    Property(id=5, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmnthZAPviouETBDUGIOPXK5BmAycXPG3uvA&s",
             description="City Center Apartments", 
             price=500.0),
    Property(id=6, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrhsqqk1S4hW_8P4mq5TWjVCKfgCA6KwmSSg&s", 
             description="Masterways apt", 
             price=600.0),
    Property(id=7, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3-M6h_A1m8bmrTcjxm35z8zI73wTaxr4fJw&s", 
             description="NOVA LUXURY APARTMENT NAIROBI", 
             price=700.0),
    Property(id=8, 
             image="https://masterways.co.ke/storage/property/luxury-2-bedroom-apartment-to-let-in-westlands-2021-04-19-607d49273ecab.jpg",
             description="Luxury 2 bedroom apartment Masterways", 
             price=800.0),
    Property(id=9, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaB1nT_zuwysvu6XHOZyQpqJTE9xgff0nkg&s", 
             description="Northcote Apartments Kiliman", 
             price=900.0),
    Property(id=10, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmb7Wp7t-lorDjGkfKovxNji3EVbwBeeDBFw&s", 
             description="Naiwest 1 Bedroom Apartments", 
             price=1000.0),
    Property(id=11, 
             image="https://cf.bstatic.com/xdata/images/hotel/max1024x768/444773318.jpg?k=09feed4deb6aba50093330720b06cb60d7509cdb1da16f425ee120514774d5a4&o=&hp=1",
             description="LC at Staroot Apartments, Nairobi", 
             price=1100.0),
    Property(id=12, 
             image="https://images.squarespace-cdn.com/content/v1/651ec56bfbaffe41c352b587/efc9bf10-34a5-4293-9b4e-7a06e0f2bc1c/11-Aston+Place-POI-005.jpg", 
             description="Aston Place | Short North", 
             price=1200.0),
    Property(id=13, 
             image="https://podcity.ke/wp-content/uploads/2023/08/Apartment-1.webp", 
             description="UB1701C Curved balconies Apartment", 
             price=1300.0),
    Property(id=14, 
             image="https://sirfrancismarketingltd.co.ke/wp-content/uploads/2023/02/one_plus_2.jpg", 
             description="South Park Apartment in South C ", 
             price=1400.0),
    Property(id=15, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi7vQdq0Z1cbhmiKZZvWKe7XQSh0sW4DarJOogOrI9tJxcbipx5_Amdf7CjMTtgnAGD5I&usqp=CAU", 
             description="Emerald Park - Kilimani", 
             price=1500.0),
    Property(id=16, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1kLe5sLiAUqON9Wj6UJdRpbjJNoJZVadSoVS4Jgu1A9cRTtCl6iv9u-kOICIizjhWdmE&usqp=CAU", 
             description="Chelwood Place - Kilimani", 
             price=1600.0),
    Property(id=17, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb93qR2OW4IqmkoJiFAgeu8TqHDBqnPYSFnIzhcQn5H7n8lyc1-YBQIuuuUwcnWhbiKtw&usqp=CAU", 
             description="One West Park - 3 Bedroom", 
             price=1700.0),
    Property(id=18, 
             image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHU7k4A4CQGiSU-H1fZf67SsnW_sSKcSc9xzSjOXZIUMeso1juLvncTCcTGu7rspsJXcI&usqp=CAU", 
             description="Sakan | Apartment", 
             price=1800.0),
    Property(id=19, 
             image="https://www.sobha.com/blog/wp-content/uploads/2023/07/Apartment-Complex.png", 
             description="8 Benefits apt", 
             price=1900.0),
    Property(id=20, 
             image="https://sirfrancismarketingltd.co.ke/wp-content/uploads/2024/04/3-1024x724.png", 
             description="The Terraces Arboretum Apartments", 
             price=2000.0),
]

@app.get("/properties", response_model=List[Property])
async def get_properties():
    return properties

@app.get("/properties/{id}", response_model=Property)
async def get_property(id: int):
    for prop in properties:
        if prop.id == id:
            return prop
    raise HTTPException(status_code=404, detail="Property not found")
