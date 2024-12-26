import random
dic = { 1 : "rock" , 2 : "paper" , 3 : "scissor"}

def Game_Fun():
    for i in range(0, 3):
        user_input = input("(Rock , Paper , Scissor or Exit ) \n Enter your choice: ").lower().strip()
        cpu_input = lambda: random.randint(1, 3)
        cpu_ans = dic[cpu_input()]
        if user_input == 'exit':
            return False
        if((user_input == 'rock' and cpu_ans =='scissor') or (user_input == 'paper' and cpu_ans == 'rock') or (user_input == 'scissor' and cpu_ans == 'paper')):
            print(f"Player win\n {cpu_ans}")
        elif((user_input == 'scissor' and cpu_ans =='rock') or (user_input == 'rock' and cpu_ans == 'paper') or (user_input == 'paper' and cpu_ans == 'scissor')):
            print(f"Player lose\n{cpu_ans}")
        elif(user_input == cpu_ans):
            print(f"Draw!!\n{cpu_ans}")
        else:
            print("WARNING : Invalid Choice!!!!")
    return True

if __name__ =="__main__":
    while True:
        ch = input("Do you want to play (y, n): ").lower().strip()
        if ch == 'y':
            if not Game_Fun():
                break
        else:
            break