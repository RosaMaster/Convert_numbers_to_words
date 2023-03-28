# link_doc: https://pypi.org/project/num2words/


from num2words import num2words


numero = int(input("Digite um número: "))


num_en = num2words(numero, lang='en')
print(f"Em inglês: {num_en}")


num_en_ord = num2words(numero, lang='en', to='ordinal')
print(f"Em inglês (ordinal): {num_en_ord}")


num_pt = num2words(numero, lang='pt-br')
print(f"Em português: {num_pt}")


num_pt_ord = num2words(numero, lang='pt-br', to='ordinal')
print(f"Em português (ordinal): {num_pt_ord}")


