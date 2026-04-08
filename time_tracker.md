# TIME TRACKER PROPOSITION 1

```
writing clean logic
structuring backend
understanding FastAPI patterns
building your time tracker
```

```
first project: TIME TRACKER
second project: something with TEXT (context: future task is AI-transription of voice meetings into text - first, I want to master fullstack with text before AI)
```

That’s a strong progression.

## Why this sequence works

**1. Time Tracker** gives you the full-stack basics:

- CRUD
- forms
- validation
- filtering
- auth
- database design
- charts/tables
- deployments

**2. Text project** builds on the same stack, but adds:

- larger text inputs
- search
- tagging
- summaries
- text processing workflows
- better UX for content-heavy apps

So the second project is a smart bridge toward your later **AI meeting transcription** goal.

---

## Recommended project path

| Project                  | Goal                                     | What you learn                                            |
| ------------------------ | ---------------------------------------- | --------------------------------------------------------- |
| Time Tracker             | Master full-stack fundamentals           | CRUD, auth, DB, dashboards, filtering                     |
| Text App                 | Master text-heavy product design         | search, notes/docs, text workflows, organization          |
| Later: AI Transcript App | Add ML/AI on top of solid product skills | upload, transcription pipeline, summarization, extraction |

---

## Project 1: Time Tracker

### Best version

Build a **personal time tracker for deep work and study/work sessions**.

### Core features

- register/login
- create task/project/category
- start session
- stop session
- manual time entry
- edit/delete sessions
- daily/weekly/monthly reports
- total time by project/category
- notes for each session

### Good extra features

- timer currently running
- tags
- streaks
- productivity score
- export CSV
- dark mode
- session goals

### Why it’s a good first project

It teaches almost everything a junior full-stack role wants:

- backend endpoints
- database relations
- frontend forms and state
- charts
- date/time handling
- validation

---

## Project 2: Text project

For your context, the best second app is not “just notes.”
It should train you to handle **text as the core product object**.

## Best choice:

### **Meeting Notes / Transcript Workspace**

This is the cleanest bridge to future AI transcription.

Before AI, users can:

- create meeting entries
- paste raw text notes/transcripts
- edit and save text
- organize by meeting/project/client
- search by keyword
- tag entries
- mark action items manually
- create summaries manually
- track speaker notes or sections

Later, AI can plug into the same app.

---

## Strong version of Project 2

### Core entities

- Workspace
- Meeting
- Transcript
- Summary
- Action Item
- Tag

### Core features

- create meeting
- paste transcript text
- save/edit transcript
- rich or plain text notes
- keyword search
- filter by tag/date/project
- summary field
- action items list
- archive meetings

### Very useful extras

- highlight important passages
- pin important meetings
- full-text search
- markdown support
- text statistics:
  - word count
  - reading time
  - most common words

- compare original transcript vs cleaned version

---

## Why this is better than a generic text app

Because it prepares you for your future AI system architecture.

Later, you can add:

- audio upload
- transcription engine
- speaker diarization
- automatic summary
- action item extraction
- topic detection
- semantic search

So you are not building throwaway projects.
You are building **steps in one direction**.

---

## Best stack for your goal

Since you said **FastAPI + Streamlit**:

| Layer       | Recommendation                |
| ----------- | ----------------------------- |
| Backend API | FastAPI                       |
| Database    | PostgreSQL                    |
| ORM         | SQLAlchemy or SQLModel        |
| Validation  | Pydantic                      |
| Frontend    | Streamlit for MVP             |
| Auth        | simple JWT/session-based auth |
| Migrations  | Alembic                       |

### Important note

For learning full-stack product skills, **Streamlit is good for MVPs**, but it is not the strongest choice for a polished job-style frontend.

A practical path is:

- first ship MVPs in Streamlit
- later rebuild one frontend in React/Next

But for now, FastAPI + Streamlit is enough to learn backend and product flow fast.

---

## Suggested scope

### Project 1 — Time Tracker

Keep it tight:

- auth
- projects
- sessions
- reports
- charts

### Project 2 — Transcript Workspace

Keep it tight:

- meetings
- pasted text
- summaries
- search
- action items

Do not start with AI yet.

---

## What each project proves

### Time Tracker proves

- you can build a full CRUD business app
- you understand user workflows
- you can handle dates, filters, and analytics

### Text app proves

- you can build content-centric systems
- you can model more complex data
- you can prepare an architecture for future AI features

