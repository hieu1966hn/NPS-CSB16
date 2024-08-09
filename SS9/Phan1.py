def reverse_str(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s  ### m / im / nim / dnim / Xdnim
    return reverse_s


print(reverse_str("mindX"))
