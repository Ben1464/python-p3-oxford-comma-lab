def oxford_comma(words):
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"
    else:
        # Use ', ' to join all elements except the last one
        # Use ', and ' to join the last element
        return f"{', '.join(words[:-1])}, and {words[-1]}"
result = oxford_comma(["fiddleheads", "okra", "kohlrabi"])
print(result)