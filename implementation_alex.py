from core import gt_stratagy_base
from random import randint

class AlexNiceStratagy(gt_stratagy_base):
    def __init__(self):
        super().__init__()

    def cooperate(self) -> bool:
        return True
    
class AlexMeanStratagy(gt_stratagy_base):
    def __init__(self):
        super().__init__()

    def cooperate(self) -> bool:
        return False
    
class AlexPassiveUntilAttackedStrategy(gt_stratagy_base):
    def __init__(self):
        super().__init__()
        
class AlexRandomStrategy(gt_stratagy_base):
    def __init__(self):
        super().__init__()
        
    def cooperate(self) -> bool:
        if randint(1, 2) == 1:
            return True
        else:
            return False
        
class AlexSwapStratagy(gt_stratagy_base):
    def __init__(self):
        super().__init__()
        