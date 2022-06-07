database = {'0': 'AND', '1': 'ADD', '2': 'LDA', '3': 'STA', '4': 'BUN', '5': 'BSA', '6': 'ISZ',
            '8': 'AND', '9': 'ADD', 'A': 'LDA', 'B': 'STA', 'C': 'BUN', 'D': 'BSA', 'E': 'ISZ'}


def finish_exec(values, message):
    values['SC'] = '-1'
    values['INST'] = ''
    return '[EXECUTE] ' + message


def AND(values, memory):
    if values['SC'] == '4':
        values['DR'] = memory[int(values['AR'], 16)][1]
        return '[EXECUTE] DR<-M[AR]'
    else:
        values['AC'] = str(
            hex(int(values['AC'], 16) & int(values['DR'], 16))).upper()[2:].zfill(4)
        return finish_exec(values, 'AC<-AC&DR, SC<-0')


def ADD(values, memory):
    if values['SC'] == '4':
        values['DR'] = memory[int(values['AR'], 16)][1]
        return '[EXECUTE] DR<-M[AR]'
    else:
        values['AC'] = str(hex(int(values['AC'], 16) +
                           int(values['DR'], 16))).upper()[2:].zfill(4)
        if len(values['AC']) == 5:
            values['AC'] = values['AC'][1:]
            values['E'] = True
        else:
            values['E'] = False
        return finish_exec(values, 'AC<-AC+DR, E<-Cout, SC<-0')


def LDA(values, memory):
    if values['SC'] == '4':
        values['DR'] = memory[int(values['AR'], 16)][1]
        return '[EXECUTE] DR<-M[AR]'
    else:
        values['AC'] = values['DR']
        return finish_exec(values, 'AC<-DR, SC<-0')


def STA(values, memory):
    memory[int(values['AR'], 16)][1] = values['AC']
    return finish_exec(values, 'AC<-DR, SC<-0')


def BUN(values, memory):
    values['PC'] = values['AR']
    return finish_exec(values, 'PC<-AR, SC<-0')


def BSA(values, memory):
    if values['SC'] == '4':
        memory[int(values['AR'], 16)][1] = values['PC']
        values['AR'] = str(hex(int(values['AR'], 16) + 1)).upper()[2:].zfill(3)
        return '[EXECUTE] M[AR]<-PC, AR<-AR+1'
    else:
        values['PC'] = values['AR']
        return finish_exec(values, 'PC<-AR, SC<-0')


def ISZ(values, memory):
    if values['SC'] == '4':
        values['DR'] = memory[int(values['AR'], 16)][1]
        return '[EXECUTE] DR<-M[AR]'
    elif values['SC'] == '5':
        values['DR'] = str(hex(int(values['DR'], 16) + 1)
                           ).upper()[2:][-4:].zfill(4)
        return '[EXECUTE] DR<-DR+1'
    else:
        memory[int(values['AR'], 16)][1] = values['DR']
        if memory[int(values['AR'], 16)][1] == '0000':
            values['PC'] = str(hex(int(values['PC'], 16) + 1)
                               ).upper()[2:].zfill(3)
        return finish_exec(values, 'M[AR]<-DR, PC=?PC+1, SC<-0')
