# 🤝 Contributing to DS Agent Skills

First — thank you. Every skill you add makes this library more valuable for everyone.

---

## How to add a new skill

### Step 1 — Pick a task worth repeating
A good skill candidate:
- Is something you do more than once a week
- Has clear steps that don't change much
- Produces a consistent output

### Step 2 — Copy the template
```bash
cp -r _template/ skill-your-skill-name/
```

### Step 3 — Fill in SKILL.md

At minimum, your `SKILL.md` must include:

```markdown
---
name: your-skill-name
description: >
  Use this skill when [specific situation].
  Triggers on: [keywords that should activate this skill].
---

# Skill Name

## What it does
[One paragraph — plain language]

## When to use
[Bullet list of trigger situations]

## Steps
[Numbered steps with commands]

## Output
[What the user gets at the end]

## Key Rules
[2-5 rules that prevent common mistakes]
```

### Step 4 — Add a script (optional but encouraged)
If your skill has executable steps, add them to `scripts/`.
Scripts should:
- Accept `--input` and `--output` arguments
- Print clear progress messages
- Always produce a human-readable report

### Step 5 — Add an example
Put a small sample dataset or input file in `examples/`
so anyone can test the skill immediately.

### Step 6 — Open a Pull Request
Title format: `feat: add skill-[name]`
Description: What does this skill do? Why is it useful?

---

## Skill Quality Checklist

Before submitting, make sure:
- [ ] SKILL.md has a clear `description` (this is what triggers the agent)
- [ ] Steps are clear enough for a junior data scientist to follow
- [ ] Output format is defined
- [ ] Key rules are included (at least 2)
- [ ] Script runs without errors on the example file
- [ ] No hardcoded file paths

---

## Not sure where to start?

Check the [Issues](../../issues) tab for skills marked `help wanted`.
Or open a new issue with your idea — we'll help you design it.

---

*Good skills outlive the models that run them.*
