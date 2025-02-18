# AI Grammar Checker

## Overview
The AI Grammar Checker is a Python-based tool that helps users improve their English by analyzing sentences for grammatical errors. It provides corrections, feedback, and a score based on the accuracy of the sentence. Additionally, it encourages users to learn new words daily by requiring them to use specific words in their sentences.

## Features
- Checks and corrects grammar mistakes using LanguageTool.
- Provides a score based on sentence correctness.
- Highlights grammatical errors and offers suggestions.
- Requires users to use newly learned words in sentences.
- Saves daily words for tracking progress.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.7 or later). You also need the required dependencies.

### Install Dependencies
```sh
pip install language-tool-python
```

## Usage
1. Run the script:
   ```sh
   python ai_grammar_checker.py
   ```
2. Enter three new words for the day when prompted.
3. Input sentences using those words.
4. Get feedback, corrections, and a score for each sentence.

## Example
```
Welcome to AI Grammar Checker!
Today's words: intricate, persevere, elated

Enter a sentence using the word 'intricate': The design was very intricated.

Feedback:
Corrected Sentence: The design was very intricate.
Score: 85 / 100
Errors:
- Spelling mistake: "intricated" should be "intricate".
```

## File Structure
```
/
├── grammar.py  # Main script
├── daily_words.json       # Stores user's daily words
├── README.md              # Documentation
```

## Contributing
Pull requests are welcome! If you'd like to improve the AI Grammar Checker, feel free to fork the repository and submit a PR.

## License
This project is licensed under the MIT License.

## Author
Developed by [Your Name]
