* Parašykite funkciją su dokumentaciniais testais
* Ištestuokite funkciją
* Paverskite dokumentacinius testus unittest'ais
* Parašykite funkcijai X unittest'us

### Polinomai
Užduočiai atlikti pasirinkau Pycharm. Sukūriau klasę Polynomial, turinčią dviejų 
daugianarių dauginimo metodą. Šis metodas turėtų veikti greitai, nes visos jame esančios 
operacijos yra vektorizuotos. Aplanke yra trys failai: 

### Failai
* polynomial_doctest.py - polinomų klasė su dokumentaciniais testais
* polynomial_unittest.py - unittestai polinomų klasei
* doctest_to_unittest.py - abiejų tipų testinių pavyzdžių rinkinys

Prireiks taip pat dviejų bibliotekų - `numpy` ir `numpy_indexed`. 
Jos Pycharme yra įdiegiamos automatiškai iš `requirements.txt` failo

### Kita
Dokumentacinius testus taip pat pamėginau rašyti ir tais atvejais, kai klasės sudėtingesnės. 
Vienas iš pavyzdžių būtų aplanke **kita/exponentations**. Tačiau darydamas įvairius projektus
nuolat susiduriu su tuo pačiu klausimu: kaip vertėtų testuoti algoritmus, sudarytus iš 
daugiau arba sudėtingesnių komandų? Tokius kaip:

```
cells = self.cartessian_product(self.pows, other.pows) # finding pairs of powers
powers = np.sum(cells, axis=1) # summation of each pair of powers
coeffs = self.coeffs[cells[:, 0]] * other.coeffs[cells[:, 1]] # multiplication of corresponding coeffs
terms = np.column_stack([coeffs, powers]) # result as terms (coeff and power in each row)
return Polynomial(*npi.group_by(terms[:, 1]).sum(terms[:,0])) # reducing similar terms
```

 