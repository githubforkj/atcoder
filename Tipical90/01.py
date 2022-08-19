
# import library
import itertools as it

# N個からK個を重複なしの組み合わせを選ぶ
# chose k in N with itertools combinations
def comb(A,K):
    all = it.combinations(A,K)
    comb = []
    for x in all:
        comb.append(list(x))
    return comb
  
# splitting
def split(comb,L,K):
    sp = []
    for i in comb:
        sp.append(i[0])
        if K == 1:
            sp.append(L-i[0])
        else:
            for j in range(K):
                if i[j] >= i[j-1]:
                    sp.append(i[j]-i[j-1])
                last = i[j]
            sp.append(L-last)
    return sp

# reshape array
def chunks(l):
    result = []
    for i in range(0, len(l), K+1):
        result.append(l[i:i + K+1])
    return result


# choose min
def chose_min(sp_list,K):
    min_list = []
    for i in sp_list:
        for j in range(K+1):
            if j == 0:
                min = i[j]
            else:
                if min >= i[j]:
                    min = i[j]
                else:
                    continue
        min_list.append(min)
    return min_list

# choose max
def chose_max(min_list):
    max_len = max(min_list)
    return max_len


# instantiation
def imp(A,L,K,N):
    com = comb(A,K)
    sp = split(com,L,K)
    new_sp = chunks(sp)
    min_list = chose_min(new_sp,K)
    max = chose_max(min_list,K)
    N = N
    return max


print(imp(A,L,K,N))
