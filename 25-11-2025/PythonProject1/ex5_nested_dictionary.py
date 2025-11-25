x={
    "e1": {"dept": "IT"},
    "e2":{"dept": "IT"},
    "e3": {"dept": "HR"},
}

trial={}
for k,v in x.items():
    for a,y in v.items():
        if y not in trial:
            trial[y]=1
        else:
            trial[y]+=1

print(trial)
