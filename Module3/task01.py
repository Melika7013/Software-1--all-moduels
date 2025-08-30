length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42
if length >= size_limit:
    print("The zander meets the size limit. You can keep it.")
else:
    below_limit = size_limit - length
    print(f"The zander is too small! Release it back into the lake.")
    print(f"It is {below_limit:.1f} cm below the size limit.")
