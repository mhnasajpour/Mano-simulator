from .save import Save
from .compile import Compile
from .execution import Execution


class Interface:
    def __init__(self):
        self.last_compiled_code = None

    def save(self, code):
        fix_code = Save()
        return fix_code.get_corrected_code(code)

    def compile(self, code):
        compile = Compile()
        result = compile.start(code)
        if result[0] == True:
            self.last_compiled_code = code
            # Console, PC, Memory
            self.exe = Execution(*result[1])
            return True, 'Compiled successfully', str(hex(result[1][0]))[2:].upper().zfill(3), result[1][1]
        console = 'Compilation failed'
        for line in result[1]:
            console += f'\n{line[0]}: {line[1]}'
        return False, console

    def get_values(self):
        return self.exe.values

    def get_memory(self):
        return self.exe.memory

    def next_step(self, code):
        if self.last_compiled_code == code:
            return self.exe.next_step()
        return None

    def run(self, code):
        if self.last_compiled_code == code:
            self.exe.run()
            return True
        return False

    def update_input(self, inp):
        try:
            self.exe.set_input(inp)
        except:
            pass
