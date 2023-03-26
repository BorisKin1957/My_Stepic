def func_apply(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result