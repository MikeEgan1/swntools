

def calculate_distance(start, destination):

    start_coords = parse_coords(start)
    dest_coords = parse_coords(destination)

    # outer_diff = (abs(start_x - destination_x) + abs(start_y - destination_y))
    #
    # inner_diff = abs(abs(start_x + start_y) - abs(destination_x + destination_y)) / 2

    # dist_calc = lambda sx, sy, dx, dy: (abs(sx - dx) + abs(sy - dy))
    #
    # inner_diff = (abs(sx - sy) - abs(dx - dy))
    #
    # distance = dist_calc(start_x, start_y, destination_x, destination_y)


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