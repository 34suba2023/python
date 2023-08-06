class goa:
    name="asdfg"
    drink="MAZAAA"
    def party(self):
        print("Let's party.....")
    def beach(self):
        print("Enjoying the beach")

ramesh=goa()
suresh=goa()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="Yes drink"
suresh.drink="Not drink"



print(ramesh.name)
print("Drink:",ramesh.drink)

print(suresh.name)
print("Suresh:",suresh.drink)

ramesh.party()
suresh.beach()
