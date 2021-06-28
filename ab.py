class abc(Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    accnum=int(input('the enter accnum :'))
    bal=1000
    wd=int(input('the enter wd amount :',))
    
    if wd>bal:
        raise abc(' insufficient foubds in your account')
except abc as bbc:
    print(bbc)
    
