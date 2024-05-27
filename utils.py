import numpy as np


def compute_outer_weights(capital_to_cognitive_ratio,K,Cog,rho):

    omega = capital_to_cognitive_ratio*((Cog/K)**rho)
    alpha = omega/1+omega

    return alpha

def compute_inner_weights(compute_to_labour_ratio,n_labour_tasks,C_eff,rho):

    omega_ = compute_to_labour_ratio * ((L/(n_labour_tasks*C_eff))**rho)
    beta_0 = omega_ / (1+omega_)
    beta_i = (1-beta_0)/n_labour_tasks

    inner_weights = np.concatenate(\
                    (np.ones(1)*beta_0,np.ones(n_labour_tasks)*beta_i),\
                    axis=0
                    )

    return inner_weights


def labour_compute_arrays(L,C_eff,n_labour_tasks,automation_index,optimal_allocation=False):


    if not optimal_allocation:
        labour_per_task = L/n_labour_tasks
        effective_compute_per_task = C_eff/(automation_index+1)
    else: 
        raise Exception('Optimal allocation not implemented')

    labour_array = np.concatenate(\
                (np.zeros(1),np.ones(n_labour_tasks) * labour_per_task),\
                axis=0
                )

    effective_compute_array = np.concatenate( \
                (np.ones(automation_index+1)*effective_compute_per_task,np.zeros(n_labour_tasks-automation_index)),\
                axis=0
                )

    return labour_array, effective_compute_array

def compute_runtime_efficiencies(baseline_runtime_requirements,C_T,automation_training_threshold,delta):

    eta_0 = 1/baseline_runtime_requirements
    training_requirements_multiplier = (C_T/automation_training_threshold)**delta
    eta = training_requirements_multiplier*eta_0

    return eta

def compute_task_inputs(labour_array,effective_compute_array,eta):
    eta_ = np.concatenate(\
                    (np.ones(1),eta),
                    axis=0) #for compute only task

    task_inputs = labour_array + (eta_*effective_compute_array)
    
    return task_inputs



def compute_cognitive_inputs(inner_weights,task_inputs,psi):

    assert len(inner_weights)==len(task_inputs)
    
    Cog = (np.sum(inner_weights*(task_inputs)**(psi)))**(1/psi)

    return Cog

def compute_production(alpha,K,Cog,rho,TFP=1):

    return TFP * (alpha*K**rho + (1-alpha)*Cog**rho)**(1/rho)


    

