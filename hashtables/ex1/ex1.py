def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = []
    res = []
    if length < 2:
        return None

    for i in range(length):
        diff = limit - weights[i]
        print(diff)
        if diff in cache:
            res.append(i)
            res.append(cache.index(diff))
            return res
        else:
            cache.append(weights[i])
    # print(cache)
