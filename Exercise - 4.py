def evaluate_polynomial(coeffs, x):
    """
    Evaluates a polynomial using Horner's Method.
    Example: coeffs [a0, a1, a2] represents a0 + a1*x + a2*x^2
    Complexity: Time O(n), Space O(1)
    """
    n = len(coeffs) # [cite: 46]
    if n == 0:
        return 0
    
    # Start with the coefficient of the highest degree term [cite: 47]
    # In this implementation, coeffs[n-1] is the highest degree term
    result = coeffs[n - 1]
    
    # Iterate downwards from the second-to-last coefficient to the first [cite: 48]
    for i in range(n - 2, -1, -1):
        result = (result * x) + coeffs[i] # [cite: 48]
        
    return result

# --- Example Usage ---
if __name__ == "__main__":
    # Example: 3x^2 + 2x + 1  => coeffs = [1, 2, 3], x = 2
    # Calculation: ((3 * 2) + 2) * 2 + 1 = 17
    coefficients = [1, 2, 3] 
    x_val = 2
    
    print("\n--- Exercise 4: Horner's Method ---")
    print(f"Polynomial coefficients: {coefficients}")
    print(f"Value at x = {x_val}: {evaluate_polynomial(coefficients, x_val)}")