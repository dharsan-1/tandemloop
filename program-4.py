num_int = [1,2,3,4,5,6,7,8,9]
int_num = list(map(int,input().split()))
frq = {}
for first_item in num_int:
    count = 0
    for sec_num in int_num:
        if(sec_num%first_item == 0):
            count += 1
    frq[first_item] = count        
print(frq)