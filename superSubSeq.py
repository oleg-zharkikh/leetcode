class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            s= str2
            l= str1
        else:
            s= str1
            l= str2

        # граничный случай - короткая строка внутри длинной
        if s in l:  
            return l
        
        # пытаемся прикрепить короткую к длинной слева
        head = s[0]
        tail = s[1:]
        shortest_right = s+l
        while tail != '':
            if str.find(l, tail) == 0:
                if  len(head+l) < len(shortest_right):
                    shortest_right = head+l
                    break
            head = head + tail[0]
            tail = tail[1:]


        # пытаемся прикрепить короткую к длинной справа
        tail = s[len(s)-1]
        head = s[0:len(s)-1]
        shortest_left = l + s
        while head != '':
            if str.find(l, head) == len(l)-len(head):
                if  len(l + tail) < len(shortest_left):
                    shortest_left = l + tail
                    break
            tail = head[len(head)-1] + tail
            head = head[0:len(head)-1]

        print('кратчайшая справа:',shortest_right) 
        print('кратчайшая слева:',shortest_left)      

s = Solution
str2 = 'bbbaaaba'
str1 = 'bbababbb' bbbaaababbb
print('Самая короткая суперстрока:',s.shortestCommonSupersequence(s,str1,str2))