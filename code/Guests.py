guest_list = ["Einstein","Tesla","Gagarin"]
Emess = "Hello, " + guest_list[0] + ". You are invited to a party!"
Tmess = "Hello, " + guest_list[1] + ". You are invited to a party!"
Gmess = "Hello, " + guest_list[2] + ". You are invited to a party!"
#print ("A bigger table was found !!!")
print (Emess, "\n",Tmess, "\n",Gmess)
print ("Einstein can't make it :(")
guest_list[0]= "Hitler"
Emess = "Hello, " + guest_list[0] + ". You are invited to a party!"
print (Emess)
print ("A bigger table was found !!!")
guest_list.insert(0, "Petko")
guest_list.insert(2, "Vlado")
guest_list.append("Joro")
Pmess = "Hello, " + guest_list[0] + ". You are invited to a party!"
Vmess = "Hello, " + guest_list[2] + ". You are invited to a party!"
Jmess = "Hello, " + guest_list[5] + ". You are invited to a party!"
print (Pmess, "\n",Vmess, "\n",Jmess)
print ("The table wont be able to arrive for dinner.. Four people will have to skip it")
first_removed = guest_list.pop(0)
print ("Sorry " + first_removed.title() + ", there is no room for you")
first_removed = guest_list.pop(0)
print ("Sorry " + first_removed.title() + ", there is no room for you")
first_removed = guest_list.pop(0)
print ("Sorry " + first_removed.title() + ", there is no room for you")
first_removed = guest_list.pop(0)
print ("Sorry " + first_removed.title() + ", there is no room for you")
print ("Ola " + guest_list[0] + " and " + guest_list[1])
del guest_list[0]
del guest_list[0]
print (len(guest_list))
