from typing import Optional
from pydantic import BaseModel

class Property(BaseModel):
    id: int
    image: str
    description: str
    price: float

    @classmethod
    def find_all(cls):
        return [
            Property(id=1, image="image1.jpg", description="Description 1", price=100.0),
            Property(id=2, image="image2.jpg", description="Description 2", price=200.0),
            Property(id=3, image="image3.jpg", description="Description 3", price=300.0),
            Property(id=4, image="image4.jpg", description="Description 4", price=400.0),
            Property(id=5, image="image5.jpg", description="Description 5", price=500.0),
            Property(id=6, image="image6.jpg", description="Description 6", price=600.0),
            Property(id=7, image="image7.jpg", description="Description 7", price=700.0),
            Property(id=8, image="image8.jpg", description="Description 8", price=800.0),
            Property(id=9, image="image9.jpg", description="Description 9", price=900.0),
            Property(id=10, image="image10.jpg", description="Description 10", price=1000.0),
            Property(id=11, image="image11.jpg", description="Description 11", price=1100.0),
            Property(id=12, image="image12.jpg", description="Description 12", price=1200.0),
            Property(id=13, image="image13.jpg", description="Description 13", price=1300.0),
            Property(id=14, image="image14.jpg", description="Description 14", price=1400.0),
            Property(id=15, image="image15.jpg", description="Description 15", price=1500.0),
            Property(id=16, image="image16.jpg", description="Description 16", price=1600.0),
            Property(id=17, image="image17.jpg", description="Description 17", price=1700.0),
            Property(id=18, image="image18.jpg", description="Description 18", price=1800.0),
            Property(id=19, image="image19.jpg", description="Description 19", price=1900.0),
            Property(id=20, image="image20.jpg", description="Description 20", price=2000.0),
        ]

    @classmethod
    def find_by_id(cls, id: int):
        properties = cls.find_all()
        for property in properties:
            if property.id == id:
                return property
        return None