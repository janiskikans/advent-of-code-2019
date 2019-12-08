import re

# Get wire paths in 2d list format
def get_wire_paths():
    wire_paths = []
    
    file = open('input.txt', 'r')
    for line in file.readlines():
        line = line.rstrip('\n')
        wire_paths.append(line.split(','))
    
    return wire_paths

# Get all wire path step coordinates in list form [[x,y], [x,y], ...]
def get_wire_path_coordinates(wire_path):
    x = 0
    y = 0
    wire_coordinate_path = []
    
    for step in wire_path:
        step_distance = get_step_distance(step)
        step_direction = get_step_direction(step)
        
        for step in range(0, step_distance):
            if (step_direction == "R") or (step_direction == "L"):
                if (step_direction == "R"):
                    x += 1
                else:
                    x -= 1
                wire_coordinate_path.append(str(x) + ',' + str(y))
                continue
                    
            
            if (step_direction == "U") or (step_direction == "D"):
                if (step_direction == "U"):
                    y += 1
                else:
                    y -= 1
                wire_coordinate_path.append(str(x) + ',' + str(y))
    
    return wire_coordinate_path

# Step through both wires, find the crossing point and manhattan distance to crossing point
def go_through_wire_path():
    wire_paths = get_wire_paths()
    first_wire_path = wire_paths[0]
    second_wire_path = wire_paths[1]
    
    first_wire_coordinate_path = get_wire_path_coordinates(first_wire_path)
    second_wire_coordinate_path = get_wire_path_coordinates(second_wire_path)
    
    crossing_points = find_crossing_point_coordinates(first_wire_coordinate_path, second_wire_coordinate_path)    
    lowest_step_count = get_min_steps_to_intersections(first_wire_coordinate_path, second_wire_coordinate_path, crossing_points)
    
    print("Lowest step count to intersection is " + str(lowest_step_count))

# Calculate manhattan distance to the closest crossing point
def calculate_manhattan_distance(coordinates):
    distances = []
    
    for coordinate in coordinates:
        x = int(coordinate.split(',')[0])
        y = int(coordinate.split(',')[1])
        distances.append(abs(x) + abs(y))
        
    return min(distances)

# Get the direction of the step
def get_step_direction(step):
    direction = re.search("([A-Z]+)", step)[0]
    return direction

# Get the distance of the step
def get_step_distance(step):
    distance = int(re.findall("(\d+)", step)[0])
    return distance

# Return the crossing point coordinate of two wires
def find_crossing_point_coordinates(first_path, second_path):            
    return set(first_path) & set(second_path)

# Return fewest combined steps the wires must take to reach an intersection
def get_min_steps_to_intersections(first_wire_path, second_wire_path, intersections):
    steps_to_intersections_first = []
    steps_to_intersections_second = []
    
    for intersection in intersections:
        step_count_first = 0
        step_count_second = 0
        
        for step in first_wire_path:
            step_count_first += 1
            if (step == intersection):
                steps_to_intersections_first.append(step_count_first)
                
        for step in second_wire_path:
            step_count_second += 1
            if (step == intersection):
                steps_to_intersections_second.append(step_count_second)
     
    step_sum_by_intersection = [x + y for x, y in zip(steps_to_intersections_first, steps_to_intersections_second)]
    return min(step_sum_by_intersection)

if __name__ == '__main__':
    go_through_wire_path()