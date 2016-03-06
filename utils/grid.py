

def calculate_distance(start, destination):

    start_coords = parse_coords(start)
    dest_coords = parse_coords(destination)



    print outer_diff
    print inner_diff


def traverse_hex(start, destination):
    start_coords = parse_coords(start)
    dest_coords = parse_coords(destination)


    #first coord even or odd
    odd_connections = [(1,0), (-1,0), (0,1), (0,-1), (-1,1),(1,1)]
    even_connections = [(1,0), (-1,0), (0,1), (0,-1), (1,-1),(-1,-1)]


def parse_coords(coords):
    return [coords / 100, coords % 10]

def main():
    calculate_distance(101, 202)

if __name__ == "__main__":
    main()