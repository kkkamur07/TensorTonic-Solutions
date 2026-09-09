import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    def dot_product(a,b) : 
        return np.sum(a*b)

    def euclidean_norm(a) : 
        norm = (np.sum(a**2))**0.5

        return norm


    dot_products = dot_product(a,b)
    a_norm = euclidean_norm(a)
    b_norm = euclidean_norm(b)

    if a_norm == 0 or b_norm == 0 : 
        return 0 
    else : 
        return dot_products/(a_norm * b_norm)