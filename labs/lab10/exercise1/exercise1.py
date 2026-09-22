num_rounds = int(input())

final_score =0
rounds_processed =0

for i in range (1, num_rounds + 1):
    score = int(input("Enter each round's score:"))
    
    if score > 100:
        final_score += score + (score*20/100)

    else:
        final_score += score

rounds_processed = num_rounds
    

print(f"{final_score:.1f}")
print(rounds_processed)
