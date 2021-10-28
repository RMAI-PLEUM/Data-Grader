class Roman:
    def __init__(self):
        self.roman = ''
        self.dic = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I",
            0 : ""  }

    def calRoman(self,x,y):
        while x >= y:
            x -= y
            self.roman += self.dic[y]

    def intToRoman(self,x):
   
        if x == 0:
            return  self.dic[0]
        if x >= 1000:
            while x >= 1000:
             x = x-1000
             self.roman += self.dic[1000]
        if x >= 900:
            while x >= 900:
                x = x-900
                self.roman += self.dic[900]
        if x >= 500:
          while x >= 500:
             x = x-500
             self.roman += self.dic[500]   
        if x >= 400:
         while x >= 400:
              x = x-400
              self.roman += self.dic[400]
        if x >= 100:
            while x >= 100:
                x = x-100
                self.roman += self.dic[100]
        if x >= 90:
            while x >= 90:
                x = x-90
                self.roman += self.dic[90]
        if x >= 50:
            while x >= 50:
                x = x-50
                self.roman += self.dic[50] 
        if x >= 40:
            while x >= 40:
                x = x-40
                self.roman += self.dic[40]
        if x >= 10:
            while x >= 10:
                x = x-10
                self.roman += self.dic[10]
        if x >= 9:
            while x >= 9:
                x = x-9
                self.roman += self.dic[9]
        if x >= 5:
            while x >= 5:
                x = x-5
                self.roman += self.dic[5]
        if x >= 4:
            while x >= 4:
                x = x-4
                self.roman += self.dic[4]
        if x >= 1:
            while x >= 1:
                x = x-1
                self.roman += self.dic[1]

        return self.roman 




x = int(input("input: "))
print(Roman().intToRoman(x))
