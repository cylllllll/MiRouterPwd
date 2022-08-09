import hashlib

# 输入SN
sn = "****/E********"

salt = "d44fb0960aa0-a5e6-4a30-250f-6d2df50a"


def get_salt():
    return '-'.join(reversed(salt.split("-")))


def generate_md5(sn):
    passwd = sn + get_salt()
    m = hashlib.md5(passwd.encode())
    return m.hexdigest()[:8]


if __name__ == '__main__':
    print('密码是： ' + generate_md5(sn))
