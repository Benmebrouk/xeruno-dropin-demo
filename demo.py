#!/usr/bin/env python3
"""
Drop-in OpenAI Replacement Demo

Shows identical code running with OpenAI vs Xeruno.
Only 2 lines changed.
"""

import time
import os
from openai import OpenAI

# ANSI colors for terminal
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def run_openai():
    """Original OpenAI code (UNCHANGED LOGIC)"""
    print(f"\n{BLUE}{BOLD}=== OpenAI (Original) ==={RESET}")

    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print(f"{YELLOW}⚠️  OPENAI_API_KEY not set - skipping OpenAI demo{RESET}")
        print(f"{YELLOW}   Set it to compare side-by-side{RESET}\n")
        return None

    client = OpenAI()

    start = time.time()
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Explain TCP congestion control in 3 sentences"}],
        stream=True
    )

    print(f"{BLUE}Response:{RESET} ", end="", flush=True)
    tokens = 0
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            tokens += 1

    latency = time.time() - start
    cost = tokens * 0.000003  # Approximate GPT-4o-mini cost

    print(f"\n\n{BLUE}Tokens:{RESET} {tokens}")
    print(f"{BLUE}Latency:{RESET} {latency:.2f}s")
    print(f"{BLUE}Cost:{RESET} ${cost:.4f}")
    print(f"{BLUE}Network:{RESET} api.openai.com")

    return {"tokens": tokens, "latency": latency, "cost": cost}

def run_Xeruno():
    """Xeruno - ONLY 2 LINES CHANGED"""
    print(f"\n{GREEN}{BOLD}=== Xeruno (Local) ==={RESET}")

    # ✨ ONLY CHANGE: base_url + api_key
    # This is the only code change needed to swap OpenAI -> Xeruno
    client = OpenAI(
        base_url="http://127.0.0.1:11434/v1",
        api_key="xeruno"
    )

    start = time.time()
    stream = client.chat.completions.create(
        model="llama3",  # Local model
        messages=[{"role": "user", "content": "Explain TCP congestion control in 3 sentences"}],
        stream=True
    )

    print(f"{GREEN}Response:{RESET} ", end="", flush=True)
    tokens = 0
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            tokens += 1

    latency = time.time() - start
    cost = 0.0  # Local = free

    print(f"\n\n{GREEN}Tokens:{RESET} {tokens}")
    print(f"{GREEN}Latency:{RESET} {latency:.2f}s")
    print(f"{GREEN}Cost:{RESET} ${cost:.4f}")
    print(f"{GREEN}Network:{RESET} 127.0.0.1 (LOCAL ONLY)")

    return {"tokens": tokens, "latency": latency, "cost": cost}

def main():
    print(f"\n{BOLD}{'='*60}")
    print(f"  Drop-in OpenAI Replacement Demo")
    print(f"  Change 2 lines. Run local. Cost = $0.")
    print(f"{'='*60}{RESET}\n")

    # Run OpenAI (if API key set)
    openai_stats = run_openai()

    # Run Xeruno
    try:
        local_stats = run_Xeruno()
    except Exception as e:
        print(f"\n{YELLOW}❌ Xeruno not running: {e}{RESET}")
        print(f"{YELLOW}   Run ./run.sh to start it{RESET}\n")
        return

    # Comparison
    if openai_stats and local_stats:
        print(f"\n{BOLD}{'='*60}")
        print(f"  Comparison")
        print(f"{'='*60}{RESET}")
        print(f"Cost savings: {BOLD}${openai_stats['cost']:.4f} → $0.00{RESET}")
        latency_diff = ((local_stats['latency'] - openai_stats['latency']) / openai_stats['latency']) * 100
        if latency_diff < 0:
            print(f"Latency: {BOLD}{abs(latency_diff):.1f}% faster{RESET}")
        else:
            print(f"Latency: {latency_diff:.1f}% slower (local)")
        print(f"Privacy: {BOLD}0 bytes external traffic{RESET}")

    print(f"\n✅ {BOLD}Demo complete!{RESET}\n")

if __name__ == "__main__":
    main()
