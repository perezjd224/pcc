# 3-4 Guest List
guest_list = ['albert enstein',
              'aristocles son of ariston',
              'stephen hawkings',
              'brian greene']
for name in guest_list:
    print(name.title() + " has been invited to dinner.\n")

# 3-5 Changing Guest List
print(guest_list[2].title()+" is notable to attend.\n")
guest_list[2] = 'sean carroll'
for name in guest_list:
    print(name.title() + " has been invited to dinner.\n")

# 3-6 More Guest
print("We have found a bigger table.\n")
guest_list.insert(0,'aristotle')
guest_list.insert(3,'michael angelo')
guest_list.append('tal')
for name in guest_list:
    print(name.title() + " has been invited to dinner.\n")

# 3-9 Dinner Guest
print(str(len(guest_list)) + " people have been invited to dinner.\n")


# 3-7 Shrinking Guest List
print("There is only space for two guest.\n")
print(guest_list.pop(6).title()+ "'s inviation has been cancelled.\n")
print(guest_list.pop(5).title()+ "'s inviation has been cancelled.\n")
print(guest_list.pop(4).title()+ "'s inviation has been cancelled.\n")
print(guest_list.pop(3).title()+ "'s inviation has been cancelled.\n")
print(guest_list.pop(2).title()+ "'s inviation has been cancelled.\n")
for name in guest_list:
    print(name.title() + " has been invited to dinner.\n")
del guest_list[0]
del guest_list[0]
print(guest_list)

