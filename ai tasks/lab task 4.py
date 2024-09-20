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


text=input("Enter a sentence:")
cleaned_text=""
for character in text:
    if character.isalnum() or character.isspace():
        cleaned_text += character
print("Text without punctuation:", cleaned_text)

        
