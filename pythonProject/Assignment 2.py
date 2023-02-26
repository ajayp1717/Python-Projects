class StringOperation():
    def _init_(self):
        self.string = ''
        self.string_create()
    def length(self,string):
        c = 0
        for i in string:
            c+=1
        return c
    def string_create(self):
        self.string = input("Enter a string: ")
    def longest(self):
        ls = self.separate()
        ma = 0
        for i in range(self.length(ls)):
            if(self.length(ls[i])>self.length(ls[ma])):
                ma = i
        return ls[ma]
    def separate(self):
        ls = []
        wr = ''
        self.string+=' '
        for i in range(self.length(self.string)):
            if(self.string[i]==' ' or self.string[i]=='.' or self.string[i]==',' or self.string[i]=='!'):
                if self.length(wr) != 0:
                    ls.append(wr)
                wr = ''
            else:
                wr+=self.string[i]
        return ls
    def freq(self, ch):
        c = 0
        self.string = self.string.lower()
        for i in range(self.length(self.string)):
            if(self.string[i] == ch):
                c+=1
        return c
    def palindrome(self):
        self.string = self.string.lower()
        rev = self.string[::-1]
        if(rev == self.string):
            return True
        else:
            return False
    def apsub(self, sub):
        for i in range(self.length(self.string)-self.length(sub)+1):
            if(self.string[i:i+self.length(sub)] == sub):
                return i
        return -1
    def word_freq(self, wr,ls):
        c = 0
        for i in ls:
            if(i == wr):
                c+=1
        return c
    def frequency_word(self):
        ls = self.separate()
        c = 0
        for i in ls:
            c = self.word_freq(i,ls)
            print(i,": ",c)
        return
f1 = StringOperation()
while(True):
    print("Choose from the following options: ")
    print("1) Display word with longest length.\n2) Frequency of particular character.")
    print("3) Check if string is palindrome or not.\n4) Display index of first appearance of substring.")
    print("5) Count appearance of each word in string.")
    choice = int(input())
    if(choice == 1):
        print(f1.longest())
    elif(choice == 2):
        ch = input("Enter required character: ")
        c = f1.freq(ch)
        if(c == 0):
            print("Not present.")
        else:
            print(ch, ": present", c,"times.")
    elif(choice == 3):
        if(f1.palindrome()):
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")
    elif(choice == 4):
        subs = input("Enter substring: ")
        x = f1.apsub(subs)
        if(x>=0):
            print("Found at: ",x)
        else:
            print("Not present.")
    elif(choice == 5):
        f1.frequency_word()
    else:
        print("Wrong option!")
    ch = int(input("Choose from following:\n1) Continue with same string.\n2) Enter new string."))
    if(ch == 1):
        continue
    elif ch == 2:
        f1 = StringOperation()
    else:
        print("Program ended.")
        break