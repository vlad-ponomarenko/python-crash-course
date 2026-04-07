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

# TODO

- Chapter 4: last exercise - set up vscode, read through PEP 8

# FUNCTIONS

## Chapter 3

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

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

# HOW TO LEARN TS PYTHON AT THE SAME TIME

# CHAPTER 3 - INTRODUCING LISTS

- A list is a collection of items in a particular order

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
```

## Exercise

```
Try these short programs to get some firsthand experience with Python’s lists. You might want to create a new folder for each chapter’s exercises, to keep them organized.

3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
```

- Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course

## Lists

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# appending elements to a list
motorcycles.append('ducati')
print(motorcycles)

# inserting elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']

# This operation shifts every other value in the list one position to the right.
motorcycles.insert(0, 'ducati')
print(motorcycles)
# ['ducati', 'honda', 'yamaha', 'suzuki']


# removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Sometimes you’ll want to use the value of an item after you remove it from a list.

# The pop() method removes the last item in a list, but it lets you work with that item after removing it

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
```

- when you want to delete an item from a list and not use that item in any way, use the del statement;
- if you want to use an item as you remove it, use the pop() method.

* If you only know the value of the item you want to remove, you can use the remove() method.

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```

```python
❶ motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

❷ too_expensive = 'ducati'
❸ motorcycles.remove(too_expensive)
print(motorcycles)
❹ print(f"\nA {too_expensive.title()} is too expensive for me.")

```

- The remove() method deletes only the first occurrence of the value you specify.
- If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed.
  You’ll learn how to do this in Chapter 7

## Exercise

```
Try It Yourself
The following exercises are a bit more complex than those in Chapter 2, but they give you an opportunity to use lists in all of the ways described.

3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
Print a message to each of the two people still on your list, letting them know they’re still invited.
Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
```

## Organizing a List

- permament sort

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
```

- temporarily sort a list

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

❶ print("Here is the original list:")
print(cars)

❷ print("\nHere is the sorted list:")
print(sorted(cars))

❸ print("\nHere is the original list again:")
print(cars)

print(sorted(cars, reverse=True))
```

## Printing List in Reverse Order

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

len(cars)
```

## Exercise

```
Try It Yourself
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show that its order has changed.
Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.

3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once
```

In this chapter, you learned what lists are and how to work with the individual items in a list.

You learned how to define a list and how to add and remove elements.

You learned how to sort lists permanently and temporarily for display purposes.

You also learned how to find the length of a list and how to avoid index errors when you’re working with lists.

In Chapter 4 you’ll learn how to work with items in a list more efficiently.

By looping through each item in a list using just a few lines of code you’ll be able to work efficiently, even when your list contains thousands or millions of items.

# CHAPTER 4 - WORKING WITH LISTS

```
Looping Through an Entire List
Avoiding Intendation Errors
Making Numerical List
Working with Part of a List
Tuples
Styling Your Code
Summary
```

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


for cat in cats:
for dog in dogs:
for item in list_of_items:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

## Avoiding Intendation Errors

- ez

## Exercise

```
Try It Yourself
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

Modify your program to print a statement about each animal, such as A dog would make a great pet.
Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
```

## Numerical Lists

- Python’s range() function makes it easy to generate a series of numbers

```python
for value in range(1, 5):
    print(value)

# [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)

# [2, 4, 6, 8, 10]
even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
❶     square = value ** 2
❷     squares.append(square)

print(squares)


squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
```

- min, max, sum

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

## List Comprehensions

```python
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = [value**2 for value in range(1, 11)]
print(squares)

```

## Exercise

```
Try It Yourself
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

```

## Working with Part of a List

- in this chapter you’ve been learning how to work through all the elements in a list.
- You can also work with a specific group of items in a list, called a slice in Python

```python
# ['charles', 'martina', 'michael']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# ['martina', 'michael', 'florence']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


# ['charles', 'martina', 'michael', 'florence']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])


# ['michael', 'florence', 'eli']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])


#  if we want to output the last three players on the roster
# ['michael', 'florence', 'eli']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```

- You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

```

## Copying a List

```python
# we make a copy of my_foods by asking for a slice of my_foods without specifying any indices ❶, and assign the copy to friend_foods
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# my_foods = friends_foods is WRONG


```

## Exercise

```
Try It Yourself
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

```

## Tuples

- a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# causes TypeError
# dimensions[0] = 250

# A Tuple with one element
my_t = (3,)


dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing Over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


```

## Exercise

```
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects the change.
The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
```

## Styling Your Code

- write code that’s easier to read

* TODO!

- Appendix B shows you how to configure your text editor so it always inserts four spaces each time you press the TAB key and shows a vertical guideline to help you follow the 79-character limit.

```
Intendation: four spaces per intedtation level
    never mix tabs and spaces. convert tabs into spaces via editor

Line Length: max 79 characters (<80) or <99. Visual Cue in editor (vertical line on the screen)

Blank Lines: To group parts of your program visually, use blank lines
    The Python interpreter uses horizontal indentation to interpret the meaning of your code, but it disregards vertical spacing.

    Do not use them excessively
```

- TODO !!!

## Exercise

```
Try It Yourself
4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. You won’t use much of it now, but it might be interesting to skim through it.

4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

Use four spaces for each indentation level. Set your text editor to insert four spaces every time you press the TAB key, if you haven’t already done so (see Appendix B for instructions on how to do this).
Use less than 80 characters on each line, and set your editor to show a vertical guideline at the 80th character position.
Don’t use blank lines excessively in your program files.

```

Great—this is exactly the kind of **habit setup that pays off long-term**.
Let’s configure Visual Studio Code so it naturally enforces PEP 8 without you thinking about it.

---

# ⚙️ 1. Set indentation to 4 spaces (NO tabs)

### Quick way (per file)

- Bottom right in VS Code → click **“Spaces: 2” or “Tab Size”**
- Set:
  - **Indent Using Spaces**
  - **Tab Size: 4**

---

### Permanent setting (recommended)

Open settings JSON:

👉 `Ctrl + Shift + P` → “Preferences: Open Settings (JSON)”

Add:

```json id="1n4skz"
"[python]": {
  "editor.insertSpaces": true,
  "editor.tabSize": 4
}
```

---

# 📏 2. 80-character line limit + vertical ruler

Add this to settings:

```json id="o4shx6"
"editor.rulers": [80],
"editor.wordWrap": "off"
```

👉 You’ll now see a vertical line at column 80

---

# ✂️ 3. Auto-format to PEP 8 (VERY IMPORTANT)

Install formatter:

👉 Extension:

- Black

Then in settings:

```json id="xygkqb"
"[python]": {
  "editor.defaultFormatter": "ms-python.black-formatter",
  "editor.formatOnSave": true
}
```

👉 Now every save = clean code

---

# 🧹 4. Linting (to catch style issues)

Install:

- Flake8

Then:

```json id="y66h4t"
"python.linting.enabled": true,
"python.linting.flake8Enabled": true
```

👉 This warns you about:

- long lines
- unused variables
- style violations

---

# 🧠 5. Blank line discipline (PEP 8 rule)

VS Code won’t fully enforce this automatically, but follow:

### Use:

- 2 blank lines → between top-level functions/classes
- 1 blank line → inside logical sections

### Avoid:

❌ huge vertical gaps
❌ no spacing at all

---

# 🔥 6. Optional but HIGHLY recommended

## Auto organize imports

```json id="cvikqk"
"editor.codeActionsOnSave": {
  "source.organizeImports": true
}
```

---

# 🧠 What This Setup Gives You

After this:

👉 You don’t think about formatting
👉 You focus on logic
👉 Your code looks professional automatically

---

# ⚠️ Important Reality Check

PEP 8 is not about:

❌ “perfect formatting”
❌ “strict rules”

It’s about:

👉 **making your code readable for other developers**

---

# 💥 Minimal Setup Summary

If you only do 3 things:

1. 4 spaces indentation
2. 80-char ruler
3. Black formatter on save

👉 You’re already ahead of most beginners

---

# If you want

I can show you:

👉 “bad Python (JS-style)” vs “clean Python (PEP 8)” on your actual code

That will lock this in much faster.

# RESULT: 04 04 26

Good—your config is already solid. You only need to **add a few Python-specific overrides** so styles don’t clash with your JS/TS setup.

👉 **Do NOT rewrite everything**. Just add/adjust this block.

---

# ✅ Add / Update this in your `settings.json`

Replace your current `[python]` block with:

```json
"[python]": {
  "editor.insertSpaces": true,
  "editor.tabSize": 4,
  "editor.rulers": [80],
  "editor.wordWrap": "off",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "ms-python.black-formatter"
},
```

---

# ➕ ALSO add React support (important)

Right now you only configured JS/TS, not React files.

Add this:

```json
"[javascriptreact]": {
  "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[typescriptreact]": {
  "editor.defaultFormatter": "esbenp.prettier-vscode"
},
```

---

# 🧠 What this does (very important)

Now your editor behaves like this:

## 🐍 Python files

- 4 spaces
- 80 char line limit
- no auto wrap (you control formatting)
- formatted with **Black**
- PEP 8 style enforced

---

## ⚛️ JS / TS / React files

- formatted with **Prettier**
- ESLint still works
- your existing setup unchanged

---

# ⚠️ One thing you MUST do

Install the formatter:

👉 Extension:

- **Black Formatter** (ms-python.black-formatter)

If you don’t install it → Python formatting won’t work

---

# 💥 That’s it

You now have:

👉 Clean separation of styles
👉 No mixing Python ↔ React habits
👉 Automatic formatting for both stacks

---

# 🔥 Optional (nice upgrade later)

If you want even stricter Python quality later, add:

```json
"python.linting.enabled": true,
"python.linting.flake8Enabled": true,
```

---

