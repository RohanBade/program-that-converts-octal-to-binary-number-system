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


octalnum = NumberSystem(7)
octalnum.convert_octal_to_binary()
