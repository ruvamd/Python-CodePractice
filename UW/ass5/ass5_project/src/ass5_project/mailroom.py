import sys

def get_donors():
    donors = {'bill gates':[1000,2000,3000],
              'jeff bezos':[500,6000,7000],
              'elon mask':[8000,9000],
              'warren buffett':[23000,4532],
              'andrew carnegie':[9834,9286,3975]}
    return donors

def send_thank_you(donors):
    mailto = input("Enter the full name who to send or type 'list' to see all donors: ")
    if mailto == "list":
        for i in donors:
            print(i)
    elif mailto in donors:
        print(f"{mailto} thanks for ${str(donors[mailto][-1:]).strip('[]')}")
    else:
        users_choice=input(f'{mailto} not in the donors list.add the new donor:')
        donation_amount=int(input('enter donation amount: $'))
        donors[mailto] = donation_amount
        print(f'{mailto} thanks for {donation_amount}')

def create_report(donors):
    report=[f'{i:<20}${sum(donors[i]):<15}{len(donors[i]):<10}${sum(donors[i])/2:<20}' for i in donors]
    print(f"{'|donor name|':<18}{'|total given|':<10}{'|num gift|':<5}{'|avarage gift|':<20}")
    for i in report:
        print(f'{i}')
    return report

def quit(q):
    print('bye')
    sys.exit()

def choose_an_option():
    functions_list = {'1':send_thank_you,
                      '2':create_report,
                      '3':quit}
    print('\n1.Send a Thank You \n2.Create a Report \n3.Quit\n')
    user_choice = input('enter the number:')
    functions_list[user_choice](donors)

def mail_room(donors):
    while True:
        choose_an_option()

if __name__ == '__main__':
    donors = get_donors()
    mail_room(donors)

