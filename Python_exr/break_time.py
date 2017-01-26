import time
import webbrowser

#program which opens youtube song after a fixed time interval

total_break=3
break_count =0;

print("The program started at "+time.ctime())
while (break_count<total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=YSew_OnDEFE")
    break_count = break_count+1
