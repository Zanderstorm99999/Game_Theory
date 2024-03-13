from core import gt_stratagy_base
from random import randint

class nice_stratagy(gt_stratagy_base):
    def __init__(self):
        super().__init__()

    def cooperate(self) -> bool:
        return True
    
class mean_stratagy(gt_stratagy_base):
    def __init__(self):
        super().__init__()

    def cooperate(self) -> bool:
        return False
    
class PassiveUntilAttackedStrategy(gt_stratagy_base):
    def __init__(self):
        super().__init__()
        
    