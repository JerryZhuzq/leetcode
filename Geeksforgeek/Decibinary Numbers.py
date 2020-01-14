import sys
def DeciBinaryNum(num):
    store = []
    shang = len(str(num)) - 1
    while(shang>-1):
        divide = num // 10**shang
        store.append(divide)
        num -= divide * 10**shang
        shang -= 1

    while(store):
        if store[0] == 0:
            store = store[1:]
            continue
        ans = ""
        for i in range(len(store)):
            if store[i] != 0:
                ans += "1"
                store[i] -= 1
            else:
                ans += "0"
        sys.stdout.write(ans+" ")

def psuedoBinary(num):
    while(num):
        temp = num
        step = 1
        n = 0
        while(temp):
            m = temp % 10
            temp = temp // 10
            if m > 0:
                n += 10**(step-1)
            step += 1
        num -= n
        sys.stdout.write(str(n) + " ")

psuedoBinary(3234)