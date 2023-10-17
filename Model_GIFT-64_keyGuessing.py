import gurobipy as gp
from gurobipy import GRB

m = gp.Model('gift_64_key_guess')

# ------------------------------ variables ---------------------------------

# known Eb
knownX2 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownX_2')
knownY2 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownY_2')
knownX3 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownX_3')
knownY3 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownY_3')
# known Ef
knownX24 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownX_24')
knownY24 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownY_24')
knownX25 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownX_25')
knownY25 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownY_25')
knownX26 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownX_26')
knownY26 = m.addVars(16, 4, vtype=GRB.BINARY, name='knownY_26')

# fix Eb
fixX2 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixX_2')
fixY2 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixY_2')
fixX3 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixX_3')
fixY3 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixY_3')
# fix Ef
fixX24 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixX_24')
fixY24 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixY_24')
fixX25 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixX_25')
fixY25 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixY_25')
fixX26 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixX_26')
fixY26 = m.addVars(16, 4, vtype=GRB.BINARY, name='fixY_26')

# sub-key
gk_0 = m.addVars(16, vtype=GRB.BINARY, name='gk_0')
gk_1 = m.addVars(16, vtype=GRB.BINARY, name='gk_1')
gk_2 = m.addVars(16, vtype=GRB.BINARY, name='gk_2')
gk_3 = m.addVars(16, vtype=GRB.BINARY, name='gk_3')
gk_6 = m.addVars(16, vtype=GRB.BINARY, name='gk_6')
gk_7 = m.addVars(16, vtype=GRB.BINARY, name='gk_7')

T1 = m.addVar(name='T1')
T2 = m.addVar(name='T2')
T3 = m.addVar(name='T3')
T = m.addVar(name='T')


# ------------------------------ fix ---------------------------------

'''
fix the state X and Y only, 
plaintext = Z1 -> X2, 
ciphertext = Z26 -> Y26
'''
# Eb
stateX2 = list(reversed(['????', '????', '????', '????', '0000', '0000', '0000', '0000',
                         '11??', '????', '????', '????', '????', '11??', '????', '????']))
stateY2 = list(reversed(['0?01', '00?0', '000?', '?000', '0000', '0000', '0000', '0000',
                         '0100', '00?0', '000?', '?000', '?000', '0100', '00?0', '000?']))
stateX3 = list(reversed(['????', '0000', '?1??', '0000', '0000', '0000', '0000', '0000',
                         '0001', '0000', '0000', '0000', '0000', '0000', '0000', '?1??']))
stateY3 = list(reversed(['1000', '0000', '0010', '0000', '0000', '0000', '0000', '0000',
                         '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0010']))

# Ef
stateX24 = list(reversed(['0000', '0100', '0000', '0000', '0000', '0000', '0000', '0000',
                          '0000', '0001', '0010', '0000', '0001', '0000', '0000', '0000']))
stateY24 = list(reversed(['0000', '???1', '0000', '0000', '0000', '0000', '0000', '0000',
                          '0000', '????', '????', '0000', '????', '0000', '0000', '0000']))
stateX25 = list(reversed(['00?0', '0000', '00??', '0?00', '0001', '0000', '?00?', '00?0',
                          '?010', '0000', '??00', '000?', '0?00', '0000', '0??0', '?000']))
stateY25 = list(reversed(['????', '0000', '????', '????', '????', '0000', '????', '????',
                          '????', '0000', '????', '????', '????', '0000', '????', '????']))
stateX26 = list(reversed(['??0?', '??0?', '??0?', '??0?', '???0', '???0', '???0', '???0',
                          '0???', '0???', '0???', '0???', '?0??', '?0??', '?0??', '?0??']))
stateY26 = list(reversed(['????', '????', '????', '????', '????', '????', '????', '????',
                          '????', '????', '????', '????', '????', '????', '????', '????']))

