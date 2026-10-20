import json

with open("report_example.json", encoding="utf-8") as f:
    rapor = json.load(f)

print(f"Sorgu: {rapor['query']}")
print(f"Toplam sonuç sayısı: {len(rapor['findings'])}")
for i, sonuc in enumerate(rapor['findings'], start=1):
    if sonuc['match']:
        print(f"\nSonuç {i}:")
        print(f"Track ID: {sonuc['track_id']}")
        print(f"Sınıf: {sonuc['class_name']}")
        print(f"Güven: {sonuc['confidence']}")
        print(f"İlk Görülme (s): {sonuc['first_seen_sec']}")
        print(f"Son Görülme (s): {sonuc['last_seen_sec']}")
        print(f"Bounding Box: {sonuc['bbox']}")
        print(f"Delil Çerçevesi: {sonuc['evidence_frame']}")
        print(f"VLM Cevabı: {sonuc['vlm_answer']}")
        print(f"Eşleşti: {sonuc['match']}")
    else:
        print(f"\nSonuç {i}: Eşleşme bulunamadı.")    