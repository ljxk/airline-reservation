print ("is this working")
fromlocation = input("where are you. belarus,chad,philadelphia,brazil,jamaica,democratic republic of the congo,australia")
locations = ["belarus","chad","philadelphia","brazil","democratic republic of the congo","australia"]
if not fromlocation in locations:
  print ("you lyin")
  quit()
golocation = input("where are you going. belarus,chad,philadelphia,brazil,jamaica,democratic republic of the congo,australia")
if not golocation in locations:
  print ("we dont go there")
  quit()
if golocation == fromlocation:
  print ("you already there")
  quit()
name = input("what is your name")
city = input("what is your city")
birthdate = input("when were you birthed m/d/y")
if len(birthdate) > 9:
  print ("nah")
  quit()
classairplane = input("what class your ordering 1st class, 2nd class, 3rd class")
classes = ("1st class", "2nd class","3rd class")

if not classairplane in classes:
  print ("nah")
  quit()
print ("--------------------------------------------------")
print (name)
print ("going to "+golocation+" from "+fromlocation+".")
print ("in "+city+".")
print ("born "+birthdate+".")
print (classairplane)