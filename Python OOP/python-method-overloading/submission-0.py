class TextProcessor:
    # Implement method overloading for format_text method
    @staticmethod
    def format_text(text1: str, text2: str = "") -> str:
        if text1 + text2 == text1:
            return text1.upper()
        else:
            return text1 + text2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
