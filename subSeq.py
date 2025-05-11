class Solution:
    def is_desisions(self, d: dict) -> int:

        desisions_counter = 0
        for i in d:
            if i[2] == True: 
                desisions_counter += 1
        return desisions_counter


    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            s= str2
            l= str1
        else:
            s= str1
            l= str2


        sub_strings_d = list()

        # построение начального списка двухсимвольных подстрок (i, l, True)
        for i in range(0,len(s)-1): # перебор начиная с позиции search_start до конца строки - 1
                current_sub_str = s[i:i+2]
                if current_sub_str in l:
                    sub_strings_d.append(list((i,2,True)))

        # обход для поиска решений вглубь
        is_the_end = False
        while (self.is_desisions(self, sub_strings_d) >= 1) and is_the_end == False:
            new_list = []
            for i in sub_strings_d:
                if i[2]: # для каждой подстроки получаем увеличенную подстроку из s
                    current_sub_str = s[i[0]:i[0]+i[1]+1]
                    if current_sub_str == s[i[0]:i[0]+i[1]]: # строчка как и была, значит мы в конце списка
                        if self.is_desisions(self, sub_strings_d) < 2:
                            is_the_end = True
                        new_list.append(list((i[0],i[1],False)))
                    elif current_sub_str in l: # новая подстрочка больше и общая, добавляем в решения
                        new_list.append(list((i[0],i[1],False)))
                        new_item = list((i[0],i[1]+1,True))
                        if not (new_item in sub_strings_d):
                            new_list.append(new_item)
                    else: # увеличенная подстрочка не входит в длинную, значит путь - тупиковый
                        new_list.append(list((i[0],i[1],False)))
            sub_strings_d = new_list            
        if sub_strings_d == []: 
            result = ''
        else:
            k = sub_strings_d[0]
            result = s[k[0]:k[0]+k[1]]
            return result
            #print ('Самая длинная субстрока: ',result)
            if str.find(str1, result)==0 and str.find(str2, result)==len(str2)-len(result):
                return str2[0:str.find(str2, result)]+str1
            if str.find(str2, result)==0 and str.find(str1, result)==len(str1)-len(result):
                return str1[0:str.find(str1, result)]+str2
            return result
s = Solution
str2 = 'abac'
str1 = 'bacf'
print('Самая  длинная подстрока:',s.shortestCommonSupersequence(s,str1,str2))