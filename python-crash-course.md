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