# 🧠 Final mental model

You’ve now encoded this into your editor:

- Python → **readable, strict, explicit**
- TS/React → **flexible, formatted, composable**

👉 This is exactly how strong full-stack engineers work across ecosystems.

---

If you want, next step I can show you:

👉 “Same feature written badly vs correctly in Python + React”

That will make this separation _fully click_.

# CURRENT STYLING SETUP

```json
"[python]": {
  "editor.insertSpaces": true,
  "editor.tabSize": 4,
  "editor.rulers": [80],
  "editor.wordWrap": "off",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "ms-python.black-formatter"
},
"python.analysis.typeCheckingMode": "basic",
"python.analysis.autoImportCompletions": true,
"ruff.enable": true

```

# SKIP FOR NOW

```json
"python.analysis.inlayHints.variableTypes": true,
"python.analysis.inlayHints.functionReturnTypes": true,
"python.analysis.inlayHints.callArgumentNames": "partial"

```

Good pushback—this is exactly the kind of thinking that makes you improve fast.

You’re right to question it. So let’s be precise:

👉 You’re **not skipping them because they’re bad**
👉 You’re skipping them because of **cognitive load vs value right now**

---

# 🧠 The Real Reason (not generic advice)

As a fullstack beginner (in Python):

You are already juggling:

- new language (Python)
- new framework (FastAPI)
- new UI model (Streamlit)
- DB + SQLAlchemy
- job pressure

👉 Adding too many editor signals = **noise > signal**

---

# ⚖️ What those extra settings actually do

These:

```json
"python.analysis.inlayHints.variableTypes": true,
"python.analysis.inlayHints.functionReturnTypes": true,
"python.analysis.inlayHints.callArgumentNames": "partial"
```

👉 show _visual hints inside your code_

Example:

```python
result = calculate(a, b)
```

Becomes (visually):

```python
result: int = calculate(a: int, b: int)
```

---

# 🔥 Why this can hurt you (right now)

## 1. It hides learning

You stop thinking:

> “What type is this?”

Because the editor tells you.

👉 You want to **build that intuition yourself first**

---

## 2. It clutters your screen

Instead of:

```python
process_data(data)
```

You see:

```python
process_data(data: dict[str, Any])
```

👉 harder to read
👉 more mental overhead

---

## 3. It encourages passive coding

You start:

- trusting hints
- not understanding flow

👉 dangerous when debugging real systems

---

# 🧠 What you SHOULD build first

Before adding hints, you want:

### 1. Mental model of types

- what is a list vs dict
- what a function returns
- where data flows

---

### 2. Confidence without assistance

You should be able to read:

```python
sessions = get_sessions(user_id)
```

and know:

- what `sessions` likely is
- what shape it has

---

# ⚡ When hints become USEFUL

Later (very useful actually):

👉 When your codebase grows

Then hints help:

- navigating unfamiliar code
- understanding APIs quickly
- reducing context switching

---

# 🎯 So the real answer

## You skip them NOW because:

👉 they reduce **active thinking**
👉 they increase **visual noise**
👉 they don’t solve your current bottleneck

---

# 💥 What your current bottleneck actually is

Not:

- missing type hints UI

But:

- understanding Python style
- writing clean logic
- structuring backend code

---

# 🧭 Better progression (for YOU)

## Phase 1 (now)

- minimal setup
- think actively
- write and debug

---

## Phase 2 (2–4 weeks later)

👉 add:

```json
"python.analysis.inlayHints.variableTypes": true,
"python.analysis.inlayHints.functionReturnTypes": true
```

Now they become:
👉 productivity boost

---

# 🔥 Analogy

Learning Python with hints ON too early is like:

👉 learning math with answers shown next to every problem

You:

- solve faster ❌
- understand less ❌

---

# 🧠 Final Recommendation

👉 Start without them
👉 Turn them on once you feel:

> “I understand most of what I write, now I want speed”

---

# 💡 Important nuance

You are NOT “avoiding tools”

You are:
👉 **timing them correctly**

---

If you want, I can show you:

👉 same Python function with and without hints
👉 and how it affects readability + thinking

That usually makes this click instantly.

# SUMMARY CHAPTER 4

Summary
In this chapter, you learned how to work efficiently with the elements in a list.

You learned how to work through a list using a for loop,

how Python uses indentation to structure a program, and how to avoid some common indentation errors.

You learned to make simple numerical lists, as well as a few operations you can perform on numerical lists.

You learned how to slice a list to work with a subset of items and how to copy lists properly using a slice.

You also learned about tuples, which provide a degree of protection to a set of values that shouldn’t change,

and how to style your increasingly complex code to make it easy to read.

In Chapter 5, you’ll learn to

respond appropriately to different conditions by using if statements.

You’ll learn to string together relatively complex sets of conditional tests to respond appropriately to exactly the kind of situation or information you’re looking for.

You’ll also learn to use if statements while looping through a list to take specific actions with selected elements from a list.

# CHAPTER 5 - if Statements

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
❶     if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


car = 'bmw'
car == 'bmw'

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# true
car = "bmw"
print(car == "bmw")

# true
car2 = "bmw"
print(car == car2)

# true
car = "Audi"
print(car.lower() == "audi")

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

# numerical comparisons
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

print(age < 17)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
multiple_condition = age_0 >= 21 and age_1 >= 21

# for better readability
another_condition = (age_0 >= 21) and (age_1 >= 21)

or_condition = age_0 >= 21 or age_1 <= 21

# checking whether a value is in a list

requested_toppings = ["mushrooms", "onions", "pineapple"]
list_condition_1 = "mushrooms" in requested_toppings
list_condition_2 = "pepperoni" in requested_toppings

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expression
game_active = True
can_edit = False

```

## Exercise

```
Try It Yourself
5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
Look closely at your results, and make sure you understand why each line evaluates to True or False.
Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list

```

## If Statements

```python
age = 12
❶ if age < 4:
    print("Your admission cost is $0.")
❷ elif age < 18:
    print("Your admission cost is $25.")
❸ else:
    print("Your admission cost is $40.")


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

## Exercise

```
Try It Yourself
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
If the alien’s color isn’t green, print a statement that the player just earned 10 points.
Write one version of this program that runs the if block and another that runs the else block.
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

If the alien is green, print a message that the player earned 5 points.
If the alien is yellow, print a message that the player earned 10 points.
If the alien is red, print a message that the player earned 15 points.
Write three versions of this program, making sure each message is printed for the appropriate color alien.
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

If the person is less than 2 years old, print a message that the person is a baby.
If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
If the person is at least 4 years old but less than 13, print a message that the person is a kid.
If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
If the person is at least 20 years old but less than 65, print a message that the person is an adult.
If the person is age 65 or older, print a message that the person is an elder.
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

Make a list of your three favorite fruits and call it favorite_fruits.
Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!
```

## Using Statements with lists

```python
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


requested_toppings = []

# check for emptiness
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")




# check against the other list
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

❶ requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
❷     if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
❸     else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

```

## Exercise

```
Try It Yourself
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.

If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.

If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct message is printed.
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

Store the numbers 1 through 9 in a list.
Loop through the list.
Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
```

## Styling your statements

- use a single space around comparison operators, such as ==, >=, and <=. For example

```python
if age < 4:

```

## Exercise

```
Try It Yourself
5-12. Styling if Statements: Review the programs you wrote in this chapter, and make sure you styled your conditional tests appropriately.

5-13. Your Ideas: At this point, you’re a more capable programmer than you were when you started this book. Now that you have a better sense of how real-world situations are modeled in programs, you might be thinking of some problems you could solve with your own programs. Record any new ideas you have about problems you might want to solve as your programming skills continue to improve. Consider games you might want to write, datasets you might want to explore, and web applications you’d like to create.
```

## Summary Chapter 5

In this chapter you learned how to
write conditional tests, which always evaluate to True or False.

You learned to write simple if statements, if-else chains, and if-elif-else chains.

You began using these structures to identify particular conditions you need to test and to know when those conditions have been met in your programs.

You learned to handle certain items in a list differently than all other items while continuing to utilize the efficiency of a for loop.

You also revisited Python’s style recommendations to ensure that your increasingly complex programs are still relatively easy to read and understand.

In Chapter 6 you’ll learn about Python’s dictionaries.

A dictionary is similar to a list, but it allows you to connect pieces of information.

You’ll learn how to build dictionaries, loop through them, and use them in combination with lists and if statements.

Learning about dictionaries will enable you to model an even wider variety of real-world situations.

# CHAPTER 6 - DICTIONARIES

- A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.

- A key’s value can be a number, a string, a list, or even another dictionary.

* In fact, you can use any object that you can create in Python as a value in a dictionary.

* In Python, a dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces

* A key-value pair is a set of values associated with each other

```python
alien_0 = {'color': 'green'}
alien_0 = {'color': 'green', 'points': 5}
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)



alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modify

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
```

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
❶ if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
❷ alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

```

## Removing key-value pairs

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

❶ del alien_0['points']
print(alien_0)
```

## A Dictionary of similar objects

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")


```

## Using get() to access values

- Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


# None

point_value = alien_0.get("points")
print(point_value)

```

- if you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value. You’ll see more uses for None in Chapter 8.

## Exercise

```
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

```

## Looping throgh a dictionary: for k, v in user_0.items()

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
# same as for name in favorite_languages
for name in favorite_languages.keys():
    print(name.title())
