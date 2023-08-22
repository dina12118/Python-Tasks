import firelink

print("Type Your Fav Website from the below websites:")
print(list(firelink.fav.keys()))
website = input()
firelink.firefox(website)
