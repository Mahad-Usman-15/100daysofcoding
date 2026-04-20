import time
start_time=time.perf_counter()
for i in range(1,100):
  pass

end_time=time.perf_counter()
elapsed = end_time - start_time
print(elapsed)