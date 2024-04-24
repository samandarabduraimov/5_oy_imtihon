import threading
import time

product = {
    'name': 'Samad',
    'year': 46,
    'place': 'Toshkent',
}
def malumot_olish():

    print("Malumotlar olinmoqda...")
    time.sleep(2) 
    print("Olingan malumotlar:", product)

def sorov():
    print("So'rov bajarilmoqda...")
    malumot_olish() 

thread1 = threading.Thread(target=sorov)
thread2 = threading.Thread(target=malumot_olish)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Operatsiyalar tugallandi")
