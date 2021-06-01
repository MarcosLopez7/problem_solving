def solve(array, queries):
    searched_queries = {}

    start_comp = 0
    end_comp = 0

    for query in queries:
        if query in searched_queries.keys():
            index = searched_queries[query]

        else:
            index = array.index(query)
            searched_queries[query] = index
        start_comp += index + 1
        end_comp += len(array) - index

    return [start_comp, end_comp]


n = int(input())
array = [int(num) for num in input().split()]
queries_num = int(input())
queries = [int(num) for num in input().split()]
results = solve(array, queries)

print(f"{results[0]} {results[1]}")
