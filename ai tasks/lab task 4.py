class LUHN:
    def __init__(self, card_nber):
        self.card_nber = [int(dgt) for dgt in card_nber]
    def validation(self):
        if len(self.card_nber)!=16:
            print("Please enter a valid 16-digit card number")
            return
        check_digit=self.card_nber.pop()
        self.card_nber.reverse()
        for i in range(0, len(self.card_nber), 2):
            self.card_nber[i]*= 2
            if self.card_nber[i]>9:
                self.card_nber[i]-=9
        total_sum=sum(self.card_nber)+check_digit0
        if total_sum%10==0:
            print("Congratulations the card is valid")
        else:
            print("The card number is invalid.")
card_nber=input("Enter a 16-digit card number: ")
Card1=LUHN(card_nber)
Card1.validation()
Remove Punctuations from UserInput String (without using remove function)


punc='''!@$%^&*()_+{}:"<>?|\;-~`<>/'''
string=input("enter anything here:")
empty_str=""
for i in string:
    if i not in punc:
        empty_str+=i
print(empty_str)

Sort text (word) in Alphabetical Order (without using sort function)
a="Harry Potter and the Gobllet of Fire"
w=a.split()
print(w)
for i in range(len(w)):
    w[i]=w[i].lower()
print(w) 
w.sort()
for i in w:
    print(i) 
    or we can also take it from user
a=input("enter anything:")
w=a.split()
print(w)
for i in range(len(w)):
    w[i]=w[i].lower()
print(w) 
w.sort()
for i in w:
    print(i) 

        
