# 🧩 DS Agent Skills

> A free, open-source library of modular AI skills for Data Science workflows.
> Built for beginners and professionals alike.

Instead of rebuilding your AI agent every time requirements change —
just add a skill. That's the idea.

---

## 👥 Who is this for?

### 🟢 If you're a beginner
You don't need to write code to use these skills.
Just give the skill file to any AI assistant (Claude, ChatGPT, etc.) and describe your data.
The skill tells the AI exactly what to do.

**Your first command:**
```
"Read SKILL.md in skill-data-cleaning, then clean the file in examples/"
```
That's it. The AI takes it from there.

### 🔵 If you're a professional
Each skill comes with production-ready Python scripts you can run directly,
integrate into pipelines, or extend for your own use cases.

```bash
python skill-data-cleaning/scripts/clean.py --input raw.csv --output clean.csv
```

---

## 📁 Skills Library

| Skill | What it does | Beginner | Pro |
|---|---|---|---|
| [`skill-data-cleaning`](./skill-data-cleaning/) | Cleans messy datasets automatically | ✅ | ✅ |
| [`skill-eda`](./skill-eda/) | Exploratory Data Analysis + smart insights | ✅ | ✅ |
| [`skill-ml-pipeline`](./skill-ml-pipeline/) | End-to-end ML pipeline from data to model | ✅ | ✅ |
| [`skill-report-generator`](./skill-report-generator/) | Turns raw results into clear client reports | ✅ | ✅ |

---

## 🗺️ The Full DS Workflow

These skills are designed to work **in sequence**:

```
Raw Data
   │
   ▼
🧹 skill-data-cleaning    →  Clean, structured dataset
   │
   ▼
🔍 skill-eda              →  Insights & patterns
   │
   ▼
🤖 skill-ml-pipeline      →  Trained model + metrics
   │
   ▼
📄 skill-report-generator →  Client-ready report
```

Use one. Use all four. Each works standalone or as part of the chain.

---

## 🚀 Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/ds-agent-skills.git
```

**2. Try it immediately with the sample data**
```bash
python skill-data-cleaning/scripts/clean.py \
  --input skill-data-cleaning/examples/sample_dirty.csv \
  --output cleaned.csv
```

**3. Or give it to your AI agent**
```
"Read skill-data-cleaning/SKILL.md, then clean the file sample_dirty.csv"
```

Your agent reads the skill → knows exactly what to do. ✅

---

## 🧠 How Skills Work

```
📁 skill-data-cleaning/
   ├── SKILL.md          ← Instructions for the agent (and for you)
   ├── scripts/
   │   └── clean.py      ← Executable code
   └── examples/
       └── sample_dirty.csv  ← Test immediately, no setup needed
```

The agent reads `SKILL.md` to understand the task,
then runs the scripts to execute it.

**No retraining. No fine-tuning. Just plug and run.**

---

## 🛣️ Roadmap

### v1.0 — Current ✅
- skill-data-cleaning
- skill-eda
- skill-ml-pipeline
- skill-report-generator

### v1.1 — Coming next
- [ ] skill-time-series (forecasting)
- [ ] skill-nlp-classifier (text classification)
- [ ] skill-dashboard-builder (auto-generate charts)
- [ ] skill-data-validation (schema checks before pipeline)

### v2.0 — Community milestone (when we reach 50 contributors)
- Full workflow orchestrator (agent that chains skills automatically)
- Skill versioning
- Arabic language support for reports

---

## 💡 The Philosophy

> The agent is the conductor.
> The skills are the orchestra.

You don't rebuild the conductor every time you add a new instrument.
You just expand the orchestra.

That's what this library is — an orchestra that keeps growing,
built by a community of data scientists who are tired of starting from scratch.

---

## 🤝 Contributing

Found a workflow you repeat every week?
Turn it into a skill and open a PR.

**You don't need to be an expert.** The best skills are written by people
who know the task well — not necessarily the best coders.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the skill template and guidelines.

---

## 📬 Community

Built as part of the **Agent Skills Community** on Facebook.
A place where builders share skills, ask questions, and grow the library together.

👉 Join us → https://www.facebook.com/groups/1843449089701764/?ref=share&mibextid=NSMWBT

---

## 📄 License

MIT — free to use, modify, and share.

---

*Built with ❤️ for data scientists who are tired of starting from scratch.*
*Beginner-friendly. Production-ready. Community-driven.*
