from datetime import datetime

# Each helper checks one subject and returns a ready-to-show text line.
def maths(hw):
    final = ""
    if hw:
        final = f"*Maths*: {hw}"
    return final
def phy(hw):
    final = ""
    if hw:
        final = f"*Physics*: {hw}"
    return final
def chem(hw):
    final = ""
    if hw:
        final = f"*Chemistry*: {hw}"
    return final
def bio(hw):
    final = ""
    if hw:
        final = f"*Biology*: {hw}"
    return final
def sst(hw):
    final = ""
    if hw:
        final = f"*SST*: {hw}"
    return final
def hindi(hw):
    final = ""
    if hw:
        final = f"*Hindi*: {hw}"
    return final
def eng(hw):
    final = ""
    if hw:
        final = f"*English*: {hw}"
    return final

# This one keeps any extra note exactly as the user typed it.
def additional(additional):
    return additional

# Make today's date look neat for the homework output.
def date():
    sys_time = datetime.now()
    date_str = f"*{sys_time.strftime('%d/%m/%y')}*"
    return date_str
