# TOC

- https://ehmatthes.github.io/pcc_3e/
- https://github.com/ehmatthes/pcc_3e/
- solutions: https://ehmatthes.github.io/pcc_3e/solutions/

```
Table of contents
Preface to the Third Edition
Acknowledgments
Introduction
Part I: BASICS
Chapter 1: Getting Started
Chapter 2: Variables and Simple Data Types
Chapter 3: Introducing Lists
Chapter 4: Working with Lists
Chapter 5: if Statements
Chapter 6: Dictionaries
Chapter 7: User Input and while Loops
Chapter 8: Functions
Chapter 9: Classes
Chapter 10: Files and Exceptions
Chapter 11: Testing Your Code
Part II: PROJECTS
Chapter 12: A Ship That Fires Bullets
Chapter 13: Aliens!
Chapter 14: Scoring
Chapter 15: Generating Data
Chapter 16: Downloading Data
Chapter 17: Working with APIs
Chapter 18: Getting Started with Django
Chapter 19: User Accounts
Chapter 20: Styling and Deploying an App
Afterword
Appendix A: Installation and Troubleshooting
Appendix B: Text Editors and IDEs
Appendix C: Getting Help
Appendix D: Using Git for Version Control
Appendix E: Troubleshooting Deployments
Index
```

# Introdction

# Part 1

In Chapter 1 you’ll install Python on your computer and run your first program, which prints the message Hello world! to the screen.

In Chapter 2 you’ll learn to assign information to variables and work with text and numerical values.

Chapters 3 and 4 introduce lists. Lists can store as much information as you want in one place, allowing you to work with that data efficiently. You’ll be able to work with hundreds, thousands, and even millions of values in just a few lines of code.

In Chapter 5 you’ll use if statements to write code that responds one way if certain conditions are true, and responds in a different way if those conditions are not true.

Chapter 6 shows you how to use Python’s dictionaries, which let you make connections between different pieces of information. Like lists, dictionaries can contain as much information as you need to store.

In Chapter 7 you’ll learn how to accept input from users to make your programs interactive. You’ll also learn about while loops, which run blocks of code repeatedly as long as certain conditions remain true.

In Chapter 8 you’ll write functions, which are named blocks of code that perform a specific task and can be run whenever you need them.

Chapter 9 introduces classes, which allow you to model real-world objects. You’ll write code that represents dogs, cats, people, cars, rockets, and more.

Chapter 10 shows you how to work with files and handle errors so your programs won’t crash unexpectedly. You’ll store data before your program closes and read the data back in when the program runs again. You’ll learn about Python’s exceptions, which allow you to anticipate errors and make your programs handle those errors gracefully.

In Chapter 11 you’ll learn to write tests for your code, to check that your programs work the way you intend them to. As a result, you’ll be able to expand your programs without worrying about introducing new bugs. Testing your code is one of the first skills that will help you transition from beginner to intermediate programmer.

# Chapter 1: Getting Started

```
The exercises in this chapter are exploratory in nature. Starting in Chapter 2, the challenges you’ll solve will be based on what you’ve learned.

1-1. python.org: Explore the Python home page (https://python.org) to find topics that interest you. As you become familiar with Python, different parts of the site will be more useful to you.

1-2. Hello World Typos: Open the hello_world.py file you just created. Make a typo somewhere in the line and run the program again. Can you make a typo that generates an error? Can you make sense of the error message? Can you make a typo that doesn’t generate an error? Why do you think it didn’t make an error?

1-3. Infinite Skills: If you had infinite programming skills, what would you build? You’re about to learn how to program. If you have an end goal in mind, you’ll have an immediate use for your new skills; now is a great time to write brief descriptions of what you want to create. It’s a good habit to keep an “ideas” notebook that you can refer to whenever you want to start a new project. Take a few minutes now to describe three programs you want to create.
```

## Programs I want to create

1. TIME TRACKER APP
2. ...
3. ...

# Chapter 2: Variables and Simple Data Types

## Variables

```
start with a letter or an underscore, but not with a number. For instance, you can call a variable message_1 but not 1_message.
Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, greeting_message works but greeting message will cause errors.
Avoid using Python keywords and function names as variable names. For example, do not use the word print as a variable name; Python has reserved it for a particular programmatic purpose. (See “Python Keywords and Built-in Functions” on page 466.)
Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length is better than length_of_persons_name.
Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

```

- A traceback is a record of where the interpreter ran into trouble when trying to execute your code.

