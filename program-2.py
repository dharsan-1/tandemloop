int_a = int(input())
final = ""
for i in range(1, int_a*2):
    if(i % 2 != 0):
        final += str(i) + ","
print(final[:len(final) - 1])