```

```python
favorite_languages = {
    --snip--
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

❶     if name in friends:
❷         language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
```

```python
if "erin" not in favorite_languages.keys():
        print("Erin, please take our poll!")

```

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

- This approach pulls all the values from the dictionary without checking for repeats

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

```

- but in a poll with a large number of respondents, it would result in a very repetitive list
- To see each language chosen without repetition, we can use a set. A set is a collection in wh

```python
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

```

- Set

```python
languages = {'python', 'rust', 'python', 'c'}
# {'rust', 'python', 'c'}
```

## Exercise

Try It Yourself
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
6-6. Polling: Use the code in favorite_languages.py (page 96).

Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

## Nesting

### A list of Dictionaries

- store multiple dictionaries in a list,
- or a list of items as a value in a dictionary.

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

❶ aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}
```

```python
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

print("PRINT 5 ALIENS")

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

```

### A list in a Dictionary

```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
❶ print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

❷ for topping in pizza['toppings']:
    print(f"\t{topping}")


# output
You ordered a thick-crust pizza with the following toppings:
        mushrooms
        extra cheese
```

- We begin with a dictionary that holds information about a pizza that has been ordered.

One key in the dictionary is 'crust', and the associated value is the string 'thick'. The next key, 'toppings', has a list as its value that stores all requested toppings.

We summarize the order before building the pizza ❶. When you need to break up a long line in a print() call, choose an appropriate point at which to break the line being printed, and end the line with a quotation mark.

Indent the next line, add an opening quotation mark, and continue the string.

Python will automatically combine all of the strings it finds inside the parentheses. To print the toppings, we write a for loop ❷.

To access the list of toppings, we use the key 'toppings', and Python grabs the list of toppings from the dictionary.

- You can nest a list inside a dictionary anytime you want more than one value to be associated with a single key in a dictionary.

```python
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

❶ for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
❷     for language in languages:
        print(f"\t{language.title()}")

```

- You should not nest lists and dictionaries too deeply. If you’re nesting items much deeper than what you see in the preceding examples, or if you’re working with someone else’s code with significant levels of nesting, there’s most likely a simpler way to solve the problem.

### A Dictionary in a Dictionary

- For example, if you have several users for a website, each with a unique username, you can use the usernames as the keys in a dictionary.

- You can then store information about each user by using a dictionary as the value associated with their username

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

❶ for username, user_info in users.items():
❷     print(f"\nUsername: {username}")
❸     full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

❹     print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

## Exercise

```Try It Yourself
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

```

## Summary

In this chapter, you learned how to

define a dictionary and
how to work with the information stored in a dictionary.

You learned how to access and modify individual elements in a dictionary,

and how to loop through all of the information in a dictionary.

You learned to loop through a dictionary’s key-value pairs, its keys, and its values.

You also learned how to
nest multiple dictionaries in a list,
nest lists in a dictionary, and
nest a dictionary inside a dictionary.

In the next chapter you’ll learn about
while loops and how to accept input from people who are using your programs.

This will be an exciting chapter, because you’ll learn to make all of your programs interactive: they’ll be able to respond to user input.

```python
# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")


favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")


favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}"
```

# CHAPTER 7 - User Input and while Loops

- With the ability to work with user input and the ability to control how long your programs run, you’ll be able to write fully interactive programs.

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Prompt that's longer than one line
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

```

## Exercise

```
Try It Yourself
7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

```

## Introducing while Loops

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

- using a flag

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
❶ while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

```

- using break to exit loop

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

❶ while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

- using continue

```python
current_number = 0
while current_number < 10:
❶     current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

```

## Exercise

```
Try It Yourself
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:

Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)
```

## Using a while Loop with Lists and Dictionaries

- A for loop is effective for looping through a list,
- but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list.
- To modify a list as you work through it, use a while loop.
- Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

```python
# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
❶ unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
❷ while unconfirmed_users:
❸     current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
❹     confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

- remove all instances of specific values from a list

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

```

- dictionaries

```python
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
❶     name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
❷     responses[name] = response

    # Find out if anyone else is going to take the poll.
❸     repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
❹ for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

## Exercise

```
Try It Yourself
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
```

# Summary CHAPTER 7

In this chapter, you learned how to use input() to allow users to provide their own information in your programs.

You learned to work with both text and numerical input and how to use while loops to make your programs run as long as your users want them to.

You saw several ways to control the flow of a while loop by setting an active flag, using the break statement, and using the continue statement.

You learned how to use a while loop to move items from one list to another and how to remove all instances of a value from a list.

You also learned how while loops can be used with dictionaries.

In Chapter 8 you’ll learn about functions.

Functions allow you to break your programs into small parts, each of which does one specific job.

You can call a function as many times as you want, and you can store your functions in separate files.

By using functions, you’ll be able to write more efficient code that’s easier to troubleshoot and maintain and that can be reused in many different programs.

```python
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
```

```python
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")

```

```python
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}
```

# CHAPTER 8 - FUNCTIONS

- functions, which are named blocks of code designed to do one specific job

In this chapter you’ll also learn a variety of ways to pass information to functions.

You’ll learn how to write certain functions whose primary job is to display information and other functions designed to process data and return a value or set of values.

Finally, you’ll learn to store functions in separate files called modules to help organize your main program files.

```python
# function definition
def greet_user():
    # The text on the second line is a comment called a docstring, which describes what the function does.
    """Display a simple greeting."""
    print("Hello!")

greet_user()


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

- parameter, a piece of information the function needs to do its job.
- An argument is a piece of information that’s passed from a function call to a function

## Exercise

```
Try It Yourself
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.


```

- You can use positional arguments, which need to be in the same order the parameters were written;

- keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values

```python
# positional
❶ def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

❷ describe_pet('hamster', 'harry')

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# keyword arguemnts
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

- default values

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# The only argument provided is 'willie', so it is matched up with the first parameter in the definition, pet_name
describe_pet(pet_name='willie')
describe_pet('willie')
# Because an explicit argument for animal_type is provided, Python will ignore the parameter’s default value.
describe_pet(pet_name='harry', animal_type='hamster')
```

- equivalent function calls

```python
def describe_pet(pet_name, animal_type='dog'):
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


```

## Exercise

```
Try It Yourself
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
```

## Return Values

- The value the function returns is called a return value.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
❶     full_name = f"{first_name} {last_name}"
❷     return full_name.title()

❸ musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

- making an argument optional

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
❶     if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
❷     else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

❸ musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Jimi Hendrix
# John Lee Hooker
```

- Returning a dictionary

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
❶     person = {'first': first_name, 'last': last_name}
❷     return person

musician = build_person('jimi', 'hendrix')
❸ print(musician)
# {'first': 'jimi', 'last': 'hendrix'}
```

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

- using a function with a while Loop

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

## Exercise

```
Try It Yourself
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.

8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
```

## Passing a List

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

## Modifying a List in a Function

- Any changes made to the list inside the function’s body are permanent

- reorganizing the code

```python
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

- This example also demonstrates the idea that every function should have one specific job.
- If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions.

```python
❶ def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

❷ def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

```

## Preventing a Function from Modifying a List

```python
print_models(unprinted_designs[:], completed_models)
```

## Passing an Arbitrary Number of Arguments

- Python allows a function to collect an arbitrary number of arguments from the calling statement.

- tells Python to make a tuple called toppings, containing all the values this function receives.

- Note that Python packs the arguments into a tuple, even if the function receives only one value:

```
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

## Mixing Positional and Arbitrary Arguments

- If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.

- Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

- You’ll often see the generic parameter name \*args, which collects arbitrary positional arguments like this.

## Using Arbitrary Keyword Arguments

- The double asterisks before the parameter \*\*user_info cause Python to create a dictionary called user_info containing all the extra name-value pairs the function receives

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
❶     user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```

- You’ll often see the parameter name \*\*kwargs used to collect nonspecific keyword arguments.

## Exercise

```
Try It Yourself
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.
```

- WTF IS THIS BULLSHIT?

```python
def get_items(*toppings):
    print("\nThe following toppings are provided:")
    for topping in toppings:
        print(f"- {topping}")


get_items(["a"])
get_items(["a", "b"])
get_items(["c", "b", "a"])

items = ["a", "b"]
get_items(*items)   # ✅ unpacking
```

```
The following toppings are provided: - ['a', 'b'] The following toppings are provided: - ['c', 'b', 'a']

```

- correct

```python
get_items("a")
get_items("a", "b")
get_items("c", "b", "a")
```

```python
def make_car(manufacturer, model, **kvargs):
    kvargs["manufacturer"] = manufacturer
    kvargs["model"] = model
    return kvargs


my_car = make_car("audi", "tt", color="blue", tow_package=True)
print(my_car)

```

## Storing Your Functions in Modules

- When you use descriptive names for your functions, your programs become much easier to follow
- You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program.
- An import statement tells Python to make the code in a module available in the currently running program file.

- Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic.
- It also allows you to reuse functions in many different programs.

### Importing an Entire Module

- pizza is name of the module
- module_name.function_name()

```python
# pizza.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

- When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program

```python
# making_pizzas.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing Specific Functions

```python
from module_name import function_name
from module_name import function_0, function_1, function_2
```

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using as to Give a Function an Alias

```python
from module_name import function_name as fn
```

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using as to Give a Module an Alias

```python
import module_name as mn
```

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

```

### Importing all functions in a Module

```python
from module_name import *
```

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

- The asterisk in the import statement tells Python to copy every function from the module pizza into this program file.

Because every function is imported, you can call each function by name without using the dot notation.

However, it’s best not to use this approach when you’re working with larger modules that you didn’t write:

- if the module has a function name that matches an existing name in your project, you can get unexpected results.
- Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions.

- The best approach is to import the function or functions you want, or import the entire module and use the dot notation

```python
from module_name import *
```

## Styling Functions

- If you specify a default value for a parameter, no spaces should be used on either side of the equal sign
- The same convention should be used for keyword arguments in function calls:

```python
def function_name(parameter_0, parameter_1='default value')
function_name(value_0, parameter_1='value')
```

- Functions should have descriptive names, and these names should use lowercase letters and underscores.
- Every function should have a comment that explains concisely what the function does.
- This comment should appear immediately after the function definition and use the docstring format

```
 In a well-documented function, other programmers can use the function by reading only the description in the docstring. They should be able to trust that the code works as described, and as long as they know the name of the function, the arguments it needs, and the kind of value it returns, they should be able to use it in their programs.
