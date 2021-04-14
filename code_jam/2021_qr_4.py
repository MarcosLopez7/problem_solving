line = input().split(" ")
test_cases = int(line[0])
n = int(line[1])
q = int(line[2])

error = False

def add(query, result):
    print(' '.join(query))
    answer = input()

    if len(result) == 0:
        median_index = query.index(answer)

        if median_index == 0:
            result = [query[1], query[0], query[2]]
        elif median_index == 1:
            result = [query[0], query[1], query[2]]
        else:
            result = [query[0], query[2], query[1]]
    else:
        if answer in result: 
            mid_index = result.index(answer)

    
for t in range(test_cases):
    
    finished = False

    result = []
    query = ["1","2","3"]
    
    print(' '.join(query))
    answer = input()

    median_index = query.index(answer)

    if median_index == 0:
        result = [query[1], query[0], query[2]]
    elif median_index == 1:
        result = [query[0], query[1], query[2]]
    else:
        result = [query[0], query[2], query[1]]

    while not finished:
        allString = True
        index_with_list = []

        for e in result:
            if type(e) != str:
                allString = False
                index_with_list.append(result.index(e))

        if allString:
            mid_index = len(result) // 2
            new_number = str(len(result) + 1)
            left_index = mid_index - 1
            query = [result[left_index], result[mid_index], new_number]
            print(' '.join(query))
            answer = input()

            if answer == new_number:
                 result.insert(mid_index, new_number)
            elif answer == result[left_index]:
                if left_index == 0:
                    result.insert(0, new_number)
                else:
                    i = left_index - 1
                    while i >= 0:
                        result[i] = [result[i], new_number]
                        i = i - 1
            else:
                i = mid_index + 1
                while i < len(result):
                    result[i] = [result[i], new_number]
                    i = i + 1
        else:
            right_index = -1
            left_index = -1
            list_to_check_index =  index_with_list[len(index_with_list) // 2]
            query = [result[list_to_check_index][0], result[list_to_check_index][1]]
            if 0 in index_with_list:
                right_index = max(index_with_list) + 1
                query.append(result[right_index])
            else:
                left_index = min(index_with_list) - 1
                query.append(result[left_index])

            print(' '.join(query))
            answer = input()

            if left_index != -1:
                if answer == result[list_to_check_index][0]:
                    if list_to_check_index == index_with_list[0]:
                        result.insert(list_to_check_index, result[list_to_check_index][0])
                        list_to_check_index = list_to_check_index + 1

                    result[list_to_check_index] = result[list_to_check_index][1]
                elif answer == result[list_to_check_index][1]:
                    if list_to_check_index == index_with_list[0]:
                        result.insert(list_to_check_index, result[list_to_check_index][1])
                        list_to_check_index = list_to_check_index + 1
                    
                    result[list_to_check_index] = result[list_to_check_index][0]

                if answer == new_number:
                    i = list_to_check_index + 1

                    while i < len(result) and type(result[i]) != str:
                        result[i] = result[i][0]
                        i = i + 1
                else:
                    i = list_to_check_index - 1
                    while i >= 0 and type(result[i]) != str:
                        result[i] = result[i][0]
                        i = i - 1        

            elif right_index != -1:
                if answer == result[list_to_check_index][0]:
                    if list_to_check_index == 0:
                        result.insert(list_to_check_index, result[list_to_check_index][1])
                        list_to_check_index = list_to_check_index + 1
                    result[list_to_check_index] = result[list_to_check_index][0]
                elif answer == result[list_to_check_index][1]:
                    if list_to_check_index == 0:
                        result.insert(list_to_check_index, result[list_to_check_index][0])
                        index_with_list = index_with_list + 1
                    result[list_to_check_index] = result[list_to_check_index][1]

                if answer == new_number:
                    i = list_to_check_index - 2

                    while i >= 0 and type(result[i]) != str:
                        result[i] = result[i][0]
                        i = i - 1
                else:
                    i = list_to_check_index + 1
                    while i < len(result) and type(result[i]) != str:
                        result[i] = result[i][0]
                        i = i + 1        
   

        if answer == "-1":
            error = True
            break

    if error:
        break

