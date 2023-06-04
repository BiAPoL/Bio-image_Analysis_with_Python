def generate_biomodal_2d_data():
    import numpy as np
        
    rs = np.random.RandomState(seed=0)

    x1 = rs.normal(3, 1, (150,2))
    x2 = rs.normal(8, 1.5, (150,2))

    x_all = np.concatenate((x1, x2), axis=0)
    rs.shuffle(x_all)
    return x_all
