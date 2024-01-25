import counter_package

count_text = "This is is is is is is is is is a a a a sample text text text text text This."
result = counter_package.text_counters(count_text)
print(result)  # output Counter({'This': 1, 'is': 1, 'a': 1, 'sample': 1, 'text.': 1})


counter_sum = counter_package.sum_counters([result, result])
print(counter_sum)  # Counter({'This': 2, 'is': 2, 'a': 2, 'sample': 2, 'text.': 2})

counter_package.plot_counter(counter_sum)  # output a graph