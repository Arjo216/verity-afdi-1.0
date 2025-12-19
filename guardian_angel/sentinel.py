import time
import subprocess
import os

def check_security_status():
    """Checks if the Wazuh Agent is running and protecting the node."""
    try:
        # Check if the wazuh-agentd process is alive
        result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        
        if "wazuh-agentd" in output:
            print("🛡️ [SENTINEL] Security Active. Agent is monitoring this node.")
            return True
        else:
            print("⚠️ [SENTINEL] ALERT! Security Agent is DOWN!")
            return False
    except Exception as e:
        print(f"❌ [SENTINEL] Error checking status: {e}")
        return False

if __name__ == "__main__":
    print("👼 Guardian Angel Module Loaded...")
    while True:
        check_security_status()
        time.sleep(10) # Check every 10 seconds