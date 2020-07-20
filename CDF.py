from decimal import Decimal
class probability():
    """
    input prob=1/2, amostral_space=2 at_least=1 possibly= 3
    output 7/8
    possibly= numero de vezes que joga
    """

    def __init__(self,prob):
        self.prob=prob
        self.prob1=1-prob
        #self.amostral_space=len(amostral_space)
    
    def probindv(self,possibly,ntimes):
        ntimes1=possibly-ntimes
        chance=(self.prob**ntimes)*(self.prob1**ntimes1)
        #print("passou 3")
        return chance
    def probconj(self,difchanc,possibly,ntimes):
        chance= Decimal(self.probindv(possibly,ntimes))*Decimal(difchanc)
        #print("passou 2")
        return chance
    def combination(self,n,p):
        a=1
        b=1
        con=n-p
        for x in range(n,con,-1):
            a=x*a
        for x in range(p,0,-1):
            b=x*b
        a=round(a,5)
        b=round(b,5)
        result= a//b
        return result
    def acumulate(self,atleast,possibly):
        result=0
        for x in range(atleast,possibly+1):
            difchanc=self.combination(possibly,x)
            #print("passou 1")
            result=self.probconj(int(difchanc),possibly,x)+result
        return result

cara=probability(8/2048)
plays=50*15
print(str(round(cara.acumulate(3,plays)*100,2))+"%" )
