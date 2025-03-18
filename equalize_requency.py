class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {}
        for i in word:
            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1
        average = 0
        for i in d: average += d[i]
        average = average // len(d) 
        one_char_freq = average
        count_of_difference = 0
        difference = 0
        summ = 0
        set_of_f = set()
        just_one = 0
        for i in d:
            if d[i] == 1: just_one += 1
            set_of_f.add(d[i])
            print(f'Итерация с элементом i={i}, d[i]={d[i]}, сравниваем с one_char_freq={one_char_freq}')
            if d[i] != one_char_freq:
               count_of_difference += 1
               if abs(d[i] - one_char_freq)> abs(difference): 
                   difference = d[i] - one_char_freq 
            summ += d[i]
        print(f'Параметры ({word}): разница={difference}, частотность сред= {one_char_freq}, число разниц = {count_of_difference}')
        case_1 = ((summ - 1) % len(d) == 0) and (difference == 1) and (count_of_difference == 1)
        case_2 = (summ % len(d) == 0) and difference == 0 and (one_char_freq == 1)
        case_3 = one_char_freq == 2 and difference == -1 and count_of_difference == 1
        #case_4 = d[word[0]] == 1 and abs (difference) == 1 and count_of_difference == len(d)-1
        case_5 = len(d) == 1
        case_6 = len(set_of_f) == 2 and (1 in set_of_f) and just_one == 1
        #print(case_1 , case_2 , case_3, case_4 , case_5 , case_6)
        return  case_1 or case_2 or case_3  or case_5 or case_6
    
s = Solution
#word1 = 'abcc' #true
#word2 = 'aazz' #false
#word3 = 'bac' # true
#word4 = 'aca' #true
word5 = 'abbcccfff' #false
#word6 = 'aaaabbbbccccccdddd' # true
#word7 = 'aabbbbdddfffff' # false
#print(s.equalFrequency (s,word1))
#print(s.equalFrequency (s,word2))
#print(s.equalFrequency (s,word3))
#print(s.equalFrequency (s,word4))
print(s.equalFrequency (s,word5))
#print(s.equalFrequency (s,word6))
#print(s.equalFrequency (s,word7))