from faker import Faker

fake = Faker()

def fake_gen():
    testmessage = {
        'name': fake.name(),
        'address': fake.address(),
        'phone_no': fake.phone_number()
    }
    return testmessage