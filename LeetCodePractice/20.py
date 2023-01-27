from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        ori_list = ['(', ')', '[', ']', '{', '}']
        rev_ori_list = [')', '(', ']', '[', '}', '{']

        new_dict = dict(zip(ori_list, rev_ori_list))
        #new_dict

        if len(s) % 2 != 0:
            return False
        
        set_s = sorted(set(s))

        counter = Counter(s)

        for i in set_s:
            if counter[i] != counter[new_dict[i]]:
                return False
                
        return True