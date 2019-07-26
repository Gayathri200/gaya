def main():
    ch=input()
    if ch=='a'or ch=='e'or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='i' or ch=='o' or ch=='u':
        print("Vowel")
    elif ord(ch)>=97 and ord(ch)<=117 or ord(ch)>=65 and ord(ch)<=90:
        print("Consonanat")
    else:
        print("invalid")
main()        
