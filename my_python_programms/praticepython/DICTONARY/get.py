



roomNo = input('hi')
roomFloor = input("")
roomYouWant = {'room no':roomNo, 'roomFloor':roomFloor,}
print("you entered" + str(roomYouWant.get('room no', 'dosenot exist')))
