import os.path

cop = (
        'code4nz.py',)
exec_ = ('py4nz',)

target_bin = '/usr/bin/'
target_lib = '/usr/lib/python3.7/'

def check_files() -> bool:
    print('checking have to be copied files...')
    for p in cop:
        if not os.path.exists(p):
            return False
    print('done!')
    print('checking exec files...')
    for p in exec_:
        if not os.path.exists(p):
            return False
    print('done!')
    return True


def chomd_exec():
    print('changing mode to 777...')
    for p in exec_:
        os.system('chmod 777 {}'.format(p))


def cpy_file(from_, to):
    print('coping file %s to %s' % (from_, to))
    f_f = open(from_)
    f_t = open(to, 'w')


    f_t.write(f_f.read())
    f_f.close()
    f_t.close()


def cpy_files():
    for c in cop:
        p = os.path.join(target_lib, c)
        cpy_file(c, p)
    
    for c in exec_:
        p = os.path.join(target_bin, c)
        cpy_file(c, p)


if __name__ == '__main__':
    import readline

    print('Nezha -- I am destiny!')
    print('Python for Nezha installer')

    print()

    t_b = input("'bin' path (default : /usr/bin) :")
    t_l = input("'lib' path (default: /usr/lib/python3.7) :")

    if t_b:
        target_bin = t_b
    if t_l:
        target_lib = t_l

    if not check_files():
        print('E: Please check that the directory is complete')
        import sys
        sys.exit(1)
    chomd_exec()
    cpy_files()

    print('done!')
    print("Enter 'py4nz' to run.")
