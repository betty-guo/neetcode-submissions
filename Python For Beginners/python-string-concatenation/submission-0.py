def concatenate(s1: str, s2: str) -> str:
    new_str = s1 + s2
    if len(new_str) > 10:
        return "Too long!"
    return new_str




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