- It’s much better to think of variables as labels that you can assign to values. You can also say that a variable references a certain value.

- The best way to understand new programming concepts is to try using them in your programs. If you get stuck while working on an exercise in this book, try doing something else for a while.

## Exercise

```
Write a separate program to accomplish each of these exercises. Save each program with a filename that follows standard Python conventions, using lowercase letters and underscores, such as simple_message.py and simple_messages.py.

2-1. Simple Message: Assign a message to a variable, and then print that message.

2-2. Simple Messages: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
```

## Strings

- "This is a string."
- 'This is also a string.'

```
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

```python
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

```

- A syntax error occurs when Python doesn’t recognize a section of your program as valid Python code

```

message = 'One of Python's strengths is its diverse community.'
print(message)


first_name = "ada"
last_name = "lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favourite_language = ' python '
print(favourite_language.lstrip())
print(favourite_language.rstrip())
print(favourite_language.strip())


nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)


removesuffix('.txt')
```

### Exercise

```
Try It Yourself
Save each of the following exercises as a separate file, with a name like name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

Albert Einstein once said, “A person who never made a mistake never tried anything new.”

2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.

Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

```

## Numbers

### Integers

```
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5

>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000

>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

### Floats

- Python calls any number with a decimal point a float.

```
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4

>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

### Integers and Floats

```
>>> 4/2
2.0

>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

### Underscors in Numbers

```
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000
```

### Multiple Assignment

```
>>> x, y, z = 0, 0, 0
```

### Constants

- Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed

```
MAX_CONNECTIONS = 5000
```

### Exercise

```
Try It Yourself
2-9. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:

print(5+3)
Your output should be four lines, with the number 8 appearing once on each line.

2-10. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.
```

### Comments

```
# Say hello to everyone.
print("Hello Python people!")
```

- The main reason to write comments is to explain what your code is supposed to do and how you are making it work.
  When you’re in the middle of working on a project, you understand how all of the pieces fit together
- writing good comments can save you time by summarizing your overall approach clearly.
- If you want to become a professional programmer or collaborate with other programmers, you should write meaningful comments.
- it’s best to start adding descriptive comments to your programs now.
  Writing clear, concise comments in your code is one of the most beneficial habits you can form as a new programmer.

- When you’re deciding whether to write a comment, ask yourself if you had to consider several approaches before coming up with a reasonable way to make something work
- If so, write a comment about your solution; remove later if needed

### Exercise

```
Try It Yourself
2-11. Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.
```

## Zen Of Python

- avoid complexity and aim for simplicity whenever possible

```python
>>> import this
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
```

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

- much of programming consists of using small, common approaches to simple situations within a larger, more creative project

### Exercise

```
Try It Yourself
2-12. Zen of Python: Enter import this into a Python terminal session and skim through the additional principles.
```

### Chapter 2 Summary

In this chapter you learned how to work with variables.

You learned to use descriptive variable names and resolve name errors and syntax errors when they arise.

You learned what strings are and how to display them using lowercase, uppercase, and title case.

You started using whitespace to organize output neatly, and you learned how to remove unneeded elements from a string.

You started working with integers and floats, and you learned some of the ways you can work with numerical data.

You also learned to write explanatory comments to make your code easier for you and others to read.

Finally, you read about the philosophy of keeping your code as simple as possible, whenever possible.

In Chapter 3, you’ll learn how to

- store collections of information in data structures called lists.
- You’ll also learn how to work through a list, manipulating any information in that list.

# ZEN ADDITIONAL COMPARISON

Great—this is exactly how you internalize the Zen: **contrast it with how you’d naturally write JS/TS**.

I’ll go line-by-line and show:

- 👉 what it means
- ⚖️ typical JS/TS behavior
- 🐍 Pythonic approach (mentally, not just syntax)

---

# 1. Beautiful is better than ugly

👉 Code should look clean and intentional

### ⚖️ JS/TS (often compressed)

```js
const result = arr.filter((x) => x.active).map((x) => x.value);
```

### 🐍 Python mindset

```python
active_items = [item for item in items if item.active]
values = [item.value for item in active_items]
```

👉 JS favors compactness
👉 Python favors **visual clarity**

---

# 2. Explicit is better than implicit

👉 No hidden behavior

### ⚖️ JS

```js
if (value) { ... }  // truthy/falsy magic
```

### 🐍 Python

```python
if value is not None:
```

