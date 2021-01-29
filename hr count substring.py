def count_substring(string, sub_string):
    string=input()
    sub_string=input()
    #c=string.count(sub_string)

    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count

#-----alt code------    
    # count=0
    # for string[_:_+len(sub_string)]==sub_string:
    #     count+=1
    # return count

#-----alt code-----
# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)-len(sub_string) + 1):
#         if string[i:i+len(sub_string)]==sub_string:
#             count += 1
#     return count

print(count_substring('',''))