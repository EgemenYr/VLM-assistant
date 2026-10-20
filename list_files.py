from pathlib import Path


def dosyalari_bul(klasor, kalip):
    bulunanlar = []
    for dosya in Path(klasor).rglob(kalip):
        if ".venv" in dosya.parts:
            continue
        bulunanlar.append(dosya)
    return bulunanlar


py_dosyalari = dosyalari_bul(".", "*.py")
print(f"{len(py_dosyalari)} dosya bulundu:")
for dosya in py_dosyalari:
    print(dosya)