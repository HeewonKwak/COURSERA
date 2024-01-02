def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
    
def parentheses(num_list, op_list):
    num_len = len(num_list)
    min_mat = [[float('INF')] * (num_len+1) for _ in range(num_len+1)]
    max_mat = [[-float('INF')] * (num_len+1) for _ in range(num_len+1)]
    for i in range(1, num_len + 1):
        min_mat[i][i] = num_list[i-1]
        max_mat[i][i] = num_list[i-1]
    def minandmax(i, j):
        min_v = min_mat[i][j]
        max_v = max_mat[i][j]
        for k in range(i, j):
            a = evaluate(max_mat[i][k], max_mat[k+1][j], op_list[k-1])
            b = evaluate(max_mat[i][k], min_mat[k+1][j], op_list[k-1])
            c = evaluate(min_mat[i][k], max_mat[k+1][j], op_list[k-1])
            d = evaluate(min_mat[i][k], min_mat[k+1][j], op_list[k-1])
            min_v = min(min_v, a, b, c, d)
            max_v = max(max_v, a, b, c, d)
        return min_v, max_v
    for s in range(1, num_len):
        for i in range( 1, num_len+1-s):
            j = i + s
            min_mat[i][j], max_mat[i][j] = minandmax(i, j)
    return max_mat[1][num_len]

def maximum_value(dataset):
    # write your code here
    num_list = []
    op_list = []
    for data in dataset:
        if data in ['+', '-', '*']:
            op_list.append(data)
        else:
            num_list.append(int(data))
    return parentheses(num_list, op_list)


if __name__ == "__main__":
    print(maximum_value(input()))
