"""To find how much order to be fulfilled."""
order,k=[10,30],40

order.sort()
count=0
available=[(k:=k-i) for i in order  ]
print(available)
count=sum(int(i)>=0 for i in available  )
print(count)