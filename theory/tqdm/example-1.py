from tqdm import tqdm
import numpy as np
from time import sleep

loop_obj = tqdm(np.arange(10))

for i in loop_obj:
    loop_obj.set_description(f"Voltage {i}")  # Adds text before progessbar
    # loop_obj.set_postfix_str(f"Next count: {i+1}")  # Adds text after progressbar
    sleep(0.1)