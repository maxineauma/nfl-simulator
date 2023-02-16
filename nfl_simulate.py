import nfl_generate
import time

for x in range(18):
    print("Simulating week " + str(x+1) + "...")
    nfl_generate.simulate_week(x+1)
    time.sleep(2)

for e, f in nfl_generate.ELO.items():
    print(e, f)