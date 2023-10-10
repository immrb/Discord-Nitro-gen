import random
import string
import time


print("\033[34;1m[=] NITRO GEN")
def generate(num_codes):
    try:
        if num_codes <= 0:
            raise ValueError("\033[31mNumber of codes must be greater than 0")
        
        
        codes = []
        
        
        characters = string.ascii_letters + string.digits
        
        start_time = time.perf_counter()  
        
        for _ in range(num_codes):
            
            random_text = ''.join(random.choice(characters) for _ in range(9))
            discord_gift_code = f"http://discord.gift/{random_text}"
            codes.append(discord_gift_code)
        
        end_time = time.perf_counter()  
        
        
        with open('nitro_codes.txt', 'w') as file:
            for code in codes:
                file.write(code + '\n')
        
        return f"\033[92m[+] Generated {num_codes} codes saved to 'nitro_codes.txt'. Took {end_time - start_time:.2f} seconds to finish.\033[0m"
    
    except Exception as e:
        return f"\033[31m[-] Error: {str(e)}\033[0m"


num_codes = int(input("\033[92m[+] How many codes to generate: \033[0m"))

result = generate(num_codes)
print(result)
