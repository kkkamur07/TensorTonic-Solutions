import numpy as np

def skewness_kurtosis(data):
    """
    Returns: dict with 'skewness', 'kurtosis', and interpretation strings.
    """
    data = np.array(data)
    
    def normalizer(data) : 
        return (data - np.mean(data))
    
    def std_dev(data) : 
        lenn = len(data)
        varrr = (1.0/(lenn - 1)) * np.sum(normalizer(data) ** 2)
        return varrr ** 0.5

    def normalizer_index(data) : 
        return (data - np.mean(data))

    def skewness(data) : 
        summ = np.sum((normalizer(data)/std_dev(data))**3)
        n = len(data)
        return (n/((n-1)*(n-2))) * summ

    def kurtosis(data) : 
        n = len(data)
        first_term = (n * (n+1))/((n-1)*(n-2)*(n-3))
        last_term = (3*((n-1)**2)/((n-2)*(n-3)))
        mid_term = np.sum((normalizer(data)/std_dev(data))**4)

        return (first_term * mid_term) - last_term

    def skew_interpretation(data) : 
        damm = skewness(data)

        if damm > 0.5 : 
            return "right-skewed"
        elif damm < -0.5 :
            return "left-skewed"
        else :
            return "approximately symmetric"

    def kurtosis_interpretation(data) : 
        damm = kurtosis(data)

        if damm > 1 : 
            return "leptokurtic"
        elif damm < -1 : 
            return "platykurtic"
        else : 
            return "mesokurtic"


    return {
        "skewness" : round(skewness(data),4),
        "kurtosis" : round(kurtosis(data),4),
        "skew_interpretation" : skew_interpretation(data),
        "kurtosis_interpretation" : kurtosis_interpretation(data)
    }
        
        