for s in range(16):
    # indexes follow the diagram
    stateX2[s] = stateX2[s][::-1]
    stateY2[s] = stateY2[s][::-1]

    stateX3[s] = stateX3[s][::-1]
    stateY3[s] = stateY3[s][::-1]

    stateX24[s] = stateX24[s][::-1]
    stateY24[s] = stateY24[s][::-1]

    stateX25[s] = stateX25[s][::-1]
    stateY25[s] = stateY25[s][::-1]

    stateX26[s] = stateX26[s][::-1]
    stateY26[s] = stateY26[s][::-1]

for i in range(16):
    for j in range(4):
        # mark all plaintext/ciphertext known
        m.addConstr(knownX2[i, j] == 1)
        m.addConstr(knownY26[i, j] == 1)

        # mark all fix position Eb
        m.addConstr(fixX2[i, j] == 0) if stateX2[i][j] == '?' else m.addConstr(fixX2[i, j] == 1)
        m.addConstr(fixY2[i, j] == 0) if stateY2[i][j] == '?' else m.addConstr(fixY2[i, j] == 1)

        m.addConstr(fixX3[i, j] == 0) if stateX3[i][j] == '?' else m.addConstr(fixX3[i, j] == 1)
        m.addConstr(fixY3[i, j] == 0) if stateY3[i][j] == '?' else m.addConstr(fixY3[i, j] == 1)

        m.addConstr(fixX24[i, j] == 0) if stateX24[i][j] == '?' else m.addConstr(fixX24[i, j] == 1)
        m.addConstr(fixY24[i, j] == 0) if stateY24[i][j] == '?' else m.addConstr(fixY24[i, j] == 1)

        m.addConstr(fixX25[i, j] == 0) if stateX25[i][j] == '?' else m.addConstr(fixX25[i, j] == 1)
        m.addConstr(fixY25[i, j] == 0) if stateY25[i][j] == '?' else m.addConstr(fixY25[i, j] == 1)

        m.addConstr(fixX26[i, j] == 0) if stateX26[i][j] == '?' else m.addConstr(fixX26[i, j] == 1)
        m.addConstr(fixY26[i, j] == 0) if stateY26[i][j] == '?' else m.addConstr(fixY26[i, j] == 1)

# ------------------------------ find known ---------------------------------
for cell in range(16):
    '''
    idea: X known to Y known
    if x[0,1,2,3] and gk [0,1] are all 1 (sum=6) then known[0,1,2,3] are all 1,
    else known are all 0

    11 entries
    1. each input fix,gk >= known[0]
    2. all input - sum(fix,gk) + known[0] - 5 >= 0
    3. known[1,2,3] == known[0]
    '''
    # round 2
    m.addConstr(- knownX2[cell, 0] - knownX2[cell, 1] - knownX2[cell, 2] - knownX2[cell, 3]
                - gk_0[cell] - gk_1[cell] + knownY2[cell, 0] + 5 >= 0)
    for pos in range(4):
        m.addConstr(knownX2[cell, pos] >= knownY2[cell, 0])
    m.addConstr(gk_0[cell] >= knownY2[cell, 0])
    m.addConstr(gk_1[cell] >= knownY2[cell, 0])
    m.addConstr(knownY2[cell, 1] == knownY2[cell, 0])
    m.addConstr(knownY2[cell, 2] == knownY2[cell, 0])
    m.addConstr(knownY2[cell, 3] == knownY2[cell, 0])

    # round 3
    m.addConstr(- knownX3[cell, 0] - knownX3[cell, 1] - knownX3[cell, 2] - knownX3[cell, 3]
                - gk_2[cell] - gk_3[cell] + knownY3[cell, 0] + 5 >= 0)
    for pos in range(4):
        m.addConstr(knownX3[cell, pos] >= knownY3[cell, 0])
    m.addConstr(gk_2[cell] >= knownY3[cell, 0])
    m.addConstr(gk_3[cell] >= knownY3[cell, 0])
    m.addConstr(knownY3[cell, 1] == knownY3[cell, 0])
    m.addConstr(knownY3[cell, 2] == knownY3[cell, 0])
    m.addConstr(knownY3[cell, 3] == knownY3[cell, 0])


