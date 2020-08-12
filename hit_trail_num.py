from os import system, name
from time import sleep

print("""
Rules:
1. Hit -> no of digit-num which is in the number and in the same digit index
2. Trail -> no of digit-num which is in the number
3. You have 7 chances to guess the number
""")
orginal_num = int(input("Enter The 3- digit number you want to make your oppenent guess (100-999)? "))

#clearing the screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

sleep(2)
clear()

if (orginal_num >99 and orginal_num<1000):
        duplicate_num = int(orginal_num)
        num_list = []
        sum = 0
        while (duplicate_num != 0):
                mod_num = duplicate_num % 10
                # print(mod_num)
                sum = sum * 10 + mod_num
                duplicate_num = duplicate_num // 10
        while (sum != 0 ):
                mod_sum = sum % 10
                num_list.append(mod_sum)
                sum = sum // 10
        print("""
        Time to guess..........
        You have 7 chances.....
        Good Luck!!!!!!!!
        """)
        for n in range(1,8):
                count = 2
                hit_no = 0
                trial_no = 0
                guess_num = int(input("Enter 3-digits number only: ")) 
                previus_num = guess_num
                if orginal_num == guess_num :
                        break
                while (guess_num != 0):
                        mod_guess_num = guess_num % 10
                        if (mod_guess_num in num_list and num_list[count]== mod_guess_num):
                                hit_no += 1
                        if (mod_guess_num in num_list):
                                trial_no += 1
                        count -= 1
                        guess_num = guess_num // 10
                print(f"""Previous number = {previus_num}
                hit-number ={hit_no}
                trail-number = {trial_no}
                """)
                # print(trial_no)
        if (n==7):
                print("You failed !!!")
        else:
                print("You Won.... CONGRATS !!")  
else:
        print("The number you entered is not 3-digits....")   