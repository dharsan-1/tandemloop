int_a = int(input())
if int_a%2 == 0:
    int_a = int_a-1
final = ""
for i in range(1, int_a*2):
    if(i % 2 != 0):
        final += str(i) + ","
print(final[:len(final) - 1])