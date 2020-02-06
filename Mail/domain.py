def domain_gmail():
    return "@gmail.com"

def domain_hotmail():
    return "@hotmail.com"
    
def domain_yahoo():
    return "@yahoo.com"
    
def test_gmail(gmail: str):
    assert(gmail == "@gmail.com")
    
    assert(len(gmail) == 10)
    
def test_hotmail(hotmail: str):
    assert(hotmail == "@hotmail.com")
    
    assert(len(hotmail) == 12)


def test_yahoo(yahoo: str):
    assert(yahoo == "@yahoo.com")
    
    assert(len(yahoo) == 10)


if __name__ == "__main__":
    
    print(len(domain_gmail()))
    print(len(domain_yahoo()))
    print(len(domain_hotmail()))
    
    
    test_gmail(domain_gmail())
    test_hotmail(domain_hotmail())
    test_yahoo(domain_yahoo())
    