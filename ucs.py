import queue

state_space = {"S": {}, "A": {}, "B": {}, "C": {}, "D": {}, "E": {}, "G": {}}
state_space["S"]["A"] = 1
state_space["S"]["B"] = 5
state_space["S"]["C"] = 8
state_space["A"]["D"] = 3
state_space["A"]["E"] = 7
state_space["A"]["G"] = 9
state_space["B"]["G"] = 4
state_space["C"]["G"] = 5

h_value = {"S": 8, "A": 8, "B": 4, "C": 3, "D": 1000, "E": 1000, "G": 0}

initial_state = "S"
goal_state = "G"

my_queue = queue.PriorityQueue()
my_queue.put((0, initial_state))
visited = {}

while my_queue.qsize() > 0:
    cost, path = my_queue.get()
    node = path[-1]

    if node == goal_state:
        print("Solution found: ", path)
        break

    if node not in visited:
        for child in state_space[node]:
            my_queue.put((cost + state_space[node][child], path + child))
        visited[node] = True