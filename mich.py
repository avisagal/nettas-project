from fuzzywuzzy import fuzz
from googletrans import Translator
import smtplib

HEADERS = ["id", "medicine name", "amount", "city", "expiration date", "is closed", "owner name", "picture"]

def best_word(list_of_words, word_to_find):
    """
    picks the closest worf from the list to the word to find
    :return: the best word or None if not found any close enough.
    """
    best_ratio = 0
    bst_word = None

    for word in list_of_words:
        if fuzz.partial_ratio(word, word_to_find) > best_ratio:
            best_ratio = fuzz.partial_ratio(word, word_to_find)
            bst_word = word
    if bst_word is not None and best_ratio > 50:
        return bst_word
    return None

def my_trans(word):
    tran = Translator(service_urls=['translate.google.com',
                                    'translate.google.co.il',])
    new = tran.translate(word)
    return new.text


def send_mail(address_mail):

    # Specifying the from and to addresses

    fromaddr = 'meditakeisrael@gmail.com'
    toaddrs = address_mail

    # Writing the message (this message will appear in the email)

    msg = 'take med!'

    # Gmail Login

    username = 'meditakeisrael'
    password = 'netta1234'

    # Sending the mail

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


def translate_to_dict(list_data):
    dict_id = 1
    outer_dict = {}
    for cur_tuple in list_data:
        inner_dict = {}
        for i in range(8):
            inner_dict[HEADERS[i]] = cur_tuple[i]
        outer_dict[dict_id] = inner_dict
        dict_id += 1

    return outer_dict

if __name__ == "__main__":
    send_mail("hassidm@gmail.com")