import math

def euclidean_distance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: İlk noktayı temsil eden bir demet (tuple).
    point2: İkinci noktayı temsil eden bir demet (tuple).

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """

  x1, y1 = point1
  x2, y2 = point2
  distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return distance

def find_min_distance(points):
  """
  Verilen noktalar listesindeki en küçük Öklid mesafesini bulur.

  Args:
    points: Noktaları temsil eden demetlerin bir listesi.

  Returns:
    En küçük Öklid mesafesi.
  """

  min_distance = float('inf')  # Sonsuzluk ile başlatarak en küçük değeri bulmak için
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      distance = euclidean_distance(points[i], points[j])
      if distance < min_distance:
        min_distance = distance
  return min_distance

# Örnek kullanım:
points = [(1, 2), (4, 6), (2, 3), (5, 1)]
min_distance = find_min_distance(points)
print("En küçük Öklid mesafesi:", min_distance)
