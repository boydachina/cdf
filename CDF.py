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
        return chance
    def probconj(self,difchanc,possibly,ntimes):
        chance=0
        for x in range(difchanc):
            chance= self.probindv(possibly,ntimes)+chance
        return chance
    def combination(self,n,p):
        a=1
        b=1
        con=n-p
        for x in range(n,con,-1):
            a=x*a
        for x in range(p,0,-1):
            b=x*b
        result= a/b
        return result
    def acumulate(self,atleast,possibly):
        result=0
        for x in range(atleast,possibly+1):
            difchanc=self.combination(possibly,x)
            result=self.probconj(int(difchanc),possibly,x)+result
        return result

cara=probability(1/2)
print(cara.acumulate(1,5))