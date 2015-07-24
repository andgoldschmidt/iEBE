controlParameterList = {
    'simulation_type'       :   'hydro',  # 'hybrid' or 'hydro'
    'initialCondition'      :   'superMC', # 'trento' or 'superMC'
    'niceness'              :   10,       # range from 0 to 19 for process priority, 0 for the highest priority
}

# tables available for superMC, set empty for trento
centralityParameters = {
    'centrality': '20-30%',     # centrality bin
    'cut_type': '',             # centrality cut variable: total_entropy or Npart
                                # if empty, no cut (set manually)
}

superMCParameters = {
    'which_mc_model'                :   5,          # MC-Glb=5, MC-KLN=1
    'sub_model'                     :   1,          # default: Glb=1, KLN=7
    'Aproj'                         :   196,        # use mass number
    'Atarg'                         :   196,
    'ecm'                           :   200,
    'finalFactor'                   :   28.66,
    'alpha'                         :   0.14,       # WN/BC mixing ratio in MCGlb
    'lambda'                        :   0.218,      # saturation scale parameter in MCKLN
    'operation'                     :   1,
    'include_NN_correlation'        :   0,
    'cc_fluctuation_model'          :   6,
    'cc_fluctuation_Gamma_theta'    :   0.75,
    'maxx'                          :   13.0,       # grid size in x (fm)
    'maxy'                          :   13.0,       # grid size in y (fm)
    'dx'                            :   0.1,        # grid spacing in x (fm)
    'dy'                            :   0.1,        # grid spacing in y (fm)
    'Npmin'                         :   0,
    'Npmax'                         :   400,
    'bmin'                          :   0,
    'bmax'                          :   20,
    'cutdSdy'                       :   0,
    'cutdSdy_lowerBound'            :   0,
    'cutdSdy_upperBound'            :   10000.0,
}

trentoParameters = {
    'reduced-thickness'             :   0,
    'projectile1'                   :   'Pb',
    'projectile2'                   :   'Pb',
    'fluctuation'                   :   1e12,   # inf -> off
    'nucleon-width'                 :   0.5,
    'deposition-width'              :   0.5,
    'cross-section'                 :   6.4,
    'normalization'                 :   56,
    'b-min'                         :   0,
    'b-max'                         :   20,
    'grid-max'                      :   13.1,   # max for x any y
    'grid-step'                     :   0.1,
}

hydroParameters = {
    'vis'       :   0.08,
    'visflag'   :   1,          # flag to use temperature dependent eta/s(T)
    'T0'        :   0.6,        # tau_0
    'dt'        :   0.02,       # dtau
    'Edec'      :   0.18,
    'iLS'       :   130,        # lattice size in transverse plane 2*iLS+1
    'dx'        :   0.1,        # lattice spacing in x (fm)
                                # need to be the same as dx in initial condition
    'dy'        :   0.1,        # lattice spacing in y (fm)
                                # need to be the same as dy in initial condition
    'IhydroJetoutput' :   0,    # switch for output hydro evolution history into hdf5 file
    'InitialURead'    :   0,    # set it to be 1 when simulation_type == hydroEM_preEquilibrium
    'Initialpitensor' :   0,    # initialization of pi tensor
}

iSSParameters = {
    'number_of_repeated_sampling'   :   1,
    'MC_sampling'                   :   2,
    'y_LB'                          :   -2.5,
    'y_RB'                          :   2.5,
}

iSSParameters = {
    'calculate_vn'                  :   1,
    'MC_sampling'                   :   2,
    'number_of_repeated_sampling'   :   1,
    'y_LB'                          :   -2.5,
    'y_RB'                          :   2.5,
    'sample_y_minus_eta_s_range'    :   2.0,
}

