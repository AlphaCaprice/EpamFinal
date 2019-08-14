from subprocess import Popen, PIPE, TimeoutExpired
import re

def execute_code(code: str, stdin: str, timeout: float) -> dict:
    print(timeout)
    # Вставка в начало пользовательского кода
    # функции для удаления модулей и встроенных функций
    configuration_str = "import prohibit_functions\n" \
                        "prohibit_functions.prohibit()\n"
    code = configuration_str + code
    print(code)
    with Popen(['python', '-c', code], stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
        try:
            out, err = proc.communicate(input=bytes(stdin, encoding='utf-8'), timeout=timeout)
        except TimeoutExpired:
            return {"output": "", "error": "Timeout expired"}
        else:
            error_msg = ""
            if err:
                # Берём только последнюю часть сообщения и номер строки об ошибке
                # без traceback, чтобы не давать лишнюю информацию пользователю
                line_num = int(re.findall("line (\d*)", err.decode())[0])-2
                error_msg = f"Line num: {line_num}\n" + err.decode().split('\n')[-2]
            print(out.decode(), '\n', error_msg)
            return {"output": out.decode(), "error": error_msg}
