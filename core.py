import randomname

def calculate_score(player_a_choice: bool, player_b_choice: bool) -> tuple:
    if player_a_choice == True and player_b_choice == True:
        return (3, 3)
    
    if player_a_choice == False and player_b_choice == False:
        return (1, 1)
    
    if player_a_choice == True and player_b_choice == False:
        return (1, 5)
    
    if player_a_choice == False and player_b_choice == True:
        return (5, 1)

class gt_stratagy_base():
    def __init__(self, append_random_name = False):
        self.name = type(self).__name__
        if append_random_name:
            self.name = f"{self.name}_{randomname.get_name()}"
        
    def cooperate(self) -> bool:
        pass

    def update_score(self, score: int) -> None:
        pass        

if __name__ == "__main__":    
    bools = [True, False]
    answers = [(b1, b2) for b1 in bools
                        for b2 in bools]
    print(answers)

    for answer in answers:
        print(calculate_score(*answer))