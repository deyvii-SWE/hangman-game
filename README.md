# Hangman Game

## How the Game Works

I created a list of 20 words, and one of them is randomly selected. Your goal is to guess the word letter by letter.

Every time you guess a letter correctly, its position in the word is revealed. However, if the letter is not present in the word, another part of the hangman appears, starting with the head and gradually completing the body.

You have 7 chances in total, and if the entire body is completed, you lose!

## About the Code

I kept the console interface inside a class. I think separating the interface into its own class is a good way to keep the code organized. This time, however, I also stored the remaining chances there.

To display the hangman, I used one-line conditional expressions to check how many chances are left and determine which parts of the body should appear. This way, you can see how many parts are still missing. But if that is too confusing, don't worry! There's also a **chances board** displayed above the hangman.

As for displaying the underlines, I kept things simple. The function iterates through every letter in the word and checks whether it is present in the **letter_used** list. If it isn't, an underscore is printed instead. Otherwise, the letter is revealed.

Here's an example:

```python
word = "fish"
letter_used = ["i"]

for letter in word: # -> Runs through every letter in the word
    if letter in letter_used: # -> If the letter is present in letter_used
        print(f" {letter.upper()}", end=" ") # -> Print the letter in uppercase
    else:
        print(" _", end=" ") # -> Otherwise, print an underscore
print()
```

The game doesn't have a PvP mode yet, but just like Rock, Paper and Scizor, I will probably add it later!
