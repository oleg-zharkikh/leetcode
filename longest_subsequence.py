class Solution:
    def is_desisions(self, d: dict) -> int:

        desisions_counter = 0
        for i in d:
            if i[2] == True: 
                desisions_counter += 1
        return desisions_counter
    
   
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l = text1 if len(text1) > len(text2) else text2
        s = text1 if len(text1) <= len(text2) else text2

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
            result = 0
        else:
            k = sub_strings_d[0]
            result = len(s[k[0]:k[0]+k[1]])
        return result
s = Solution
str1 = 'abaaba1aba2abaaaba2f'
str2 = 'qwe2abrt'
print('Самая длинная подстрока:',s.longestCommonSubsequence(s,str1,str2))