import statistics as st
s = st.stdev([float(s) for s in input().split()])
print("COMFY" if s <= 1.0 else "NOT COMFY")