```

```
PEP 8 (https://www.python.org/dev/peps/pep-0008) recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window. If a set of parameters causes a function’s definition to be longer than 79 characters, press ENTER after the opening parenthesis on the definition line. On the next line, press the TAB key twice to separate the list of arguments from the body of the function, which will only be indented one level.

Most editors automatically line up any additional lines of arguments to match the indentation you have established on the first line:

def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```

- If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins.

- All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.

```python
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
```

```python
# printing_functions.py
"""Functions related to printing 3d models."""

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


#printing_models.py:

printing_models.py
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

```

## Summary

```
In this chapter, you learned how to write functions and to pass arguments so that your functions have access to the information they need to do their work. You learned how to use positional and keyword arguments, and also how to accept an arbitrary number of arguments. You saw functions that display output and functions that return values. You learned how to use functions with lists, dictionaries, if statements, and while loops. You also saw how to store your functions in separate files called modules, so your program files will be simpler and easier to understand. Finally, you learned to style your functions so your programs will continue to be well-structured and as easy as possible for you and others to read.

One of your goals as a programmer should be to write simple code that does what you want it to, and functions help you do this. They allow you to write blocks of code and leave them alone once you know they work. When you know a function does its job correctly, you can trust that it will continue to work and move on to your next coding task.

Functions allow you to write code once and then reuse that code as many times as you want. When you need to run the code in a function, all you need to do is write a one-line call and the function does its job. When you need to modify a function’s behavior, you only have to modify one block of code, and your change takes effect everywhere you’ve made a call to that function.

Using functions makes your programs easier to read, and good function names summarize what each part of a program does. Reading a series of function calls gives you a much quicker sense of what a program does than reading a long series of code blocks.

Functions also make your code easier to test and debug. When the bulk of your program’s work is done by a set of functions, each of which has a specific job, it’s much easier to test and maintain the code you’ve written. You can write a separate program that calls each function and tests whether each function works in all the situations it may encounter. When you do this, you can be confident that your functions will work properly each time you call them.
```

| Method                     | Syntax                         | How you use it          | When to use                            | Verdict     |
| -------------------------- | ------------------------------ | ----------------------- | -------------------------------------- | ----------- |
| Import module              | `import module`                | `module.func()`         | Default, best practice, large projects | ✅ BEST     |
| Import with alias          | `import module as m`           | `m.func()`              | Shorten long names                     | ✅ GOOD     |
| Import specific            | `from module import func`      | `func()`                | Small scripts, few functions           | ✅ OK       |
| Import specific with alias | `from module import func as f` | `f()`                   | Avoid name conflicts                   | ✅ GOOD     |
| Import everything          | `from module import *`         | `func()`                | Never (except quick testing)           | ❌ AVOID    |
| Import submodule           | `import package.module`        | `package.module.func()` | Working with packages                  | ✅ GOOD     |
| Relative import            | `from .module import func`     | `func()`                | Inside your own packages               | ✅ ADVANCED |

Here’s a **clean table summary of the styling rules** (PEP 8 + your book section):

---

## 🧠 Python Function Styling Rules — Table

| Rule                   | What it means               | Example                   | Why it matters                 |
| ---------------------- | --------------------------- | ------------------------- | ------------------------------ |
| Function names         | lowercase + underscores     | `def make_car():`         | Readable, standard             |
| Module names           | lowercase + underscores     | `printing_functions.py`   | Consistency                    |
| Descriptive names      | Name reflects purpose       | `calculate_total_price()` | Self-explanatory code          |
| Docstring required     | Comment right after `def`   | `"""Create a car dict"""` | Others can use function easily |
| Default params spacing | No spaces around `=`        | `x=10`                    | PEP 8 consistency              |
| Keyword args spacing   | No spaces around `=`        | `func(a=1)`               | Clean syntax                   |
| Line length            | Max ~79–80 chars            | (use ruler)               | Readability                    |
| Long parameter lists   | Break into multiple lines   | see below                 | Avoid long lines               |
| Indentation in params  | Align parameters cleanly    | see below                 | Readable structure             |
| Multiple functions     | Separate with 2 blank lines | ⬜⬜ between functions    | Visual clarity                 |
| Imports location       | Top of file                 | `import module`           | Standard structure             |

---

## 🔹 Example: long function definition

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4):
    """Short description of function."""
    pass
```

---

## 🔥 Clean example (fully styled)

```python
import printing_functions


def make_car(manufacturer, model, color='black'):
    """Create a dictionary describing a car."""
    return {
        'manufacturer': manufacturer,
        'model': model,
        'color': color,
    }


def print_car(car):
    """Print car details."""
    print(car)
```

---

## ⚡ Quick checklist (mental)

Before finishing code, ask:

- ✔ names readable?
- ✔ docstring present?
- ✔ no weird spacing (`=`)?
- ✔ lines not too long?
- ✔ imports at top?
- ✔ functions separated?

---

## 🔥 One-line takeaway

> Write code so others understand it **without reading the implementation**

---

# CHAPTER 9 - CLASSES

- In object-oriented programming, you write classes that represent real-world things and situations, and you create objects based on these classes.

- When you write a class, you define the general behavior that a whole category of objects can have.

* When you create individual objects from the class, each object is automatically equipped with the general behavior;

* you can then give each object whatever unique traits you desire

* Making an object from a class is called instantiation, and you work with instances of a class.

```python
❶ class Dog:
    """A simple attempt to model a dog."""

❷     def __init__(self, name, age):
        """Initialize name and age attributes."""
❸         self.name = name
        self.age = age

❹     def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

- Variables that are accessible through instances like this are called attributes.

## Exercise o

```
Try It Yourself
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.

Create several instances representing different users, and call both methods for each user.

```

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name)
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


my_title = "helo my friend"
print(my_title.title())
```

- You can change an attribute’s value in three ways:

1. you can change the value directly through an instance,

```python
class Car:
    --snip--

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

```

2. set the value through a method, or

```python
class Car:
    --snip--
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
❶         if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
❷             print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

❶ my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

3. increment the value (add a certain amount to it) through a method.

```python
class Car:
    --snip--

    def update_odometer(self, mileage):
        --snip--

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

❶ my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

❷ my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

```

## Inheritance

- . When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class.

- It’s also free to define new attributes and methods of its own.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


# my_new_car = Car("audi", "a4", 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
```

### Inheritance: Overriding Methods from the Parent Class

```python
class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
```

### Instances As Attributes: COMPOSITION

- When modeling something from the real world in code, you may find that you’re adding more and more detail to a class.
- You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy.
- In these situations, you might recognize that part of one class can be written as a separate class.
- You can break your large class into smaller classes that work together; this approach is called composition.

```python
class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

❶     def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

❷     def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
❸         self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

```

- As you begin to model more complicated things like electric cars, you’ll wrestle with interesting questions. Is the range of an electric car a property of the battery or of the car?

- You’re thinking not about Python, but about how to represent the real world in code. When you reach this point, you’ll realize there are often no right or wrong approaches to modeling real-world situations.

- If your code is working as you want it to, you’re doing well! Don’t be discouraged if you find you’re ripping apart your classes and rewriting them several times using different approaches. In the quest to write accurate, efficient code, everyone goes through this process.

## Exercise

```
Try It Yourself
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

```

```python
# my example
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if not self.battery_size == 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


# my_new_car = Car("audi", "a4", 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

```

```python
# gemini example
class User:
    """A simple model of a user profile."""
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f" - Name: {self.first_name} {self.last_name}")
        print(f" - Age: {self.age}")
        print(f" - Location: {self.country}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """A class to store an admin's privileges."""
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


class Admin(User):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name, age, country):
        # Initialize attributes from the parent class
        super().__init__(first_name, last_name, age, country)

        # Create a Privileges instance as an attribute (Composition)
        self.privileges = Privileges()


# --- Testing the Classes ---

# 1. Create the Admin instance
admin_alex = Admin("Alex", "Arkhipov", 31, "Russia")

# 2. Describe the user (Method inherited from User)
admin_alex.describe_user()

# 3. Show privileges (Method called from the Privileges instance inside Admin)
admin_alex.privileges.show_privileges()
```

## Improting Classes

- As you add more functionality to your classes, your files can get long, even when you use inheritance and composition properly.
- In keeping with the overall philosophy of Python, you’ll want to keep your files as uncluttered as possible.
- To help, Python lets you store classes in modules and then import the classes you need into your main program.

```python
"""A class that can be used to represent a car."""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

- The import statement ❶ tells Python to open the car module and import the class Car. Now we can use the Car class as if it were defined in this file

```python
# my_car.py
from car import Car

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

```

```python
from car import ElectricCar

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
```

- importing multiple classes from a module

```python
from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

- importing an entire modle

```python
# from car import Car, ElectricCar
import car

my_mustang = car.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

```

```python
# not recommended due to naming conflicts, errors
from module_name import *
```

- importing module into a module

* Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module

* Whena calss in one module depends on a class in another module, you can import the required class into the first module

```python
# car.py
"""A class that can be used to represent a car."""

class Car:
    --snip--
```

```python
# electric_carp.py
"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    --snip--

class ElectricCar(Car):
    --snip--
```

```python
# my_cars.py
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

- using aliases

```python
from electric_car import ElectricCar as EC
my_leaf = EC('nissan', 'leaf', 2024)

# you can also give a module an alias
import electric_car as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
```

- When you’re starting out, keep your code structure simple. Try doing everything in one file and moving your classes to separate modules once everything is working.
- If you like how modules and files interact, try storing your classes in modules when you start a project. Find an approach that lets you write code that works, and go from there.

## Exercise

```
Try It Yourself
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
```

## The Python Standard Library

- The Python standard library is a set of modules included with every Python installation

```python
>>> from random import randint
# generate a random number between 1 and 6
>>> randint(1, 6)
3
```

```python
>>> from random import choice
>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
# This function takes in a list or tuple and returns a randomly chosen element
>>> first_up = choice(players)
>>> first_up
'florence'
```

- You can also download modules from external sources -> PART 2

## Exercise

```
Try It Yourself
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.

9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.

9-16. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. Go to https://pymotw.com and look at the table of contents. Find a module that looks interesting to you and read about it, perhaps starting with the random module.
```

## Styling Classes

- Class names should be written in CamelCase. To do this, capitalize the first letter of each word in the name, and don’t use underscores.

- Instance and module names should be written in lowercase, with underscores between words.

- Every class should have a docstring immediately following the class definition.
- The docstring should be a brief description of what the class does, and you should follow the same formatting conventions you used for writing docstrings in functions.

* Each module should also have a docstring describing what the classes in a module can be used for.

* You can use blank lines to organize code, but don’t use them excessively. Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.

* If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote.

* In programs with multiple import statements, this convention makes it easier to see where the different modules used in the program come from.

```
Good—this is exactly the level you should focus on.
Here’s a tight, no-fluff checklist you can actually apply daily.

🧠 Core Naming Rules
Classes → CamelCase
TimeTracker, UserSession
Functions / variables → snake_case
get_user_data, active_sessions
Constants → UPPER_CASE
MAX_RETRIES
🧱 Structure Rules
Files (modules)
one clear responsibility per file
avoid “utils.py” dumping ground
Classes
class TimeTracker:
    """Track user work sessions."""
always add docstring
keep classes focused (not 1000 lines)
Functions
do one thing
≤ ~20–30 lines ideally
name describes behavior

Bad:

def process():

Good:

def calculate_daily_hours():
📏 Formatting Rules
Indentation
4 spaces (no tabs)
Line length
≤ 80–88 chars
break long lines manually
Blank lines
2 lines → between top-level classes/functions
1 line → between class methods
0 lines → inside tight logic blocks
📦 Imports (VERY IMPORTANT)

Order:

# standard library
import os
import datetime

# third-party
from fastapi import FastAPI

# local
from app.services.tracker import TimeTracker

👉 always group + separate

🔁 Loops & Data
prefer .items() for dicts
avoid repeated lookups
avoid deep nesting
🧠 Control Flow
Prefer early returns

Bad:

if user:
    if user.active:
        do_something()

Good:

if not user:
    return
if not user.active:
    return

do_something()
⚠️ Avoid “JS habits”

❌ chaining everything
❌ overly compact code
❌ unnecessary abstractions

🔥 Strings
use f-strings
f"User: {name}"
split long strings with parentheses
🧪 Error handling

Be explicit:

if data is None:
    raise ValueError("Missing data")
🧠 Comments
explain why, not what

Bad:

# increment i
i += 1

Good:

# skip invalid entries
🧩 Complexity
avoid functions with:
too many parameters (>4–5)
deep nesting
unclear flow
⚡ FastAPI-specific (for your job)
keep routes thin
move logic to services

Bad:

@app.get("/users")
def get_users():
    # 50 lines of logic

Good:

@app.get("/users")
def get_users():
    return user_service.get_all_users()
💥 Golden Rules (memorize these)
Readable > clever
Flat > nested
Explicit > implicit
Simple > abstract
One clear way > many options
🧠 Quick self-check before saving

Ask:

Can someone understand this in 5 seconds?
Is anything unnecessarily clever?
Can I simplify one thing?

That’s enough to write clean, professional Python at your job.

If you want next, I can give you:

👉 a “bad vs good Python file” (real FastAPI example)
→ this locks everything in instantly
```

## SUMMARY CHAPTER 9

Summary
In this chapter, you learned how to write your own classes. You learned how to store information in a class using attributes and how to write methods that give your classes the behavior they need. You learned to write **init**() methods that create instances from your classes with exactly the attributes you want. You saw how to modify the attributes of an instance directly and through methods. You learned that inheritance can simplify the creation of classes that are related to each other, and you learned to use instances of one class as attributes in another class to keep each class simple.

You saw how storing classes in modules and importing classes you need into the files where they’ll be used can keep your projects organized. You started learning about the Python standard library, and you saw an example based on the random module. Finally, you learned to style your classes using Python conventions.

In Chapter 10, you’ll learn to work with files so you can save the work you’ve done in a program and the work you’ve allowed users to do.

You’ll also learn about exceptions, a special Python class designed to help you respond to errors when they arise.

# CHAPTER 10 - FILES and EXCEPTIONS

1. Reading from a File
2. Writing to a File
3. Exceptions
4. Storing Data
5. Summary

- Exceptions, which are special objects Python creates to manage errors that arise while a program is running.
- the json module, which allows you to save user data so it isn’t lost when your program stops running.

- bad data, malicious attempts to break programs

## Reading from a File

- When you want to work with the information in a text file, the first step is to read the file into memory.

- You can then work through all of the file’s contents at once or work through the contents line by line.

```txt
# pi_digits.txx
3.1415926535
  8979323846
  2643383279
```

```python
from pathlib import Path

# For example, you can check that the file exists before working with it, read the file’s contents, or write new data to the file.
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

# path = Path('chapter10/pi_digits.txt') - depends on where the terminal is
```

- To work with the contents of a file, we need to tell Python the path to the file.
- A path is the exact location of a file or folder on a system.
- Python provides a module called pathlib that makes it easier to work with files and directories, no matter which operating system you or your program’s users are working with.
- A module that provides specific functionality like this is often called a library, hence the name pathlib

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
```

```python
# method chaining
contents = path.read_text().rstrip()
```

```python
# relative path
path = Path('text_files/filename.txt')

# absolute path
path = Path('/home/eric/data_files/text_files/filename.txt')

```

- splitlines()

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
```

```
# containts whitespace that was on th left side of the digits in each line

3.1415926535  8979323846  2643383279
36
```

```python
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

# 3.141592653589793238462643383279
# 32
```

```python
# py_string.py
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# 3.14159265358979323846264338327950288419716939937510...
# 1000002
```

```python
--snip--
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

```

## EXERCISE

```
Try It Yourself
10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote two times: print the contents once by reading in the entire file, and once by storing the lines in a list and then looping over each line.

10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:

>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

10-3. Simpler Code: The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works. You can skip the temporary variable and loop directly over the list that splitlines() returns:

for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section, to make them more concise.
```

- use replace() method

```python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

```python
from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

# print(contents)

for line in contents.splitlines():
    line = line.replace("Python", "Java")
    print(line)
```

### COOL - no temporary variable

```python
for line in contents.splitlines():
```

```python
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()


pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
```

## WRITING TO A FILE

```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")
```

- Note
  Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

- The write_text() method does a few things behind the scenes. If the file that path points to doesn’t exist, it creates that file.
- Also, after writing the string to the file, it makes sure the file is closed properly. Files that aren’t closed properly can lead to missing or corrupted data.

* writing multiple lines

```python
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
```

- Be careful when calling write_text() on a path object. If the file already exists, write_text() will erase the current contents of the file and write new contents to the file.
- Later in this chapter, you’ll learn to check whether a file exists using pathlib.

## EXERCISE

```
10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
```

## Exceptions

- Python uses special objects called exceptions to manage errors that arise during a program’s execution.
- Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object.
- If you write code that handles the exception, the program will continue running.
- If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.

- Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see
  friendly error messages that you’ve written.

```python
try:
    print(5/0)
    # Exception object
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- It’s bad that the program crashed, but it’s also not a good idea to let users see tracebacks.
- Nontechnical users will be confused by them, and in a malicious setting, attackers will learn more than you want them to. For example, they’ll know the name of your program file, and they’ll see a part of your code that isn’t working properly.
- A skilled attacker can sometimes use this information to determine which kind of attacks to use against your code.

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")

    else:
        print(answer)

```

- handling missing file exception

```python
from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')
```

```python
Traceback (most recent call last):
❶   File "alice.py", line 4, in <module>
❷     contents = path.read_text(encoding='utf-8')
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/.../pathlib.py", line 1056, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/.../pathlib.py", line 1042, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
❸ FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

- It’s often best to start at the very end of the traceback. On the last line, we can see that a FileNotFoundError exception was raised ❸. This is important because it tells us what kind of exception to use in the except block that we’ll write.

- Looking back near the beginning of the traceback ❶, we can see that the error occurred at line 4 in the file alice.py. The next line shows the line of code that caused the error ❷. The rest of the traceback shows some code from the libraries that are involved in opening and reading from files. You don’t usually need to read through or understand all of these lines in a traceback.

- To handle the error that’s being raised, the try block will begin with the line that was identified as problematic in the traceback. In our example, this is the line that contains read_text():

```python
from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

```

- how exception handling can help when you’re working with more than one file.

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
❶     words = contents.split()
❷     num_words = len(words)
    print(f"The file {path} has about {num_words} words.")


print("abc".split())
# ['abc']
```

- We take the string contents, which now contains the entire text of Alice in Wonderland as one long string, and use split() to produce a list of all the words in the book ❶. Using len() on this list ❷ gives us a good approximation of the number of words in the original text.

* working with multiple files

```
word_count.py
```

```python
from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path("alice.txt")
count_words(path)


```

- We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it’s able to find.

```python
from pathlib import Path

def count_words(filename):
    --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
        'little_women.txt']
for filename in filenames:
❶   path = Path(filename)
    count_words(path)

```

- FAILING SILIENTLY

```python
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--
```

- Deciding which error to report:

- How do you know when to report an error to your users and when to let your program fail silently

- Giving users information they aren’t looking for can decrease the usability of your program.

- Python’s error-handling structures give you fine-grained control over how much to share with users when things go wrong; it’s up to you to decide how much information to share

- Well-written, properly tested code is not very prone to internal errors, such as syntax or logical errors.

- But every time your program depends on something external such as user input, the existence of a file, or the availability of a network connection, there is a possibility of an exception being raised.

- A little experience will help you know where to include exception-handling blocks in your program and how much to report to users about errors that arise.

## EXERCISE

```python
try:
    # 1. Input and conversion
    number_1 = int(input("Give first number: "))
    number_2 = int(input("Give second number: "))

    # 2. Calculation
    result = number_1 / number_2
    print(f"The result is: {result}")

except ValueError:
    # This catches things like 'hello' or '10.5'
    print("Error: Please enter whole numbers only.")

except ZeroDivisionError:
    # This catches when the second number is 0
    print("Error: You cannot divide by zero!")

except Exception as e:
    # Optional: Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
```

```python
while True:
    try:
        # Get inputs
        number_1 = int(input("\nGive first number (or '0' to exit): "))
        number_2 = int(input("Give second number: "))

        # Attempt calculation
        result = number_1 / number_2

    except ValueError:
        print("--> Error: Please enter whole numbers only.")
        continue # Restarts the loop

    except ZeroDivisionError:
        print("--> Error: You cannot divide by zero.")
        continue # Restarts the loop

    else:
        # This block runs ONLY if the try block succeeded
        print(f"The result is: {result}")
        break # Exit the loop successfully
```

## PROBLEM WITH MY CODE !!!!

```python
from pathlib import Path

cats_path = Path("cats.txt")
dogs_path = Path("dogs.txt")

files = [cats_path, dogs_path]

for file in files:

    try:
        file = file.read_text()
        for line in file.splitlines():
            print(line)
    except FileNotFoundError:
        # print(f"The file {file} is missing.")
        pass
```

- By assigning the content of the file to the variable name file, you overwrite the Path object. If a FileNotFoundError occurs, the variable file might not refer to what you think it does, or your error message (if you uncomment it) might try to print the entire contents of a previous file instead of the missing filename.

- Instead of reading the whole text and splitting it (which can be memory-intensive for huge files), you can use open() within pathlib to read line-by-line.

```python
from pathlib import Path

files = [Path("cats.txt"), Path("dogs.txt")]

for file_path in files:
    try:
        # Use .open() to read line by line efficiently
        with file_path.open(encoding='utf-8') as f:
            print(f"\n--- Contents of {file_path.name} ---")
            for line in f:
                print(line.strip())

    except FileNotFoundError:
        # Using 'pass' is fine for "silent" failures as per exercise 10-9
        pass
```

## ANOTHER PROBLEM

```python
from pathlib import Path

path = Path("alice.txt")

try:
    contents = path.read_text()
    amount = 0
    for line in contents.splitlines():
        amount += line.lower().count("the ")
    print(f"'the' appears {amount} times")

except FileNotFoundError:
    print(f"The file {path} not found")

```

- better solution for efficiency: just use count()!

```python
from pathlib import Path

path = Path("alice.txt")

try:
    contents = path.read_text(encoding='utf-8')

    # Split into individual words
    words = contents.lower().split()

    # Use count() on the list to find exact matches only
    amount = words.count('the')

    print(f"The word 'the' appears {amount} times.")

except FileNotFoundError:
    print(f"The file {path} was not found.")

```

- better?

```python
from pathlib import Path

path = Path("alice.txt")

try:
    contents = path.read_text()

    count = contents.lower().count("the ")
    print(f"'the' appears {count} times")

    # print(f"'the' appears {len(contents.lower().count("the "))} times")

except FileNotFoundError:
    print(f"The file {path} not found")

```

- idk which is better...

```python
from pathlib import Path

path = Path("alice.txt")

try:
    # Adding encoding='utf-8' is a great habit for reading books/files
    contents = path.read_text(encoding='utf-8')

    # 1. Lowercase everything
    # 2. Split into a list of individual words
    words = contents.lower().split()

    # 3. Count exact matches in that list
    count = words.count("the")

    print(f"The word 'the' appears {count} times.")

except FileNotFoundError:
    print(f"The file {path} was not found.")

```

## STORING DATA (json module)

- you’ll store the information users provide in data structures such as lists and dictionaries.

- The json module allows you to convert simple Python data structures into JSON-formatted strings, and then load the data from that file the next time the program runs.

- You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn.

- The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python.

```python
# store set of numbers
# The json.dumps() function takes one argument: a piece of data that should be converted to the JSON format.
# The function returns a string, which we can then write to a data file
json.dumps()
# read
json.loads()
```

```python
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
# [2, 3, 5, 7, 11, 13]
```

```python
from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
# This function takes in a JSON-formatted string and returns a Python object (in this case, a list), which we assign to numbers
numbers = json.loads(contents)

print(numbers)

```

- saving and reading user-generated data

```python
from pathlib import Path
import json

username = input("What is your name? ")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")
```

```python
from pathlib import Path
import json

path = Path("username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")

```

- combined

```python
from pathlib import Path
import json

path = Path("username.json")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
```

### Refactoring

- Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs.
- This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.

* . This file is a little cleaner, but the function greet_user() is doing more than just greeting the user—it’s also retrieving a stored username if one exists and prompting for a new username if one doesn’t.

```python
from pathlib import Path
import json

def greet_user():
❶     """Greet the user by name."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()



```

- Let’s refactor greet_user() so it’s not doing so many different tasks. We’ll start by moving the code for retrieving a stored username to a separate function:

```python
from pathlib import Path
import json

def get_stored_username(path):
❶     """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
❷         return None

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
❸     if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

- We should factor one more block of code out of greet_user(). If the username doesn’t exist, we should move the code that prompts for a new username to a function dedicated to that purpose:

```python
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    --snip--

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
❶     username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
❷         username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

```

## Exercise

```
Try It Yourself
10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”

10-12. Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.

10-14. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.

Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.

```

```python
import json
from pathlib import Path

# 1. Setup the path once at the top
path = Path("number.json")

while True:
    try:
        # 2. Get the input and force it to be an integer
        number = int(input("What is your favorite number? "))
    except ValueError:
        # 3. Handle text-entry errors
        print("That's not a number! Please try again.")
    else:
        # 4. If input is valid, save it and exit the loop
        contents = json.dumps(number)
        path.write_text(contents)
        print(f"Got it! I've saved {number} to {path}.")
        break
```

```python
import json
from pathlib import Path

path = Path("number.json")

try:
    # 1. Attempt to read the file
    contents = path.read_text()
except FileNotFoundError:
    # 2. Handle the case where the file hasn't been created yet
    print(f"Sorry, I couldn't find {path}. Run the writer program first!")
else:
    # 3. Convert JSON string back to a Python integer
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")

```

```python
import json
from pathlib import Path

path = Path("number.json")

if path.exists():
    # If it exists, just read and show it
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I remember! Your favorite number is {number}.")
else:
    # If it doesn't exist, we need to get it (the risky part)
    try:
        number = int(input("I don't know your favorite number. What is it? "))
    except ValueError:
        print("Sorry, I need an actual number (digits), not text.")
    else:
        # This only runs if the input was a valid integer
        contents = json.dumps(number)
        path.write_text(contents)
        print(f"Thanks! I'll remember {number} for next time.")

```

- my solution

```python
import json
from pathlib import Path


path = Path("number.json")


def greet_user(contents):
    user_info = json.loads(contents)
    print(f"Welcome Back, {user_info['name']}")


def register_new_user():
    name = input("Give me a name: ")
    number = int(input("Give me a number: "))
    age = int(input("Give me a your age: "))

    user_info = {"name": name, "number": number, "age": age}

    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"A user with the following info {contents} has been written to a file!")


