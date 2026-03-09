previous_lines = {}

def detect_bump(player, stat, new_line):

    key = f"{player}_{stat}"

    if key in previous_lines:
        old_line = previous_lines[key]

        if new_line > old_line:
            return old_line, new_line

    previous_lines[key] = new_line

    return None
