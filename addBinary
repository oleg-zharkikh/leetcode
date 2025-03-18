class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = ''
        flag = False
        while len(a)>len(b): b = '0'+ b
        while len(b)>len(a): a = '0'+ a
        li = len(a)-1
        for i in range(li,-1,-1):
            if (a[i] == '1' or b[i] == '1') and not (a[i] == '1' and b[i] == '1'):
                if flag == True:
                    r = '0' + r
                    flaf = False
                else:
                    r = '1' + r 
            if a[i] == '0' and b[i] == '0':
                if not flag:
                    r = '0' + r
                else:
                    r = '1' + r
                    flag = False
            if a[i] == '1' and b[i] == '1':
                if flag == True:
                    r = '1' + r
                else:
                    r = '0' + r
                    flag = True
        if flag == True:
            r = '1' + r
        return r

s = Solution
a= '1010'
b = '1011'
print(s.addBinary(s,a,b))
