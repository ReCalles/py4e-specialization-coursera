# Chapter 11: Regular Expressions

* **Regular Expressions (Regex / RegEx):** Powerful language for searching and matching complex text patterns.
* **`re` Module:** Python's built-in module for regular expressions.
* **`re.search(pattern, string)`:**
    * Finds the *first* occurrence of the pattern in the string.
    * Returns a match object if found, `None` otherwise.
    * Match object has `group()` method to retrieve matched text.
* **`re.findall(pattern, string)`:**
    * Finds *all* non-overlapping occurrences of the pattern.
    * Returns a list of matching strings.
* **Common Regex Characters (Metacharacters):**
    * `.` (dot): Matches any single character (except newline).
    * `*`: Matches zero or more occurrences of the preceding character/group (greedy).
    * `+`: Matches one or more occurrences of the preceding character/group (greedy).
    * `?`: Matches zero or one occurrence of the preceding character/group (non-greedy, also used as a quantifier).
    * `^`: Matches the start of the string/line.
    * `$`: Matches the end of the string/line.
    * `\s`: Matches any whitespace character.
    * `\S`: Matches any non-whitespace character.
    * `\d`: Matches any digit (0-9).
    * `\D`: Matches any non-digit character.
    * `\w`: Matches any word character (alphanumeric + underscore).
    * `\W`: Matches any non-word character.
* **Character Sets `[]`:**
    * `[aeiou]`: Matches any one vowel.
    * `[a-z0-9]`: Matches any lowercase letter or digit.
    * `[^xyz]`: Matches any character *except* x, y, or z.
* **Quantifiers:**
    * `{n}`: Exactly `n` times.
    * `{n,}`: `n` or more times.
    * `{n,m}`: Between `n` and `m` times.
* **Greedy vs. Non-Greedy:**
    * `*` and `+` are **greedy** by default (match longest possible string).
    * Add `?` after `*` or `+` to make them **non-greedy** (match shortest possible string): `*?`, `+?`.
* **Extracting Data with Parentheses `()`:**
    * Parentheses define "groups" you want to extract.
    * When using `re.findall()` with parentheses, it returns a list of *tuples* if multiple groups are defined, or a list of strings if one group.
* **Escaping Special Characters:**
    * If you want to match a literal metacharacter (e.g., a literal dot `.` or asterisk `*`), escape it with a backslash: `\.`, `\*`.
    * Use raw strings (`r"pattern"`) to avoid issues with backslashes in Python strings conflicting with regex backslashes.