try:
    if path.exists():

        contents = path.read_text()
        username = json.loads(contents)["name"]

        verification = input(f"Is your name {username} (y/n)? ")
        if verification.lower() == "n":
            register_new_user()
        else:
            greet_user(contents)

    else:
        register_new_user()


except ValueError:
    print("Please, provide a number, not a string!")

```

- gpt solution

```python

import json
from pathlib import Path

path = Path("number.json")

def greet_user(user_info):
    """Greets the user using the dictionary already loaded."""
    print(f"Welcome Back, {user_info['name']}!")
    print(f"I remember your favorite number is {user_info['number']}.")

def register_new_user():
    """Prompts for data and saves it to the path."""
    try:
        name = input("Give me a name: ")
        number = int(input("Give me a number: "))
        age = int(input("Give me your age: "))

        user_info = {"name": name, "number": number, "age": age}
        path.write_text(json.dumps(user_info))
        print(f"Registration complete for {name}!")
    except ValueError:
        print("Error: Age and Number must be numerical.")

# --- Main Logic ---
if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents) # Load it ONCE here

    verify = input(f"Are you {user_info['name']}? (y/n): ").lower()

    if verify == 'y':
        greet_user(user_info) # Pass the dictionary directly
    else:
        register_new_user()
else:
    register_new_user()
