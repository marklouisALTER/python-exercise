#### How To find dubplicate values ? 

# The .dubplicated() method 
- subset : List of column names to check for duplicate values
- keep : Whenever to keep <b>first</b>('firstname'), <b>last</b>('lastname'), or <b>all</b>('false') dublicate values;

for example 
```bash
    column_names = ['firstname', 'lastname', 'address']
    duplicates = height_weight.duplicated(subset = column_names, keep = all);

    # The output of dubplicate0 can sort by firstname or other column name
    height_weight[duplicates].sort_values(by = 'firstname');
```

# .drop_dubplicates()
 - inplace = Drop the duplicates directly from the rows inside DataFrame without creating new values <b>True</b>

```bash 
    height_weight.drop_dubplicates(inplace = True);
```