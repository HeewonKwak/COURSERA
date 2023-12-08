# Algorithm 1: Generating a test for Maximum Pairwise product
# cmd: 'python script.py 10'
# cmd2: 'python script.py 17 > input.txt '
# import sys
# n = int(sys.argv[1])
# print(n)
# print(' '.join([str(i*2) for i in range(n)]))


# Algorithm 2: Generator that accepts a seed from the command line
# cmd: python script.py 10 2
# import random
# import sys
# n = int(sys.argv[1])
# myseed = int(sys.argv[2])
# random.seed(myseed)

# print(n)
# # 1000 could also be moved to parameters instead of making it
# # a hard constant in the code
# print(' '.join([str(random.randint (1, 1000)) for i in range(n)]))

# Algorithm 3: Main script
import random
import sys
import os
# accept the number of tests as a command line parameter
tests = int(sys.argv[1])
# accept the parameter for the tests as a command line parameter
n = int(sys.argv[2])
for i in range (tests):
    print('Test #' + str(i))
    # run the generator gen.py with parameter n and the seed i
    os.system('python gen.py ' + str(n) + ' ' + str(i) + ' > input.txt')
    # run the model solution model.py
    # Notice that it is not necessary that solution is implemented in
    # python , you can as well run ./model <input.txt >model.txt for a C++
    # solution.
    os.system('python model.py <input.txt >model.txt' )
    # run the main solution
    os.system('python main.py <input.txt >main.txt' )
    # read the output of the model solution:
    with open ('model.txt') as f : model = f.read()
    print('Model : ' , model)
    # read the output of the main solution:
    with open ('main.txt') as f : main = f.read()
    print( 'Main : ' , main )
    if model != main :
        break