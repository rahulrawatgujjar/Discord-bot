
# import keyboard as kb
# # recorded_keys=kb.record(until="enter")
# recorded_keys=kb.start_recording()


# # recorded_keys=recorded_keys[:-1:2]
# string_1=""
# for element in recorded_keys[:-1]:
#     if "down" in str(element):
#         element=str(element)
#         element=element.replace("KeyboardEvent(","")
#         element=element.replace(" down)","")
#         string_1+=element

# print(string_1)


# # print(recorded_keys)

# # KeyboardEvent(r down)

# import keyboard
# events = keyboard.record()
# print(list(keyboard.get_typed_strings(events)))

# events= keyboard.start_recording()

# events=keyboard.stop_recording()
# print(events)

# import keyboard as kb
# kb.press_and_release("ctrl+backspace,ctrl+backspace")

import os 
path=os.getcwd()

if "example" not in os.listdir(rf"{path}"):
    os.mkdir(rf"{path}\example")

