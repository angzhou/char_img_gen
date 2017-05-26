# char-img-gen

Generate images from font files.

The images that are generated are useful in machine learning training for image applications.

These categories of characters are used:

1. simplified Chinese (selected)
1. Hànyǔ Pīnyīn vowels with tone marks - diacritics
1. traditional Chinese including Zhuyin (selected)
1. Chinese characters used in Cantonese only (selected)
1. Japanese Kanji (selected)
1. Japnese 平仮名-hiragana & 片仮名-katakana
1. Korean syllables (selected)
1. ascii - windows-1250
1. Windows-1252, Russian, Greek characters
1. Math symbols (selected)

See [README.md in char_lists/](char_lists/README.md) for character selection rationales.

## Directory structure

1. `char_lists` contains lists of characters, each file contains one category of characters.
1. `fonts` will contain font files
1. `scripts` has the main program

