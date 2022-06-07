from backend.interface import Interface
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QPixmap
import images


interface = Interface()
file_path = ''


def set_values(SC, PC, AR, IR, DR, AC, TR, INPR, OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT):
    try:
        result = interface.get_values()
        SC.setText(result['SC'])
        PC.setText(result['PC'])
        AR.setText(result['AR'])
        IR.setText(result['IR'])
        DR.setText(result['DR'])
        AC.setText(result['AC'])
        TR.setText(result['TR'])
        INPR.setText(result['INPR'])
        OUTR.setText(result['OUTR'])
        INST.setText(result['INST'])
        INPUT.setText(result['INPUT'])

        green = QPixmap(":/images/images/green.png")
        red = QPixmap(":/images/images/red.png")

        I.setPixmap(green if result['I'] else red)
        S.setPixmap(green if result['S'] else red)
        E.setPixmap(green if result['E'] else red)
        R.setPixmap(green if result['R'] else red)
        IEN.setPixmap(green if result['IEN'] else red)
        FGI.setPixmap(green if result['FGI'] else red)
        FGO.setPixmap(green if result['FGO'] else red)
    except:
        pass


def set_memory(memory):
    try:
        result = interface.get_memory()
        for i in range(4096):
            item0 = QTableWidgetItem(result[i][0])
            item2 = QTableWidgetItem(result[i][1])
            item0.setTextAlignment(4)
            item2.setTextAlignment(4)
            memory.setItem(i, 0, item0)
            memory.setItem(i, 2, item2)
    except:
        for i in range(4096):
            item0 = QTableWidgetItem('')
            item2 = QTableWidgetItem('0000')
            item0.setTextAlignment(4)
            item2.setTextAlignment(4)
            memory.setItem(i, 0, item0)
            memory.setItem(i, 2, item2)


def text_changed(inp):
    interface.update_input(inp.text())


def beautify_code(code):
    text = interface.save(code.toPlainText())
    code.setPlainText(text)


def save_code(code):
    value = code.toPlainText()
    code.setPlainText(interface.save(value))


def compile_code(console, code, microoperation, memory, SC, PC, AR, IR, DR, AC, TR, INPR, OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT):
    try:
        result = interface.compile(code.toPlainText())
        console.setPlainText(result[1])
        microoperation.setText('')
        if result[0]:
            I.setEnabled(True)
            S.setEnabled(True)
            E.setEnabled(True)
            R.setEnabled(True)
            IEN.setEnabled(True)
            FGI.setEnabled(True)
            FGO.setEnabled(True)

    except:
        pass
    set_memory(memory)
    set_values(SC, PC, AR, IR, DR, AC, TR, INPR,
               OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT)


def next_step(console, code, microoperation, memory, SC, PC, AR, IR, DR, AC, TR, INPR, OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT):
    message = interface.next_step(code.toPlainText())
    if message == None:
        console.setPlainText(
            'Compile code first!')
        microoperation.setText('')
    else:
        console.setPlainText('')
        microoperation.setText(message)
    set_memory(memory)
    set_values(SC, PC, AR, IR, DR, AC, TR, INPR,
               OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT)


def run(console, code, microoperation, memory, SC, PC, AR, IR, DR, AC, TR, INPR, OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT):
    message = interface.run(code.toPlainText())
    if message == False:
        console.setPlainText(
            'Compile code first!')
        microoperation.setText('')
    else:
        console.setPlainText('')
        microoperation.setText('[FINISHED PROGRAM]')
    set_memory(memory)
    set_values(SC, PC, AR, IR, DR, AC, TR, INPR,
               OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT)


def reset(console, code, microoperation, memory, SC, PC, AR, IR, DR, AC, TR, INPR, OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT):
    compile_code(console, code, microoperation, memory, SC, PC, AR,
                 IR, DR, AC, TR, INPR, OUTR, INST, I, S, E, R, IEN, FGI, FGO, INPUT)
    console.setPlainText('Reset execution')
    microoperation.setText('')


def save_code(code):
    global file_path
    if not file_path:
        file_path = QFileDialog.getSaveFileName()[0]
    if file_path:
        file = open(file_path, 'w')
        text = code.toPlainText()
        file.write(text)
        file.close()


def open_code(code):
    global file_path
    file_path = QFileDialog.getOpenFileName()[0]
    if file_path:
        file = open(file_path, 'r')
        text = file.read()
        code.setPlainText(text)
        file.close()
