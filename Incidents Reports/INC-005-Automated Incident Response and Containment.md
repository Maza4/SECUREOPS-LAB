Incident ID: INC-005
Title: Automated Incident Response and Containment Pipeline
Severity: HIGH
Detection Source: Custom Python Log Analyzer (log_analyzer.py)
Affected Asset: Ubuntu Server (192.168.56.102 / vtcsec)
MITRE ATT&CK Mapping: Mitigation of T1110.001 (Brute Force: Password Guessing)

Executive Summary
To reduce the dwell time of active network attacks, a custom Security Orchestration, Automation, and Response (SOAR) pipeline was engineered and deployed. A Python script was utilized to parse raw authentication logs and extract malicious IP addresses via Regular Expressions (Regex). The extracted IP was then dynamically passed to a Bash script to execute host-based firewall containment rules, instantly neutralizing the threat.

Indicators of Compromise (IoCs)
Trigger Event: High frequency of "Failed password" strings in /var/log/auth.log
Extracted Threat Actor IP: 192.168.56.105
Containment Mechanism: UFW (Uncomplicated Firewall)
Enforcement Rule Applied: sudo ufw deny from 192.168.56.105 to any

Attack Timeline
T-0: Continuous SSH brute-force activity is logged on the Ubuntu system.
T+1 min: log_analyzer.py executed, utilizing regex to isolate the attacking IPv4 address from the raw log strings.
T+2 min: Python script successfully extracts 192.168.56.105 and pipes the variable to block_ip.sh.
T+2 min: Bash script executes the UFW command, severing the network connection with the attacker.

Technical Investigation
The technical workflow required writing a Python parser with the `re` module using the pattern `r'Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'`. This ensured accurate identification of the IPv4 address without capturing benign log data. Once extracted, the secondary Bash script (block_ip.sh) validated the input variable to prevent syntax errors and executed the containment command `sudo ufw deny from $TARGET_IP to any`, followed by a firewall reload to enforce the drop rule immediately.

Impact & Root Cause
Impact: The attacker's network connection was successfully severed at the host level, eliminating the immediate brute-force threat with zero manual network intervention required.
Root Cause: The necessity for this automated containment arose from the latency inherent in manual SOC response workflows; this engineered pipeline effectively closes the gap between threat detection and threat remediation.