# from plyer import notification
import time


print("What should I remin you about?")
text= str(input())
print("In how many minutes?")
local_time= float(input())
local_time= local_time*60
time.sleep(local_time)
print(text)

#notification.notify(title="BREAK TIME", message="Time to drink some Water!", timeout=1)
# while True:
#     reminder()
#     time.sleep(10)
