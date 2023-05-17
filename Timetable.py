# Nhóm 30
# Ngô Duy Tân-N19DCCN165
# Trương Hoàng Sang- N19DCCN157
import random
import math

# Đầu vào
m = 5  # Số lớp học
n = 15  # Số giáo viên
p = 15  # Tổng số tiết học trong một tuần của giáo viên

# Ràng buộc cứng
def hard_constraints(schedule):
    violation_count = 0

    # H1: Đảm bảo các giáo viên dạy đủ số tiết
    for j in range(n):
        total_hours = sum(schedule[i][j][k] for i in range(m) for k in range(p))
        if total_hours != p:
            violation_count += 1

    # H2: Mỗi một giáo viên tại 1 thời điểm chỉ dạy một lớp
    for i in range(m):
        for k in range(p):
            teacher_count = sum(schedule[i][j][k] for j in range(n) if schedule[i][j][k] == 1)
            if teacher_count > 1:
                violation_count += 1

    # H3: Mỗi một lớp tại 1 thời điểm chỉ có một giáo viên dạy
    for k in range(p):
        for i in range(m):
            class_count = sum(schedule[i][j][k] for j in range(n) if schedule[i][j][k] == 1)
            if class_count > 1:
                violation_count += 1

    return violation_count


# Ràng buộc mềm
def soft_constraints(schedule):
    violation_count = 0

    # S1: Không xếp một giáo viên có tiết dạy ở các thứ liên tiếp
    for i in range(m):
        for j in range(n):
            for k in range(p - 1):
                if schedule[i][j][k] == 1 and schedule[i][j][k + 1] == 1:
                    violation_count += 1

    return violation_count


# Tạo lịch biểu ban đầu
def create_initial_schedule():
    schedule = [[[0] * p for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for k in range(p):
            teacher = random.randint(0, n - 1)
            schedule[i][teacher][k] = 1
    return schedule

# Hàm tạo lịch mới từ lịch hiện tại
def create_new_schedule(schedule):
    new_schedule = schedule.copy()
    # Tạo lịch mới bằng cách hoán đổi lớp học của hai giáo viên ngẫu nhiên
    teacher1 = random.randint(0, n - 1)
    teacher2 = random.randint(0, n - 1)
    for i in range(m):
        new_schedule[i][teacher1], new_schedule[i][teacher2] = new_schedule[i][teacher2], new_schedule[i][teacher1]
    return new_schedule

# Hàm tính điểm mục tiêu

def calculate_objective(schedule):
    return 20 * hard_constraints(schedule) + 10 * soft_constraints(schedule)

# Hàm chấp nhận lịch mới
def accept_new_schedule(old_schedule, new_schedule, temperature):
    old_score = calculate_objective(old_schedule)
    new_score = calculate_objective(new_schedule)
    if new_score < old_score:
        return True
    else:
        probability = math.exp((old_score - new_score) / temperature)
        return random.random() < probability
#Thuật toán Tôi rèn
def simulated_annealing():
    temperature = 100
    cooling_rate = 0.95
    current_schedule = create_initial_schedule()
    best_schedule = current_schedule.copy()
    while temperature > 0.1:
        new_schedule = create_new_schedule(current_schedule)
        if accept_new_schedule(current_schedule, new_schedule, temperature):
            current_schedule = new_schedule.copy()
        if calculate_objective(current_schedule) < calculate_objective(best_schedule):
            best_schedule = current_schedule.copy()
        temperature *= cooling_rate
    return best_schedule

#Thực thi thuật toán Tôi rèn
best_solution = simulated_annealing()

# Tính điểm mục tiêu
objective = calculate_objective(best_solution)
print("Điểm mục tiêu:", objective)
# # Xuất bảng dữ liệu
# print("Bảng dữ liệu:")
#
# # Tiêu đề hàng đầu
# header = ["Thứ", "Tiết"]
# header.extend([f"T{j+1}" for j in range(n)])
# print("\t".join(header))
#
# # Xuất dữ liệu
# day_counter = 1
# for k in range(p):
#     if (k % 5) == 0:
#         day_counter += 1
#     row = [str(day_counter), str((k % 5) + 1)]
#     for j in range(n):
#         class_schedule = "\t"
#         for i in range(m):
#             if best_solution[i][j][k] == 1:
#                 class_schedule += f"C{i+1} "
#         row.append(class_schedule)
#     print("\t".join(row))
# Ma trận R
print("Ma trận R:")
for i in range(m):
    row = []
    for j in range(n):
        total_hours = sum(best_solution[i][j][k] for k in range(p))
        row.append(str(total_hours))
    print("\t".join(row))

# Ma trận T
print("Ma trận T:")
for j in range(n):
    row = []
    for k in range(p):
        tjk = 1 if any(best_solution[i][j][k] for i in range(m)) else 0
        row.append(str(tjk))
    print("\t".join(row))

# Ma trận C
print("Ma trận C:")
for i in range(m):
    row = []
    for k in range(p):
        cik = 1 if any(best_solution[i][j][k] for j in range(n)) else 0
        row.append(str(cik))
    print("\t".join(row))

# Ma trận D
print("Ma trận D:")
for i in range(m):
    row = []
    for k in range(p):
        djk = 1 if any(best_solution[i][j][k] for j in range(n)) else 0
        row.append(str(djk))
    print("\t".join(row))

