# Union of fuzzy sets (max of the membership values)
def fuzzy_union(set1, set2):
    union_result = {}
    for key in set1.keys():
        union_result[key] = max(set1.get(key, 0), set2.get(key, 0))
    return union_result


# Intersection of fuzzy sets (min of the membership values)
def fuzzy_intersection(set1, set2):
    intersection_result = {}
    for key in set1.keys():
        intersection_result[key] = min(set1.get(key, 0), set2.get(key, 0))
    return intersection_result


# Complement of a fuzzy set (1 - membership value)
def fuzzy_complement(set1):
    complement_result = {}
    for key in set1.keys():
        complement_result[key] = round(
            1 - set1.get(key, 0), 2
        )  # Round to 2 decimal places for clarity
    return complement_result

A = {1: 0.7, 2: 0.4, 3: 0.8}
B = {1: 0.9, 2: 0.6, 3: 0.3}

# Taking user input for fuzzy sets A and B
# A = {}
# num_elements_a = int(input("Enter the number of elements in fuzzy set A: "))
# for _ in range(num_elements_a):
#     element = int(input("Enter the element: "))
#     membership_value = float(
#         input(f"Enter the membership value for element {element}: ")
#     )
#     A[element] = membership_value

# B = {}
# num_elements_b = int(input("\nEnter the number of elements in fuzzy set B: "))
# for _ in range(num_elements_b):
#     element = int(input("Enter the element: "))
#     membership_value = float(
#         input(f"Enter the membership value for element {element}: ")
#     )
#     B[element] = membership_value

# Demonstrating the operations
union_ab = fuzzy_union(A, B)
intersection_ab = fuzzy_intersection(A, B)
complement_a = fuzzy_complement(A)
complement_b = fuzzy_complement(B)

# De Morgan's Law verification (Complement of Union)
complement_union_ab = fuzzy_complement(union_ab)
complement_intersection_ab = fuzzy_intersection(complement_a, complement_b)

# Output results
print("\nFuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Union of A and B:", union_ab)
print("Intersection of A and B:", intersection_ab)
print("Complement of A:", complement_a)
print("Complement of B:", complement_b)

print("\nDe Morgan's Law Verification:")
print("Complement of Union (A ∪ B)^c:", complement_union_ab)
print("Complement of A ∩ B (A^c ∩ B^c):", complement_intersection_ab)

# Check if both sides of De Morgan's Law are the same
if complement_union_ab == complement_intersection_ab:
    print("\nDe Morgan's Law is verified: (A ∪ B)^c = A^c ∩ B^c")
else:
    print("\nDe Morgan's Law is not verified!")

