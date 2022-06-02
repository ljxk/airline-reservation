def loop():
  print ("--------------------------------------------------")
  fromlocation = input("where are you. belarus,chad,philadelphia,brazil,jamaica,democratic republic of the congo,australia,new mexico          ")
  locations = ["belarus","chad","philadelphia","brazil","democratic republic of the congo","australia"," belarus"," chad","new mexico"," philadelphia"," brazil"," democratic republic of the congo"," australia"," new mexico"]
  if not fromlocation in locations:
    print ("you lyin")
    loop()
  golocation = input("where are you going. belarus,chad,philadelphia,brazil,jamaica,democratic republic of the congo,australia,new mexico          ")
  if not golocation in locations:
    print ("we dont go there")
    loop()
  if golocation == fromlocation:
    print ("you already there")
    loop()
  name = input("what is your name          ")
  city = input("what is your city          ")
  birthmonth = input("what month were you born?          ")
  months = ('january','february','march', 'april', 'may','june','july','august','september','october','november','december')
  if not birthmonth in months:
    print ("nah")
    loop()
  birthday = input("what day were you born(number not monday,tuesday,wednesday,etc)          ")
  days = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
  if not int(birthday) in days:
    print ("nah")
    loop()
  birthyear = input("what year were you born?          ")
  
  
  classairplane = input("what class your ordering 1st class, 2nd class, 3rd class          ")
  classes = ("1st class", "2nd class","3rd class")
  
  if not classairplane in classes:
    print ("nah")
    loop()
  print ("--------------------------------------------------")
  print (name)
  print ("going to "+golocation+" from "+fromlocation+".")
  print ("in "+city+".")
  print ("born "+birthmonth+" "+birthday+" "+birthyear+".")
  print (classairplane)
loop()