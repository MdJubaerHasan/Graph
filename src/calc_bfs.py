from collections import deque


def calc_bfs(start:int, target:int):
    if start == target:
        return 0

    start_node = start
    queue = deque([(start_node, 0)])
    visited = {start_node}

    while queue:

        current_node, current_step = queue.popleft()
        print(f"Current node : {current_node} step : {current_step}")


        if current_node < target:
            mul_two = current_node * 2
            if mul_two == target:
                return current_step + 1
            else:
                if mul_two not in visited:
                    queue.append((mul_two, current_step + 1))
                    visited.add(mul_two)

        if current_node > 1:
            sub_one = current_node - 1
            if sub_one == target:
                return current_step + 1
            else:
                if sub_one not in visited:
                    queue.append((sub_one, current_step + 1))
                    visited.add(sub_one)

    return None

src = 11
dest = 11
res = calc_bfs(src, dest)
print(f"Shortest path from {src} -> {dest} is : {res}")


