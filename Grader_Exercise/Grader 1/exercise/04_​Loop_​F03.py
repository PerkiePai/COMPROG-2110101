def grade_mcq(sol, ans):
    sol = sol.strip()
    ans = ans.strip()
    
    if len(sol) != len(ans):
        return -1
    else:
        score=0
        for i in range(len(sol)):
            if sol[i]==ans[i]:
                score+=1
        return score

exec(input()) # DON'T remove this line