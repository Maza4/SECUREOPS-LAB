Incident ID: INC-004
Title: Threat Investigation and Log Analysis via SIEM Querying
Severity: MEDIUM
Detection Source: Wazuh SIEM Querying & Local Authentication Logs
Affected Asset: Ubuntu Server (192.168.56.102 / vtcsec)
MITRE ATT&CK Mapping: T1110.001 (Brute Force: Password Guessing)

Executive Summary
Following SIEM alerts indicating a high volume of SSH authentication failures, an in-depth log investigation was conducted. Utilizing query languages within the Wazuh dashboard (Lucene/Elastic syntax) and command-line log parsing on the local endpoint, the investigation successfully isolated the threat actor's IP address, quantified the scope of the attack, and verified that no unauthorized access was achieved.

Indicators of Compromise (IoCs)
Target Service: SSH (Port 22)
Attacker IP Address: 192.168.56.105 (Kali Linux VM)
Log Artifact: /var/log/auth.log
Query Pattern: rule.groups: "syslog, sshd, authentication_failed"

Attack Timeline
T-0: Attacker initiated an automated SSH brute-force script against the Ubuntu endpoint.
T+1 min: Wazuh SIEM aggregated the incoming authentication failures.
T+5 min: SOC Analyst executed SIEM query (rule.id: 5712 OR rule.id: 5710) to identify the threshold breach.
T+10 min: SOC Analyst validated the findings directly on the endpoint using Linux command-line parsing.

Technical Investigation
The investigation began in the SIEM by grouping alerts by source IP using the query `rule.groups: "syslog, sshd, authentication_failed" | top srcip`. This pinpointed the origin as 192.168.56.105. To validate the SIEM telemetry, a local endpoint investigation was conducted using the command `grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr`. This returned exactly 54 failed attempts from the attacker's IP. A final SIEM query (`rule.id: 5715`) confirmed zero successful login events during the timeframe.

Impact & Root Cause
Impact: Increased authentication traffic and log generation. No successful breach occurred, maintaining the integrity of the endpoint.
Root Cause: Unrestricted external SSH access to the endpoint allowed the attacker to interact with the authentication daemon continuously, prompting the need for automated firewall containment.
