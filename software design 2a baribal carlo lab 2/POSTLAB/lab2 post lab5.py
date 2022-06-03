import random
class Doctor:
 def __init__(self, greeting_message: str, signo!_message: str, hedges: list, quali"ers: list, replacements:
dict):
Comments
Anonymous posted 3 years ago
Doesn’t work.. it said following error: File "doctor.py", line 18 def__init__(self): ^ IndentationError: expected
an indented block
Anonymous posted 3 years ago
Hi could you include indents please?
Anonymous posted 2 years ago
Any way to get the indents here?
Anonymous posted 2 years ago
Error msg says, print(d.reply(sentence)) TypeError: reply() takes 1 positional argument but 2 were given
Anonymous posted 2 years ago
Error msg says, print(d.reply(sentence)) TypeError: reply() takes 1 positional argument but 2 were given
Leave a comment

 self.greeting_message = greeting_message
 self.signo!_message = signo!_message
 self.history = []
 self.hedges = hedges
 self.quali"ers = quali"ers
 self.replacements = replacements

 def greeting(self):
 return self.greeting_message

 def farewell(self):
 return self.signo!_message

 def changePerson(self, sentence):
 """Replaces "rst person pronouns with second person pronouns."""
 words = sentence.split()
 replyWords = []

 for word in words:
 replyWords.append(self.replacements.get(word, word))

 return " ".join(replyWords)

 def reply(self, sentence):
 """Implements three di!erent reply strategies."""
 probability = random.randint(1, 5)

 if probability in (1, 2):
 # Just hedge
 answer = random.choice(self.hedges)
 elif probability == 3 and len(self.history) > 3:
 # Go back to an earlier topic
 answer = "Earlier you said that " + \
 self.changePerson(random.choice(self.history))
 else:
 # Transform the current input
 answer = random.choice(self.quali"ers) + self.changePerson(sentence)

 # Always add the current sentence to the history list
 self.history.append(sentence)

 return answer
main.py
from doctor import Doctor
def main():
 hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
 quali"ers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
 replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "you":"I",
"your":"my", "yours":"mine"}

 greeting_message = "Good morning, I hope you are well today. \nWhat can I do for you?"

 signo!_message = "Have a nice day!"

 doctor = Doctor(greeting_message, signo!_message, hedges, quali"ers, replacements)

 print(doctor.greeting())

 while True:
 sentence = input("\n>> ")
 if sentence.upper() == "QUIT":
 print(doctor.farewell())
 break

 print(doctor.reply(sentence))
# The entry point for program execution
if __name__ == "__main__":
 main()