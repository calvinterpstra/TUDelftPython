
import queue as Q
import time
# import resource
import sys
import math


class PuzzleState(object):

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

    def __lt__(self, other):
        return False

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)
        print("")

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


class PuzzleSolver():

    def __init__(self, solver, initial_state):
        goal_state = "0,1,2,3,4,5,6,7,8"
        goal_state = goal_state.split(",")
        goal_state = tuple(map(int, goal_state))
        size = int(math.sqrt(len(goal_state)))
        self.goal_state = PuzzleState(goal_state, size)

        self.nodes_expanded = 0
        self.frontier_size = 0
        self.explored_size = 0
        self.max_search_depth = 0

        self.LOCATIONS = [[0, 0], [1, 0], [2, 0],
                          [0, 1], [1, 1], [2, 1],
                          [0, 2], [1, 2], [2, 2]]

        if solver == "bfs":
            self.bfs_search(initial_state)
        elif solver == "dfs":
            self.dfs_search(initial_state)
        elif solver == "ast":
            self.a_star_search(initial_state)
        else:
            print("Enter valid command arguments !")

    # Function that Writes to output.txt
    def writeOutput(self, state):
        print("path to goal:", self.get_path(state))
        print("cost of path:", state.cost)
        print("nodes expanded:", self.nodes_expanded)
        print("search depth:", len(self.get_path(state)))
        print("max search depth:", self.max_search_depth)
        print("running time:", resource.getrusage(
            resource.RUSAGE_SELF).ru_utime)
        print("max ram usage:", resource.getrusage(
            resource.RUSAGE_SELF).ru_maxrss)

    def get_path(self, state):
        parent_state = state
        path = [state.action]
        for i in range(state.cost-1):
            parent_state = parent_state.parent
            path.append(parent_state.action)
        return list(reversed(path))

    # BFS search
    def bfs_search(self, initial_state):
        frontier_q = Q.Queue()
        frontier_q.put(initial_state)
        # frontier = [initial_state.config]
        explored = []

        while not frontier_q.empty():
            state = frontier_q.get()
            explored.append(state.config)
            # frontier.remove(state.config)

            if(self.test_goal(state)):
                self.writeOutput(state)
                return True

            self.nodes_expanded += 1
            state.expand()
            for neighbor in state.children:
                if neighbor.config not in (explored):  # + frontier):
                    self.update_max_depth(neighbor)
                    frontier_q.put(neighbor)
                    # frontier.append(neighbor.config)
                    explored.append(neighbor.config)

        print("Failure")
        return False

    # DFS search
    def dfs_search(self, initial_state):
        frontier_q = Q.LifoQueue()
        frontier_q.put(initial_state)
        # frontier = [initial_state.config]
        explored = [initial_state.config]

        while not frontier_q.empty():
            state = frontier_q.get()
            # explored.append(state.config)
            # frontier.remove(state.config)

            if(self.test_goal(state)):
                self.writeOutput(state)
                return True

            self.nodes_expanded += 1
            # self.print_nodes()
            state.expand()
            for neighbor in state.children:
                if neighbor.config not in (explored):  # + frontier):
                    # self.update_max_depth(neighbor)
                    frontier_q.put(neighbor)
                    # frontier.append(neighbor.config)
                    explored.append(neighbor.config)

        print("Failure")
        return False

    def print_nodes(self):
        print(self.nodes_expanded)

    def update_max_depth(self, neighbor):
        search_depth = len(self.get_path(neighbor))
        if(self.max_search_depth < search_depth):
            self.max_search_depth = search_depth

    # A * search
    def a_star_search(self, initial_state):
        frontier_q = Q.PriorityQueue()
        frontier_q.put(
            [self.calculate_total_cost(initial_state), initial_state])
        # frontier = [initial_state.config]
        explored = [initial_state.config]

        while not frontier_q.empty():
            state = frontier_q.get()[1]
            explored.append(state.config)
            # frontier.remove(state.config)

            if(self.test_goal(state)):
                self.writeOutput(state)
                return True

            self.nodes_expanded += 1
            self.print_nodes()

            state.expand()
            for neighbor in state.children:
                if neighbor.config not in (explored):  # + frontier):
                    self.update_max_depth(neighbor)
                    frontier_q.put([self.calculate_total_cost(neighbor), neighbor])
                    # frontier.append(neighbor.config)
                    explored.append(neighbor.config)

        print("Failure")
        return False

    # calculate the total estimated cost of a state
    def calculate_total_cost(self, state):
        g_x = state.cost
        h_x = 0
        for i in range(state.n**2):
            h_x += self.calculate_manhattan_dist(
                self.get_location(state, i), i)
        return g_x + h_x

    # calculate the manhattan distance of a tile
    def calculate_manhattan_dist(self, location, value):
        return abs(location[0] - self.LOCATIONS[value][0]) + abs(location[1] - self.LOCATIONS[value][1])

    def get_location(self, state, value):
        for i, item in enumerate(state.config):
            if item == value:
                row = i // state.n
                col = i % state.n
                return [row, col]

    # test the state is the goal state or not
    def test_goal(self, puzzle_state):
        if(puzzle_state.config == self.goal_state.config):
            return True
        else:
            return False


# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    solver = "ast"
    begin_state = "1,2,5,3,4,0,6,7,8"
    # begin_state = "0,1,2,3,4,5,6,7,8"
    # begin_state = "6,1,8,4,0,2,7,3,5"
    solver = solver.lower()
    begin_state = begin_state.split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)

    solver = PuzzleSolver(solver, hard_state)


if __name__ == '__main__':
    main()
