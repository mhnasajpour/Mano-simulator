from .commands import io, memory, register


def str_to_hex(number, opr, z):
    return str(hex(int(number, 16) + opr)).upper()[2:].zfill(z)


class Execution:
    def __init__(self, PC, memory):
        self.memory = memory
        self.values = {
            'INST': '',
            'PC': str(hex(PC)).upper()[2:].zfill(3),
            'SC': '0',
            'IR': '0000',
            'AR': '000',
            'DR': '0000',
            'AC': '0000',
            'TR': '0000',
            'INPR': '00',
            'OUTR': '00',
            'I': False,
            'E': False,
            'R': False,
            'S': True,
            'IEN': False,
            'FGI': False,
            'FGO': False,
            'INPUT': ''
        }

    def set_input(self, value):
        self.values['INPUT'] = value
        if value:
            self.values['FGI'] = True

    def next_step(self):
        message = ''
        if self.values['S']:
            SC = int(self.values['SC'], 16)
            if not self.values['R']:
                if (SC) < 2:
                    message = self.fetch()
                elif SC == 2:
                    message = self.decode()
                elif SC == 3 and not self.values['INST']:
                    message = self.decode()
                else:
                    message = self.execute()
                    if self.values['IEN'] and (self.values['FGI'] or self.values['FGO']):
                        self.values['R'] = True

            else:
                io.interrupt_cycle(self.values, self.memory)

            self.values['SC'] = str_to_hex(self.values['SC'], 1, 1)
        return message

    def run(self):
        while self.values['S']:
            self.next_step()

    def fetch(self):
        if self.values['SC'] == '0':
            self.values['AR'] = self.values['PC']
            return '[FETCH] AR<-PC'
        if self.values['SC'] == '1':
            self.values['IR'] = self.memory[int(self.values['AR'], 16)][1]
            self.values['I'] = True if int(
                self.values['IR'][0], 16) > 7 else False
            self.values['PC'] = str_to_hex(self.values['PC'], 1, 3)
            return '[FETCH] IR<-M[AR], PC<-PC+1'

    def decode(self):
        if self.values['SC'] == '2':
            self.values['AR'] = self.values['IR'][1:]
            if self.values['IR'][0] in ['7', 'F']:
                if self.values['I']:
                    self.values['INST'] = io.database[self.values['IR']]
                else:
                    self.values['INST'] = register.database[self.values['IR']]
            return '[DECODE] AR<-IR(0-11) I<-IR(15)'
        else:
            if self.values['I']:
                self.values['AR'] = self.memory[int(
                    self.values['AR'], 16)][1][1:]
                self.values['INST'] = memory.database[self.values['IR'][0]]
                return '[DECODE] AR<-M[AR]'
            self.values['INST'] = memory.database[self.values['IR'][0]]
            return '[DECODE] NOP'

    def execute(self):
        if self.values['IR'][0] == 'F':
            message = getattr(io, self.values['INST'])(self.values)
        elif self.values['IR'][0] == '7':
            message = getattr(register, self.values['INST'])(self.values)
        else:
            message = getattr(memory, self.values['INST'])(
                self.values, self.memory)
        return message
