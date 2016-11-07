import random
import textwrap

def show_game_mission():
    print("Find a place to rest")

def print_bold(msg, end='\n'):
    #Print a string in BOLD
    print("\033[1m" + msg + "\033[0m", end=end)

def show_health(hp_points, bold=False):
    if bold is True:
        print_bold("The health is: %d".format(hp_points))
    print("The health is: {}".format(hp_points))
def print_dotted_line(width=72):
    #Print a dotted Line
    print('-'*width)
    
def run_application():
    #Top level control function for running the Application
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()
    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")

def reset_health_meter(health_meter):
    #Reset the values of health_meter dict to the original ones 
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def reveal_occupants(idx, huts):
    #Print the occupants in the hut
    msg = ''
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()    
    
def occupy_huts():
    occupants = ['friend', 'enemy', 'empty']
    huts = [random.choice(occupants) for i in range(5)]
    return huts

def process_user_choice():
    num = input("Which hut do you want to enter? ")
    return int(num)
    
def play_game(health_meter):
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)
    if huts[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold("Enemy sighted", end='')
        show_health(health_meter, bold=True)
        continue_attack = True
        while continue_attack:
            continue_attack = input("..........continue attack? (y/n): ")
            if continue_attack == 'n':
                print_bold("Running awai with health status....")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break
            attack(health_meter)
            
            if health_meter['enemy'] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break
            
            if health_meter['player'] <= 0:
                print_bold("YOU LOSE!!!")
                break
            
def attack(health_meter):
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)
    
if __name__ == '__main__':
    run_application()