import copy
import random

class Hat:
    def __init__(self, **ball_colors):
        self.contents = []
        for color, num_balls in ball_colors.items():
            self.contents.extend([color] * num_balls)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        ball_counts = {color: drawn_balls.count(color) for color in expected_balls}
        success = all(ball_counts.get(color, 0) >= count for color, count in expected_balls.items())
        
        if success:
            successes += 1
    
    probability = successes / num_experiments
    return probability