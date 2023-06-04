import random
from sympy import symbols, simplify
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

#등차수열 기본문제(1)
def generate_arithmetic1_problem():
    a = random.randint(-10, 10)  # 제 1항 범위: -10부터 10까지의 정수로 설정
    d = random.randint(-8, 8)  # 공차 범위: -8부터 8까지의 정수로 설정
    n = random.randint(2, 15)  # n 범위: 2부터 15까지의 정수로 설정

    problem = f"제 1항이 {a}이고, 공차가 {d}인 등차수열의 제 {n}항을 구하시오."
    answer =a + (n-1) * d
    return problem, answer

problem_statement, answer_expression = generate_arithmetic1_problem()


#등차수열 기본문제(2)
def generate_arithmetic2_problem():
    a = random.randint(1, 10)  # 첫 번째 항 범위: 1부터 10까지의 정수로 설정
    d = random.randint(1, 5)  # 공차 범위: 1부터 5까지의 정수로 설정

    n = symbols('n')  # n을 심볼로 정의
    general_term = a + (n - 1) * d  # 일반항을 계산

    problem = f"등차수열에서 일반항을 구하시오. (첫 번째 항: {a}, 공차: {d})"
    answer = simplify(general_term)  # 일반항을 간단하게 표현
    return problem, answer

problem_statement, answer_expression = generate_arithmetic2_problem()



#등차수열 기본문제(3)
def generate_arithmetic3_problem():
    a = random.randint(-10, 10)  # 첫 번째 항 범위: -10부터 10까지의 정수로 설정
    d = random.randint(-5, 5)  # 공차 범위: -5부터 5까지의 정수로 설정
    n = random.randint(8, 20)  # n 범위: 8부터 20까지의 정수로 설정

    sequence = [str(a + (i * d)) for i in range(5)]  # 등차 수열 생성
    sequence_expression = " + ".join(sequence)  # 등차 수열을 "+"로 연결하여 표현

    problem = f"등차수열의 합을 구하시오. (첫 번째 항부터 {n}번째 항까지)\n수열: {sequence_expression} + ..."
    answer = (n / 2) * (2 * a + (n - 1) * d)  # 등차 수열의 합 계산
    return problem, answer

problem_statement, answer_value = generate_arithmetic3_problem()



#등차수열 기본문제(4)    
def generate_arithmetic4_problem():
    a = random.randint(10, 60)  # 첫 번째 항 범위: 10부터 60까지의 정수로 설정
    d = random.randint(-8, -4)  # 공차 범위: -8부터 -4까지의 정수로 설정

    n = abs(a // d) + 1  # 음수가 나오는 항의 순서 계산

    problem = f"첫째항이 {a}, 공차가 {d}인 등차수열에서 처음으로 음수가 나오는 항은?"
    answer = f'제 {n}항'

    return problem, answer

problem_statement, answer_value = generate_arithmetic4_problem()


#등비수열 기본문제(1)
def generate_geometric1_problem():
    a = random.randint(-10, 10)  # 제 1항 범위: -10부터 10까지의 정수로 설정
    r = random.randint(-5, 5)  # 공비 범위: -5부터 5까지의 정수로 설정
    n = random.randint(2, 8)  # n 범위: 2부터 8까지의 정수로 설정

    problem = f"제 1항이 {a}이고, 공비가 {r}인 등비수열의 제 {n}항을 구하시오."
    answer = a * (r ** (n-1))
    return problem, answer

problem_statement, answer_value = generate_geometric1_problem()



#등비수열 기본문제(2)
def generate_geometric2_problem():
    r = random.randint(-5, 5)  # 등비수열의 공비 범위: -5부터 5까지의 랜덤 정수
    a = random.randint(1, 5)  # 제 a항 범위: 1부터 5까지의 랜덤 자연수
    b = random.randint(a + 1, 10)  # 제 b항 범위: a항 이후부터 10까지의 랜덤 자연수

    # 등비수열에서 a항과 b항의 위치 계산
    position_a = a - 1
    position_b = b - 1

    # a항과 b항의 값
    value_a = random.randint(1, 10)  # 제 a항 값 범위: 1부터 5까지의 랜덤 자연수
    value_b = value_a * (r ** (position_b - position_a))

    problem = f"등비수열에서 제 {a}항이 {value_a}이고, 제 {b}항이 {value_b}일 때, 이 등비수열의 공비는?"
    answer = r

    return problem, answer

problem_statement, answer_value = generate_geometric2_problem()



#등비수열 기본문제(3)
def generate_geometric3_problem():
    a = random.randint(1, 5)  # 첫항 a 범위: 1부터 5까지의 랜덤 자연수
    r = random.randint(-5, 5)  # 공비 r 범위: -5부터 5까지의 랜덤 자연수

    n = random.randint(6,10 )  # 구하고자 하는 항의 위치 n 범위: 6부터 10까지의 랜덤 자연수

    # 주어진 항들로부터 제 n항 구하기
    value_n = a * (r ** (n - 1))

    problem = f"등비수열 {a},{a*r},{a*(r**2)},{a*(r**3)},...에서 제 {n}항을 구하시오."
    answer = value_n

    return problem, answer

problem_statement, answer_value = generate_geometric3_problem()

# 문제 유형 리스트에 함수들 추가
problem_generators = [
    generate_arithmetic1_problem,
    generate_arithmetic2_problem,
    generate_arithmetic3_problem,
    generate_arithmetic4_problem,
    generate_geometric1_problem,
    generate_geometric2_problem,
    generate_geometric3_problem
]


@app.route('/', methods=['GET', 'POST'])
def generate_problems():
    if request.method == 'POST':
        num_problems = int(request.form['num_problems'])

        selected_problems = random.choices(problem_generators, k=num_problems)

        problems = []
        for problem_generator in selected_problems:
            problem_statement, answer_value = problem_generator()
            problems.append((problem_statement, answer_value))

        return render_template('problems.html', problems=problems)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()