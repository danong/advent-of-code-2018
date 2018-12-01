inp = """+3
+3
+4
-2
-4"""
# part 1
val = ''.join(inp.split('\n'))
print(eval(val))

# part 2
start = 0
seen = {0}
while True:
    for num in inp.splitlines():
        start += int(num)
        if start in seen:
            print(start)
            exit()
        else:
            seen.add(start)
