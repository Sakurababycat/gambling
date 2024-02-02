from policy import PolicyRegister

policyPool = []
for key, policyClass in PolicyRegister.items():
    policyPool += policyClass.makePolicy()

print(policyPool)
