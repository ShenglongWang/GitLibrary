from atoutils import *

MIN_SIZE = 1 * pow(1024, 3)  # G


def disk_usage(directory):
    du = {}
    usage = 0
    if os.path.isdir(directory):
        try:
            root, dirs, files = next(os.walk(directory))
            for d in dirs:
                d = os.path.join(root, d)
                du = dict(du, **disk_usage(d))
                usage += du[d]
            for f in files:
                usage += os.path.getsize(os.path.join(root, f))
        except:
            pass
    else:
        warning(directory, 'should be a directory')

    du[directory] = usage
    return du


def main():
    du = disk_usage('.')
    du_copy = du.copy()
    for k, v in du_copy.items():
        if v < MIN_SIZE:
            du.pop(k)
        else:
            while True:
                k, _ = os.path.split(k)
                if k == '':
                    break
                if k in du:
                    du.pop(k)

    with open('du.txt', 'w') as f:
        for k, v in sorted(du.items(), key=lambda x: x[0], reverse=False):
            print(k, '%.2fG' % (v / pow(1024, 3)), file=f)


if __name__ == '__main__':
    main()
