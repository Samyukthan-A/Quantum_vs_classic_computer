import math
LOWERCASE = 26
UPPERCASE = 26
DIGITS = 10
SPECIALS = 32 
TOTAL_CHARS = LOWERCASE + UPPERCASE + DIGITS + SPECIALS  # 94

#cracking speeds (attempts per second)
CPU_SPEED = 50_000_000  #50 million/sec (mid-range CPU, multi-threaded)
GPU_SPEED = 15_000_000_000  #15 billion/sec (mid-range RTX 4060)
QUANTUM_SPEED = 1_000_000  #1 million/sec (hypothetical quantum clock rate)

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.2f} minutes"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.2f} hours"
    elif seconds < 31536000:
        days = seconds / 86400
        return f"{days:.2f} days"
    else:
        years = seconds / 31536000
        return f"{years:.2f} years"

def calculate_crack_time(password):
    length = len(password)
    #total possibilities = TOTAL_CHARS to the power of length
    possibilities = TOTAL_CHARS ** length

    #CPU time
    cpu_time = possibilities / CPU_SPEED

    #GPU time
    gpu_time = possibilities / GPU_SPEED

    #quantum time 
    quantum_possibilities = math.sqrt(possibilities) #(grover's algorithm: sqrt(possibilities))
    quantum_time = quantum_possibilities / QUANTUM_SPEED

    return possibilities, cpu_time, gpu_time, quantum_time

def main():
    print("Password Cracking Time Estimator")
    print(f"Character set: {TOTAL_CHARS} (A-Z, a-z, 0-9, 32 specials)")
    print(f"CPU speed: {CPU_SPEED:,} attempts/sec")
    print(f"GPU speed: {GPU_SPEED:,} attempts/sec")
    print(f"Quantum speed: {QUANTUM_SPEED:,} checks/sec (Grover's algorithm)")
    print("-" * 50)

    password = input("Enter a password to test: ")#dw i wont get your passwords.........for now :)
    if not password:
        print("Password cannot be empty!")
        return

    possibilities, cpu_time, gpu_time, quantum_time = calculate_crack_time(password)

    print(f"\nPassword: '{password}' (length: {len(password)})")
    print(f"Total possibilities: {possibilities:,}")
    print("\nCracking Time Estimates:")
    print(f"Classical CPU: {format_time(cpu_time)}")
    print(f"Classical GPU: {format_time(gpu_time)}")
    print(f"Quantum (Grover's): {format_time(quantum_time)}")

if __name__ == "__main__":
    main()