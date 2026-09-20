Future recommendation per labs

INC 001

Remediation & Recommendations
Enforce Key-Based Authentication: Disable password authentication in /etc/ssh/sshd_config by setting PasswordAuthentication no.

Deploy Active Response: Configure Wazuh Execd to automatically execute firewall-drop scripts upon detection of Rule 5712.

Implement Rate Limiting: Deploy Fail2ban or UFW connection rate limits on port 22.



INC 002

Remediation & Recommendations
Configure Local Firewall: Restrict open network ports on vtcsec using ufw default deny incoming.

Signature Updates: Automate suricata-update via cron jobs to ensure rulesets remain current against new NSE scripts.

Active Response Integration: Create custom Wazuh XML rules to automatically block scanner IPs showing elevated event frequencies.



INC 003

Remediation & Recommendations
Enforce Least Privilege: Modify file permissions using chmod 640 and restrict ownership using chown to ensure only the root or specific service accounts can modify the file.

Apply Immutable Flags: For highly sensitive configuration files that should never change, apply the Linux immutable attribute (chattr +i).

Audit syscheck Scope: Review the /var/ossec/etc/ossec.conf file to ensure all critical system directories (e.g., /etc, /bin, /sbin) are included in the real-time FIM baseline.