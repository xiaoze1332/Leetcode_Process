def solution(n,r):
  # Write your answer here
    new_dict = dict(zip(n, r))

    # 存储目前的值
    task_name = ''
    group_num = ''

    # 存储之前的值
    tmp_task_name = ''
    tmp_group_num = ''

    group_list = []
    res_list = []

    for i,k in enumerate(new_dict):
        for j, char in enumerate(k):
            if char.isdigit():
                
                tmp_group_num = group_num
                tmp_task_name = task_name
                
                group_num = k[j:]
                task_name = k[:j]
                
                break
                
        group_list.append([task_name, group_num, new_dict[k]])

        if tmp_group_num != group_num:
            res_list.append(group_list)
            group_list = []

    tmp_list = []

    for i in res_list:
        tmp_list.append(i[0])

    res_list = tmp_list

    tmp_task_name = ''
    tmp_group_num = ''
    count_total = 0
    count_passed = 0
    group_pass = 0

    for i in res_list:
        if i[0] != tmp_task_name:
            task_name = i[0]
            tmp_task_name = i[0]
            if count_total == count_passed and count_total != 0:
                group_pass += 1
                count_total = 0
                count_passed = 0
            else:
                count_total = 0
                count_passed = 0

        
        if i[-1] == 'passed':
            count_passed += 1
            count_total += 1
        else:
            count_total += 1

    count_list = []

    for i in res_list:
        count_list.append(i[0])

    group_len = len(set(count_list))

    return (group_pass / group_len) * 100