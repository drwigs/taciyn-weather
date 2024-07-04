import shutil

def get_terminal_size():
    size = shutil.get_terminal_size()
    return size.lines, size.columns

def center_text_in_terminal(text):
    rows, columns = get_terminal_size()
    lines = text.split('\n')
    
    for line in lines:
        centered_line = line.center(columns)
        print(centered_line)