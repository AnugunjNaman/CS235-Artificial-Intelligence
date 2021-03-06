import random
class Queens:

    def __init__(self, n=8):
        self.n = n
        self.reset()

    def reset(self):
        n = self.n
        self.y = [None] * n             
        self.row = [0] * n              
        self.up = [0] * (2*n-1)         
        self.down = [0] * (2*n-1)       
        self.nfound = 0                 

    def solve(self, x=0):               
        for y in range(self.n):
            if self.safe(x, y):
                self.place(x, y)
                if x+1 == self.n:
                    self.display()
                    exit(0)
                else:
                    self.solve(x+1)
                self.remove(x, y)

    def safe(self, x, y):
        return not self.row[y] and not self.up[x-y] and not self.down[x+y]

    def place(self, x, y):
        self.y[x] = y
        self.row[y] = 1
        self.up[x-y] = 1
        self.down[x+y] = 1

    def remove(self, x, y):
        self.y[x] = None
        self.row[y] = 0
        self.up[x-y] = 0
        self.down[x+y] = 0

    def display(self):
        self.nfound = self.nfound + 1
        print('+-' + '--'*self.n + '+')
        for y in range(self.n-1, -1, -1):
            print('|', end=' ')
            for x in range(self.n):
                if self.y[x] == y:
                    print("Q", end=' ')
                else:
                    print(".", end=' ')
            print('|')
        print('+-' + '--'*self.n + '+')

def main():
    q = Queens(8)
    q.solve()

if __name__ == "__main__":
    main()
