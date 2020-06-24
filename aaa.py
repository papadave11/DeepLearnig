from sklearn.preprocessing import MinMaxScaler
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = MinMaxScaler()
print(scaler.fit(data))


MinMaxScaler()
print(scaler.data_max_)
"""
[ 1. 18.]
"""

print(scaler.transform(data))

"""
[[0.   0.  ]
 [0.25 0.25]
 [0.5  0.5 ]
 [1.   1.  ]]

 """
print(scaler.transform([[2, 2]]))

"""
[[1.5 0. ]]

"""