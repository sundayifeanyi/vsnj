x = 0

if x > 0:
    print(f"{x} is positive!" )
elif x < 0:
    print("{x} is nagetive")
else:
    print("{x} is zero")


print(f"hello ' '{x}!" )

name = "sanny"
cordinate = (10.0,20.0)
names = ["a","b","c"]

print( name,cordinate,names[0])

for i in range(5):
    print(i)
for name in names:
    print(name)

s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)

ages = {"alice": 22, "bob": 25}
ages["chalse"] = 19
ages["alice"] += 1
print(ages)

