
# s = ladspa.compress_rms(s)


s = ladspa.hardlimiter(
    db_limit=0.0,
    s)


s = ladspa.limit_rms(s)


s = ladspa.dj_eq(
	lo_gain=-2.0,
	mid_gain=2.0,
	hi_gain=1.0,
    s)


s = ladspa.tap_dynamics_st(
    attack=64.0,
    release=256.0,
    function=10,
    makeup_gain=5.0,
    s)

