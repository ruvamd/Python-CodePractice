def printing(undef_pr,def_pr):
    while undef_pr:
        cur_pr=undef_pr.pop()
        print(f'printing model {cur_pr}')
        def_pr.append(cur_pr)

undef_pr=['a','b','c']
def_pr=[]