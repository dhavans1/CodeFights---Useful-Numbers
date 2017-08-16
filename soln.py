def usefulNumbers(k):

#Approach 1
    return pow(2, list(bin(k)[2:]).count('0'))

#Approach 2 : Time consuming
#     count = 0
#     if k%2 == 1:
#         for i in range(k):
#             if i%2 == 1:
#                 continue
#             if k+i == k|i:
#                 count += 1
#     else:
#         for i in range(k):
#             if k+i == k|i:
#                 count += 1
                
#     return count

#Approach 3 : Time consuming
#     count = 0
#     res = []
#     for i in range(k):
#         if k+i == k|i:
#             count += 1
#             res.append(i)
#             
#     print(k, bin(k)[2:],"\t", len(res), res)
# #     print(res)
#     return count

