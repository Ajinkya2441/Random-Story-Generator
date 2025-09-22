import random

def generate_story():
    characters = ["a brave knight", "a clever detective", "an adventurous astronaut", "a curious cat", "a fearless pirate"]
    places = ["in a haunted castle", "on a distant planet", "in the bustling city", "on a mysterious island", "in a secret laboratory"]
    actions = [
        "found a hidden treasure",
        "solved a baffling mystery",
        "fought a fierce dragon",
        "discovered an ancient secret",
        "escaped from danger just in time"
    ]
    twists = [
        "but then everything changed when they met a talking parrot.",
        "only to realize it was all a dream.",
        "and became the hero of the day.",
        "but lost their way and had to ask for help.",
        "and made a surprising new friend."
    ]

    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    twist = random.choice(twists)

    story = f"Once upon a time, {character} {place} {action}, {twist}"

    return story

def main():
    print("📖 Random Story Generator\n")
    while True:
        story = generate_story()
        print(story)
        again = input("\nGenerate another story? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
