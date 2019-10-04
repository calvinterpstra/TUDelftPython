import queue as Q
import time
# import resource
import sys
import math

#### SKELETON CODE ####
# The Class that Represents the Puzzle


class PuzzleState(object):
    """docstring for PuzzleState"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        if n*n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")
        
        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []

        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""
        # add child nodes in order of UDLR
        if len(self.children) == 0:
            up_child = self.move_up()
            if up_child is not None:
                self.children.append(up_child)
            down_child = self.move_down()
            if down_child is not None:
                self.children.append(down_child)
            left_child = self.move_left()
            if left_child is not None:
                self.children.append(left_child)
            right_child = self.move_right()
            if right_child is not None:
                self.children.append(right_child)

        return self.children

# Function that Writes to output.txt
# Students need to change the method to have the corresponding parameters


class PuzzleSolver():

    def __init__(self, solver, initial_state):
        goal_state = "0,1,2,3,4,5,6,7,8"
        goal_state = goal_state.split(",")
        goal_state = tuple(map(int, goal_state))
        size = int(math.sqrt(len(goal_state)))
        self.goal_state = PuzzleState(goal_state, size)

        if solver == "bfs":
            self.bfs_search(initial_state)
        elif solver == "dfs":
            self.dfs_search(initial_state)
        elif solver == "ast":
            self.a_star_search(initial_state)
        else:
            print("Enter valid command arguments !")

    def writeOutput(self, state):
        # Student Code Goes here
        print("cost:", state.cost)

    def bfs_search(self, initial_state):
        """BFS search"""
        
        frontier = Q.Queue()
        frontier.put(initial_state)
        explored = [initial_state.config]

        while not frontier.empty():
            state = frontier.get()

            if(self.test_goal(state)):
                return True
            
            state.expand()
            for neighbor in state.children:
                if neighbor.config not in explored:
                    frontier.put(neighbor)
                    explored.append(neighbor)


        print("Failure")
        return False

        self.test_goal(initial_state)

    def dfs_search(self, initial_state):
        """DFS search"""
        ### STUDENT CODE GOES HERE ###
        print("dfs search")

    def A_star_search(self, initial_state):
        """A * search"""
        ### STUDENT CODE GOES HERE ###
        print("a* search")

    def calculate_total_cost(self, state):
        """calculate the total estimated cost of a state"""
        ### STUDENT CODE GOES HERE ###
        print("calculate total cost")

    def calculate_manhattan_dist(self, idx, value, n):
        """calculate the manhattan distance of a tile"""
        ### STUDENT CODE GOES HERE ###
        print("calculate manhattan dist")

    def test_goal(self, puzzle_state):
        """test the state is the goal state or not"""
        ### STUDENT CODE GOES HERE ###
        if(puzzle_state.config == self.goal_state.config):
            self.writeOutput(puzzle_state)
            return True
        else:
            return False
            print("false")

# Main Function that reads in Input and Runs corresponding Algorithm


def main():
    solver = "bfs"
    begin_state = "1,2,5,3,4,0,6,7,8"
    # begin_state = "0,1,2,3,4,5,6,7,8"
    solver = solver.lower()
    begin_state = begin_state.split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)

    solver = PuzzleSolver(solver, hard_state)


if __name__ == '__main__':
    main()