👉 JS allows guessing
👉 Python prefers **being precise about intent**

---

# 3. Simple is better than complex

👉 Prefer the easiest understandable solution

### ⚖️ JS (overengineering tendency)

```js
const handler = ({ config }) => new Processor(config).execute();
```

### 🐍 Python

```python
def handle(config):
    return process(config)
```

👉 Python discourages unnecessary abstraction

---

# 4. Complex is better than complicated

👉 If complexity is needed, structure it well

### ⚖️ JS (can become tangled)

```js
if (a) {
  if (b) {
    doSomething()
  } else {
    if (c) {
```

### 🐍 Python

```python
if not a:
    return

if b:
    do_something()
elif c:
    do_other()
```

👉 Python pushes **structured complexity**, not nesting chaos

---

# 5. Flat is better than nested

👉 Reduce indentation depth

### ⚖️ JS

```js
if (user) {
  if (user.active) {
    if (user.role === "admin") {
```

### 🐍 Python

```python
if not user:
    return
if not user.active:
    return
if user.role != "admin":
    return
```

👉 Early exits > deep nesting

---

# 6. Sparse is better than dense

👉 Use space to improve readability

### ⚖️ JS

```js
if (a) {
  doX();
  doY();
}
```

### 🐍 Python

```python
if a:
    do_x()
    do_y()
```

👉 Python embraces whitespace as structure

---

# 7. Readability counts

👉 The ultimate rule

### ⚖️ JS (clever but unclear)

```js
const r = a?.b?.c?.d ?? defaultVal;
```

### 🐍 Python

```python
if a and a.b and a.b.c:
    value = a.b.c.d
else:
    value = default_val
```

👉 Python sacrifices brevity for **clarity**

---

# 8. Special cases aren't special enough to break the rules

👉 Don’t introduce hacks

### ⚖️ JS

```js
if (type === "special") return weirdLogic();
```

### 🐍 Python

👉 Prefer:

- consistent flow
- same structure for all cases

---

# 9. Although practicality beats purity

👉 Be pragmatic

### ⚖️ JS

- often pragmatic already

### 🐍 Python

```python
# Not perfect, but clear and works
data = json.loads(raw_data)
```

👉 Don’t over-engineer “perfect” systems

---

# 10. Errors should never pass silently

👉 Don’t ignore failures

### ⚖️ JS (bad habit)

```js
try {
  doThing();
} catch (e) {}
```

### 🐍 Python

```python
try:
    do_thing()
except Exception as e:
    log_error(e)
```

👉 Errors must be visible

---

# 11. Unless explicitly silenced

👉 If you ignore errors, do it intentionally

### ⚖️ JS

Rarely explicit

### 🐍 Python

```python
try:
    optional_operation()
except FileNotFoundError:
    pass
```

👉 You know exactly what you’re ignoring

---

# 12. In the face of ambiguity, refuse the temptation to guess

👉 Don’t rely on unclear behavior

### ⚖️ JS

```js
Number("123abc"); // NaN but weird behavior elsewhere
```

### 🐍 Python

```python
int("123abc")  # raises error
```

👉 Python prefers **fail fast over guessing**

---

# 13. One obvious way to do it

👉 Standard patterns matter

### ⚖️ JS

```js
arr.map(...)
for (let i=0; i<arr.length; i++)
for (const x of arr)
```

### 🐍 Python

```python
[x for x in arr]
```

👉 Python pushes **idiomatic consistency**

---

# 14. “Unless you're Dutch”

👉 Learn the “Pythonic way”

### ⚖️ JS

- many valid styles

### 🐍 Python

- strong conventions
- less freedom, more consistency

---

# 15. Now is better than never

👉 Build something instead of overthinking

### ⚖️ JS & Python

Same idea:
👉 ship > over-plan

---

# 16. Never is often better than right now

👉 Don’t rush bad decisions

### ⚖️ JS

- fast prototyping culture

### 🐍 Python

- slightly more cautious

👉 balance speed vs correctness

---

# 17. Hard to explain = bad idea

### ⚖️ JS

```js
const result = pipe(compose(fn1, fn2))(input);
```

### 🐍 Python

```python
result = fn1(fn2(input))
```

👉 If you need to “explain the trick” → it’s bad

---

# 18. Easy to explain = good idea

👉 Simplicity = quality

---

# 19. Namespaces are great

👉 Organize code properly

### ⚖️ JS

```js
import * as utils from "./utils";
```

