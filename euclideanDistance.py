#calculation of euclidean distance between the points
import math

#2D uzaydaki noktaları temsil eden noktalar (tuple)
points = [(1,3),(2,6),(5,8),(9,4)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1,point2):
    x1, y1=point1
    x2, y2=point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Mesafeleri saklayacağımız liste
distances=[]

# Noktalar arasındaki mesafeleri hesaplamak için döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # j, i'den bir sonraki noktadan başlar
        point1 = points[i]
        point2 = points[j]
        dist = euclideanDistance(point1, point2)
        # Hesaplanan mesafeyi distances listesine ekle
        distances.append(dist)
        
# En küçük mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print(f"Min distance between the points: {min_distance}")