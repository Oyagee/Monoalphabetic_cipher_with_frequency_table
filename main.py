# Создаем словарь для хранения частотности символов
def create_frequency_table(text):
    frequency_table = {}
    for letter in text:
        if letter in frequency_table:
            frequency_table[letter] += 1
        else:
            frequency_table[letter] = 1
    return frequency_table

# Выводим таблицу частотности символов
def print_frequency_table(frequency_table):
    print("Буква\tЧастота")
    for letter, frequency in frequency_table.items():
        print(letter, "\t", "{:.2f}%".format(frequency / sum(frequency_table.values()) * 100))

# Создаем таблицу шифрования
def create_cipher_table(alphabet, shift):
    cipher_table = {}
    for i in range(len(alphabet)):
        cipher_table[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]
    return cipher_table

# Шифруем сообщение
def encrypt_message(message, cipher_table):
    encrypted_message = ""
    for letter in message:
        if letter in cipher_table:
            encrypted_message += cipher_table[letter]
        else:
            encrypted_message += letter
    return encrypted_message

# Расшифровываем сообщение
def decrypt_message(message, cipher_table):
    decrypted_message = ""
    for letter in message:
        if letter in cipher_table:
            decrypted_message += cipher_table[letter]
        else:
            decrypted_message += letter
    return decrypted_message

# Создаем исходный алфавит и сообщение
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789"
initiator_message = "уважаемый игорь феодосьевич свободный текст 12082002 слобожанин роман анатольевич"
responder_message = "уважаемый роман анатольевич безмерно рад нашему сотрудничеству надеюсь на его дальнейшее успешное и взаимовыгодное развитие  с уважением игорь феодосьевич"

# Сливаем сообщения инициатора и ответчика
merged_message = initiator_message + responder_message

# Создаем таблицу шифрования и расшифрования
shift = 3
cipher_table = create_cipher_table(alphabet, shift)
decipher_table = create_cipher_table(alphabet, -shift)

# Зашифровываем сообщение
encrypted_message = encrypt_message(merged_message, cipher_table)

# Расшифровываем сообщение
decrypted_message = decrypt_message(encrypted_message, decipher_table)

# Выводим результаты
print("Исходный алфавит:", alphabet)
print("Сообщение инициатора:", initiator_message)
print("Сообщение ответчика:", responder_message)
print("Слияние сообщений:", merged_message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)

# Выводим таблицу частотности символов исходного алфавита
print("\nТаблица частотности символов исходного алфавита:")
alphabet_frequency_table = create_frequency_table(alphabet)
print_frequency_table(alphabet_frequency_table)

# Выводим таблицу частотности символов зашифрованного сообщения
print("\nТаблица частотности символов зашифрованного сообщения:")
encrypted_message_frequency_table = create_frequency_table(encrypted_message)
print_frequency_table(encrypted_message_frequency_table)

# Выводим таблицу частотности символов исходного сообщения
print("\nТаблица частотности символов исходного сообщения, полученного путём слияния:")
merged_message_frequency_table = create_frequency_table(merged_message)
print_frequency_table(merged_message_frequency_table)