import py_compile
a = py_compile.compile("C:\\Users\\Dell\\Desktop\\Python files\\SpaceInvaders\\main.py")
print(a)
import dis
b = dis.show_code("C:\\Users\\Dell\\Desktop\\Python files\\SpaceInvaders\\main.py")
print(b)