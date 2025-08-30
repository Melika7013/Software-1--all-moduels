length = float(input("Enter the length of the zander in centimeters: "))
if length >= 42:
    print("The zander meets the size limit. You can keep it.")
else:
    print(f"The zander is too small! Release it back into the lake.")
    print(f"It is {42 - length:.1f} cm below the size limit.")
