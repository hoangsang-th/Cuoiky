import random
import math

# Hàm tính tổng thời gian hoàn thành của lịch công việc
def calculate_completion_time(schedule):
    completion_time = 0
    current_time = 0
    for job in schedule:
        current_time += job
        completion_time += max(current_time, job)
    return completion_time

# Hàm tạo lịch lập công việc mới
def generate_new_schedule(schedule):
    new_schedule = schedule[:]
    # Hoán đổi vị trí của hai công việc ngẫu nhiên
    index1 = random.randint(0, len(schedule) - 1)
    index2 = random.randint(0, len(schedule) - 1)
    new_schedule[index1], new_schedule[index2] = new_schedule[index2], new_schedule[index1]
    return new_schedule

# Hàm tính xác suất chấp nhận lịch mới
def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

# Hàm tìm kiếm tôi thép
def simulated_annealing(jobs, initial_temperature, cooling_rate, num_iterations):
    current_schedule = jobs[:]
    best_schedule = jobs[:]
    current_cost = calculate_completion_time(current_schedule)
    best_cost = current_cost
    temperature = initial_temperature

    for i in range(num_iterations):
        new_schedule = generate_new_schedule(current_schedule)
        new_cost = calculate_completion_time(new_schedule)

        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_schedule = new_schedule
            current_cost = new_cost

        if new_cost < best_cost:
            best_schedule = new_schedule
            best_cost = new_cost

        temperature *= cooling_rate

    return best_schedule, best_cost

# Các công việc và thời gian thực hiện của chúng
jobs = [3, 4, 5, 1, 2]

# Tham số của thuật toán tôi thép
initial_temperature = 1000
cooling_rate = 0.95
num_iterations = 1000

# Giải quyết bài toán bằng thuật toán tôi thép
best_schedule, best_cost = simulated_annealing(jobs, initial_temperature, cooling_rate, num_iterations)

# Kết quả
print("Lịch lập công việc tốt nhất:", best_schedule)
print("Tổng thời gian hoàn thành tốt nhất:", best_cost)
