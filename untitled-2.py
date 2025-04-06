def main():
    while True:
        sen = input("Enter a sentence,or 'q' to quit")
        if sen == 'q':
            break
        else:
            upper = sen.my_str_upper()
            return upper
main()
        