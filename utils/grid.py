

def calculate_distance(start, destination):
    start_x = start / 100
    start_y = start % 10
    destination_x = destination / 100
    destination_y = destination % 10

    distance = (abs(start_x - destination_x) + abs(start_y - destination_y)) - 1

    print distance