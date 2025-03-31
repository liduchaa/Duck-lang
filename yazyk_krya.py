import sys
import re
from re import escape

class DuckError(Exception):
    pass

def ban_python_commands(code):
    banned = [
        'input', 'print', 'int', 'float', 'str', 'list', 'dict',
        'True', 'False', 'None', 'or', 'and', 'not', 'in', '=',
        '+', '-', '*', '/', '%', '**', '==', '!=', '>', '<', '>=', '<=',
        'while', 'for', 'if', 'else', 'elif', 'break', 'continue', 'range', 'pass',
        'def', 'import', 'return', 'append', 'del', 'len'
    ]
    
    for cmd in banned:
        pattern = r'(^|\W)' + re.escape(cmd) + r'($|\W)'
        if re.search(pattern, code):
            raise DuckError(f"Python command not allowed: {cmd}")

def translate_ducky(code):
    ban_python_commands(code)
    
    replacements = {
        # I/O
        'крякни': 'print',
        'съешь': 'input',
        
        # Data types
        'заумное': 'int',
        'плавающее': 'float',
        'буковки': 'str',
        'списочек': 'list',
        'словарик': 'dict',
        
        # Boolean
        'моёяйцо': 'True',
        'яйцокукушки': 'False',
        'пустота': 'None',
        
        # Operations
        'кря': 'or',
        'икря': 'and',
        'некря': 'not',
        'болотный': 'in',
        
        # Assignment
        'положи': '=',
        
        # Math
        'прибавить': '+',
        'отнять': '-',
        'умножить': '*',
        'поделить': '/',
        'остаток': '%',
        'встепень': '**',
        
        # Comparison
        'равноутятам': '==',
        'неравноутятам': '!=',
        'большеуток': '>',
        'меньшеуток': '<',
        'большеравноутятам': '>=',
        'меньшеравноутятам': '<=',
        
        # Control flow
        'водоворот': 'while',
        'водопад': 'for',
        'если': 'if',
        'вредное': 'else',
        'аесли': 'elif',
        'застрелили': 'break',
        'плыви': 'continue',
        'озеро': 'range',
        'погрейся на солнышке': 'pass',
        
        # Functions
        'клюв': 'def',
        'проглоти': 'import',
        'плюнь': 'return',
        
        # Collections
        'прицепи': 'append',
        'плесень': 'del',
        'длина': 'len'
    }
    
    for ru, py in replacements.items():
        code = code.replace(ru, py)
    
    return code

def execute_ducky(code):
    try:
        translated = translate_ducky(code)
        safe_builtins = {
            'print': print,
            'input': input,
            'range': range,
            'len': len
        }
        exec(translated, {'__builtins__': safe_builtins}, {})
    except Exception as e:
        raise DuckError(f"Duck error: {str(e)}")

def interactive_mode():
    print("Напишите 'улетаю' для выхода")
    while True:
        try:
            code = input("(Уточка)>>> ")
            if code.strip() == 'улетаю':
                break
            execute_ducky(code)
        except DuckError as e:
            print(e)
        except (KeyboardInterrupt, EOFError):
            print("\nУтка улетает...")
            break

def run_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        execute_ducky(code)
    except FileNotFoundError:
        raise DuckError(f"Файл не найден: {filename}")
    except Exception as e:
        raise DuckError(f"Ошибка файла: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        print("Использование: yazyk_krya.py")
