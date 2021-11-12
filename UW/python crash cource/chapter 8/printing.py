# undef_pr=['a','b','c']
# comp_pr=[]

# while undef_pr:
#     cur_pr=undef_pr.pop()
#     print(f'printing model {cur_pr}')
#     comp_pr.append(cur_pr)

# for com_pr in comp_pr:
#     print(com_pr)

def printing(undef_pr,def_pr):
    while undef_pr:
        cur_pr=undef_pr.pop()
        print(f'printing model {cur_pr}')
        def_pr.append(cur_pr)

def show_comp(def_pr):
    for com_p in def_pr:
        print(com_p)

undef_pr=['a','b','c']
def_pr=[]

printing(undef_pr,def_pr)
show_comp(def_pr)