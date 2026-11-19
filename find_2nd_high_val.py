list =[22,33,44,56,77,80,88]

high_val = 0 
sec_high_val = 0

for i in list:
    if i > high_val:
        sec_high_val = high_val
        high_val = i

print(sec_high_val)
# printed the 2nd high val