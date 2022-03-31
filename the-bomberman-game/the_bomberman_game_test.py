from the_bomberman_game import bomberMan


def get_from_file(file):
    f = open(file,'r')

    line = f.readline().strip().split(' ')
    r = int(line[0])
    c = int(line[1])
    n = int(line[2])
   
    grid = []
    while True:
        line = f.readline().strip()
        if line:
            grid.append(line)
        else:
            break
    return n, grid

def get_expected(file):
    f = open(file,'r')
    result = []
    while True:
        line = f.readline().strip()
        if line:
            result.append(line)
        else:
            break
    return result


get_from_file('./test_cases/input1.txt')


def evaluate_bomberman(i):
    n, grid = get_from_file(f'./test_cases/input{i}.txt')
    expected = get_expected(f'./test_cases/expected{i}.txt')
    result = bomberMan(n, grid)
    assert result == expected

def test1():
    evaluate_bomberman(1)

def test2():
    evaluate_bomberman(2)

def test3():
    evaluate_bomberman(3)

def test4():
    evaluate_bomberman(4)