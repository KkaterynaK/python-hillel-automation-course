from datetime import datetime


def analyze_heartbeat(input_file_path="hblog.txt", output_file_path="hb_test.log"):
    target_key = "Key TSTFEED0300|7E3E|0400"
    filtered_events = []

 
    with open(input_file_path, "r", encoding="utf-8") as file:
        for line in file:
            if target_key in line:
                time_index = line.find("Timestamp ")
                if time_index != -1:
                    time_str = line[time_index + 10: time_index + 18]
                    time_obj = datetime.strptime(time_str, "%H:%M:%S")

                    filtered_events.append({
                        "raw_line": line.strip(),
                        "time_str": time_str,
                        "time_obj": time_obj
                    })

  
    with open(output_file_path, "w", encoding="utf-8") as out_file:
        for i in range(len(filtered_events) - 1):
            current_event = filtered_events[i]
            next_event = filtered_events[i + 1]

            delta = (current_event["time_obj"] - next_event["time_obj"]).total_seconds()

            if delta < 0:
                delta += 86400  # обробка переходу через північ

            log_msg = None
            if 31 < delta < 33:
                log_msg = f"WARNING: Heartbeat is {delta}s. Detected at {current_event['time_str']} (Interval between {next_event['time_str']} and {current_event['time_str']})\n"
            elif delta >= 33:
                log_msg = f"ERROR: Heartbeat is {delta}s. Detected at {current_event['time_str']} (Interval between {next_event['time_str']} and {current_event['time_str']})\n"

            if log_msg:
                out_file.write(log_msg)


if __name__ == "__main__":
    analyze_heartbeat()
    print("Аналіз завершено! Файл hb_test.log успішно створено.")
