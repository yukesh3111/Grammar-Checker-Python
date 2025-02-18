import json
import language_tool_python


def load_daily_words():
    try:
        with open("daily_words.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_daily_words(words):
    with open("daily_words.json", "w") as file:
        json.dump(words, file)


def check_grammar(sentence, daily_word):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(sentence)
    corrected_sentence = language_tool_python.utils.correct(sentence, matches)

    error_count = len(matches)

    # Improved scoring formula with stricter evaluation
    score = max(0, 100 - (error_count * 15))  # Higher penalty per error

    # Check if the daily word is used
    if daily_word.lower() not in sentence.lower():
        feedback_message = f"You did not use the word: {daily_word}. Try again!"
        score = max(0, score - 30)  # Even higher penalty for missing word
    else:
        feedback_message = "Great! You used the word correctly."

    # Ensure the corrected sentence is different from the input
    if corrected_sentence.lower() == sentence.lower():
        feedback_message += " However, your sentence may still be incorrect. Consider rephrasing."
        score = max(0, score - 20)  # Penalize unchanged incorrect sentences
    elif corrected_sentence == "":  # Handle cases where the correction fails
        corrected_sentence = sentence  # Keep the original sentence if correction is empty
        feedback_message += " The AI could not correct the sentence properly."

    errors = [f"{match.ruleIssueType}: {match.message}" for match in matches]

    if not errors:
        errors.append("No grammatical errors detected, but consider rephrasing for clarity.")

    feedback = {
        "original": sentence,
        "corrected": corrected_sentence,
        "errors": errors,
        "score": max(0, score),
        "feedback": feedback_message
    }
    return feedback


def main():
    print("Welcome to AI Grammar Checker!")
    daily_words = load_daily_words()

    if not daily_words:
        daily_words = input("Enter today's 3 new words (comma-separated): ").split(",")
        daily_words = [word.strip() for word in daily_words]  # Remove spaces
        save_daily_words(daily_words)

    print(f"Today's words: {', '.join(daily_words)}")

    for word in daily_words:
        sentence = input(f"Enter a sentence using the word '{word}': ")
        feedback = check_grammar(sentence, word)

        print("\nFeedback:")
        print(f"Corrected Sentence: {feedback['corrected']}")
        print(f"Score: {feedback['score']} / 100")
        print(feedback["feedback"])
        print("Errors:")
        for error in feedback['errors']:
            print(f"- {error}")


if __name__ == "__main__":
    main()
