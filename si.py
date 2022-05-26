class bank:
    def __init__(self,name,principle,rate,time):
        self.n=name
        self.p=principle
        self.r=rate
        self.t=time
        
    def simple_intrest(self):
        self.si = (self.p * self.r * self.t)/100
        print(self.si)
        
    def compound_intrest(self):
        self.amount = self.p*((1+self.r/100)**self.t)
        self.ci = int(self.amount-self.p)
        print(self.ci)
        
hdfc=bank("hdfc",20000,11,2)
hdfc.simple_intrest()
hdfc.compound_intrest()

'''pnb=bank("hdfc",30000,10,2)
pnb.simple_intrest()
pnb.compound_intrest()

icici=bank("hdfc",10000,12,2)
icici.simple_intrest()
icici.compound_intrest()'''