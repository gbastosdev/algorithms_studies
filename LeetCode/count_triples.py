def countTriples(self, n: int) -> int:
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