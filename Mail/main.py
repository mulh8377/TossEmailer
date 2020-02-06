import domain


def create_email(name: str, email: str):
    email_address = name + email
    #print(email_address + "," + name)
    return email_address + "," + name
    
    
def prime_number_generator(prime: int, multiplier = 100):
    prime_list = []
    for i in range(prime, prime * multiplier):
        prime_list.append(i)
    return prime_list
    
def email_tag(name, prime_number: int):
    return name + "-" + str(prime_number)

def main():
    #print("email program")
    first_names = ["Chad", "Brad", "Jack", "John", "Michael", "Elliot"]
    last_names = ["XXLJohnson", "Smith", "William", "Wellcrom", "Lado", "Hernandez"]
    
    name_list = []
    
    for i in range(0, 6):
        #print(first_names[i])
        first_name_guy = first_names[i] + first_names[i]
        last_name_man = last_names[i] + last_names[i]
        formal_name_guy = first_names[i] + last_names[i]
        
        name_list.append(first_name_guy)
        name_list.append(last_name_man)
        name_list.append(formal_name_guy)
        
    #print(name_list)
    
    prim_num = 3
    
    
    email_list = []
    for name in name_list:
        p_list = prime_number_generator(prim_num)
        for p in p_list:
            email_list.append(email_tag(name=name, prime_number=p) + domain.domain_gmail())
            email_list.append(email_tag(name=name, prime_number=p) + domain.domain_hotmail())
            email_list.append(email_tag(name=name, prime_number=p) + domain.domain_yahoo())

        
    for e in email_list:
        print(e)
    
    

if __name__ == "__main__":
    #print(create_email(name="joebob", email=domain.domain_gmail()))
    main()