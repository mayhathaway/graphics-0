import random

def main():
    img = ''
    i = 0
    while i < 100000:
        r1 = random.randint(0, 256)
        b1 = random.randint(0, 256)
        g1 = random.randint(0, 256)
        r2 = random.randint(0, 128)
        b2 = random.randint(0, 128)
        g2 = random.randint(0, 128)
        r3 = random.randint(128, 256)
        b3 = random.randint(128, 256)
        g3 = random.randint(128, 256)
        a = 0
        while a < 10:
            img += str(r1) + ' ' + str(b1) + ' ' + str(g1) + '\n'
            a += 1
        b = 0
        while b < 10:
            img += str(r2) + ' ' + str(b2) + ' ' + str(g2) + '\n'
            b += 2
        c = 0
        while c < 10:
            img += str(r3) + ' ' + str(b3) + ' ' + str(g3) + '\n'
            c += 5
        i += 1

    pic = open('image.ppm', 'w')
    pic.write('P3 500 500 255\n')
    pic.write(img)
    pic.close()

main()
