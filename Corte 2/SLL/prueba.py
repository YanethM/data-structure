class Prueba:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    
    def comparar(self):
        self.list1.append(2)
        self.list1.append(1)
        self.list1.append(3)
        self.list1.append(4)
        self.list1.append(5)
        self.list2.append(1)
        self.list2.append(2)
        self.list2.append(3)
        self.list2.append(4)
        self.list2.append(5)


        for i in range(len(self.list1)-1):
            print("comparo "+str(i)+ ": "+str(self.list1[i]) + " con " + str(i+1)+ ": "+ str(self.list1[i+1]))
            if self.list1[i] > self.list1[i+1]:
                print('false')
            else:
                print('true')


        if(self.list1 == self.list2):
            print('Listas iguales')
        else:
            print('Listas diferentes')

