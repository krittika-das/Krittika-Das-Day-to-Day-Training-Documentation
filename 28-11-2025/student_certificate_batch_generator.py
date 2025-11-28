def write_cert(user):
    return f"""
            This is to certify that {user} has succesfully completed
            the bootcamp on Python basics with 30 hours of learning
            and hands-on-practise.
            """

with open('student_certificate.txt', 'r') as f:
    c=f.readlines()
    for i in c:
        i=i.strip()
        ki=f"certificate_{i}.txt"
        with open (ki, 'w') as k:
            k.write(write_cert(i))
