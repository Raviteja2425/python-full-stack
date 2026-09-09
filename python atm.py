ravi_details_sbi ={
    "Name" : 'ravi',
    'adr' : '1234567890',
    'pan' : 'TZJPS564E',
    'ATMPIN' : '2331',
    'Balance' : 10000,
    'Mini state':[],
}
All_attmps = 3
while All_attmps >0:
    user_pin = input('Enter you Atm pin: ')
    if user_pin in ravi_details_sbi['ATMPIN'] and len(user_pin)==4:
        print('Welcome to sbi ATM')
        choice_= int(input('Enter \n1.withdraw \n2.diposite \n3.balance check \n4.Mini: '))
        if choice_ == 1:
            with_m = int(input('Enter amount to withdraw: '))
            if with_m <= ravi_details_sbi['Balance'] and with_m % 100 ==0:
                ravi_details_sbi['Balance'] -= with_m
                print(f'take your cash and balance is {ravi_details_sbi['Balance']} ')
                ravi_details_sbi['Mini state'].append(f'withdraw: {with_m}')
                user_opt=int(input('\n1.Homepage \n2.Exit :'))
                if user_opt==1:
                    print('taking to homepage')
                    continue
                elif user_opt==2:
                    print('Thanks for visiting')
                    break
                            
            else:
                print(f'insuficiant balance or this Atm not provide change')
        elif choice_ ==2:
                depo_m = int(input('Enter ammount to deposite: '))
                if depo_m % 100 == 0:
                    ravi_details_sbi['Balance'] += depo_m
                    print(f'amount is deposite and total balance is {ravi_details_sbi['Balance']}')
                    ravi_details_sbi['Mini state'].append(f'deposit: {depo_m}')
                    print(f'{ravi_details_sbi['Mini state']}')
                    user_opt=int(input('\n1.Homepage \n2.Exit :'))
                if user_opt==1:
                    print('taking to homepage')
                    continue
                elif user_opt==2:
                    print('Thanks for visiting')
                    break
                else:
                    print(f'This ATM is not accepts change')
        elif choice_ == 3:
            print(f' your balance is {ravi_details_sbi['Balance']}')
        elif choice_==4:
            mini_m = ravi_details_sbi['Mini state'].append(f'withdraw: {with_m} and deposite: {depo_m}')
            print(f'{ravi_details_sbi['Mini state']}')
        break
    else:
        All_attmps -= 1
        if All_attmps >0:
            print(f'incorrect pin entered and you have {All_attmps} left')
        else:
            print('your card is blocked')
