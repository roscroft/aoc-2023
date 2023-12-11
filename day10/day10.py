import networkx as nx

def get_input():
    with open("input.txt", "r", encoding="utf-8") as infile:
        return [line.strip() for line in infile]

def get_neighbors(coord):
    return [(coord[0]-1, coord[1]), (coord[0]+1, coord[1]), (coord[0],coord[1]-1), (coord[0], coord[1]+1)]

def get_graph(seqs):
    point_dct = {}
    start = ()
    graph = nx.Graph()
    for r_idx, row  in enumerate(seqs):
        for c_idx, val in enumerate(row):
            point_dct[(r_idx, c_idx)] = val
            graph.add_node((r_idx, c_idx, "n"))
            edge_nodes = [(r_idx, c_idx, "e"), (r_idx, c_idx+1, "e"), (r_idx+1, c_idx, "e"), (r_idx+1, c_idx+1, "e")]
            graph.add_nodes_from(edge_nodes)
            for edge_node in edge_nodes:
                graph.add_edge((r_idx, c_idx, "n"), edge_node)
            graph.add_edge((r_idx, c_idx, "e"), (r_idx, c_idx+1, "e"))
            graph.add_edge((r_idx, c_idx+1, "e"), (r_idx+1, c_idx+1, "e"))
            graph.add_edge((r_idx+1, c_idx, "e"), (r_idx+1, c_idx+1, "e"))
            graph.add_edge((r_idx, c_idx, "e"), (r_idx+1, c_idx, "e"))
            if val == "S":
                start = (r_idx, c_idx)

    return point_dct, start, graph

# Given a direction and a pipe in that direction, return the next direciton
def route(heading, pipe):
    if heading == "N": # going north
        dir_dict = {"|":"N", "7":"W", "F":"E"}
        return dir_dict.get(pipe, None)
    if heading == "E": #going east
        dir_dict = {"-":"E", "J":"N", "7":"S"}
        return dir_dict.get(pipe, None)
    if heading == "S": #going east
        dir_dict = {"|":"S", "J":"W", "L":"E"}
        return dir_dict.get(pipe, None)
    if heading == "W": #going east
        dir_dict = {"-":"W", "L":"N", "F":"S"}
        return dir_dict.get(pipe, None)
    return None

# Given a coordinate and a direction, return the coordinate one step in that direction
def dir_to_coord_change(coord, direction):
    if direction == "N":
        return (coord[0]-1, coord[1])
    if direction == "E":
        return (coord[0], coord[1]+1)
    if direction == "S":
        return (coord[0]+1, coord[1])
    if direction == "W":
        return (coord[0], coord[1]-1)

if __name__ == "__main__":
    # Given a direction and a current coordinate, return the next direction and next coordinate
    def enter_pipe_at_coord(heading, coord):
        new_coord = dir_to_coord_change(coord, heading)
        new_direction = route(heading, points[new_coord])
        return [new_direction, new_coord]

    def get_starts():
        valid_dirs = []
        for direction in ["N", "E", "S", "W"]:
            coord_in_dir = dir_to_coord_change(start, direction)
            pipe_in_dir = points.get(coord_in_dir, None)
            if pipe_in_dir is not None:
                next_step = route(direction, pipe_in_dir)
                if next_step is not None:
                    valid_dirs.append(direction)
        return valid_dirs

    def get_edge_to_remove(direction, coordinate):
        x,y = coordinate
        if direction == "N":
            return (x,y), (x,y+1)
        if direction == "E":
            return (x,y+1), (x+1,y+1)
        if direction == "S":
            return (x+1,y+1), (x+1,y)
        if direction == "W":
            return (x+1,y), (x,y)
    
    seqs = get_input()
    points, start, graph = get_graph(seqs)
    print("Start: ",start)
    start_dirs = get_starts()
    cur_dir = start_dirs[0]
    graph.remove_node((*start, "n"))
    next_dir, next_coord = enter_pipe_at_coord(cur_dir, start) #[direction, coordinate]
    left, right = get_edge_to_remove(cur_dir, start)
    graph.remove_edge((*left, "e"), (*right, "e"))
    forward_counter = 1
    # remove from the graph:
    # 1. all space nodes that are on the path
    # 2. edge nodes from the sides the pipe goes through

    while next_coord != start:
        cur_dir, cur_coord = next_dir, next_coord
        graph.remove_node((*cur_coord, "n"))
        next_dir, next_coord = enter_pipe_at_coord(cur_dir, cur_coord)
        left, right = get_edge_to_remove(cur_dir, cur_coord)
        graph.remove_edge((*left, "e"), (*right, "e"))
        forward_counter += 1
    print(forward_counter/2)
    connected = list(sorted(nx.connected_components(graph), key=len, reverse=True))
    subsizes = sorted([len(list(filter(lambda x: x[2]=="n", sub))) for sub in connected])
    print(sum(subsizes[:-1]))
    
