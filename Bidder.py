from os import system

def highest(bidders):
    high=0
    winner=''
    for key,value in bidders.items():
        if value>high:
            high=value
            winner=key
    print(f'Congratulations {winner} you have won the bid !!!!')


def main():
    print(f"{'*'*40}'Welcome to the Bid'{'*'*40}")

    flag = 'yes'
    bidders={}
    while flag =='yes':
        name=input('Enter you name: ')
        bid=input('Enter the bid amount: ')
        while not bid.isdigit():
            print('Please enter bid amount as numeric')
            bid=input('Enter the bid amount: ')
        bidders[name]=int(bid)

        flag=input('Do you want to continue the bid ?:(Enter "yes" or "no" only!) ').lower()
        while flag not in ['yes','no']:
            flag=input('Kindly Enter "yes" or "no" only!').lower()
        if flag=='yes':
            system("clear")
        else:
            highest(bidders)
            break

    



        
            
if __name__=='__main__':
    main()

    