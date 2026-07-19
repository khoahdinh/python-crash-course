cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'huyndai'? I predict False.")
print(car == "huyndai")

car = "yamaha"
print("\nIs car == 'yamaha'? I predict True.")
print(car == "yamaha")
