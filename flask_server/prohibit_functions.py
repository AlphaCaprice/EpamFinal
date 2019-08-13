import sys


def prohibit():
    # Удаляет заданные встроенные функции и модули для обеспечения безопасности
    prohibited_modules = ["os"]
    prohibited_builtins = ['open', 'eval', 'exec']
    for name in prohibited_builtins:
        if name in __builtins__:
            del __builtins__[name]

    for name in prohibited_modules:
        if name in sys.modules:
            del sys.modules[name]