# Ef, == note: the shuffled^-1 sub_keys ==
cells = [[i] for i in range(16)]
sub_keys24 = [[12, 14], [8, 10], [4, 6], [0, 2], [13, 15], [9, 11], [5, 7], [1, 3],
              [14, 0], [10, 12], [6, 8], [2, 4], [15, 1], [11, 13], [7, 9], [3, 5]]
position24 = []
for i in range(16):
    position24.append(cells[i] + sub_keys24[i])
# position: [0, 12, 14], [1, 8, 10], [2, 4, 6]...

for cell, i, j in position24:
    m.addConstr(- knownY24[cell, 0] - knownY24[cell, 1] - knownY24[cell, 2] - knownY24[cell, 3]
                - gk_6[i] - gk_7[j] + knownX24[cell, 0] + 5 >= 0)

    for pos in range(4):
        m.addConstr(knownY24[cell, pos] >= knownX24[cell, 0])

    m.addConstr(gk_6[i] >= knownX24[cell, 0])
    m.addConstr(gk_7[j] >= knownX24[cell, 0])
    m.addConstr(knownX24[cell, 1] == knownX24[cell, 0])
    m.addConstr(knownX24[cell, 2] == knownX24[cell, 0])
    m.addConstr(knownX24[cell, 3] == knownX24[cell, 0])


# round 25 with reused sub_keys
sub_keys256 = [[8, 0], [4, 12], [0, 8], [12, 4], [9, 1], [5, 13], [1, 9], [13, 5],
              [10, 2], [6, 14], [2, 10], [14, 6], [11, 3], [7, 15], [3, 11], [15, 7]]
position256 = []
for i in range(16):
    position256.append(cells[i] + sub_keys256[i])
# position: [0, 8, 0], [1, 4, 12], [2, 0, 8]...

for cell, i, j in position256:

    m.addConstr(- knownY26[cell, 0] - knownY26[cell, 1] - knownY26[cell, 2] - knownY26[cell, 3]
                - gk_2[i] - gk_3[j] + knownX26[cell, 0] + 5 >= 0)
    for pos in range(4):
        m.addConstr(knownY26[cell, pos] >= knownX26[cell, 0])

    m.addConstr(gk_2[i] >= knownX26[cell, 0])
    m.addConstr(gk_3[j] >= knownX26[cell, 0])
    m.addConstr(knownX26[cell, 1] == knownX26[cell, 0])
    m.addConstr(knownX26[cell, 2] == knownX26[cell, 0])
    m.addConstr(knownX26[cell, 3] == knownX26[cell, 0])

    # position: [0, 8, 0], [1, 4, 12], [2, 0, 8]...
    m.addConstr(- knownY25[cell, 0] - knownY25[cell, 1] - knownY25[cell, 2] - knownY25[cell, 3]
                - gk_0[i] - gk_1[j] + knownX25[cell, 0] + 5 >= 0)
    for pos in range(4):
        m.addConstr(knownY25[cell, pos] >= knownX25[cell, 0])

    m.addConstr(gk_0[i] >= knownX25[cell, 0])
    m.addConstr(gk_1[j] >= knownX25[cell, 0])
    m.addConstr(knownX25[cell, 1] == knownX25[cell, 0])
    m.addConstr(knownX25[cell, 2] == knownX25[cell, 0])
    m.addConstr(knownX25[cell, 3] == knownX25[cell, 0])

