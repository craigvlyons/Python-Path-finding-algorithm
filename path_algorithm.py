from queue import PriorityQueue
import pygame


# gets the distance between two points
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# draw the found path.
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


# main algorithm for searching though the grid from start to end Node.
def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    # run until all possible neighbors are checked or end is found
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # from open set after start / end position
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            # draw path function
            reconstruct_path(came_from, end, draw)
            # redraw start and end color after path.
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                # if not already seen add to open set
                if neighbor not in open_set_hash:
                    count += 1
                    # keeping track of the count back to the start.
                    open_set.put((f_score[neighbor], count, neighbor))
                    # add neighbor to open set
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            # mark as seen
            current.make_closed()

    return False
