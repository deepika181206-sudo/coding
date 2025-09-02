import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(a, op, b):
    if op in ops:
        return ops[op](a, b)
    else:
        return "Invalid operator"

while True:
    inp = input("Enter calculation (e.g., 3 + 4), or 'q' to quit: ")
    if inp.lower() == 'q':
        print("Goodbye!")
        break

    try:
        parts = inp.split()
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])
        print("Result:", calculate(a, op, b))
    except Exception as e:
        print("Error:", e)
