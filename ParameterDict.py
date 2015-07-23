controlParameterList = {
    'simulation_type'       :   'hydro',  # 'hybrid' or 'hydro'
    'initialCondition'      :   'trento', # 'trento' or 'superMC'
    'niceness'              :   10,       # range from 0 to 19 for process priority, 0 for the highest priority
}

centralityParameters = {
    'centrality': '20-30%',  # centrality bin
    'cut_type': '',
    # centrality cut variable: total_entropy or Npart
    # if string is empty, ignore
}

superMCParameters = {
    'which_mc_model'                :   5,
    'sub_model'                     :   1,
    'Aproj'                         :   208,
    'Atarg'                         :   208,
    'ecm'                           :   2760,
    'finalFactor'                   :   56.763,
    'alpha'                         :   0.118,
    'lambda'                        :   0.218,
    'bmin'                          :   0, # ignore if cut_type chosen
    'bmax'                          :   20,
}

trentoParameters = {
    'reduced-thickness'             :   0,
    'projectile1'                   :   'Pb',
    'projectile2'                   :   'Pb',
    'fluctuation'                   :   1e12, # inf -> off
    'nucleon-width'                 :   0.5,
    'deposition-width'              :   0.5,
    'cross-section'                 :   6.4,
    'normalization'                 :   56,
    'b-min'                         :   0,
    'b-max'                         :   20,
}

hydroParameters = {
    'vis'       :   0.08,
    'T0'        :   0.6, # tau_0
    'Edec'      :   0.18222,
}

iSSParameters = {
    'number_of_repeated_sampling'   :   1,
    'MC_sampling'                   :   2,
    'y_LB'                          :   -2.5,
    'y_RB'                          :   2.5,
}
