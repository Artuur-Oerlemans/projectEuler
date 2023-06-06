from queue import PriorityQueue

file = open("p081_matrix.txt", "r")
contents = file.read()
matrix = [[int(s) for s in line.split(',')] for line in contents.split('\n')]

pq = PriorityQueue()
visited = {}


def add_to_queue(new_score, new_location):
    if new_location not in visited or visited[new_location] > new_score:
        pq.put((new_score, new_location))
        visited[new_location] = new_score


def find_minimal_path():
    score, location = (matrix[0][0], (0, 0))
    while location != (79, 79):
        if location[0] < 79:
            new_score = score + matrix[location[0] + 1][location[1]]
            new_location = (location[0] + 1, location[1])
            add_to_queue(new_score, new_location)

        if location[1] < 79:
            new_score = score + matrix[location[0]][location[1] + 1]
            new_location = (location[0], location[1] + 1)
            add_to_queue(new_score, new_location)

        score, location = pq.get()
    return score


print(find_minimal_path())
