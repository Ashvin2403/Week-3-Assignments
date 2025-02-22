def caesar_cypher(cyphertext):
    # Define the set of symbols that can be decrypted
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
    
    # Try all possible shift keys
    for key in range(len(symbols)):
        decrypted_text = ''
        
        # Decrypt each symbol in the ciphertext
        for symbol in cyphertext:
            if symbol in symbols:
                symbol_index = symbols.find(symbol)  # Find the symbol
                new_index = (symbol_index - key) % len(symbols)  # Shift backwards by key amount
                decrypted_text += symbols[new_index]  # Apply decrypted character
            else:
                decrypted_text += symbol  # Apply unchanged character if not in the symbols
        
        # Print the decrypted message with the current key
        print('Key', key, ':', decrypted_text)

# Example usage
cyphertext = "Brute Force"  # Encrypted message
caesar_cypher(cyphertext)  # Run brute-force decryption
