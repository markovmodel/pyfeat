r"""

==============
Data container
==============

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>, Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

import pytram as pt
import numpy as np

class Forge( pt.TRAMData ):
    """I am the data forge
    """
    def __init__( self, trajs, b_K_i=None, kT_K=None, kT_target=None, verbose=False ):
        super( Forge, self ).__init__( trajs, b_K_i=b_K_i, kT_K=kT_K, kT_target=kT_target, verbose=verbose )
        self.M_K_t = None
        self.u_IK_t = None

    @property
    def M_K_t( self ):
        if self._M_K_t is None:
            if self.verbose:
                print "# Copying Markov state sequences"
            self._M_K_t = np.zeros( shape=(self.n_therm_states,self.N_K.max()), dtype=np.intc )
            t_K = np.zeros( shape=(self.n_therm_states,), dtype=np.intc )
            for traj in self.trajs:
                # SPEEDUP POSSIBLE!
                for t in xrange( traj['t'].shape[0] ):
                    K = traj['t'][t]
                    self._M_K_t[K,t_K[K]] = traj['m'][t]
                    t_K[K] += 1
            if self.verbose:
                print "# ... done"
        return self._M_K_t

    @property
    def u_IK_t( self ):
        if self._u_IK_t is None:
            if self.verbose:
                print "# Copying bias energy sequences"
            self._u_IK_t = np.zeros( shape=(self.n_therm_states,self.n_therm_states,self.N_K.max()), dtype=np.intc )
            if not self.kT_K is None:
                self.gen_u_IK_t_from_kT_K()
            else:
                self.gen_u_IK_t()
            if self.verbose:
                print "# ... done"
        return self._u_IK_t

    def gen_u_IK_t_from_kT_K( self ):
        t_K = np.zeros( shape=(self.n_therm_states,), dtype=np.intc )
        for traj in self.trajs:
            # SPEEDUP POSSIBLE!
            for t in xrange( traj['t'].shape[0] ):
                K = traj['t'][t]
                for I in xrange( self.n_therm_states ):
                    self._u_IK_t[I,K,t_K[K]] = self.kT_K[K] * ( 1.0/self.kT_K[I] - 1.0/self.kT_K[self.kT_target] ) * traj['u'][t]
                t_K[K] += 1

    def gen_u_IK_t( self ):
        t_K = np.zeros( shape=(self.n_therm_states,), dtype=np.intc )
        for traj in self.trajs:
            if traj['u'].shape[1] == 1:
                raise pt.ExpressionError(
                        "u_I_x",
                        "Trajectory with single energy columns detected - use kT file and kT target"
                    )
            if traj['u'].shape[1] != self.n_therm_states:
                raise pt.ExpressionError(
                        "u_I_x",
                        "Trajectory with wrong number of energy columns detected (%d!=%d)" \
                        % ( traj['u'].shape[1], self.n_therm_states )
                    )
            # SPEEDUP POSSIBLE!
            for t in xrange( traj['t'].shape[0] ):
                K = traj['t'][t]
                for I in xrange( self.n_therm_states ):
                    self._u_IK_t[I,K,t_K[K]] = traj['u'][I,t]
                t_K[K] += 1





