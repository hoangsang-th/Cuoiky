# Nhóm 30
# Ngô Duy Tân-N19DCCN165
# Trương Hoàng Sang- N19DCCN157
import math
import random
# Các thành phố
cities = ['A', 'B', 'C', 'D']
# Ma trận chi phí C
cost_matrix = {
    ('A', 'B'): 20,
    ('A', 'C'): 42,
    ('A', 'D'): 35,
    ('B', 'A'): 20,  # Chi phí từ B đến A
    ('B', 'C'): 30,
    ('B', 'D'): 34,
    ('C', 'A'): 42,  # Chi phí từ C đến A
    ('C', 'B'): 30,  # Chi phí từ C đến B
    ('C', 'D'): 12,
    ('D', 'A'): 35,  # Chi phí từ D đến A
    ('D', 'B'): 34,  # Chi phí từ D đến B
    ('D', 'C'): 12   # Chi phí từ D đến C
}


# Hàm tính tổng chi phí của một hành trình
def calculate_total_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_cost += cost_matrix[(city1, city2)]
    return total_cost

# Hàm tạo hành trình ban đầu
def create_initial_route(cities):
    route = cities.copy()
    random.shuffle(route)
    return route

# Hàm tạo hành trình mới từ hành trình hiện tại
def create_new_route(route):
    new_route = route.copy()
    index1 = random.randint(1, len(route) - 2)
    index2 = random.randint(1, len(route) - 2)
    new_route[index1], new_route[index2] = new_route[index2], new_route[index1]
    return new_route

# Hàm chấp nhận hành trình mới
def accept_new_route(old_route, new_route, temperature):
    old_cost = calculate_total_cost(old_route)
    new_cost = calculate_total_cost(new_route)
    if new_cost < old_cost:
        return 1
    else:
        probability = math.exp((old_cost - new_cost) / temperature)
        return random.random() < probability

# Thuật toán simulated annealing
def simulated_annealing(cities):
    temperature = 100000
    cooling_rate = 0.99
    current_route = create_initial_route(cities)
    best_route = current_route.copy()
    while temperature >= 0.01:
        new_route = create_new_route(current_route)
        if accept_new_route(current_route, new_route, temperature):
            current_route = new_route.copy()
        if calculate_total_cost(current_route) < calculate_total_cost(best_route):
            best_route = current_route.copy()
        cooling_factor = random.uniform(0.9, 1.0)  # Hệ số ngẫu nhiên từ 0.9 đến 1.0
        temperature *= cooling_rate* cooling_factor
    return best_route


# Tìm hành trình tối ưu
best_route = simulated_annealing(cities)
print("Hành trình tối ưu:", best_route)
print("Tổng chi phí:", calculate_total_cost(best_route))
