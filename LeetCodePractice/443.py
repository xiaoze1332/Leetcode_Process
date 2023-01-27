class Solution:
    def compress(self, chars: List[str]) -> int:

        chars.append('!')

        tmp_char = chars[0] # a
        count = 0
        res = []

        for i, char in enumerate(chars):
            #print(i, char)
            if char == tmp_char:
                count += 1
            else:
                res.append(tmp_char)
                if count > 1:
                    res.append(int(count))
                tmp_char = char
                count = 1

        new_list = []

        for i in res:
            if not isinstance(i, int):
                new_list.append(i)
            else:
                if i == 1:
                    pass
                elif 1 < i < 10:
                    new_list.append(i)
                elif i >= 10:
                    tmp_list = list(str(i))
                    for j in tmp_list:
                        new_list.append(int(j))
        
        chars[:] = [str(x) for x in new_list]
            
        return len(chars)