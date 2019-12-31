secret='sw'
pw=''
auth=False
count=0
max_attempt=5

while pw!=secret:
    count+=1
    if count>max_attempt:break
    if count ==3:continue
    pw=input(f'{count}: what is the secret password? ')
else:
    auth=True
print('authorized' if auth else 'haha')

