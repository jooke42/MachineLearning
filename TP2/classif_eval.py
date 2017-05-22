import numpy as np
import pandas as pd

def classif_eval(y_true,y_pred,nb_values=1000):
    """
    Evalue la qualité de la classification en calculant les les nombres de vrai et 
    faux positifs, de vrai et faux négatifs.
    input :
    -------
    y_true : array
        les vraies classes
    y_pred_proba : array
        les probabilités prédites pour chaque classe
    nb_values : int
        nombre de valeurs de seuils (sur les probas) pour calculer les affectations aux classes
    output :
    --------
    tp,fp,tn,fn,total_pos,total_neg
    """
    
    tp=np.zeros(nb_values)
    fp=np.zeros(nb_values)
    tn=np.zeros(nb_values)
    fn=np.zeros(nb_values)
    total_pos=np.sum(y_true)
    total_neg=np.size(y_true)-total_pos

    k=0
    for p in np.linspace(0,1,nb_values):
        tp[k]=np.sum((y_pred>p)*y_true)
        fp[k]=np.sum((y_pred>p)*(np.logical_not(y_true)))
        tn[k]=np.sum((y_pred<p)*(np.logical_not(y_true)))
        fn[k]=np.sum((y_pred<p)*(y_true))
        k+=1
    return tp,fp,tn,fn,total_pos,total_neg