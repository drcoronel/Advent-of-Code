from computer import Computer

with open('input17', 'r') as data:
    data = list(map(int, data.read().split(',')))

tape = Computer(int_code=data)
tape.compute()
print(' '.join(map(chr, reversed(tape.out))))
video = ''.join(map(chr, reversed(tape.out))).splitlines()
sum_ = 0
for y, (t, m, b) in enumerate(zip(video, video[1:], video[2:]), start=1):
    for x, (    t_,
           (m1, m2, m3),
                b_    ) in enumerate(zip(t[1:], zip(m, m[1:], m[2:]), b[1:]), start=1):
        if t_ == m1 == m2 == m3 == b_ == '#':
            sum_ += x * y

print(sum_) # Part 1

"""
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B B B B B B B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B . . . . . B . . . . . .
 . . . . . . . . . . . . . . C C C C C C C C C . . . . . . . . . B B B B B B B . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . C . . . . . . . . . A . . . . . . . . . . . B . . . . . .
 . . . . . . . . . . . . . . . . . . . . . . C . . . . . . . . . A . . . . . . . . . A A # A A A A A C
 . . . . . . . . . . . . . . . . . . . . . . C . . . . . . . . . A . . . . . . . . . A . B . . . . . C
 . . . . . . . . . . . . . . . . . . . . . . C . . . . . . . . . A . . . . . A A A A A A A . . . . . C
 . . . . . . . . . . . . . . . . . . . . . . C . . . . . . . . . A . . . . . A . . . A . . . . . . . C
 . . . . . . . . . . . . . . . . . . . . . . C C C C C C C C C C # C A . . . A . . . A . . . . . . . C
 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A . A . . . A . . . A . . . . . . . C
 B B B B B B B B B B B B ^ . . . . . . . . . . . . . . . . . . . A A A A A A A A A . A . . . . . . . C
 B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A . . . A . A . A . . . . . . . C
 B . . . . . . . . . . . . . . . . . A A A A A A A . . . . . . . . . A . . . A A A A A . C C C C C C C
 B . . . . . . . . . . . . . . . . . A . . . . . A . . . . . . . . . A . . . . . A . . . C . . . . . .
 B . . . . . . . . . . . . . . . A A A A A . . . A . . . . . . . . . A A A A A A A . . . C . . . . . .
 B . . . . . . . . . . . . . . . A . A . A . . . A . . . . . . . . . . . . . . . . . . . C . . . . . .
 B B B B B B B B B . . . . . . . A . A A A A A A A A A . . . . . . . . . . . . . . . . . C . . . . . .
 . . . . . . . . B . . . . . . . A . . . A . . . A . A . . . . . . . . . . . . . . . . . C . . . . . .
 . . . . . . . . B . . . . . . . A . . . A . . . A C # C C C C C C C C C C . . . . . . . C . . . . . .
 . . . . . . . . B . . . . . . . A . . . A . . . . . A . . . . . . . . . C . . . . . . . C . . . . . .
 . . . . . . . . B . . . . . A A A A A A A . . . . . A . . . . . . . . . C . . . . . . . C . . . . . .
 . . . . . . . . B . . . . . B . A . . . . . . . . . A . . . . . . . . . C . . . . . . . C . . . . . .
 . . . . . . . . B A A A A A # A A . . . . . . . . . A . . . . . . . . . C . . . . . . . C . . . . . .
 . . . . . . . . . . . . . . B . . . . . . . . . . . A . . . . . . . . . C . . . . . . . C2. . . . . .
 . . . . . . . . . . . . . . B . . . . . B B B B B B B . . . . . . . . . C C C C C C C C C . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B . . . . . B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . . B B B B B B B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
"""

# Solved by hand
'B,A,B,A,C,C,A,B,A,C\n' # Main
'L,8,L,8,R,4,R,6,R,6\n' # A
'L,12,L,6,L,8,R,6\n'    # B
'L,12,R,6,L,8\n'        # C

tape.int_code[0] = 2
functions = 'B,A,B,A,C,C,A,B,A,C\nL,8,L,8,R,4,R,6,R,6\nL,12,L,6,L,8,R,6\nL,12,R,6,L,8\nn\n'
tape.compute(feed=map(ord, functions))
print(tape.last()) # Part 2