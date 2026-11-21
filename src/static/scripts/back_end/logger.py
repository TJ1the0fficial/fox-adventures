import math
from datetime import datetime

start_time : datetime = datetime.now()
end_time : datetime

def calc_runtime_min_sec() -> tuple:
    end_time = datetime.now()
    # difference, but converted to min,sec
    difference = end_time.second - start_time.second

    return (
        # min
        math.floor(difference / 60),
        # sec (ex : 16,25 - 16 == 0.25 -> 0.25*100 == 25)
        difference
    )

def log(message : str):
    runtime = calc_runtime_min_sec()
    print(f"[{runtime[0]}:{runtime[1]}] : {message}")