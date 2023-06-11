# Nhóm 30
# Ngô Duy Tân-N19DCCN165
# Trương Hoàng Sang- N19DCCN157
import numpy as np
import random
import math

# Kích thước lớp học và giáo viên
m = 15
n = 22
# Tổng số tiết học trong một tuần
p = 25

# Ma trận R (số tiết mà giáo viên phải dạy cho lớp)
R = np.array([
    [4, 0, 0, 0, 4, 0, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 4, 0, 0, 4, 0, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [4, 0, 0, 0, 4, 0, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 4, 0, 0, 4, 0, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 4, 0, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 4, 0, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [4, 0, 0, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 0, 4, 0, 0, 4, 0, 0, 0, 3, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2],
    [0, 0, 0, 4, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 4, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 4, 0, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 4, 0, 0, 4, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 4, 0, 0, 0, 0, 4, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 4, 0, 0, 0, 0, 4, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 4, 0, 0, 0, 4, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]
])
def initialize_schedule(n, p):
    # Tạo ma trận  với kích thước (n x p)
    schedule = np.zeros((n, p), dtype=int)

    # Xếp lịch cho từng giáo viên ngẫu nhiên
    for j in range(n):
        # Tính tổng số tiết cho giáo viên j
        sum_periods = np.random.randint(1, p + 1)

        # Tạo một mảng chứa các tiết học sẽ được xếp lịch cho giáo viên j
        periods = np.random.choice(range(1, p + 1), size=sum_periods, replace=False)

        # Đặt các giá trị trong ma trận  cho giáo viên j
        for period in periods:
            # Chọn ngẫu nhiên một lớp
            class_number = np.random.randint(1, m+1 )
            schedule[j, period - 1] = class_number

    return schedule
def H1(state):

    # Kiểm tra ràng buộc H1: Đảm bảo các giáo viên dạy đủ số tiết trong một tuần
    # Tính tổng số tiết dạy của mỗi giáo viên trong một tuần
    total_lessons = np.sum(state, axis=1)
    # Kiểm tra nếu tổng số tiết dạy của mỗi giáo viên khớp với ma trận R
    is_satisfied = np.array_equal(total_lessons, R)
    return is_satisfied


def H2(state):
    # Kiểm tra ràng buộc H2: Mỗi giáo viên tại một thời điểm chỉ dạy một lớp
    # Kiểm tra nếu không có hai lớp của cùng một giáo viên được xếp cùng một thời điểm
    for i in range(len(state[0])):
        teacher_schedule = state[:, i]
        if np.count_nonzero(teacher_schedule) > 1:
            return False
    return True


def H3(state):
    # Kiểm tra ràng buộc H3: Mỗi lớp tại một thời điểm chỉ có một giáo viên dạy
    # Kiểm tra nếu không có hai giáo viên dạy cùng một lớp cùng một thời điểm
    for i in range(len(state)):
        class_schedule = state[i, :]
        if np.count_nonzero(class_schedule) > 1:
            return False
    return True


def S1(state):
    # Kiểm tra ràng buộc S1: Giáo viên có tiết trống giữa các tiết dạy
    # Kiểm tra nếu không có hai tiết dạy liên tiếp của cùng một giáo viên
    for teacher_schedule in state:
        for i in range(len(teacher_schedule) - 1):
            if teacher_schedule[i] != 0 and teacher_schedule[i + 1] != 0:
                return False
    return True


def S2(state):
    # Kiểm tra ràng buộc S2: Không xếp một giáo viên có tiết dạy ở các thứ liên tiếp
    # Kiểm tra nếu không có hai tiết dạy của cùng một giáo viên ở các thứ liên tiếp
    for i in range(len(state[0]) - 1):
        for j in range(len(state)):
            if state[j][i] != 0 and state[j][i + 1] != 0:
                return False
    return True


def S3(state):
    # Kiểm tra ràng buộc S3: Hai tiết của mỗi giáo viên cùng một lớp không nằm liền nhau một ngày
    # Kiểm tra nếu không có hai tiết dạy của cùng một lớp bởi cùng một giáo viên nằm liền nhau một ngày
    for teacher_schedule in state:
        for i in range(len(teacher_schedule) - 2):
            if teacher_schedule[i] != 0 and teacher_schedule[i + 1] != 0 and teacher_schedule[i + 2] != 0:
                return False
    return True

def objective(state):
    # Hàm tính giá trị mục tiêu của trạng thái
    # Tính tổng số điểm vi phạm của các ràng buộc cứng
    violation_hard = 0
    if not H1(state):
        violation_hard += 1
    if not H2(state):
        violation_hard += 1
    if not H3(state):
        violation_hard += 1

    # Tính tổng số điểm vi phạm của các ràng buộc mềm
    violation_soft = 0
    if not S1(state):
        violation_soft += 1
    if not S2(state):
        violation_soft += 1
    if not S3(state):
        violation_soft += 1

    # Tính giá trị mục tiêu
    obj_value = 20 * violation_hard + 3 * violation_soft
    return obj_value


def generate_neighbor(n,p,state):
    # Sinh ra một láng giềng ngẫu nhiên bằng cách hoán đổi ngẫu nhiên hai lớp của hai giáo viên
    neighbor = np.copy(state)

    # Chọn ngẫu nhiên hai vị trí lớp và giáo viên
    teacher1, teacher2 = random.sample(range(n), 2)
    class1, class2 = random.sample(range(p), 2)

    # Hoán đổi hai lớp

    neighbor[teacher1, class1], neighbor[teacher2, class2] = neighbor[teacher2, class2], neighbor[teacher1, class1]

    return neighbor

def simulated_annealing(m, n, p, R, max, initial_temperature, cooling_rate):
    # Đọc dữ liệu và khởi tạo trạng thái ban đầu
    state = initialize_schedule(n,p)

    # Khởi tạo nhiệt độ ban đầu
    temperature = initial_temperature

    # Lặp cho đến khi điều kiện dừng được đạt đến
    for _ in range(max):
        # Sinh ra một láng giềng mới
        neighbor_state = generate_neighbor(n,p,state)

        # Tính giá trị mục tiêu của trạng thái hiện tại và láng giềng
        current_obj = objective(state)
        neighbor_obj = objective(neighbor_state)

        # Kiểm tra nếu láng giềng tốt hơn hoặc theo xác suất dựa trên nhiệt độ
        if neighbor_obj < current_obj or random.random() <  math.exp((current_obj - neighbor_obj) / temperature):
            # Chấp nhận láng giềng làm trạng thái mới
            state = neighbor_state

        # Cập nhật nhiệt độ
        cooling_factor = random.uniform(0.9, 1.0)  # Hệ số ngẫu nhiên từ 0.9 đến 1.0
        temperature *= cooling_rate * cooling_factor

    # Trả về trạng thái cuối cùng
    return state
def main():
    # Tham số cho thuật toán Simulated Annealing
    max = 100000
    initial_temp = 10000
    cooling_rate = 0.99

    # Chạy thuật toán Simulated Annealing
    final_schedule = simulated_annealing(m, n, p, R, max, initial_temp, cooling_rate)
    obj = objective(final_schedule)
    print("Điểm vi phạm:", obj)
    # In lịch biểu cuối cùng
    print(final_schedule)
if __name__ == '__main__':
    main()


