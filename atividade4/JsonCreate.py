import json
dim = dict()
dim["comprimento"] = 20.8
dim["largura"] = 13.8
dim["altura"] = 1.0

livro = dict()
livro["título"] = "Meditações"
livro["autor"] = "Marco Aurélio"
livro["essencial"] = True
livro["preço"] = 27.73
livro["dimensões"] = dim

jsonStr = json.dumps(livro, indent=4, ensure_ascii=False)
print(jsonStr)



