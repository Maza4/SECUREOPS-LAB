log_file = "/var/log/auth.log"
failed_logins = {}

print("Analyzing logs for SSH brute-force attempts...\n")

try:
    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()

                if "from" in parts:
                    ip = parts[parts.index("from") + 1]

                    if ip in failed_logins:
                        failed_logins[ip] += 1
                    else:
                        failed_logins[ip] = 1

    print("Suspicious IP Addresses Identified:\n")

    for ip, count in failed_logins.items():
        if count > 5:
            print("[CRITICAL] {} generated {} failed attempts.".format(ip, count))
        else:
            print("[WARNING] {} generated {} failed attempts.".format(ip, count))

except PermissionError:
    print("Error: Read permission denied. Run with sudo.")
except FileNotFoundError:
    print("Error: Could not locate {}".format(log_file))