# %%
num1 = [x if x % 2 == 0 else x+100 for x in range(50)]
print(num1)

# %% 
num = [[x for x in range(50) if x % 2 == 0], [x for x in range(50) if not x % 2 == 0]]
print(num)