```

## SUMMARY CHAPTER 10

In this chapter, you learned how to work with files.

You learned to read the entire contents of a file, and then work through the contents one line at a time if you need to.

You learned to write as much text as you want to a file.

You also read about exceptions and how to handle the exceptions you’re likely to see in your programs.

Finally, you learned how to store Python data structures so you can save information your users provide, preventing them from having to start over each time they run a program.

In Chapter 11, you’ll learn efficient ways to test your code. This will help you trust that the code you develop is correct, and it will help you identify bugs that are introduced as you continue to build on the programs you’ve written.

- STRANGE ELSE HERE. WHY?

```python
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")

```

```python
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")

```

```python
from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
        # pass
    else:
        print(contents)
```

```python
from pathlib import Path

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')

```

```python
user_dictionary.py
from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    game = input("What's your favorite game? ")
    animal = input("What's your favorite animal? ")

    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

greet_user()

```

```python
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()


# cleaner version
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    #   Prompt for a new username.
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")
```

# CHAPTER 11 - TESTING YOUR CODE

- Testing proves that your code works as it’s supposed to in response to all the kinds of input it’s designed to receive.

- You’ll also be able to test new code as you add it, to make sure your changes don’t break your program’s existing behavior

- The pytest library is a collection of tools that will help you write your first tests quickly and simply, while supporting your tests as they grow in complexity along with your projects

- A third-party package is a library that’s developed outside the core Python language.

```python
$ python -m pip install --upgrade pip
❶ Requirement already satisfied: pip in /.../python3.11/site-packages (22.0.4)
--snip--
❷ Successfully installed pip-22.1.2
```

```python
python -m pip install --upgrade package_name
```

- GPT

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip


pipx install <appname>
sudo apt install python3-xyz
```

