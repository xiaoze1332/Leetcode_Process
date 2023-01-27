def StringChallenge(strParam):

    rev_strParam = strParam[::-1]

    list_str = list(strParam)

    # Determine if the initial state is a palindrome
    if len(list_str) == len(set(list_str)):
        strParam = 'not possible'
        return strParam

    # Also determine if the reversed string is a palindrome
    length = len(list_str)

    if len(list_str) % 2 == 0:
        if list_str[:length//2] == list_str[length//2:][::-1]:
            strParam = 'palindrome'
            return strParam
    else:
        if list_str[:length//2] == list_str[length//2+1:][::-1]:
            strParam = 'palindrome'
            return strParam

    # Find longest sub str in 2 strings
    def find_lcsubstr(s1, s2): 
        m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)] 
        mmax=0   
        p=0  
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i]==s2[j]:
                    m[i+1][j+1]=m[i][j]+1
                    if m[i+1][j+1]>mmax:
                        mmax=m[i+1][j+1]
                        p=i+1
        return s1[p-mmax:p],mmax   

    com_long_sub_str, _ = find_lcsubstr(strParam, rev_strParam)

    str1 = rev_strParam # 'pomm'
    str2 = com_long_sub_str # 'mm'

    list_str1 = list(str1) # ['p', 'o', 'm', 'm']
    list_str2 = list(str2) # ['m', 'm']

    ret = [ i for i in list_str1 if i not in list_str2 ]
    #ret # ['p', 'o']

    strParam = ''.join(ret)
    strParam = strParam[::-1]

    # code goes here
    return strParam

# keep this function call here 
print(StringChallenge(input()))