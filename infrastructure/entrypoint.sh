#!/bin/bash

# 1. Register with the Security Manager (The SIEM)
echo "🛡️ [SENTINEL] Registering Agent with Manager at $WAZUH_MANAGER_IP..."
/var/ossec/bin/agent-auth -m $WAZUH_MANAGER_IP -A $WAZUH_AGENT_NAME

# 2. Configure the Agent to point to the Manager
sed -i "s/MANAGER_IP/$WAZUH_MANAGER_IP/g" /var/ossec/etc/ossec.conf
sed -i "s/<address>127.0.0.1<\/address>/<address>$WAZUH_MANAGER_IP<\/address>/g" /var/ossec/etc/ossec.conf

# 3. Start the Security Agent in Background
echo "🛡️ [SENTINEL] Starting Wazuh Agent..."
/var/ossec/bin/wazuh-control start

# 4. Start the AI Brain (The Main Event)
echo "🧠 [VERITY BRAIN] Starting AI Logic..."
# We use exec so the python process becomes PID 1 (receives signals)
exec python -m node_brain.fl_client