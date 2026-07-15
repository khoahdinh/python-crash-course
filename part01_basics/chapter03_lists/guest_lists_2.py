guest_lists = ["Dung Dung", "BongBang", "Thao Dung"]
print(guest_lists)

stay_home = guest_lists.pop()
message = "Sorry " + stay_home.title() + ", I can't invite you"
print(message)
    
stay_home = guest_lists.pop()
message = "Sorry " + stay_home.title() + ", I can't invite you"
print(message)

del guest_lists[0]
print("Lists of Guest:")
print(guest_lists)
