## File Format

All files have one character per line.

All files are UTF-8 encoded.

## Filenames and details

| file   | chars | category                                        | selection details  |
| ------ | ----- | ------------------------------------------------| ------------------ |
| sc.txt | 7185  | simplified Chinese (selected)                   | National standard GB18030-2005 has 70000 characters, but most of them are not used, these 7185 characters are more than enough to coverage almost all situations |
| pm.txt | 24    | Hànyǔ Pīnyīn vowels with tone marks         | 4 for each vowel |
| tc.txt | 2521  | traditional Chinese including Zhuyin (selected) | Covers all 常用國字標準字體表 and some of 次常用國字標準字體表, exclude those already in sc.txt |
| hk.txt | 275   | Chinese characters used in Cantonese (selected) | Because most of characters used in Cantonese are in sc.txt and tc.txt, this only have those characters that only appear in Cantonese |
| jc.txt | 232   | Japanese Kanji (selected)                       | Most of Kanji characters are already in sc.txt and tc.txt, this only have those characters that only appear in Japanese |
| jp.txt | 162   | Japnese 平仮名-hiragana & 片仮名-katakana       | I hope they are complete, if not, let me know |
| kr.txt | 972   | Korean syllables (selected)                     | I got this by `sort`, `uniq` a flattened file called '6000 Most Common Korean Words', I heard from interweb that they should cover 99.9% usage |
| ws.txt | 278   | ascii, Windows-1252, Russian, Greek characters  | Most western languages are covered |
| mo.txt | 205   | Math symbols (selected)                         | Most math formulas should be covered |

These characters are removed from ws.txt:

    ª ¯ ° ² ³ ¹ º ¼ ½ ¾ 
    á è é ì í ò ó ù ú Α
    Β Ε Ζ Η Ι Κ Μ Ν Ο Ρ
    Τ Υ Χ μ ο А В Е К М
    Н О Р С Т У Х Ь а в
    г д е ж з и й к л м
    н о п р с т у ф х ц
    ч ш щ ъ ы ь э ю я ё
    ´ ×

These are removed from mo.txt:

    ∆ ∕ ∖ □ △ ▽
