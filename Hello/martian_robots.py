# def move_robot(x, y, orientation, instructions, scent_set, max_x, max_y):
#     orientations = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
#     left_turns = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
#     right_turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

#     for instruction in instructions:
#         if instruction == 'L':
#             orientation = left_turns[orientation]
#         elif instruction == 'R':
#             orientation = right_turns[orientation]
#         elif instruction == 'F':
#             dx, dy = orientations[orientation]
#             new_x = x + dx
#             new_y = y + dy

#             if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
#                 if (x, y) not in scent_set:
#                     scent_set.add((x, y))
#                     return x, y, orientation, True
#             else:
#                 x = new_x
#                 y = new_y

#     return x, y, orientation, False


# def process_robots(grid_size, robot_instructions):
#     max_x, max_y = map(int, grid_size.split())

#     for robot in robot_instructions:
#         initial_pos, instructions = robot.split('\n')
#         x, y, orientation = map(str.strip, initial_pos.split())
#         x, y = map(int, (x, y))
#         scent_set = set()

#         x, y, orientation, lost = move_robot(x, y, orientation, instructions, scent_set, max_x, max_y)

#         result = f"{x} {y} {orientation}"
#         if lost:
#             result += " LOST"

#         print(result)


# # Sample input
# grid_size = "5 3"
# robot_instructions = [
#     "1 1 E\nRFRFRFRF",
#     "3 2 N\nFRRFLLFFRRFLL",
#     "0 3 W\nLLFFFLFLFL"
# ]

# process_robots(grid_size, robot_instructions)


def move_robot(x, y, orientation, instructions, max_x, max_y):
    for instruction in instructions:
        if instruction == 'L':
            if orientation == 'N':
                orientation = 'W'
            elif orientation == 'W':
                orientation = 'S'
            elif orientation == 'S':
                orientation = 'E'
            elif orientation == 'E':
                orientation = 'N'
        elif instruction == 'R':
            if orientation == 'N':
                orientation = 'E'
            elif orientation == 'E':
                orientation = 'S'
            elif orientation == 'S':
                orientation = 'W'
            elif orientation == 'W':
                orientation = 'N'
        elif instruction == 'F':
            if orientation == 'N' and y < max_y:
                y += 1
            elif orientation == 'E' and x < max_x:
                x += 1
            elif orientation == 'S' and y > 0:
                y -= 1
            elif orientation == 'W' and x > 0:
                x -= 1

    return x, y, orientation


def process_robots(grid_size, robot_instructions):
    max_x, max_y = map(int, grid_size.split())

    for robot in robot_instructions:
        initial_pos, instructions = robot.split('\n')
        x, y, orientation = map(str.strip, initial_pos.split())
        x, y = map(int, (x, y))

        x, y, orientation = move_robot(x, y, orientation, instructions, max_x, max_y)

        result = f"{x} {y} {orientation}"
        print(result)


# Sample input
grid_size = "5 3"
robot_instructions = [
    "1 1 E\nRFRFRFRF",
    "3 2 N\nFRRFLLFFRRFLL",
    "0 3 W\nLLFFFLFLFL"
]

process_robots(grid_size, robot_instructions)
