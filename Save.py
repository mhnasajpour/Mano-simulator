class Save:
    def __init__(self, code):
        self.code = code

    def get_corrected_code(self, code):
        lines, i = code.upper().splitlines(keepends=False), 0
        while i < len(lines):
            lines[i] = lines[i].expandtabs(tabsize=1).strip()
            if not lines[i]:
                lines.pop(i)
                continue
            lines[i], j = list(lines[i]), 0
            while j < len(lines[i]):
                if lines[i][j] == '/':
                    if lines[i][j-1] != ' ':
                        lines[i].insert(j, ' ')
                    break

                if not(lines[i][j].isalnum() or lines[i][j] in [' ', ',']):
                    lines[i].pop(j)
                    continue
                if lines[i][j] == ' ' and not(lines[i][j-1].isalnum() or lines[i][j-1] in [',']):
                    lines[i].pop(j)
                    continue
                if lines[i][j] == ',' and lines[i][j-1] == ' ':
                    lines[i].pop(j-1)

                j += 1

            lines[i] = ''.join(lines[i]).strip()
            i += 1

        return '\n'.join(lines)
