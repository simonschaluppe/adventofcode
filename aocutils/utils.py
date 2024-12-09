

EMOJI_MAPPING = {
    "0": "0️⃣",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
    "#": "💢",
    " ": "⬛",
    ".": "⬛",
    "A": "🦅",
    "a": "🐵",
    "B": "🛁",
    "C": "💿",
    "D": "🦡",
    "d": "🚺",
    "E": "📫",
    "e": "📨",
    "F": "🏭",
    "f": "👪",
    "G": "🌌",
    "g": "🏒",
    "H": "🐹",
    "h": "⚓",
    "I": "🍨",
    "i": "🧊",
    "J": "🗾",
    "j": "🥋",
    "K": "☕",
    "k": "🛶",
    "L": "🧪",
    "l": "🦙",
    "M": "🎤",
    "m": "🧲",
    "N": "📝",
    "n": "💉",
    "O": "⭕",
    "o": "🆗",
    "P": "🅿",
    "p": "📦",
    "Q": "💛",
    "q": "💬",
    "R": "🚲",
    "r": "📻",
    "S": "🪐",
    "s": "🐑",
    "T": "🎹",
    "t": "🌮",
    "U": "🆙",
    "u": "🚇",
    "V": "🚫",
    "v": "🆚",
    "W": "♎",
    "w": "🚾",
    "X": "❎",
    "x": "💥",
    "Y": "🤸🏽‍♂️",
    "y": "🥮",
    "Z": "💤",
    "z": "🏁",
    "*": "⭐",
    "?": "🔎",
    '/': "🥒", 
    '@': "🐒",
    # **EMOJI_LETTERS
}

def show(nested_list, space=" ", use_emojis=False):
    """Displays the map in ASCII or emojis based on the mapping."""
    for item in nested_list:
        if use_emojis:
            print("".join(EMOJI_MAPPING.get(char, "⬜") for char in item))
        else:
            print(space.join(item))

def mark_on_map(position_tuples, nested_list_map, mark="X", marks=None):
    """Marks specified positions on the map with the given character."""
    copied = [l.copy() for l in nested_list_map]
    
    for i, (x, y) in enumerate(position_tuples):
        if marks:
            mark = marks[i]
        copied[x][y] = mark
        if mark not in EMOJI_MAPPING:
            EMOJI_MAPPING[mark] = mark
    return copied

def find_on_map(what, nested_list_map):
    """Finds all positions of a given character on the map."""
    found = set()
    for x, row in enumerate(nested_list_map):
        for y, cell in enumerate(row):
            if cell == what:
                found.add((x, y))
    return found

def replace_on_map(old, new, nested_list_map):
    """Replaces all occurrences of a character with another on the map."""
    return mark_on_map(find_on_map(old, nested_list_map), nested_list_map, new)


if __name__ == "__main__":
# Example Usage
    ascii_map = [
        [".", ".", "0", "#", "#"],
        [".", "1", "~", "~", "#"],
        ["#", "~", ".", "~", "#"],
        ["#", "~", "~", "A", "#"],
        ["#", "#", "b", "#", "#"]
    ]

    # Display map in emojis
    print("Map with Emojis:")
    show(ascii_map)
    show(ascii_map, use_emojis=True)

    # Mark a position and display updated map
    marked_map = mark_on_map([(1, 2), (3, 3)], ascii_map, "X")
    print("\nMarked Map:")
    show(marked_map)

    # Replace a character and display updated map
    replaced_map = replace_on_map("~", "O", ascii_map)
    print("\nReplaced Map:")
    show(replaced_map)