# ------------------------------ linear layer ---------------------------------
def shuffle(position, reverse):
    '''
    :param position: position of in/out-put
    :param reverse: reverse = False if forward, reverse = True otherwise
    :return:
    '''
    permutation = [0, 17, 34, 51, 48, 1, 18, 35, 32, 49, 2, 19, 16, 33, 50, 3,
                   4, 21, 38, 55, 52, 5, 22, 39, 36, 53, 6, 23, 20, 37, 54, 7,
                   8, 25, 42, 59, 56, 9, 26, 43, 40, 57, 10, 27, 24, 41, 58, 11,
                   12, 29, 46, 63, 60, 13, 30, 47, 44, 61, 14, 31, 28, 45, 62, 15]

    if not reverse:
        return permutation[position]
    else:
        return permutation.index(position)

# propagate forward, Y2 -> X3 only (omit Zi)
for cell in range(16):
    for pos in range(4):
        temp = shuffle(4 * cell + pos, 0)
        tcell = int(temp // 4)
        tpos = temp % 4
        m.addConstr(knownX3[tcell, tpos] == knownY2[cell, pos])

# propagate backward X26 -> Y26 and X25 -> Y25 (omit Zi)
for cell in range(16):
    for pos in range(4):
        temp = shuffle(4 * cell + pos, 1)
        tcell = int(temp // 4)
        tpos = temp % 4
        m.addConstr(knownX26[cell, pos] == knownY25[tcell, tpos])
        m.addConstr(knownX25[cell, pos] == knownY24[tcell, tpos])


# ------------------------------ count guessed sub_keys and filters ---------------------------------

D = 61.78

filter2 = m.addVars(16, vtype=GRB.INTEGER, name='filter_2')
filter3 = m.addVars(16, vtype=GRB.INTEGER, name='filter_3')
filter24 = m.addVars(16, vtype=GRB.INTEGER, name='filter_24')
filter25 = m.addVars(16, vtype=GRB.INTEGER, name='filter_25')
filter26 = m.addVars(16, vtype=GRB.INTEGER, name='filter_26')


guessed_key = gk_0.sum() + gk_1.sum() + gk_2.sum() + gk_3.sum() + gk_6.sum() + gk_7.sum()

# filter bits of each cell
for c in range(16):
    m.addConstr(filter2[c] == knownY2[c, 0] * (fixY2.sum(c, '*') - fixX2.sum(c, '*')))
    m.addConstr(filter3[c] == knownY3[c, 0] * (fixY3.sum(c, '*') - fixX3.sum(c, '*')))

    m.addConstr(filter24[c] == knownX24[c, 0] * (fixX24.sum(c, '*') - fixY24.sum(c, '*')))
    m.addConstr(filter25[c] == knownX25[c, 0] * (fixX25.sum(c, '*') - fixY25.sum(c, '*')))
    m.addConstr(filter26[c] == knownX26[c, 0] * (fixX26.sum(c, '*') - fixY26.sum(c, '*')))

# ------------------------------ obj function ---------------------------------

rbp = filter2.sum() + filter3.sum()
rfp = filter24.sum() + filter25.sum() + filter26.sum()

rb_star = 44 - rbp
rf_star = 64 - rfp

# ------------------------------ Ti ---------------------------------

m.addConstr(T1 == guessed_key + 2 + D - 2.11)  # 1 p.enc. = 2.11 (6/26) enc.
m.addConstr(T2 == guessed_key + 1 + D + rb_star - 4.7)  # m.a. = -4.7 (1/26) enc.
m.addConstr(T3 == guessed_key + 2 * (D + rb_star + rf_star - 64) - 2.7)  # epsilon = -2.7 enc. (guess and filter) or 1 m.a.

# m.addConstr(T1 == 111.78)
# m.addConstr(T2 == 115.78)
# m.addConstr(T3 == 115.56)

m.addConstr(T >= T1)
m.addConstr(T >= T2)
m.addConstr(T >= T3)
m.addConstr(T >= 108)


m.setObjective(T, GRB.MINIMIZE)

m.write('gift.lp')

m.optimize()

m.write('gift_solve.sol')