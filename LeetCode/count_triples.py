def countTriples(n: int) -> int:
        count = 0
        for c in range(1,n+1):
            for a in range(1, c):
                value = c*c - a*a
                if value <= 0:
                    continue
                b = value ** 0.5
                if b.is_integer():
                    count+=1
        return count

def countTriples2(n: int) -> int:
        hset = set(sum*sum for sum in range(1,n+1))
        count = 0
        for c in range(1,n+1):
            for a in range(1,c):
                equation = (c*c - a*a)
                if equation <= 0:
                    continue
                if (c*c - a*a) in hset:
                    count+=1
        return count

if __name__ == "__main__":
    n = 5
    print(countTriples(n))  
    m = 10
    print(countTriples2(m))