## GPT SOLUTION

You’ve run into a **modern Linux / Debian (including Ubuntu, etc.) behavior change**—and the book you’re using is slightly outdated for that setup.

Let’s cut through the confusion and give you the **correct way to proceed** 👇

---

## 🚫 Why your book instructions fail

The book says:

```bash
python -m pip install --upgrade pip
```

But your system Python is **externally managed (PEP 668)**, so:

- ❌ You cannot upgrade pip globally
- ❌ You cannot install packages with `--user` either (often blocked too)

👉 This is intentional: your OS wants to protect itself.

---

## ✅ The correct modern workflow (use this for your course)

### 🔹 Step 1 — Create a virtual environment

```bash
python3 -m venv venv
```

If this fails:

```bash
sudo apt install python3-venv python3-full
```

---

### 🔹 Step 2 — Activate it

```bash
source venv/bin/activate
```

Now your terminal should show something like:

```
(venv) user@machine:~$
```

---

### 🔹 Step 3 — Now update pip (THIS will work)

```bash
python -m pip install --upgrade pip
```

✔️ This works because you're no longer touching the system Python.

---

### 🔹 Step 4 — Install packages (pytest etc.)

```bash
pip install pytest
```

✔️ No `--user` needed
✔️ No errors
✔️ Clean environment

---

## 🧠 Key mindset shift (important for you as a dev)

Your book assumes:

> “Install everything globally”

Modern Python says:

> “Never touch system Python. Always use virtual environments.”

This is actually **what real developers do** (especially in backend / full-stack roles you’re targeting).

---

## 🔥 Recommended workflow for your Python Crash Course

For every project/chapter:

```bash
mkdir python-crash-course
cd python-crash-course

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
```

Then install whatever the chapter needs.

---

## ⚠️ What NOT to do

Avoid this:

```bash
python3 -m pip install --break-system-packages
```

👉 It works, but:

- can break your OS Python
- causes weird bugs later
- bad practice for professional development

---

## 🧩 Why `pip` sometimes “works” anyway

Earlier you noticed:

> “but pip / pip3 works?”

That’s usually because:

- it might point to a **different Python install**
- or just hasn’t tried installing anything yet

👉 Don’t rely on that — it’s inconsistent.

---

## 🚀 Bottom line (what you should do)

Forget the book’s global install approach.

👉 Use this every time:

```bash
python3 -m venv venv
source venv/bin/activate
pip install <package>
```

---

If you want, I can help you set up a **clean Python + JS workflow** aligned with your HEMS thesis + job goal (so Python doesn’t distract but still helps you).

```python
mkdir python-crash-course
cd python-crash-course

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

```python
$ python -m pip install --user pytest
Collecting pytest
  --snip--
Successfully installed attrs-21.4.0 iniconfig-1.1.1 ...pytest-7.x.x

```

- for me

```python
python -m pip install pytest
```

## Testing a Function

```python
# name_function.py
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

```python
# names.py
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```

- pytest provides an efficient way to automate the testing of a function’s output.

- A unit test verifies that one specific aspect of a function’s behavior is correct.
- A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.

- A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations.

- A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function.

```python
# test_name_function.py
from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"

```

- When we ask pytest to run the tests we’ve written, it will look for any file that begins with test\_, and run all of the tests it finds in that file.

```python
$ pytest
========================= test session starts =========================
❶ platform darwin -- Python 3.x.x, pytest-7.x.x, pluggy-1.x.x
❷ rootdir: /.../python_work/chapter_11
❸ collected 1 item

❹ test_name_function.py .                                          [100%]
========================== 1 passed in 0.00s ==========================

```

- failing test

```python
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

```

```python
$ pytest
========================= test session starts =========================
--snip--
❶ test_name_function.py F                                          [100%]
❷ ============================== FAILURES ===============================
❸ ________________________ test_first_last_name _________________________
    def test_first_last_name():
        """Do names like 'Janis Joplin' work?"""
❹ >       formatted_name = get_formatted_name('janis', 'joplin')
❺ E       TypeError: get_formatted_name() missing 1 required positional
            argument: 'last'

test_name_function.py:5: TypeError
======================= short test summary info =======================
FAILED test_name_function.py::test_first_last_name - TypeError:
    get_formatted_name() missing 1 required positional argument: 'last'
========================== 1 failed in 0.04s ==========================
```

- let's fix the code, not the test

```python
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

- adding another test

```python
def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"
```

## Exercise

```
Try It Yourself
11-1. City, Country: Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a module called city_functions.py, and save this file in a new folder so pytest won’t try to run the tests we’ve already written.

Create a file called test_cities.py that tests the function you just wrote. Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. Run the test, and make sure test_city_country() passes.

11-2. Population: Modify your function so it requires a third parameter, population. It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. Run the test again, and make sure test_city_country() fails this time.

