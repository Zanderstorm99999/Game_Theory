from core import calculate_score, gt_stratagy_base
from typing import List
from implementation_alex import AlexNiceStratagy, AlexMeanStratagy, AlexRandomStrategy, AlexSwapStratagy
from collections import defaultdict

def create_player_pairs(list_of_strategies: List[gt_stratagy_base]):
    '''Takes in a list of stratagys originating from gt_stratagy_base, outputs a list of tuples of all the pairs that will have a game together. (Each player plays against themself too)'''
    list_of_tuple_pairs = []
    
    for i in range(len(list_of_strategies)):
        for strategy in list_of_strategies[i:]:
            list_of_tuple_pairs.append((list_of_strategies[i:][0], strategy))
        
    return list_of_tuple_pairs
    

class Game():
    
    def __init__(self, player1: gt_stratagy_base, player2: gt_stratagy_base) -> None:
        self.player1 = player1
        self.player2 = player2

    def start(self, count: int) -> dict:
        list_of_scores = []
        player1_total_score = 0
        player2_total_score = 0 
        for count in range(count):
            player1_score, player2_score = calculate_score(self.player1.cooperate(), self.player2.cooperate())
            player1_total_score += player1_score
            player2_total_score += player2_score
            self.player1.update_score(player1_score)
            self.player2.update_score(player2_score)
            list_of_scores.append((player1_score, player2_score))

        return {"users": 
                [
                    {"player_name": self.player1.name, "total_score": player1_total_score},
                    {"player_name":self.player2.name, "total_score": player2_total_score}
                ], 
                "detail": list_of_scores}
    

class GameRunner():
    
    def __init__(self, players: List[gt_stratagy_base]):
        self.player_pairs = create_player_pairs(players) # TODO: add a function to create the play_pair tuple
    
    def run(self, count: int) -> list:
        scores = []
        for player_tuple in self.player_pairs:
            player1, player2 = player_tuple
            game_instance = Game(player1, player2)
            scores.append(game_instance.start(count))
        return scores

def get_player_and_score(scores):
    '''makes a tuple with two elements: (stratagy name, score)'''
    return (scores.get("player_name"), scores.get("total_score"))

def sort_player_scores(every_player_score: dict) -> list:
    '''uses lambda function to sort each player from top to bottem in order of highest score to lowest score'''
    sorted_player_scores = sorted(every_player_score.items(), key = lambda x:x[1], reverse = True)
    return sorted_player_scores
    
if __name__ == "__main__":
    # runner = GameRunner([AlexNiceStratagy(), AlexRandomStrategy(), AlexMeanStratagy()])
    # runner = GameRunner([AlexMeanStratagy(True), AlexMeanStratagy(True), AlexMeanStratagy(True), AlexMeanStratagy(True), AlexMeanStratagy(True), AlexMeanStratagy(True), AlexMeanStratagy(True), AlexNiceStratagy(True)])
    runner = GameRunner([AlexSwapStratagy(), AlexNiceStratagy()])
    scores = runner.run(2)
    every_player_score = defaultdict(int)
    for dict_of_scores in scores:
        list_of_scores = dict_of_scores.get("users")
        player1, player1_score = get_player_and_score(list_of_scores[0])
        player2, player2_score = get_player_and_score(list_of_scores[1])
        
        every_player_score[player1] += player1_score
        every_player_score[player2] += player2_score
        
    print(sort_player_scores(every_player_score))
    
    for index, tuple_of_score in enumerate(sort_player_scores(every_player_score)):
        player, score = tuple_of_score
        print(f"#{index + 1}. {player} - {score}")