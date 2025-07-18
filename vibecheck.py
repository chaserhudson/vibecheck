
import argparse
import sys
import requests
from datetime import datetime
import ast

# --- Vibe Definitions ---

LOW_VIBE_KEYWORDS = {
    "legacy", "temp", "workaround", "hack", "fixme", "todo", "bug", "issue",
    "problem", "error", "fail", "broken", "dirty", "kludge", "crap", "wtf"
}
HIGH_VIBE_KEYWORDS = {
    "magic", "harmony", "zen", "signal", "flow", "create", "elegant", "clean",
    "beautiful", "awesome", "love", "solution", "wisdom", "shine"
}

GOOD_VIBE_EMOJIS = {"✨", "🚀", "🧘", "💖", "🎉", "🌟", "🌈", "😂", "🙏"}
BAD_VIBE_EMOJIS = {"😡", "🔥", "😭", "🐛", "🚨", "💀", "💩", "🤯", "🤬"}


# --- Vibe Check Functions ---

def check_mercury_retrograde():
    """Astrological Vibe Check: Fails if Mercury is in retrograde."""
    print("Checking planetary alignments...")
    try:
        response = requests.get("https://mercuryretrogradeapi.com")
        response.raise_for_status()
        if response.json().get("is_retrograde", False):
            print("🚨 VIBE CHECK FAILED! 🚨 Mercury is in retrograde. Cosmic energies are unfavorable.")
            return False
        print("Planetary alignments are favorable.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not connect to astrological API: {e}", file=sys.stderr)
        return True # Assume good vibes if we can't connect

def get_moon_phase():
    """Moon Phase Check: Determines the current moon phase."""
    print("Checking lunar cycles...")
    try:
        # Using the Farmsense API for moon phases.
        response = requests.get("https://api.farmsense.net/v1/moonphases/")
        response.raise_for_status()
        # The API returns a list, we take the first element for the current phase.
        phase = response.json()[0].get("Phase", "Unknown")
        print(f"The moon is currently in the '{phase}' phase.")
        # For now, this is informational. We can add build rules later.
        return True
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not connect to lunar API: {e}", file=sys.stderr)
        return True

def check_commit_time():
    """Commit Time Check: Judges code based on when it was 'committed'."""
    print("Checking temporal vibrations...")
    hour = datetime.now().hour
    if 2 <= hour < 6:
        print("✨ Peak Productivity Hours (2 AM - 6 AM). Code is likely divinely inspired.")
    elif 12 <= hour <= 13:
        print("🍔 Lunchtime Commit. Did you drop crumbs in the keyboard? Proceed with caution.")
    elif 22 <= hour:
        print("🌙 Late Night Coding. True dedication or caffeine-fueled chaos? Only time will tell.")
    return True

def check_keyword_vibes(content):
    """Keyword Vibe Check: Scans for low and high vibe keywords."""
    print("Scanning for keyword vibrations...")
    content_lower = content.lower()
    low_vibe_found = {word for word in LOW_VIBE_KEYWORDS if word in content_lower}
    if low_vibe_found:
        print(f"🚨 Low-vibe alert! Found keywords: {', '.join(low_vibe_found)}")
        return False

    high_vibe_found = {word for word in HIGH_VIBE_KEYWORDS if word in content_lower}
    if high_vibe_found:
        print(f"✨ High-vibe keywords detected: {', '.join(high_vibe_found)}. The vibes are immaculate.")
    return True

def check_emoji_vibes(content):
    """Emoji Sentiment Analysis: Checks for good and bad vibe emojis."""
    print("Analyzing emoji sentiment...")
    bad_emojis = {emoji for emoji in BAD_VIBE_EMOJIS if emoji in content}
    if bad_emojis:
        print(f"🚨 Bad emoji vibes detected: {' '.join(bad_emojis)}. Please express yourself more constructively.")
        return False

    good_emojis = {emoji for emoji in GOOD_VIBE_EMOJIS if emoji in content}
    if good_emojis:
        print(f"💖 Good emoji vibes found: {' '.join(good_emojis)}. Your code communicates joy!")
    return True

def check_ast_vibes(content):
    """AST Vibe Check: Analyzes code structure for 'low-vibe' patterns."""
    print("Analyzing abstract syntax tree for structural dissonance...")
    try:
        tree = ast.parse(content)
        errors_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and isinstance(node.body[0], ast.If):
                 print("🚨 Structural dissonance: Deeply nested 'if' statements detected. This suggests indecisiveness.")
                 errors_found = True
            if isinstance(node, ast.For) and isinstance(node.body[0], ast.For):
                 print("🚨 Structural dissonance: Deeply nested 'for' loops. The code is spinning in circles.")
                 errors_found = True
        if not errors_found:
            print("Structural vibes are harmonious.")
        return not errors_found
    except SyntaxError as e:
        print(f"Warning: Could not parse Python file due to syntax error: {e}", file=sys.stderr)
        return True # Don't fail the build for a syntax error, that's what real linters do.


# --- Main Controller ---

def run_all_checks(file_path, args):
    """Runs all the selected vibe checks."""
    print(f"--- Starting VibeCheck for {file_path} ---")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"An error occurred while reading the file: {e}", file=sys.stderr)
        return False

    # List of all checks to run
    all_passed = True
    checks_to_run = []

    if not args.no_retrograde_check:
        checks_to_run.append(check_mercury_retrograde)
    if not args.no_moon_check:
        checks_to_run.append(get_moon_phase)
    if not args.no_time_check:
        checks_to_run.append(check_commit_time)
    
    # File content checks
    checks_to_run.append(lambda: check_keyword_vibes(content))
    checks_to_run.append(lambda: check_emoji_vibes(content))
    
    # AST check for Python files
    if file_path.endswith('.py'):
        checks_to_run.append(lambda: check_ast_vibes(content))

    # Execute all checks and collect results
    results = [check() for check in checks_to_run]
    all_passed = all(results)

    print("-" * 20)

    if all_passed:
        print("\n✅ VibeCheck Complete: All vibes are aligned. Your code is a beacon of positive energy. 🧘")
    else:
        print("\n❌ VibeCheck Failed: Please address the low-vibe issues and try again.")

    return all_passed

def main():
    """Main function to run the vibe check."""
    parser = argparse.ArgumentParser(
        description="VibeCheck: A linter for good vibes only.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("file", help="The file to check the vibes of.")
    
    # Add flags to disable specific checks
    parser.add_argument("--no-retrograde-check", action="store_true", help="Skip the Mercury retrograde check.")
    parser.add_argument("--no-moon-check", action="store_true", help="Skip the moon phase check.")
    parser.add_argument("--no-time-check", action="store_true", help="Skip the commit time check.")

    args = parser.parse_args()

    if not run_all_checks(args.file, args):
        sys.exit(1)

if __name__ == "__main__":
    main()
