#!/bin/bash
# Quick start script for Xeruno drop-in demo

set -e

echo "🚀 Starting Xeruno..."


# 1. Check prerequisites
for cmd in curl python3 ollama; do
    if ! command -v $cmd &> /dev/null; then
        echo "❌ Error: '$cmd' is required but not installed."
        exit 1
    fi
done

# 2. Install Python dependencies
if [ -f "requirements.txt" ]; then
    echo "📦 Checking Python dependencies..."
    pip install -r requirements.txt > /dev/null 2>&1 || pip3 install -r requirements.txt > /dev/null 2>&1
fi

# 3. Check/Start Ollama
if ! curl -s http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
    echo "⚙️  Ollama not running. Starting background service..."
    ollama serve > /dev/null 2>&1 &
    sleep 5
fi

# 4. Pull model if missing
if ! curl -s http://127.0.0.1:11434/api/tags | grep -q "llama3"; then
    echo "📥 Pulling llama3 model (this may take a while)..."
    ollama pull llama3
fi

echo "✅ Xeruno (Ollama) is ready on http://127.0.0.1:11434"
echo ""
echo "🎯 Ready! Run: python demo.py"
