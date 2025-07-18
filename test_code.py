
# This is a legacy script with a lot of problems. 😡
import os

# FIXME: This is a temporary hack to get things working.
def bad_function(data):
    # This is a terrible, horrible, no good, very bad function.
    # It's also a great example of a low-vibe code.
    if data:
        if isinstance(data, list):
            for item in data:
                # This is a classic WTF
                print(f"Processing {item} in a very convoluted way.")

# Let's call it with some crap data
bad_function([1, 2, 3])
