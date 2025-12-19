#!/bin/bash
echo "🚀 INITIATING COORDINATED FLEET ATTACK..."
echo "-----------------------------------------"

# Attack Node Alpha (The Sentry)
echo "🔥 Hitting Node Alpha (ID 002)..."
docker exec node_beta logger -p auth.error "Invalid user hacker from 192.168.1.100"
docker exec node_beta logger -p auth.error "Failed password for root from 192.168.1.100"

# Attack Node Beta (The Clone)
echo "🔥 Hitting Node Beta (ID 003)..."
docker exec zombie_node logger -p auth.error "Invalid user hacker from 192.168.1.200"
docker exec zombie_node logger -p auth.error "Failed password for root from 192.168.1.200"

echo "✅ ATTACK COMPLETE. Check Dashboard 'Security Events' now!"
