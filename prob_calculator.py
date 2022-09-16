import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs:
            self.contents.extend([key for _ in range(kwargs[key])])

    def draw(self, n_balls):
        if n_balls >= len(self.contents):
            all = copy.deepcopy(self.contents)
            self.contents.clear()
            return all
        selected_balls = []
        for _ in range(n_balls):
            random_index = random.randint(0, len(self.contents)-1)
            selected_balls.append(self.contents.pop(random_index))
        return selected_balls


def list_contains(l1, l2):
    cp_l1 = copy.deepcopy(l1)
    cp_l2 = copy.deepcopy(l2)
    for element in l1:
        if element in cp_l2:
            cp_l1.remove(element)
            cp_l2.remove(element)
    return len(cp_l1) == 0 or len(cp_l2) == 0


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    gotit_times = 0
    backup_hat = copy.deepcopy(hat)
    expected_drawn = []
    for key in expected_balls:
        expected_drawn.extend([key for _ in range(expected_balls[key])])
    for _ in range(num_experiments):
        hat = copy.deepcopy(backup_hat)
        drawn = hat.draw(num_balls_drawn)
        if list_contains(expected_drawn, drawn):
            gotit_times += 1
    return gotit_times / num_experiments
