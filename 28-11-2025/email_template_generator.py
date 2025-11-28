def email_template(name):
    email=f"""
            Dear {name},
            Your training session starts tomorrow.
            regards,
            Training Team!!!
            """
    x=f"email_{name}.txt"
    with open(x,"w") as f:
        f.write(email)

x=input("Please enter your name")
email_template(x)
