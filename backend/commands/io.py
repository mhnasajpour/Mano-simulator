database = {'F800': 'INP', 'F400': 'OUT', 'F200': 'SKI',
            'F100': 'SKO', 'F080': 'ION', 'F040': 'IOF'}


def finish_exec(values, message):
    values['SC'] = '-1'
    values['INST'] = ''
    return '[EXECUTE] ' + message + ', SC<-0'


def INP(values):
    values['AC'][2:] = values['INPR']
    values['INPR'] = str(hex(ord(values['INPUT'][0])))[2:].upper().zfill(4)
    values['INPUT'].pop(0)
    values['FGI'] = False
    return finish_exec(values, 'AC(0-7)<-INPR, FGI<-0')


def OUT(values):
    values['OUTR'] = values['AC'][2:]
    values['FGO'] = False
    return finish_exec(values, 'OUTR<-AC(0-7), FGO<-0')


def SKI(values):
    if values['FGI']:
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
    return finish_exec(values, 'if FGI=1 then PC<-PC+1')


def SKO(values):
    if values['FGO']:
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
    return finish_exec(values, 'if FGO=1 then PC<-PC+1')


def ION(values):
    values['IEN'] = True
    return finish_exec(values, 'IEN<-1')


def IOF(values):
    values['IEN'] = False
    return finish_exec(values, 'IEN<-0')


def interrupt_cycle(values, memory):
    if values['SC'] == '0':
        values['AR'] = '000'
        values['TR'][1:] = values['PC']
        return '[EXECUTE] AR<-0, TR<-PC'
    elif values['SC'] == '1':
        memory[int(values['AR'], 16)][1] = values['TR']
        values['PC'] = '000'
        return '[EXECUTE] M[AR]<-TR, PC<-0'
    else:
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
        values['IEN'] = False
        values['R'] = False
        return finish_exec(values, 'PC<-PC+1, IEN<-0, R<-0')
