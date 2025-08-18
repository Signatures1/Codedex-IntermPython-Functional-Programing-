def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }
    def translate_word(word):
        if word.lower() in translations[language]:
            return translations[language][word.lower()]
        else:
            return "Translation unavailable"

    return translate_word

translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  

translate_to_french = translator('french')
print(translate_to_french('hello'))  

translate_to_italian = translator('italian')
print(translate_to_italian('hello'))  

translate_to_italian = translator('italian')
print(translate_to_italian('tonight'))  