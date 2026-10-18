# Security policy

design-styles is a knowledge-and-instructions package for AI coding agents. It contains no executable service, no network calls and no dependencies; the only executable files are `tests/validate_skill.py` and `tools/set-activation.py`, both Python standard library only, both operating solely inside the skill directory.

## Reporting

If you find a security-relevant issue, report it privately via GitHub Security Advisories for this repository (preferred) or by opening an issue that says only "security report, requesting private contact" without details. Relevant classes of issue include:

- Content in the skill that could induce an agent to modify configuration outside its own directory, escalate activation beyond the documented opt-in boundary, or make unauthorised network requests.
- A validator or tool script change that executes outside the skill directory or follows attacker-controlled paths.
- Prompt-injection vectors embedded in reference or example files.

## What is out of scope

- Design opinions, historical disputes and style disagreements (open a normal issue).
- Vulnerabilities in the host agent or platform (report to that vendor).

Reports are acknowledged on a best-effort basis; this is a community-maintained project without a guaranteed response time.