### 🐍 Python

```python
from app.services import time_tracker
```

👉 Python strongly encourages **clear module structure**

---

# 🧠 Final Translation for YOU

## JS/TS mindset:

- expressive
- flexible
- many patterns
- sometimes clever

## Python mindset:

- explicit
- consistent
- readable
- predictable

---

# 💥 The Key Shift

When writing Python, stop asking:

👉 “What’s the shortest way?”

Start asking:

👉 “What’s the clearest way?”

---

# If you want

I can take your **time tracker architecture** and show:

👉 “JS/TS design vs Pythonic design”

That would directly level you up for your job.

---

This explanation from Python Crash Course is actually _perfect for your situation_—you’re transitioning from JS/TS into Python and about to work professionally.

Let’s **translate this version of the Zen into real developer behavior**, especially for you.

---

# 🧠 What This Text Is REALLY Teaching You

It’s not about philosophy—it’s about:

👉 **How other Python developers will judge your code at work**

---

# 🔍 Key Principles (with real-world meaning)

---

## 1. “Beautiful is better than ugly”

### What beginners think:

> “Nice formatting”

### What it actually means:

👉 Code should feel **natural and obvious to read**

### In your job context:

- Clean function names
- Logical structure
- No weird tricks

### 🔥 Test:

If a colleague opens your file and instantly understands it → **beautiful**

---

## 2. “Simple is better than complex”

### Core idea:

👉 Don’t over-engineer

### Your risk (coming from JS/TS):

- abstractions too early
- fancy patterns
- “architecture thinking” before needed

### At work:

Prefer:

- small functions
- direct logic
- minimal layers

---

## 3. “Complex is better than complicated”

### Important nuance:

- Complex = necessary (real systems)
- Complicated = bad design

### Example (your time tracker):

- Multiple entities → **complex (good)**
- spaghetti logic → **complicated (bad)**

👉 Your goal:
Structure complexity so it’s understandable

---

## 4. “Readability counts”

This is **THE rule**.

### What it means in practice:

- good naming
- clear flow
- not too dense
- understandable without context

### At work:

Your code is not for you—it’s for:

- teammates
- future you
- reviewers

---

## 5. “One obvious way to do it”

### Big difference vs JS:

JS:

- 5 ways to loop
- 5 ways to structure code

Python:
👉 encourages **standard patterns**

### Why this matters at your job:

- easier code reviews
- easier collaboration
- less confusion

---

## 6. “Now is better than never”

### Meaning:

👉 Don’t wait to be perfect

### For you (very important):

You:

- want to learn Python fast
- have 2 weeks

👉 So:

- build
- break things
- improve later

---

# 🧠 The Hidden Lesson in This Text

This paragraph is key:

> “Experienced programmers will respect your code more…”

👉 Translation:

Your code is judged on:

- clarity
- simplicity
- consistency

NOT:

- cleverness
- tricks
- “smart” solutions

---

# ⚠️ Biggest Trap for YOU

Coming from JS/TS, you might:

❌ write clever code
❌ compress logic
❌ over-abstract early

Python devs will think:

👉 “Why is this so complicated?”

---

# ✅ What You Should Do Instead (Practical Rules)

When writing Python, always:

### 1. Prefer boring code

Boring = good in Python

---

### 2. Expand instead of compress

```python
# GOOD
if user is None:
    return

# BAD mindset (JS-style cleverness)
if user: ...
```

---

### 3. Name everything clearly

```python
# GOOD
active_sessions = get_active_sessions()

# BAD
data = get_data()
```

---

### 4. Avoid “clever” one-liners

Readable > short

---

### 5. Structure first, optimize later

Don’t prematurely optimize

---

# 💥 What This Means for Your Job Stack

With:

- FastAPI
- SQLAlchemy
- Streamlit

You should aim for:

👉 Clean endpoints
👉 Clear models
👉 Simple business logic
👉 Predictable structure

---

# 🧠 One Powerful Mental Model

Before writing code, ask:

👉 “Can I explain this in one sentence?”

If not:
👉 it’s too complicated

---

# 🔥 Final Translation (for YOU)

The Zen is basically saying:

> Write code like you’re explaining it to another developer sitting next to you.

Not:

> Write code to impress them

---

# If you want

I can review your **time tracker design or code (even rough)** and tell you:

👉 “This is Pythonic vs this is still JS thinking”

That’s the fastest way for you to internalize this.
