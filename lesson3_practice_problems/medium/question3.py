### Problem statement

# Alyssa was asked to write an implementation of a rolling buffer. 
# You can add and remove elements from a rolling buffer. However, 
# once the buffer becomes full, any new elements will displace 
# the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements 
# to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# What is the key difference between these implementations?

### Solution:

# add_to_rolling_buffer1 uses `append` method to add the new 
#    element. This is a mutation of the `buffer` object
# add_to_rolling_buffer2 creates a new list by concatenating 
#    new element to `buffer`. This is a reassignment.