small = None
print("Before", None)
for value in [9,41,12,3,74,15]:
    if small is None:
        small = value
    elif value>small:
        small=value
    print(small,value)
print("After",small)

# #Alternatively:


# #small_peepee= float("inf")
# print("Before",small_peepee)
# for minecraft in [9,41,12,3,74,15]:
#     if minecraft <small_peepee:
#         small_peepee=minecraft
#     print(small_peepee,minecraft)
# print("After",small_peepee)
