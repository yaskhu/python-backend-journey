def Pagination_Logic():
    data = list(range(1, 101))
    page = 3
    limit = 10
    start=(page-1) * limit
    end=start+limit
    res=data[start:end]
    return res
print(Pagination_Logic())