def echo(word):
    print(word)


def fuck(word):
    combine = 'fuck ' + word
    return combine


def multi_re(word1, word2, word3):
    return word3, word2, word1


def loop(words='default', times=4):
    for i in range(times):
        print(words)


def f(a, List=[]):
    List.append(a)
    return List


def echo_ex(word, myecho):
    myecho(word)


def arbitrary_args(*args):
    print(args)


new_echo = echo

echo('int')
new_echo('new')
print(fuck('you'))
loop('some')
print(multi_re('1', '2', '3'))  # It's in a tuple
print(f(1))
print(f(2))
print(f(3))
echo_ex('Hello', loop)
print()
echo_ex('Hello', echo)
arbitrary_args(1, 2, 3)
