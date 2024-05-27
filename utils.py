
def compute_outer_weights():
    pass

def compute_inner_weights():
    pass


def compute_task_inputs(labour_inputs,compute_inputs,runtime_efficiencies):

    assert len(labour_inputs)==len(runtime_efficiencies)==(len(compute_inputs)-1) #as one compute only task
    pass


def compute_cognitive_inputs(betas,task_inputs,psi):

    assert len(betas)==len(task_inputs)
    
    Cog = sum([beta*(T**psi) for beta,T in zip(betas,task_inputs)])**(1/psi)

def compute_production(alpha,K,Cog,rho,TFP=1):

    return TFP * (alpha*K**rho + (1-alpha)*Cog**rho)**(1/rho)

def compute_runtime_efficiencies():
    pass