---

## Best naming direction

### Project 1

- FocusLedger
- TrackFlow
- SessionLog
- TimeScope

### Project 2

- MeetingCanvas
- TextWorkspace
- TranscriptDesk
- NoteFlow
- BriefForge

---

## My recommendation

Build:

### 1. **Time Tracker**

A serious personal productivity tracker with reports.

### 2. **Meeting Transcript Workspace**

A text-first app where users paste, organize, search, summarize, and extract tasks from meeting text.

That second one is the best stepping stone toward AI transcription.

If you want, I can turn these two into a **feature roadmap with DB schema, API routes, and MVP order**.

# REVISIT

It’s a **good sprint plan**, but I’d adjust 4 things.

**What’s strong**

- The **Time Tracker** is a smart choice. It forces you to model relationships, state, API routes, and a simple UI.
- Splitting the week into **code + technical reading + lighter evening reading** is sensible.
- The focus on **pytest** and **README/docs** is exactly right for a first job.

**What I’d change**

1. **Don’t force OAuth2 into this week unless your job needs auth immediately.**
   FastAPI has solid auth docs, but auth can eat a lot of time fast. For a 7-day pre-job sprint, a cleaner win is: CRUD + timer start/stop + summary + tests + simple Streamlit frontend. Add auth later unless you already know the company stack needs it. ([FastAPI][1])

2. **Docker on Day 7 is optional, not mandatory.**
   A clean `README`, working local setup, and tests are more valuable than squeezing in Docker if time is tight. If you finish early, then add Docker.

3. **Use FastAPI docs first, books second, for framework-specific topics.**
   For dependencies, DB session handling, testing patterns, and app lifecycle, the official docs are the fastest path. FastAPI’s docs cover SQL databases, testing DBs, dependency cleanup with `yield`, and lifespan handling directly. ([FastAPI][2])

4. **I would not blindly insist on AsyncSession for this sprint.**
   Async DB access is common, but it also adds complexity. SQLAlchemy’s docs emphasize that `AsyncSession` is still a mutable, stateful transaction object and should not be shared across concurrent tasks, so you need to understand the rules well. FastAPI’s own docs still support multiple approaches and do not force one stack. For a one-week prep project, **sync SQLAlchemy/SQLModel is fine** if it helps you ship faster; choose async only if your actual job codebase uses it. ([SQLAlchemy][3])

## My tighter version of the sprint

### Days 1–2

Build:

- models: `User`, `Task`, `TimeEntry`
- schemas
- SQLite first

Read:

- your reference book for `datetime`, classes
- a bit of _Pragmatic Programmer_

### Days 3–4

Build:

- `POST /tasks`
- `POST /timer/start`
- `POST /timer/stop`
- `GET /summary/today`

Read:

- FastAPI docs on path/query/body/dependencies
- _Clean Code_ on naming/functions

### Day 5

Build:

- 3–5 pytest tests
- invalid stop
- cannot start twice
- summary returns expected total

Read:

- pytest basics
- FastAPI testing docs

### Day 6

Build:

- Streamlit page:
  - list tasks
  - start timer
  - stop timer
  - show today’s total

Read:

- Streamlit docs or the practical FastAPI/Streamlit book section

### Day 7

Polish:

- README
- screenshots
- sample `.env`
- project structure cleanup
- optional Docker only if everything else works

## Book order I’d keep

1. _Clean Code_
2. _Python Testing with pytest_
3. _The Pragmatic Programmer_ in parallel
4. Your FastAPI/Streamlit practical book as a build guide
5. DDIA later, not now

## Bottom line

Use that plan, but:

- **drop OAuth2 unless necessary**
- **don’t force async DB just because it sounds modern**
- **prioritize a finished, tested, documented app over extra tech**

And yes, a simple Git workflow matters a lot:

- `main`
- small commits
- push daily
- one clean README at the end

A very simple branch/commit plan for this 7-day sprint would help.

[1]: https://fastapi.tiangolo.com/?utm_source=chatgpt.com "FastAPI"
[2]: https://fastapi.tiangolo.com/tutorial/sql-databases/?utm_source=chatgpt.com "SQL (Relational) Databases"
[3]: https://docs.sqlalchemy.org/en/latest/orm/extensions/asyncio.html?utm_source=chatgpt.com "Asynchronous I/O (asyncio) — SQLAlchemy 2.1 ..."
