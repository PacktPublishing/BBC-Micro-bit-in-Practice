from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
pattern0 = Image("00000:11111:22222:33333:44444")
pattern1 = Image("11111:22222:33333:44444:55555")
pattern2 = Image("22222:33333:44444:55555:66666")
pattern3 = Image("33333:44444:55555:66666:77777")
pattern4 = Image("44444:55555:66666:77777:88888")
pattern5 = Image("55555:66666:77777:88888:99999")
patterns = [pattern0, pattern1, pattern2,
            pattern3, pattern4, pattern5]
display.show(patterns, delay=100, loop=True)
