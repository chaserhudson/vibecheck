# VibeCheck ✨

A linter for good vibes only. Because code quality is not just about logic, it's about the *feeling*.

## What is VibeCheck?

VibeCheck is an ironic, opinionated linter that analyzes your code for its vibrational frequency. In a world of "vibe-driven development," this tool ensures your codebase is aligned with the cosmic energies of success.

Forget about traditional linters that check for syntax errors and code style. VibeCheck analyzes the *real* metrics of quality:

- **Keyword Vibes:** Scans for "low-vibe" words (`hack`, `fixme`, `crap`) and encourages "high-vibe" alternatives (`magic`, `harmony`, `zen`).
- **Astrological Alignments:** Fails your build if Mercury is in retrograde, protecting your deployments from cosmic interference.
- **Lunar Cycles:** Checks the current phase of the moon (because some features should only be built during a waxing crescent).
- **Emoji Sentiment:** Analyzes the emotional content of your comments. Too many `😡` and `🔥` emojis will fail the vibe check.
- **Structural Dissonance:** Uses AST (Abstract Syntax Tree) analysis to detect "low-vibe" code patterns like deeply nested loops and conditionals.
- **Temporal Vibrations:** Judges your code based on the time of day it was committed.

## Installation

```bash
# Clone the repository
git clone https://github.com/chasehudson/vibecheck.git # Replace with your repo URL
cd vibecheck

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install VibeCheck in editable mode
pip install -e .
```

## Usage

Once installed, you can run VibeCheck on any file from your terminal:

```bash
vibecheck /path/to/your/code.py
```

### Bypassing the Cosmos

Sometimes, a deadline is a deadline, regardless of the planetary alignments. VibeCheck provides flags to bypass the more esoteric checks:

- `--no-retrograde-check`: Skip the Mercury in retrograde check.
- `--no-moon-check`: Skip the moon phase check.
- `--no-time-check`: Skip the commit time check.

Example:

```bash
vibecheck /path/to/your/code.py --no-retrograde-check
```

## Disclaimer

VibeCheck is a satirical tool created for entertainment and educational purposes. While it is a functional linter, its checks are intentionally absurd. Please do not use it for serious code quality analysis.

That said, if your build is failing, you might want to consider if your code is truly vibing. 🧘