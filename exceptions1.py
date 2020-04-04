def main():
        humanAges=-99
        while humanAges<0 or humanAges>120:
              try:humanAges=int(input('Enter your ages from 0 to 120: '))
              except ValueError:print('Enter numbers only!')
        print('Your ages is a',dogAges(humanAges),'in a dog ages.')      
def dogAges(hAges):
    return hAges*7
main()