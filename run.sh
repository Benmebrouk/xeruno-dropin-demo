#!/bin/bash
# Quick start script for AgentAgentique drop-in demo

set -e

echo "🚀 Starting AgentAgentique..."

# Check if Ollama is running
if ! curl -s http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
    echo "❌ Ollama not running. Starting..."
    ollama serve > /dev/null 2>&1 &
    sleep 5
fi

# Pull required model if not present
if ! ollama list | grep -q "llama3"; then
    echo "📥 Pulling llama3 model..."
    ollama pull llama3
fi

# Start AgentAgentique API
if ! curl -s http://127.0.0.1:3000/health > /dev/null 2>&1; then
    echo "🔧 Starting AgentAgentique API..."
    cd ..
    cargo run -p agent-api --release > /tmp/agent-api.log 2>&1 &

    # Wait for API to be ready
    echo "⏳ Waiting for API..."
    for i in {1..30}; do
        if curl -s http://127.0.0.1:3000/health > /dev/null 2>&1; then
            echo "✅ AgentAgentique ready!"
            break
        fi
        sleep 1
    done
fi

echo ""
echo "🎯 Ready! Run: python demo.py"
