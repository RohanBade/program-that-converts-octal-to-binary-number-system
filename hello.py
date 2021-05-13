class NumberSystem:
    octal_dict = {"0": "000",
                  "1":"001",
                  "2":"010",
                  "3":"011",
                  "4":"100",
                  "5":"101",
                  "6":"110",
                  "7":"111"}
    
    def __init__(self,number):
        self.number = number
    def convert_octal_to_binary(self):
        a= str(self.number)
        if a in NumberSystem.octal_dict.keys():
            print(NumberSystem.octal_dict[a])

def append_Bits(x,L):
    return [x+ i for i in L]


def generate_Bits(n,memo={}):
    if n==0 :
        return []
    elif n==1:
        return ["0","1"]
    else:
        memo[n] = append_Bits("0",generate_Bits(n-1,memo))+append_Bits("1",generate_Bits(n-1,memo))
        return memo[n]

octal_bits = generate_Bits(3)
hexa_bits = generate_Bits(4)
octalnum = NumberSystem(7)
octalnum.convert_octal_to_binary()
