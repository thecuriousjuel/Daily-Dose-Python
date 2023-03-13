import time

start_time = time.time()
end_time = time.time()

count = 1

try:
    while True:
        input("Lap")
        current = time.time()
        lap_time = round(current - end_time, 2)
        total_time = round(current - start_time, 2)

        print(f"No.\tLap Time\tTotal Time")
        print(f"{count}\t{lap_time}\t\t{total_time}")

        end_time = time.time()
        count += 1

except KeyboardInterrupt:
    pass



