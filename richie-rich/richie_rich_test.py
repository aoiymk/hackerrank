from richie_rich import highestValuePalindrome

def get_from_file(file):
    f = open(file,'r')

    line1 = f.readline().strip().split(' ')
    n = int(line1[0])
    k = int(line1[1])

    s = f.readline().strip()
    return n,k,s

def get_expected(file):
    return open(file,'r').readline().strip()

def evaluate_richie_rich(i):
    n,k,s = get_from_file(f'./test_cases/input_{i}.txt')
    expected = get_expected(f'./test_cases/expected_{i}.txt')
    result = highestValuePalindrome(s,n,k)
    assert result == expected

def test1():
    evaluate_richie_rich(1)

def test2():
    evaluate_richie_rich(2)

def test3():
    evaluate_richie_rich(3)

def test4():
    evaluate_richie_rich(4)