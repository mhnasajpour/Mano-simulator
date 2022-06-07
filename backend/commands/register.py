database = {'7800': 'CLA', '7400': 'CLE', '7200': 'CMA', '7100': 'CME', '7080': 'CIR', '7040': 'CIL',
            '7020': 'INC', '7010': 'SPA', '7008': 'SNA', '7004': 'SZA', '7002': 'SZE', '7001': 'HLT'}


def finish_exec(values, message):
    values['SC'] = '-1'
    values['INST'] = ''
    return '[EXECUTE] ' + message + ', SC<-0'


def CLA(values):
    values['AC'] = '0000'
    return finish_exec(values, 'AC<-0')


def CLE(values):
    values['E'] = False
    return finish_exec(values, 'E<-0')


def CMA(values):
    values['AC'] = str(hex(65535 - int(values['AC'], 16))).upper()[2:].zfill(4)
    return finish_exec(values, 'AC<-~AC')


def CME(values):
    values['E'] = False if values['E'] else True
    return finish_exec(values, 'E<-~E')


def CIR(values):
    E = values['E']
    values['E'] = bool(int(values['AC'][3], 16) % 2)
    values['AC'] = str(hex(int(values['AC'], 16) >> 1)).upper()[2:].zfill(4)
    values['AC'] = str(
        hex(int(values['AC'][0], 16) + 8 if E else int(values['AC'][0], 16))).upper()[2:] + values['AC'][1:]
    return finish_exec(values, 'AC<-(shr)AC, AC(15)<-E, E<-AC(0)')


def CIL(values):
    E = values['E']
    values['E'] = bool(int(values['AC'][0], 16) > 7)
    values['AC'] = str(hex(int(values['AC'], 16) << 1)
                       ).upper()[2:][-4:].zfill(4)
    values['AC'] = values['AC'][:-1] + str(
        hex(int(values['AC'][3], 16) + 1 if E else int(values['AC'][3], 16))).upper()[2:]
    return finish_exec(values, 'AC<-(shl)AC, AC(0)<-E, E<-AC(15)')


def INC(values):
    values['AC'] = str(hex(int(values['AC'], 16) + 1)).upper()[2:].zfill(4)
    if len(values['AC']) == 5:
        values['AC'] = values['AC'][1:]
        values['E'] = True
    return finish_exec(values, 'AC<-AC+1')


def SPA(values):
    if int(values['AC'][0], 16) < 8:
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
    return finish_exec(values, 'if AC(15)=0 then PC<-PC+1')


def SNA(values):
    if int(values['AC'][0], 16) > 7:
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
    return finish_exec(values, 'if AC(15)=1 then PC<-PC+1')


def SZA(values):
    if values['AC'] == '0000':
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
    return finish_exec(values, 'if AC=0 then PC<-PC+1')


def SZE(values):
    if values['E'] == False:
        values['PC'] = str(hex(int(values['PC'], 16) + 1)).upper()[2:].zfill(3)
    return finish_exec(values, 'if E=0 then PC<-PC+1')


def HLT(values):
    values['S'] = False
    return '[FINISHED PROGRAM]'
