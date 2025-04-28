import pandas as pd

table1 = pd.DataFrame({
    "id":[1,2,3,4],
    "name":["riyan","bilal","khan","ashbal"]
})

table2 = pd.DataFrame({
    "id":[3,4,5,6],
    "score":[90,80,70,20]
})

result = pd.merge(table1,table2,on="id",how="cross")

print(result)


# vertical and horizontal concatenation
# selection where projection have


result_concat_col = pd.concat([table1, table2], axis=1)
print(result_concat_col)


