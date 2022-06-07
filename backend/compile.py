database = {'AND': '0', 'ADD': '1', 'LDA': '2', 'STA': '3', 'BUN': '4', 'BSA': '5', 'ISZ': '6',
            'ANDI': '8', 'ADDI': '9', 'LDAI': 'A', 'STAI': 'B', 'BUNI': 'C', 'BSAI': 'D', 'ISZI': 'E',
            'CLA': '7800', 'CLE': '7400', 'CMA': '7200', 'CME': '7100', 'CIR': '7080', 'CIL': '7040',
            'INC': '7020', 'SPA': '7010', 'SNA': '7008', 'SZA': '7004', 'SZE': '7002', 'HLT': '7001',
            'INP': 'F800', 'OUT': 'F400', 'SKI': 'F200', 'SKO': 'F100', 'ION': 'F080', 'IOF': 'F040',
            'ORG': 'X', 'END': 'X', 'DEC': 'X', 'HEX': 'X'}


class Compile:
    def start(self, code):
        self.code = ''
        self.address_table = dict()
        commands, error = self.serialize(code)
        if error:
            return False, error
        fixed_commands = self.mapping_address(commands)
        if fixed_commands and fixed_commands[0][1] == 'Invalid address':
            return False, fixed_commands
        return True, self.write_memory(fixed_commands)

    def process_line(self, line, id):
        label = ''
        line = line.expandtabs(tabsize=1).strip()
        if not line:
            return [id, 'empty']
        if line.find('/') != -1:
            line = line[:line.find('/')].rstrip()

        for word in line:
            if not(word.isalnum() or word in [',', ' ', '-']):
                return [id, 'error', 'You used an unauthorized character']

        if (count := line.count(',')) > 1:
            return [id, 'error', 'You used the , multiple times']
        elif count == 1:
            index = line.find(',')
            label = line[:index].rstrip()
            line = line[index+1:].lstrip()

        if line.find(' ') == -1:
            if line == 'END':
                return [id, 'pseudu', label, 'END']
            inst = database.get(line, ' ')
            if inst[0] not in ['7', 'F']:
                return [id, 'error', 'Wrong instruction']
            return [id, 'register' if inst[0] == '7' else 'io', label, inst]

        name = line[:line.find(' ')]
        inst = database.get(name, '')
        line = line[line.find(' '):].lstrip()

        if not inst:
            return [id, 'error', 'Wrong instruction']
        if inst == 'X':
            try:
                if name == 'ORG':
                    return [id, 'pseudu', label, name, int(line) % 65536]
                if name == 'DEC':
                    return [id, 'pseudu', label, name, str(hex(int(line) % 65536)[2:].zfill(4)).upper()]
                return [id, 'pseudu', label, name, str(hex(int(line, 16) % 65536)[2:].zfill(4)).upper()]
            except:
                return [id, 'error', 'Wrong number']
        if(inst[0] in ['7', 'F']):
            return [id, 'error', 'Wrong instruction']

        indirect = True if line[-2:] == ' I' else False
        if indirect:
            line = line[:-1].rstrip()

        if line.find(' ') != -1:
            return [id, 'error', 'Wrong instruction']
        return [id, 'memory', label, database.get(name+'I') if indirect else database.get(name), line]

    def serialize(self, code):
        code = code.upper().splitlines(keepends=False)
        id = 0
        error = []
        commands = []
        for line in code:
            result = self.process_line(line, id)
            if result[1] == 'empty':
                continue
            elif result[1] == 'error':
                error.append([result[0], result[2]])
            elif result[3] == 'ORG':
                id = int(result[4]) - 1
            elif result[2]:
                commands.append(result)
                self.address_table[result[2]] = id
            else:
                commands.append(result)

            id += 1
        return commands, error

    def mapping_address(self, commands):
        for i in range(len(commands)):
            if commands[i][1] == 'memory':
                addr = self.address_table.get(commands[i][4], '')
                if addr != '':
                    commands[i][3] += str(hex(addr))[2:].zfill(3).upper()
                    commands[i].pop()
                else:
                    return [[commands[i][0], 'Invalid address']]

        return commands

    def write_memory(self, commands):
        memory = [['', '0000'] for _ in range(4096)]
        line_start = commands[0][0]

        for command in commands:
            if command[3] == 'END':
                continue
            if command[1] == 'pseudu':
                memory[command[0]] = [command[2], command[4]]
                continue

            memory[command[0]] = [command[2], command[3]]

        return line_start, memory
