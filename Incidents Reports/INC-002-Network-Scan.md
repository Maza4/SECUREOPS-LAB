Incident ID: INC-003



Title: Unauthorized Modification of Sensitive Configuration File



Severity: HIGH



Detection Source: Wazuh File Integrity Monitoring (FIM / Syscheck)



Affected Asset: Ubuntu Server (192.168.56.102 / vtcsec)



MITRE ATT\&CK Mapping: T1565.001 (Data Manipulation: Stored Data Manipulation)



1\. Executive Summary

Real-time File Integrity Monitoring (FIM) detected an unauthorized modification to a sensitive configuration file (/opt/secureops\_fim/credentials.txt) on host 192.168.56.102. The Wazuh agent immediately flagged the modification, capturing the cryptographic hash discrepancy and forwarding the alert to the SIEM for investigation.



2\. Indicators of Compromise (IoCs)

Target File: /opt/secureops\_fim/credentials.txt



Action Detected: File content modified (appended data)



Pre-modification Hash (SHA256): d4e4fae0c1163684b083a598a5a8f274b617e5fe32ae85aa867990550503f8a2



Post-modification Hash (SHA256): 072114449acb3e30d1367d9d0ba62cc3431f29218329009a00cb088226b84fdc



3\. Attack Timeline

T-0: Administrator provisioned /opt/secureops\_fim and Wazuh established the baseline SHA-256 hash.



T+1 min: Unauthorized process appended admin\_user=hacker to the target file.



T+1 min: OS kernel inotify alerted the Wazuh syscheck daemon (Real-time mode active).



T+1 min: FIM module recalculated the hash, detected the mismatch, and generated a Level 7 alert in the SIEM.



4\. Technical Investigation

Analysis of the syscheck event confirmed that the file size and checksum were altered. The alert explicitly tracked the sha256\_before and sha256\_after states, proving the file contents were manipulated rather than merely having its metadata or timestamps touched. The real-time flag ensured zero dwell time between the modification and the detection.



5\. Impact \& Root Cause

Impact: A sensitive file was tampered with, simulating unauthorized credential persistence.



Root Cause: The directory and file possessed overly permissive write permissions, allowing unauthorized user contexts to append data to the file.

