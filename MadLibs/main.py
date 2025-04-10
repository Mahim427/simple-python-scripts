def user_input(word_type: str) -> str:
    word: str = input(f"Enter a {word_type}: ")
    return word


print("Welcome to MadLibs!!!")
adjective1 = user_input("adjective")
adjective2 = user_input("adjective")
noun1 = user_input("noun")
noun2 = user_input("noun")
verb1 = user_input("verb (past tense)")
verb2 = user_input("verb (present tense)")

story1 = f"""
The Night I Met a {adjective1} Talking Cat

It was 2 AM when I, a {adjective2} man who had definitely not lost count of his drinks, stumbled into an alley. That’s when I saw it—a {adjective1} cat perched on a dumpster, licking a {noun1} like it owned the place.

Me: "You’re… a cat."
Cat: "And you’re a {noun2}. What’s your point?"

I {verb1} in shock. The cat proceeded to {verb2} at me for five solid minutes about "the illusion of free will." I tried to argue, but then I {verb1} again and face-planted into a pizza box.

The last thing I heard before passing out? "Pathetic. I’ve seen squirrels handle their liquor better."
"""

story2 = f"""
The Time I Bargained With a {adjective1} Cat

There I was, a {adjective2} woman holding a {noun1} like it held the secrets of the universe, when a tiny {adjective1} cat materialized on my kitchen counter.

Cat: "You reek of poor decisions."
Me (dramatic gasp): "Excuse you, I {verb1} THREE TIMES to get home ‘responsibly’!"

The cat flicked its tail and {verb2} as I tried to feed it my leftover {noun2}. Then it said, "Pathetic. I’ve seen goldfish with better survival instincts."

I demanded it grant me wisdom. It replied, "Stop texting your ex. And maybe hydrate."

I {verb1} onto the couch. The cat vanished, leaving only a single claw mark on my dignity.
"""

story_choice = input("Pick a story (1/2): ")
if story_choice == "1":
    print(story1)
else:
    print(story2)