Modify the function so the population parameter is optional. Run the test, and make sure test_city_country() passes again.

Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'. Run the tests one more time, and make sure this new test passes.
```

## COMMON TEST CASES

### Table 11-1: Commonly Used Assertion Statements in Tests

| Assertion                    | Claim                                    |
| ---------------------------- | ---------------------------------------- |
| `assert a == b`              | Assert that two values are equal.        |
| `assert a != b`              | Assert that two values are not equal.    |
| `assert a`                   | Assert that `a` evaluates to True.       |
| `assert not a`               | Assert that `a` evaluates to False.      |
| `assert element in list`     | Assert that an element is in a list.     |
| `assert element not in list` | Assert that an element is not in a list. |

---

### Common Assertion Statements for Python, FastAPI, and Streamlit Testing

| Assertion                       | Typical use                     | Example                                                 |
| ------------------------------- | ------------------------------- | ------------------------------------------------------- |
| `assert a == b`                 | Check exact equality            | `assert response.status_code == 200`                    |
| `assert a != b`                 | Check values differ             | `assert data["status"] != "error"`                      |
| `assert a`                      | Check truthy value              | `assert response.ok`                                    |
| `assert not a`                  | Check falsy value               | `assert not errors`                                     |
| `assert x is None`              | Check missing value             | `assert result is None`                                 |
| `assert x is not None`          | Check value exists              | `assert user is not None`                               |
| `assert x is True`              | Check exact boolean `True`      | `assert payload["success"] is True`                     |
| `assert x is False`             | Check exact boolean `False`     | `assert payload["cached"] is False`                     |
| `assert item in collection`     | Check membership                | `assert "email" in response.json()`                     |
| `assert item not in collection` | Check absence                   | `assert "password" not in response.json()`              |
| `assert key in dict`            | Check JSON field exists         | `assert "id" in data`                                   |
| `assert key not in dict`        | Check field is omitted          | `assert "traceback" not in data`                        |
| `assert len(x) == n`            | Check collection size           | `assert len(data["items"]) == 3`                        |
| `assert len(x) > 0`             | Check collection is not empty   | `assert len(users) > 0`                                 |
| `assert isinstance(x, T)`       | Check type                      | `assert isinstance(data, dict)`                         |
| `assert all(...)`               | Check all items satisfy a rule  | `assert all("id" in item for item in items)`            |
| `assert any(...)`               | Check at least one item matches | `assert any(user["role"] == "admin" for user in users)` |
| `assert text in string`         | Check message/content           | `assert "Welcome" in page_text`                         |
| `assert text not in string`     | Check sensitive text absent     | `assert "Internal Server Error" not in response.text`   |
| `assert x > y`                  | Check numeric threshold         | `assert response_time_ms > 0`                           |
| `assert x < y`                  | Check upper bound               | `assert response.elapsed.total_seconds() < 1`           |
| `assert x >= y`                 | Check minimum acceptable value  | `assert progress >= 0`                                  |
| `assert x <= y`                 | Check maximum acceptable value  | `assert score <= 100`                                   |

### Common API Assertions (FastAPI)

| Assertion                                                                | Typical use                 | Example                                                                  |
| ------------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------ |
| `assert response.status_code == 200`                                     | Successful GET request      | `assert response.status_code == 200`                                     |
| `assert response.status_code == 201`                                     | Resource created            | `assert response.status_code == 201`                                     |
| `assert response.status_code == 204`                                     | Successful empty response   | `assert response.status_code == 204`                                     |
| `assert response.status_code == 400`                                     | Bad request validation case | `assert response.status_code == 400`                                     |
| `assert response.status_code == 401`                                     | Unauthorized request        | `assert response.status_code == 401`                                     |
| `assert response.status_code == 403`                                     | Forbidden request           | `assert response.status_code == 403`                                     |
| `assert response.status_code == 404`                                     | Missing route/resource      | `assert response.status_code == 404`                                     |
| `assert response.status_code == 422`                                     | FastAPI validation error    | `assert response.status_code == 422`                                     |
| `assert response.headers["content-type"].startswith("application/json")` | JSON response check         | `assert response.headers["content-type"].startswith("application/json")` |
| `assert response.json()["name"] == "Alice"`                              | Check JSON field value      | `assert response.json()["name"] == "Alice"`                              |
| `assert "detail" in response.json()`                                     | Check error payload exists  | `assert "detail" in response.json()`                                     |

### Common JSON / Dict Assertions

| Assertion                                   | Typical use           | Example                                     |
| ------------------------------------------- | --------------------- | ------------------------------------------- |
| `assert data["id"] == 1`                    | Exact field value     | `assert data["id"] == 1`                    |
| `assert data.get("email") == "a@b.com"`     | Safe lookup           | `assert data.get("email") == "a@b.com"`     |
| `assert set(data.keys()) >= {"id", "name"}` | Required keys present | `assert set(data.keys()) >= {"id", "name"}` |
| `assert data["items"] == []`                | Empty list response   | `assert data["items"] == []`                |
| `assert isinstance(data["items"], list)`    | Field type check      | `assert isinstance(data["items"], list)`    |

### Common Exception Assertions (`pytest`)

| Assertion                                | Typical use                       | Example                                            |
| ---------------------------------------- | --------------------------------- | -------------------------------------------------- |
| `with pytest.raises(ExceptionType): ...` | Check expected exception          | `with pytest.raises(ValueError): parse_age("abc")` |
| `with pytest.raises(HTTPException): ...` | FastAPI service/unit logic errors | `with pytest.raises(HTTPException): get_user(-1)`  |
| `assert "message" in str(exc.value)`     | Check exception message           | `assert "invalid input" in str(exc.value)`         |

### Common Streamlit-Oriented Assertions

| Assertion                                  | Typical use               | Example                                    |
| ------------------------------------------ | ------------------------- | ------------------------------------------ |
| `assert result_df is not None`             | Data loaded for display   | `assert result_df is not None`             |
| `assert not result_df.empty`               | DataFrame has rows        | `assert not result_df.empty`               |
| `assert "total_cost" in result_df.columns` | Expected column exists    | `assert "total_cost" in result_df.columns` |
| `assert result["chart_data"] is not None`  | Chart input prepared      | `assert result["chart_data"] is not None`  |
| `assert state["logged_in"] is True`        | Session-state logic works | `assert state["logged_in"] is True`        |
| `assert filtered_count <= total_count`     | Filter logic works        | `assert filtered_count <= total_count`     |

### Practical Notes

- Use `is None` / `is True` / `is False` for exact identity checks.
- Use `==` when comparing values.
- For FastAPI, the most common checks are:
  - `status_code`
  - `response.json()`
  - headers
  - validation/error payloads
- For Streamlit, you usually test:
  - helper functions
  - data transformation
  - session-state logic
  - filtering/sorting results
  - not the UI rendering itself

---

## CHEATSHEET

### FastAPI / Streamlit Testing Assertions Cheat Sheet

| Assertion                                                                | What it checks            | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------------ |
| `assert a == b`                                                          | exact equality            | `assert response.status_code == 200`                                     |
| `assert a != b`                                                          | not equal                 | `assert data["role"] != "guest"`                                         |
| `assert a`                                                               | truthy                    | `assert response.ok`                                                     |
| `assert not a`                                                           | falsy                     | `assert not errors`                                                      |
| `assert x is None`                                                       | missing value             | `assert result is None`                                                  |
| `assert x is not None`                                                   | value exists              | `assert user is not None`                                                |
| `assert key in dict`                                                     | field exists              | `assert "id" in data`                                                    |
| `assert key not in dict`                                                 | field absent              | `assert "password" not in data`                                          |
| `assert item in collection`                                              | membership                | `assert "email" in errors`                                               |
| `assert len(x) == n`                                                     | exact size                | `assert len(items) == 5`                                                 |
| `assert len(x) > 0`                                                      | non-empty                 | `assert len(rows) > 0`                                                   |
| `assert isinstance(x, T)`                                                | correct type              | `assert isinstance(data, dict)`                                          |
| `assert all(...)`                                                        | all items match           | `assert all("id" in item for item in items)`                             |
| `assert any(...)`                                                        | at least one matches      | `assert any(u["active"] for u in users)`                                 |
| `assert text in string`                                                  | contains text             | `assert "Welcome" in page_text`                                          |
| `assert response.status_code == 200`                                     | successful GET            | `assert response.status_code == 200`                                     |
| `assert response.status_code == 201`                                     | created resource          | `assert response.status_code == 201`                                     |
| `assert response.status_code == 404`                                     | missing resource          | `assert response.status_code == 404`                                     |
| `assert response.status_code == 422`                                     | FastAPI validation error  | `assert response.status_code == 422`                                     |
| `assert response.headers["content-type"].startswith("application/json")` | JSON response             | `assert response.headers["content-type"].startswith("application/json")` |
| `assert response.json()["name"] == "Alice"`                              | JSON value check          | `assert response.json()["name"] == "Alice"`                              |
| `with pytest.raises(ValueError): ...`                                    | expected exception        | `with pytest.raises(ValueError): parse_age("abc")`                       |
| `assert not df.empty`                                                    | DataFrame has data        | `assert not df.empty`                                                    |
| `assert "col" in df.columns`                                             | expected DataFrame column | `assert "total_cost" in df.columns`                                      |

## TESTING A CLASS

- If you have passing tests for a class you’re working on, you can be confident that improvements you make to the class won’t accidentally break its current behavior.

```python
# survey.py
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

```

```python
# language_survey.py
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()

```

- This class works for a simple anonymous survey, but say we want to improve AnonymousSurvey and the module it’s in, survey. We could allow each user to enter more than one response, we could write a method to list only unique responses and to report how many times each response was given, or we could even write another class to manage non-anonymous surveys.

- To ensure we don’t break existing behavior as we develop this module, we can write tests for the class.

```python
# test_survey.py
from survey import AnonymousSurvey


def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses


```

- now we tes more responses

```python
from survey import AnonymousSurvey

def test_store_single_response():
    --snip--

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
❶     responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

❷     for response in responses:
        assert response in language_survey.responses
```

- This works perfectly.
- However, these tests are a bit repetitive, so we’ll use another feature of pytest to make them more efficient.

## Using FIXTURES

- In test_survey.py, we created a new instance of AnonymousSurvey in each test function.
- This is fine in the short example we’re working with, but in a real-world project with tens or hundreds of tests, this would be problematic.

- In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test

- We create a fixture in pytest by writing a function with the decorator @pytest.fixture.

* A decorator is a directive placed just before a function definition; &&Python applies this directive to the function before it runs, to alter how the function code behaves.

* Don’t worry if this sounds complicated; you can start to use decorators from third-party packages before learning to write them yourself.

```python
import pytest
from survey import AnonymousSurvey

❶ @pytest.fixture
❷ def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

❸ def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
❹     language_survey.store_response('English')
    assert 'English' in language_survey.responses

❺ def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
❻         language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

- These tests would be particularly useful when trying to expand AnonymousSurvey to handle multiple responses for each person.

- After modifying the code to accept multiple responses, you could run these tests and make sure you haven’t affected the ability to store a single response or a series of individual responses.

* When you want to write a fixture, write a function that generates the resource that’s used by multiple test functions.

* Add the @pytest.fixture decorator to the new function, and add the name of this function as a parameter for each test function that uses this resource.

* Your tests will be shorter and easier to write and maintain from that point forward.

## EXERCISE

```
11-3. Employee: Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

Write a test file for Employee with two test functions, test_give_default_raise() and test_give_custom_raise(). Write your tests once without using a fixture, and make sure they both pass. Then write a fixture so you don’t have to create a new employee instance in each test function. Run the tests again, and make sure both tests still pass.
```

```python
class Employee:
    """A simple class to represent an employee."""

    def __init__(self, first, last, annual_salary):
        """Initialize the employee."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.annual_salary += amount
```

```python
import pytest
from employee import Employee

@pytest.fixture
def employee():
    """A fixture that provides an Employee instance for tests."""
    return Employee("Alex", "Arkhipov", 5000)

def test_give_default_raise(employee):
    """Test the default raise using the fixture."""
    employee.give_raise()
    assert employee.annual_salary == 10000

def test_give_custom_raise(employee):
    """Test the custom raise using the fixture."""
    employee.give_raise(20000)
    assert employee.annual_salary == 25000
```

## SUMMARY CHAPTER 11

In this chapter, you learned to write tests for functions and classes using tools in the pytest module.

You learned to write test functions that verify specific behaviors your functions and classes should exhibit.

You saw how fixtures can be used to efficiently create resources that can be used in multiple test functions in a test file.

Testing is an important topic that many newer programmers aren’t exposed to.

You don’t have to write tests for all the simple projects you try as a new programmer. But as soon as you start to work on projects that involve significant development effort, you should test the critical behaviors of your functions and classes.

You’ll be more confident that new work on your project won’t break the parts that work, and this will give you the freedom to make improvements to your code.

If you accidentally break existing functionality, you’ll know right away, so you can still fix the problem easily. Responding to a failed test that you ran is much easier than responding to a bug report from an unhappy user.

Other programmers will respect your projects more if you include some initial tests.

They’ll feel more comfortable experimenting with your code and be more willing to work with you on projects.

If you want to contribute to a project that other programmers are working on, you’ll be expected to show that your code passes existing tests and you’ll usually be expected to write tests for any new behavior you introduce to the project.

Play around with tests to become familiar with the process of testing your code. Write tests for the most critical behaviors of your functions and classes, but don’t aim for full coverage in early projects unless you have a specific reason to do so.
