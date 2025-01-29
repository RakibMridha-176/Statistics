import statistics as st

data = list(map(float, input("Enter data separated by spaces: ").split()))

print(st.mean(data))
print(st.median(data))
print(st.mode(data))

