# --------------------------------
# --------------------------------

heroes_stats = read.csv(characters_stats.csv)
heroes_info  = read.csv(marvel_characters_info.csv)
heroes_info$ID = NULL

df = merge(heroes_info, heroes_stats, by = c(Name, Alignment))
write.csv(df, file = heroes_dataset.csv, row.names = FALSE)

# --------------------------------
# Test case 01
# --------------------------------

set.seed(42)
ids1 = sample(x = nrow(df))
df1 = cbind(ids1, df)
colnames(df1)[1] = key
write.table(df1, file = input01.txt, row.names = FALSE, sep = |)
write.table(df1[order(df1$key),], file = output1.txt, row.names = FALSE, sep = |)

# --------------------------------
# Test case 02
# --------------------------------

set.seed(66)
ids2 = sample(x = nrow(df))
df2 = cbind(ids2, df)
colnames(df2)[1] = key
write.table(df2, file = input02.txt, row.names = FALSE, sep = |)
write.table(df2[order(df2$key),], file = output2.txt, row.names = FALSE, sep = |)

# --------------------------------
# Test case 03
# --------------------------------

set.seed(1)
ids3 = sample(x = nrow(df))
df3 = cbind(ids3, df)
colnames(df3)[1] = key
write.table(df3, file = input03.txt, row.names = FALSE, sep = |)
write.table(df3[order(df3$key),], file = output3.txt, row.names = FALSE, sep = |)

# --------------------------------
# Test case 04
# --------------------------------

set.seed(2)
ids4 = sample(x = nrow(df))
df4 = cbind(ids4, df)
colnames(df4)[1] = key
write.table(df4, file = input04.txt, row.names = FALSE, sep = |)
write.table(df4[order(df4$key),], file = output4.txt, row.names = FALSE, sep = |)

# --------------------------------
# Test case 05
# --------------------------------

set.seed(100)
ids5 = sample(x = nrow(df))
df5 = cbind(ids5, df)
colnames(df5)[1] = key
write.table(df5, file = input05.txt, row.names = FALSE, sep = |)
write.table(df5[order(df5$key),], file = output5.txt, row.names = FALSE, sep = |)

# --------------------------------
# --------------------------------
