import time
#using time module we estimate the time required by the loops
#and identify which one is more efficient among them
s=time.time()
k=time.localtime(s)

print(s)
print(k)
i=0
print("Stay home Stay safe")
while i<10:
    a=time.time()
    i=i+1
print("time taken ",(a-s))

print("Wash Your hands properly")
for i in range(10):
    l=time.time()
print("time taken ",(l-s))