generate_line = lambda user: f"Hello {user}, welcome to Python training"

def write_dn(user, filename):
    with open (filename, "w") as f:
        f.write(generate_line(user))

write_dn("Krittika", "hi.txt")