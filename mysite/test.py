def calc_cache_pos(strings, indexes):
    factor = 1
    pos = 0
    for s, i in zip(strings, indexes):
        pos += i * factor
        factor *= len(s)
    return pos

def lcs_back(strings, indexes, cache):
    if -1 in indexes:
        return ""
    match = all(strings[0][indexes[0]] == s[i]
                for s, i in zip(strings, indexes))
    if match:
        new_indexes = [i - 1 for i in indexes]
        result = lcs_back(strings, new_indexes, cache) + strings[0][indexes[0]]
    else:
        substrings = [""] * len(strings)
        for n in range(len(strings)):
            if indexes[n] > 0:
                new_indexes = indexes[:]
                new_indexes[n] -= 1
                cache_pos = calc_cache_pos(strings, new_indexes)
                if cache[cache_pos] is None:
                    substrings[n] = lcs_back(strings, new_indexes, cache)
                else:
                    substrings[n] = cache[cache_pos]
        result = max(substrings, key=len)
    cache[calc_cache_pos(strings, indexes)] = result
    return result

def lcs(strings):
    """
    >>> lcs(['666222054263314443712', '5432127413542377777', '6664664565464057425'])
    '54442'
    >>> lcs(['abacbdab', 'bdcaba', 'cbacaa'])
    'baa'
    """
    if len(strings) == 0:
        return ""
    elif len(strings) == 1:
        return strings[0]
    else:
        cache_size = 1
        for s in strings:
            cache_size *= len(s)
        cache = [None] * cache_size
        indexes = [len(s) - 1 for s in strings]
        return lcs_back(strings, indexes, cache)


# def lcs(S,T,P,R):
#     m = len(S)
#     n = len(T)
#     p = len(P)	
#     r = len(R)		
#     counter = [[0]*(n+1) for x in range(m+1)]
#     longest = 0
#     lcs_set = set()
#     for i in range(m):
#         for j in range(n):
#             if S[i] == T[j]:
#                 c = counter[i][j] + 1
#                 counter[i+1][j+1] = c
#                 if c > longest:
#                     lcs_set = set()
#                     longest = c
#                     lcs_set.add(S[i-c+1:i+1])
#                 elif c == longest:
#                     lcs_set.add(S[i-c+1:i+1])
# 
#     return lcs_set

# # test 1
# ret = lcs('academy', 'abracadabra')
# for s in ret:
#     print(s)
# 
# # test 2
# ret = lcs('ababc', 'abcdaba')
# for s in ret:
#     print(s)
	
#ret = lcs('aaa bbbb cccc dededeed','bbbn dedebt','aa fhgk deed', 'hello word, bbb')
#for s in ret:
#    print(s)

res=lcs(['aaa bbbb cccc dededeed','bbbn dedebt','aa fhgk deed', 'hello word, bbb'])
x=res;
print(x)