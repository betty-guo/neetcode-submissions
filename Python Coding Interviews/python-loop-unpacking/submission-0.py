from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score_name = scores[0][0]
    highest_score = scores[0][1]

    for name, score in scores:
        if score > highest_score:
            highest_score_name = name
            highest_score = score
    return highest_score_name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
