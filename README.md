# Mad libs generator with Python
This is a very simple project with Python for beginner. It's a game, you see a story with some missed points, you should complete them and at the end, you can watch the result that you created. It's very easy to do, I built this project in 15 minute (I shouldn't be proud of myself, I know >.<) and I will explain that in this document. So you haven't to open my `main.py` file to read my comments or code, I will explain it for you! But before starting, I should say somethings...

## What's this game?
Let me tell you what is this simple game. When you run the `main.py` file, in the command line you will see a short story that with some missed points. Then, the program will ask you four words and will put them within the story and replace them with the missed points. After that, you can see the result and your (probably) fantastic story! Very easy, isn't it? I'm sure you can do that without any documentation, but I'm not busy. I will write this short document for you.

## What are the things that I used in this project?
I didn't use any special thing for doing this project. I just use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to commit my code (NOTE: I know my commits are awful, but I'm new at Git!)

## Build the project, step-by-step!
Let's build this.

### Step 1: Save story, set missed points, and show.
In the first step, you should save your story in a variable, because you have to edit and print it in another line of your code. <br>
I used [AI Story Generator](https://www.aistorygenerator.org/) to generate *A philosophical story*. I don't know why this subject, but you can build your story with your favorite subject!
Let's move on and save it in variable (NOTE: You can read these lines of code in `main.py`):
```python
story = "As the afternoon sun began to cast long shadows, Aristotle sat silently, engrossed in .... contemplation. He realized that Socrates' words had touched upon a .... truth. Happiness, ... desirable, was not the ultimate goal. It was merely a byproduct of a life dedicated to the pursuit of knowledge and .... ."
```

After that, you can show this story with `print()` function in Python:
```python
story = "As the afternoon sun began to cast long shadows, Aristotle sat silently, engrossed in .... contemplation. He realized that Socrates' words had touched upon a .... truth. Happiness, ... desirable, was not the ultimate goal. It was merely a byproduct of a life dedicated to the pursuit of knowledge and .... ."
print(story)
```

### Step 2: Getting the value of missed points and save them.
Now, our user read our story, we can get our missed points from the user with `input()` function in Python. Also, we need to serve and save them in several variables:
```python
pOne = input("missing point one: ")
pTwo = input("missing point two: ")
pThree = input("missing point three: ")
pFour = input("missing point four: ")
```

### Step 3: Put user's words and show to user.
And at the end, I replaced the missed points with user's words with *format string* and show to user the result:
```python
pOne = input("missing point one: ")
pTwo = input("missing point two: ")
pThree = input("missing point three: ")
pFour = input("missing point four: ")

story = f"As the afternoon sun began to cast long shadows, Aristotle sat silently, engrossed in {pOne} contemplation. He realized that Socrates' words had touched upon a {pTwo} truth. Happiness, {pThree} desirable, was not the ultimate goal. It was merely a byproduct of a life dedicated to the pursuit of knowledge and {pFour} ."

print(story)
```
and that's it! weel done.


I hope you enjoy. [LittleOddBoy](https://github.com/LittleOddBoy)