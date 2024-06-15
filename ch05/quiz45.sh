sort verb_patterns.txt | uniq -c | sort -nr > sorted_verb_patterns.txt
grep -E '行う|なる|与える' verb_patterns.txt | sort | uniq -c | sort -nr
