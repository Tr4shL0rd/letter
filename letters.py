import string, itertools, time, math, os

passwordPicker = input("enter a password to guess: ")
password = passwordPicker
characters = string.printable
guess = 1
def iter_all_strings():
    global start
    start = time.time()
    length = 1
    while True:
        for s in itertools.product(characters, repeat=length):
            yield "".join(s)
        length +=1
for s in iter_all_strings():
        guess = guess + 1
        print(s, guess)
        if s == password:
                print('Password is {}'.format(s.upper()))
                end = time.time()
                elapsed = end - start
                print("it took {} seconds and {} guesses to crack the password {}!".format(round(elapsed, 3), guess, s.upper()))
                os.system('spd-say "your program has finished. it took {} seconds to crack the password "'.format(round(elapsed, 2)))
                break