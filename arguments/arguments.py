def main():
    x=dict(buffy='meaw',zilla='grrr',angel='purr')
    kitten(**x)
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            #print('kitten {} says {}'.format(k,kwargs[k]))
            print(f'kitten {k} says {kwargs[k]}')
    else: print('meaw')
main()  
