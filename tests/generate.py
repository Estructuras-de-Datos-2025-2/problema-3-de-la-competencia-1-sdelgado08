#!/usr/bin/env python3
import random, os; random.seed(44)
def unique_sorted(a):
    a=sorted(a); out=[]
    for x in a:
        if not out or x!=out[-1]: out.append(x)
    return out
def w(name, arr):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(str(len(arr))+"\n"+" ".join(map(str,arr))+"\n")
    u=unique_sorted(arr)
    open(f"tests/output_{name}.txt","w").write(str(len(u))+"\n"+" ".join(map(str,u))+"\n")
def main():
    w("min", [5])
    n=2*10**5; w("max", [i%1000 for i in range(n)])
    n=1234; import random; w("rnd", [random.randint(-500,500) for _ in range(n)])
if __name__=="__main__": main()
