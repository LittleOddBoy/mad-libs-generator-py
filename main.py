# Let's build this.

# Save story in a variable and set missing parts of story. (this is A philosophical story, I didn't write it, AI...)
story = "As the afternoon sun began to cast long shadows, Aristotle sat silently, engrossed in .... contemplation. He realized that Socrates' words had touched upon a .... truth. Happiness, ... desirable, was not the ultimate goal. It was merely a byproduct of a life dedicated to the pursuit of knowledge and .... ."

# Show the story to user.
print(story)

# Getting the value of missing point from user.
pOne = input("missing point one: ")
pTwo = input("missing point two: ")
pThree = input("missing point three: ")
pFour = input("missing point four: ")

# And put the user words into the story
story = f"As the afternoon sun began to cast long shadows, Aristotle sat silently, engrossed in {pOne} contemplation. He realized that Socrates' words had touched upon a {pTwo} truth. Happiness, {pThree} desirable, was not the ultimate goal. It was merely a byproduct of a life dedicated to the pursuit of knowledge and {pFour} ."
