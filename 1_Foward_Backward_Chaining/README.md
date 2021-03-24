# Tugas 1 Sistem Pakar
Tugas Sistem Pakar Foward Chain  & Backward Chain

Aturan yang digunakan
```
# Rules

# mamalia (A) ==> bertulang belakang (A).
# bertulang belakang (A) ==> hewan (A).
# bertulang belakang (A), terbang (A) ==> burung (A).
# bertulang belakang ("bebek").
# terbang ("bebek").
# mamalia ("Kucing").
```

```
global facts
global is_changed
is_changed = True
facts = [["bertulang belakang","bebek"],["terbang","bebek"],["mamalia","kucing"]]

```
Kode di atas untuk mendefinisikan dan menyimpan variable global

```
def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

```
Blok kode di atas adalah sebuah method perulangan untuk menyimpan fakta fakta baru

```
while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "mamalia":
            assert_fact(["bertulang belakang",A1[1]])
        if A1[0] == "bertulang belakang":
            assert_fact(["hewan",A1[1]])
        if A1[0] == "bertulang belakang" and ["terbang",A1[1]] in facts:
            assert_fact(["burung",A1[1]])

print("FowardChain")
print(facts)
```
Blok diatas adalah fungsi untuk melooping aturan aturan yang ditetapkan untuk menentukan fakta baru dengan metode Foward Chain kemudian menampilkan fakta tersebut

```
while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "bertulang belakang" and ["terbang",A1[1]] in facts:
            assert_fact(["burung",A1[1]])
        if A1[0] == "bertulang belakang":
            assert_fact(["hewan",A1[1]])
        if A1[0] == "mamalia":
            assert_fact(["bertulang belakang",A1[1]])
        
print("BackwardChain")
print(facts)
```
Blok diatas adalah fungsi untuk melooping aturan aturan yang ditetapkan untuk menentukan fakta baru dengan metode Backward Chain kemudian menampilkan fakta tersebut